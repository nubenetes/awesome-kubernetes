import asyncio
import sys
import os
import json
import re
import yaml
from datetime import datetime, timedelta
from src.config import TARGET_REPO, MADRID_TZ, GH_TOKEN, NUBENETES_CATEGORIES
from src.ingestion_twikit import SocialDataExtractor
from src.markdown_ast import MarkdownSanitizer
from src.agentic_curator import evaluate_extracted_assets, AgenticCurator
from src.autonomous_discovery import discover_trending_assets
from src.gitops_manager import RepositoryController
from src.logger import log_event
from src.gemini_utils import call_gemini_with_retry, resolve_url, normalize_url, sanitize_trailing_slashes
from src.state_manager import get_last_date, save_state

async def master_orchestrator():
    # 0. Ingest Mandates from GEMINI.md (Mandate Bridge)
    try:
        from src.mandate_ingestor import MandateIngestor
        MandateIngestor().save_system_instructions()
    except Exception as e:
        log_event(f"  [!] Mandate Ingestion failed (Using defaults): {e}")

    git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
    
    log_event("STARTING AGENTIC CURATION (CHRONOLOGY & TRANSPARENCY)", section_break=True)
    
    # 1. Dynamic / Historical Time Horizon
    is_historical = os.getenv("HISTORICAL_MODE", "false").lower() == "true"
    is_chunked = os.getenv("HISTORICAL_CHUNKED", "false").lower() == "true"
    
    until_date = datetime.now(MADRID_TZ)
    
    # Priority: 1. Relative Range, 2. Historical Mode, 3. Manual Start Date, 4. state.json
    days_back_env = os.getenv("CURATION_DAYS_BACK")
    if days_back_env and days_back_env.strip():
        try:
            days = int(days_back_env)
            since_date = until_date - timedelta(days=days)
            log_event(f"[*] Mode: Relative range (Last {days} days) -> {since_date.date()}")
            is_historical = False # Force normal mode for relative range
        except:
            since_date = get_last_date()
    elif is_historical:
        # DEFAULT START DATE: 2026-05-15 (as requested)
        final_stop_date = datetime(2026, 5, 15, 0, 0, tzinfo=MADRID_TZ)
        
        if is_chunked:
            chunk_days = int(os.getenv("HISTORICAL_CHUNK_DAYS", "180"))
            until_str = os.getenv("HISTORICAL_UNTIL_DATE")
            if until_str:
                until_date = datetime.fromisoformat(until_str).replace(tzinfo=MADRID_TZ)
            else:
                until_date = datetime.now(MADRID_TZ)
                
            since_date = until_date - timedelta(days=chunk_days)
            if since_date < final_stop_date:
                since_date = final_stop_date
            log_event(f"[*] HISTORICAL MODE (CHUNKED): Chunk {since_date.date()} -> {until_date.date()}")
        else:
            since_date = final_stop_date
            log_event(f"[*] HISTORICAL MODE (UNIFIED): Processing all since {since_date.date()} in a single run")
    else:
        env_start = os.getenv("CURATION_START_DATE")
        if env_start:
            try:
                since_date = datetime.fromisoformat(env_start).replace(tzinfo=MADRID_TZ)
                log_event(f"[*] Normal Mode: From manual workflow date {since_date.date()}")
            except:
                since_date = get_last_date()
                log_event(f"[*] Normal Mode: Error parsing manual date, using state.json {since_date.date()}")
        else:
            since_date = get_last_date()
            log_event(f"[*] Normal Mode: From last saved date {since_date.date()}")

    # Safety: Ensure since_date is not in the future compared to until_date
    if since_date > until_date:
        since_date = until_date - timedelta(days=1)
        log_event(f"[!] Warning: since_date was in the future. Reset to: {since_date.date()}")

    # 2. Load Multi-source Accounts with Topic Filtering
    accounts_to_scan = []
    feeds_to_scan = []
    sources_file = "data/curation_sources.yaml"
    
    # Topic Inclusion Flags (from Env)
    topic_map = {
        "Kubernetes & Cloud Native": os.getenv("INCLUDE_K8S", "true").lower() == "true",
        "Cloud Providers (AWS/Azure/GCP)": os.getenv("INCLUDE_CLOUD", "true").lower() == "true",
        "AI & Agentic Systems": os.getenv("INCLUDE_AI", "true").lower() == "true",
        "Developer Productivity & AI Agents": os.getenv("INCLUDE_DEV", "true").lower() == "true",
        "Data & Big Data": os.getenv("INCLUDE_DATA", "true").lower() == "true",
        "Infrastructure as Code & GitOps": os.getenv("INCLUDE_IAC", "true").lower() == "true"
    }

    exclude_env = os.getenv("EXCLUDE_ACCOUNTS", "")
    exclude_list = [a.strip().lower() for a in exclude_env.split(",") if a.strip()]

    if os.path.exists(sources_file):
        try:
            with open(sources_file, 'r') as f:
                data = yaml.safe_load(f)
                all_accounts = set()
                for topic_data in data.get("sources", []):
                    topic_name = topic_data.get("topic")
                    if topic_map.get(topic_name, True): # Default to true if topic not in map
                        for acc in topic_data.get("accounts", []):
                            if acc.lower() not in exclude_list:
                                all_accounts.add(acc)
                        for feed in topic_data.get("feeds", []):
                            feeds_to_scan.append(feed)

                if all_accounts:
                    accounts_to_scan = list(all_accounts)
                    log_event(f"[*] Multi-source loaded: {len(accounts_to_scan)} accounts from enabled topics.")
                if feeds_to_scan:
                    log_event(f"[*] RSS Feeds loaded: {len(feeds_to_scan)} technical blogs.")
        except Exception as e:
            log_event(f"[!] Error loading sources: {e}")
    
    if not accounts_to_scan and not exclude_list:
        accounts_to_scan = ["nubenetes"] # Ultimate fallback
        log_event("[*] No accounts found in topics, using default: nubenetes")

    # 3. Multi-source Ingestion
    backup_file = os.getenv("BACKUP_FILE")
    x_audit_trail = []
    raw_social = []

    if backup_file and os.path.exists(backup_file):
        from src.ingestion_backup import BackupDataExtractor
        extractor = BackupDataExtractor(backup_file)
        raw_social = await extractor.fetch_links()
        x_audit_trail = extractor.audit_trail
    else:
        # A. X.com Extraction
        strategy = os.getenv("EXTRACTION_STRATEGY", "search")
        twitter_client = SocialDataExtractor()
        raw_social = await twitter_client.fetch_links_since(since_date, until_date=until_date, strategy=strategy, accounts=accounts_to_scan)
        x_audit_trail = twitter_client.audit_trail

        # B. RSS Extraction
        if feeds_to_scan:
            from src.ingestion_rss import RSSDataExtractor
            rss_client = RSSDataExtractor()
            raw_rss = await rss_client.fetch_links_since(since_date, feeds_to_scan)
            raw_social.extend(raw_rss)
            x_audit_trail.extend(rss_client.audit_trail)
    
    trending = []
    if not is_historical and not backup_file:
        log_event("[*] Searching for news in GitHub Trending...")
        trending = await discover_trending_assets()
        for t in trending: 
            t["source_type"] = "GitHub Trending"
            t["timestamp"] = datetime.now(MADRID_TZ).isoformat()
    
    all_raw_assets = raw_social + trending
    if not all_raw_assets:
        log_event("[!] No new links found to process.")
        return

    # 4. Expansion, Resilient Health Check and Initial Deduplication
    log_event(f"[*] Expanding, verifying and deduplicating {len(all_raw_assets)} raw links...")
    semaphore = asyncio.Semaphore(15)
    
    # User-Agent rotation for resilient discovery
    user_agents = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
    ]

    async def process_asset(asset, idx):
        async with semaphore:
            # 1. Expand URL
            expanded_url = await resolve_url(asset["url"])
            asset["url"] = expanded_url
            
            # 2. Resilient Health Check (Identity Rotation)
            ua = user_agents[idx % len(user_agents)]
            headers = {"User-Agent": ua, "Referer": "https://www.google.com/"}

            # NOTE: All domains must be checked to ensure the link isn't a 404.
            try:
                async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=12, verify=False) as client:
                    resp = await client.get(expanded_url)
                    if resp.status_code == 404:
                        asset["health"] = "dead" # Definitively dead
                    else:
                        asset["health"] = "online"
            except:
                asset["health"] = "timeout" # Assume alive but unreachable for now

            # 3. GitHub Metadata Enrichment
            if "github.com" in expanded_url:
                match = re.search(r'github\.com/([^/]+)/([^/]+)', expanded_url)
                if match:
                    owner, repo = match.groups()
                    repo = repo.split("#")[0].split("?")[0]
                    gh_api = f"https://api.github.com/repos/{owner}/{repo}"
                    gh_headers = {"Authorization": f"token {GH_TOKEN}"} if GH_TOKEN else {}
                    try:
                        async with httpx.AsyncClient(timeout=5.0) as client:
                            gh_resp = await client.get(gh_api, headers=gh_headers)
                            if gh_resp.status_code == 200:
                                gh_data = gh_resp.json()
                                asset["gh_stars"] = gh_data.get("stargazers_count")
                                asset["gh_updated"] = gh_data.get("updated_at", "").split("T")[0]
                    except: pass
            
            return asset

    all_raw_assets = await asyncio.gather(*[process_asset(a, i) for i, a in enumerate(all_raw_assets)])
    
    # Filter out definitively dead links
    initial_count = len(all_raw_assets)
    all_raw_assets = [a for a in all_raw_assets if a.get("health") != "dead"]
    dead_count = initial_count - len(all_raw_assets)
    if dead_count > 0:
        log_event(f"[*] Health Filter: Removed {dead_count} definitively dead (404) links.")

    unique_assets_map = {}
    for asset in all_raw_assets:
        clean_url = asset["url"].split('#')[0].rstrip('/').lower()
        if clean_url not in unique_assets_map:
            unique_assets_map[clean_url] = asset
        else:
            if len(asset.get("context", "")) > len(unique_assets_map[clean_url].get("context", "")):
                unique_assets_map[clean_url] = asset

    all_raw_assets = list(unique_assets_map.values())
    log_event(f"[*] Total after initial deduplication: {len(all_raw_assets)} unique links.")

    # 5. Evaluation and Registration
    from src.gemini_utils import is_fuzzy_duplicate
    existing_urls = set()
    for root, dirs, files in os.walk("docs"):
        for file in files:
            if file.endswith(".md"):
                try:
                    with open(os.path.join(root, file), 'r') as f:
                        content = f.read()
                        found = re.findall(r'\]\((https?://[^\)]+)\)', content)
                        for url in found:
                            existing_urls.add(url.split('#')[0].rstrip('/').lower())
                except: pass
    
    log_event(f"[*] Global Deduplication: {len(existing_urls)} existing URLs loaded.")

    BATCH_SIZE = 40
    all_raw_assets_batches = [all_raw_assets[i:i + BATCH_SIZE] for i in range(0, len(all_raw_assets), BATCH_SIZE)]
    
    curator_agent = AgenticCurator()
    total_processed = 0
    max_tweet_date = since_date
    full_report_metrics = []
    modified_files_content = {}

    for batch_index, batch_assets in enumerate(all_raw_assets_batches):
        log_event(f">>> STARTING BATCH {batch_index + 1}/{len(all_raw_assets_batches)} ({len(batch_assets)} links)", section_break=True)
        assets_to_evaluate = []
        for asset in batch_assets:
            url = asset["url"]
            is_dup = False
            for existing in existing_urls:
                if is_fuzzy_duplicate(url, existing):
                    is_dup = True
                    break

            if is_dup:
                full_report_metrics.append({
                    "url": url, "status": "DUPLICATE", "reason": "Already exists in repository",
                    "category": "N/A", "post_date": asset.get('timestamp'), "source": asset.get("source_type", "Social")
                })
                continue
            
            try:
                ts = asset.get('timestamp')
                asset_date = None
                if ts:
                    if isinstance(ts, str):
                        try:
                            asset_date = datetime.strptime(ts, '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=MADRID_TZ)
                        except:
                            try: asset_date = datetime.fromisoformat(ts.replace('Z', '+00:00'))
                            except: pass
                if asset_date and asset_date > max_tweet_date:
                    max_tweet_date = asset_date
            except: pass

            assets_to_evaluate.append(asset)

        if not assets_to_evaluate: continue

        evaluations = await evaluate_extracted_assets(assets_to_evaluate)
        unique_new_assets = []
        
        for asset in assets_to_evaluate:
            url = asset["url"]
            evaluation = evaluations.get(url, {"status": "FILTERED", "reason": "Not evaluated by AI"})
            
            full_report_metrics.append({
                "url": url, "status": evaluation["status"], "reason": evaluation.get("reason", "Accepted"),
                "category": evaluation.get("category", "N/A"), 
                "related_categories": evaluation.get("related_categories", []),
                "post_date": asset.get("timestamp"),
                "source": asset.get("source_type", "Social"),
                "impact_score": evaluation.get("impact_score", 0),
                "title": evaluation.get("title", "N/A"),
                "language": evaluation.get("language", "English"),
                "type": evaluation.get("resource_type", "Reference")
            })

            if evaluation["status"] == "INCLUDED":
                # Mandate 34: Sanitize new URLs before injection
                sanitized_url = sanitize_trailing_slashes(url)
                unique_new_assets.append({
                    "url": sanitized_url, "title": evaluation["title"],
                    "description": evaluation["description"], 
                    "year": evaluation.get("year", "N/A"),
                    "category": evaluation.get("category", "kubernetes-tools"),
                    "impact_score": evaluation["impact_score"],
                    "reasoning": evaluation.get("reasoning")
                })
                existing_urls.add(normalize_url(sanitized_url))
                for rel_cat in evaluation.get("related_categories", []):
                    interlink_asset = {
                        "url": sanitized_url, "title": evaluation["title"],
                        "description": f"*(Related to {evaluation.get('category')} topic)*",
                        "category": rel_cat, "impact_score": 50 
                    }
                    unique_new_assets.append(interlink_asset)

        if unique_new_assets:
            for asset in unique_new_assets:
                category = asset["category"]
                file_path = f"docs/{category}.md"
                try:
                    if file_path in modified_files_content and asset['url'] in modified_files_content[file_path]:
                        continue
                    if file_path in modified_files_content:
                        content = modified_files_content[file_path]
                    else:
                        if not os.path.exists(file_path):
                            content = f"# {category.capitalize()}\n\n"
                        else:
                            with open(file_path, 'r') as f: content = f.read()
                    
                    if asset['url'] in content: continue 
                    new_content = await curator_agent.decide_smart_injection(content, asset)
                    if len(new_content) > len(content):
                        modified_files_content[file_path] = new_content
                        with open(file_path, 'w') as f: f.write(new_content)
                except Exception as e:
                    log_event(f"  [!] Error injecting {asset['url']}: {e}")

        total_processed += len(batch_assets)
        if batch_index < len(all_raw_assets_batches) - 1:
            await asyncio.sleep(5)

    # 5. Semantic Interlinking (Mandate 5)
    if unique_new_assets:
        try:
            await curator_agent.apply_semantic_interlinking(evaluations)
        except Exception as e:
            log_event(f"  [!] Interlinking Error: {e}")

    # 6. Finalization, Report and PR
    pr_url = None
    if modified_files_content or full_report_metrics:
        metrics = {
            "total_extracted": len(all_raw_assets),
            "start_date": since_date.isoformat(),
            "end_date": datetime.now(MADRID_TZ).isoformat(),
            "full_report": full_report_metrics,
            "x_audit": x_audit_trail
        }
        
        # 6.5. Safety & Mandate Audit (Mandate 1, 28, and Security)
        from src.safety_guard import SafetyGuard
        guard = SafetyGuard()
        safety_report = guard.generate_audit_report() # Non-blocking report

        try:
            # --- BBDD Persistence: Include YAML database files in the PR ---
            from src.config import INVENTORY_PATH
            if os.path.exists(INVENTORY_PATH):
                with open(INVENTORY_PATH, 'r') as f: modified_files_content[INVENTORY_PATH] = f.read()

            pr_url = git_controller.apply_multi_file_changes(
                modified_files_content, 
                metrics, 
                safety_report=safety_report
            )
            if pr_url:
                print(f"PULL_REQUEST_URL: {pr_url}")
        except Exception as e:
            log_event(f"[!] Error creating PR: {e}")

    await curator_agent.suggest_reorganization()

    if max_tweet_date > since_date:
        save_state(max_tweet_date + timedelta(seconds=1))

    if is_historical and is_chunked and since_date > final_stop_date:
        print(f"\nNEXT_CHUNK_START: {since_date.isoformat()}")

    log_event("PROCESS FINISHED SUCCESSFULLY.", section_break=True)

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
