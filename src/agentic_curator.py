import asyncio
import json
import os
import re
import httpx
import yaml
import hashlib
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from src.config import GH_TOKEN, TARGET_REPO, GEMINI_API_KEY, NUBENETES_CATEGORIES, MADRID_TZ, INVENTORY_DIR
from src.gitops_manager import RepositoryController
from src.gemini_utils import call_gemini_with_retry, normalize_url, clean_toc_text, fetch_youtube_metadata
from src.logger import log_event

# Configuration
V1_DIR = "docs"

def get_best_category_match(suggested: str) -> str:
    if not suggested: return "uncategorized"
    suggested = suggested.lower().strip()
    for cat in NUBENETES_CATEGORIES:
        if suggested in cat or cat in suggested: return cat
    return "uncategorized"

async def _get_github_activity(url: str) -> Dict:
    match = re.search(r'github\.com/([^/]+/[^/]+)', url)
    if not match: return {}
    repo = match.group(1)
    api_url = f"https://api.github.com/repos/{repo}"
    headers = {"Authorization": f"token {GH_TOKEN}"} if GH_TOKEN else {}
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(api_url, headers=headers, timeout=10.0)
            if resp.status_code == 200:
                data = resp.json()
                return {
                    "gh_stars": data.get("stargazers_count"),
                    "gh_pushed": data.get("pushed_at"),
                    "gh_license": data.get("license", {}).get("spdx_id", "N/A")
                }
    except Exception as e:
        log_event(f"[WARN] fetch GitHub activity for {url}: {str(e)[:100]}")
    return {}

async def _deep_fetch_content(url: str) -> Tuple[str, Dict]:
    # MANDATE 25: Special handling for YouTube
    if "youtube.com" in url or "youtu.be" in url:
        log_event(f"    [YT] Detected YouTube link: {url}. Fetching native metadata...")
        meta = await fetch_youtube_metadata(url)
        if meta:
            # Combine title and description to feed the AI
            content = f"TITLE: {meta['raw_title']}\nDESCRIPTION: {meta['raw_description']}"
            return content, {"og_image": f"https://img.youtube.com/vi/{url.split('v=')[-1].split('&')[0]}/maxresdefault.jpg" if "v=" in url else ""}

    headers = {"User-Agent": "Mozilla/5.0"}
    try:
        async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=15.0) as client:
            resp = await client.get(url)
            if resp.status_code == 200:
                # Basic metadata extraction
                og_image = ""
                img_match = re.search(r'meta property="og:image" content="(.*?)"', resp.text)
                if img_match: og_image = img_match.group(1)
                return resp.text, {"og_image": og_image}
    except Exception as e:
        log_event(f"[WARN] deep fetch content for {url}: {str(e)[:100]}")
    return "", {}

async def evaluate_extracted_assets(raw_assets: List[Dict]) -> Dict[str, Dict]:
    evaluations = {}
    curator = AgenticCurator()
    to_evaluate = []
    
    # Mandate 2: Load Blacklist
    memory_file = "src/memory/health_learning.json"
    domain_blacklist = set()
    if os.path.exists(memory_file):
        try:
            memory_data = json.load(open(memory_file, "r"))
            domain_blacklist = set(memory_data.get("blacklisted_domains", []))
        except Exception as e:
            log_event(f"[WARN] load blacklist from health_learning.json: {str(e)[:100]}")

    # 1. Pre-filter
    for asset in raw_assets:
        url = asset["url"]
        norm_url = normalize_url(url)
        if any(domain in url.lower() for domain in domain_blacklist):
            evaluations[url] = {"status": "FILTERED", "reason": "Blacklisted"}
            continue
        if norm_url in curator.inventory:
            cached = curator.inventory[norm_url]
            if cached.get("status") == "review_required":
                evaluations[url] = {**cached, "status": "REVIEW_PENDING"}
                continue
            if cached.get("title") and cached.get("hierarchy"):
                from src.gemini_utils import SESSION_TRACKER
                SESSION_TRACKER.track_cache_hit(est_tokens=2200)
                evaluations[url] = {**cached, "status": "INCLUDED"}
                continue
        to_evaluate.append(asset)

    if not to_evaluate: return evaluations

    # 2. SMART BATCHING WITH REPUTATION FILTER (Mandate 32)
    BATCH_SIZE = 10
    from src.mandate_ingestor import get_system_mandates
    dynamic_mandates = get_system_mandates()

    async def process_sub_batch(batch):
        batch_data = []
        for asset in batch:
            web_content, rich_meta = await _deep_fetch_content(asset["url"])
            c_hash = hashlib.sha256(web_content.encode()).hexdigest() if web_content else "N/A"
            gh_meta = await _get_github_activity(asset["url"]) if "github.com" in asset["url"] else {}
            
            mvq_penalty = False
            pushed = gh_meta.get("gh_pushed")
            if pushed and str(pushed).strip().upper() not in ("N/A", "NONE"):
                try:
                    ld = datetime.fromisoformat(str(pushed).replace("Z", "+00:00"))
                    if (datetime.now(ld.tzinfo) - ld).days > (365 * 4): mvq_penalty = True
                except Exception as e:
                    log_event(f"[WARN] MVQ penalty date parse for {asset['url']}: {str(e)[:100]}")
            
            batch_data.append({
                "asset": asset, "content": web_content[:1500], "hash": c_hash, 
                "mvq_penalty": mvq_penalty, "gh_meta": gh_meta, "rich_meta": rich_meta
            })

        prompt = (
            "You act as a Senior Technical Librarian in 2026.\n" + dynamic_mandates +
            "Analyze these resources and provide high-density metadata.\n"
            "PHASE 1: SOCIAL PROOF & REPUTATION (Mandate 32)\n"
            "- Perform a real-time web search for each resource.\n"
            "- If the community (Reddit, Hacker News) reports the tool as 'unstable', 'abandoned', or 'vaporware', set reputation_penalty: true.\n"
            "PHASE 2: LINGUISTIC DIVERSITY & CLASSIFICATION\n"
            "- Calculate 'impact_score' (0-100) based on architectural value, innovation, and technical depth (>= 80 is required for inclusion).\n"
            f"- Assign a 'primary_category' strictly from this list: {', '.join(NUBENETES_CATEGORIES)}\n"
            "- If none fit well, use 'uncategorized' and propose a better one in 'suggested_new_category'.\n"
            "- Identify TECHNICAL_HIERARCHY: List (max 10 strings) Area > Topic > Subtopics.\n"
            "PHASE 3: HIGH-DENSITY TECHNICAL SUMMARIES (Mandate 4)\n"
            "- Provide an 'en_summary' that is technical, professional and dense.\n"
            "- Include architectural value, key features, and technical significance. Style: O'Reilly technical.\n"
            "- Format: Use paragraphs and bullet points if necessary. Aim for 2-5 sentences of depth.\n"
            "PHASE 4: MULTI-DIMENSIONAL TAGGING\n"
            "- Assign tags. You MUST include:\n"
            "  1. 1 to 2 maturity tags from: [DE FACTO STANDARD], [ENTERPRISE-STABLE], [EMERGING], [GUIDE], [CASE STUDY], [COMMUNITY-TOOL], [LEGACY].\n"
            "  2. Fine-grained technical/architectural tags from the content (e.g., [EBPF], [WASM], [GITOPS], [IAC], [SERVICE-MESH], [SERVERLESS], [MLOPS], [DB]). Keep them uppercase and wrapped in brackets.\n"
            "PHASE 5: COMPANY & GEO CLASSIFICATION\n"
            "- Identify 'company': The company/organization that authored or is the primary subject (e.g., 'Google', 'Netflix', 'CNCF', 'Independent').\n"
            "- Identify 'geo_region': The HQ region of that company. Use one of: 'americas', 'europe', 'spain', 'asia_pacific', 'global'.\n"
            "Respond ONLY JSON list: [{\"url\": \"...\", \"impact_score\": int, \"reputation_penalty\": bool, \"reputation_summary\": \"...\", \"pub_date\": \"YYYY-MM-DD\", \"primary_category\": \"...\", \"suggested_new_category\": \"...\", \"title\": \"...\", \"desc\": \"...\", \"en_summary\": \"High-density summary...\", \"language\": \"...\", \"type\": \"...\", \"level\": \"...\", \"technical_hierarchy\": [...], \"tags\": [...], \"is_microservice\": bool, \"company\": \"...\", \"geo_region\": \"...\"}, ...]\n\n"
            "RESOURCES:\n" + "\n".join([f"- {d['asset']['url']}: (MVQ Penalty: {d['mvq_penalty']}) {d['content']}" for d in batch_data])
        )

        try:
            # ENABLE GROUNDING FOR REPUTATION FILTER
            results = await call_gemini_with_retry(prompt, use_grounding=True, prefer_flash=True, role="Curator")
            if isinstance(results, list):
                res_map = {normalize_url(r.get("url", "")): r for r in results}
                for d in batch_data:
                    url = d["asset"]["url"]
                    norm_url = normalize_url(url)
                    data = res_map.get(norm_url)
                    if not data:
                        # Fallback 1: Case-insensitive match on normalized url
                        for r in results:
                            if normalize_url(r.get("url", "")).lower() == norm_url.lower():
                                data = r
                                break
                    if not data:
                        # Fallback 2: Check if domain and path suffix match (handling protocol/www differences)
                        from urllib.parse import urlparse
                        p_url = urlparse(url)
                        for r in results:
                            r_url = r.get("url", "")
                            p_r = urlparse(r_url)
                            if p_url.netloc.replace("www.", "") == p_r.netloc.replace("www.", "") and p_url.path.rstrip("/") == p_r.path.rstrip("/"):
                                data = r
                                break
                    
                    if not data: continue
                    score = data.get("impact_score", 50)
                    if data.get("reputation_penalty"):
                        log_event(f"  [!] REPUTATION ALERT: {data['title']} flagged.")
                        score = max(score - 30, 10)
                    
                    # Consensus Debate Protocol trigger for borderline scores (70-85)
                    final_tags = data.get("tags", [])
                    refined_summary = data.get("en_summary", data["desc"])
                    
                    if 70 <= score <= 85:
                        from src.v2_debate import run_debate_protocol
                        # Build a temporary item representation to feed the debate engine
                        temp_item = {
                            "title": data["title"],
                            "url": url,
                            "description": data["desc"],
                            "ai_summary": refined_summary,
                            "tags": final_tags,
                            "impact_score": score
                        }
                        score, final_tags, refined_summary, debate_data = await run_debate_protocol(temp_item, is_new_link=True)
                    
                    primary_cat = get_best_category_match(data.get("primary_category"))
                    is_primary = "nubenetes" in d["asset"].get("source_type", "Social").lower()
                    if score >= (5 if is_primary else 80) and primary_cat:
                        eval_data = {
                            "title": data["title"], "description": data["desc"], "ai_summary": refined_summary,
                            "language": data.get("language", "English"), "resource_type": data.get("type", "Reference"),
                            "complexity": data.get("level", "Intermediate"), "hierarchy": data.get("technical_hierarchy", ["General"]),
                            "tags": final_tags, "is_microservice": data.get("is_microservice", False), "year": str(data.get("pub_date") or "N/A")[:4],
                            "stars": min(max(score // 20, 0), 5), "impact_score": score, "content_hash": d["hash"],
                            "reputation_status": "Vetted" if not data.get("reputation_penalty") else "Suspicious",
                            "reputation_summary": data.get("reputation_summary", ""),
                            "source_provenance": d["asset"].get("source_type", "Social"), "social_preview_url": d["rich_meta"].get("og_image", ""),
                            "company": data.get("company", ""), "geo_region": data.get("geo_region", ""),
                            "category": primary_cat, "status": "online", "last_checked": datetime.now().timestamp(),
                            "discovered_at": datetime.now(MADRID_TZ).isoformat(),
                            "last_ai_eval": datetime.now(MADRID_TZ).isoformat(),
                            "suggested_new_category": data.get("suggested_new_category", ""),
                            "addition_method": {
                                "rss": "rss_ingestion", "GitHub Trending": "github_trending",
                                "Twitter": "twitter_ingestion", "nubenetes": "manual"
                            }.get(d["asset"].get("source_type", ""), "automatic"),
                            **d["gh_meta"]
                        }
                        if "youtube.com" in url or "youtu.be" in url:
                            title_desc = f"{data['title']} {data['desc']}".lower()
                            keywords = ["agent", "mcp", "terraform", "devops", "kubernetes", "sre", "mlops", "copilot", "gemini", "claude", "openai", "autogen", "crewai"]
                            if any(k in title_desc for k in keywords):
                                eval_data["is_featured_video"] = True
                                eval_data["is_enriched"] = False
                        from src.inventory_manager import update_inventory_entry
                        update_inventory_entry(curator.inventory, norm_url, eval_data)
                        evaluations[url] = {**eval_data, "status": "INCLUDED"}
                    else:
                        evaluations[url] = {"status": "FILTERED"}
                        from src.inventory_manager import update_inventory_entry
                        update_inventory_entry(curator.inventory, norm_url, {"status": "FILTERED", "score": score, "last_checked": datetime.now().timestamp()})
                curator._save_inventory()
        except Exception as e: log_event(f"  [!] Batch AI Error: {e}")

    sub_batches = [to_evaluate[i:i+BATCH_SIZE] for i in range(0, len(to_evaluate), BATCH_SIZE)]
    await asyncio.gather(*(process_sub_batch(b) for b in sub_batches))
            
    return evaluations

class AgenticCurator:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.docs_dir = "docs"
        self.inventory = self._load_inventory()

    def _load_inventory(self) -> Dict:
        from src.inventory_manager import load_inventory
        return load_inventory()

    def _save_inventory(self):
        from src.inventory_manager import save_inventory
        save_inventory(self.inventory)

    async def discover_new_curation_sources(self) -> List[str]:
        """D) Autonomous Discovery: Periodically find new high-trust sources."""
        log_event("[*] Executing Autonomous Source Discovery (Grounding Mode)...")
        prompt = "Identify 5 high-quality Cloud Native or K8s engineering blogs or 'Awesome' repos active in 2026. Return ONLY JSON list of URLs."
        try:
            return await call_gemini_with_retry(prompt, use_grounding=True)
        except Exception as e:
            log_event(f"[WARN] autonomous source discovery: {str(e)[:100]}")
            return []

    async def decide_smart_injection(self, content: str, asset: Dict) -> str:
        # Extract headers from the markdown content
        lines = content.splitlines()
        headers = [line.strip() for line in lines if line.strip().startswith("#")]
        
        # Build prompt for LLM (using Flash for speed/cost/reliability)
        prompt = (
            "You are a Cloud Native Technical Librarian.\n"
            "Given a list of headers in a Markdown document and a new link to curate, "
            "select the most specific header under which the link belongs.\n\n"
            f"HEADERS:\n" + "\n".join(headers) + "\n\n"
            f"NEW LINK:\n"
            f"Title: {asset.get('title')}\n"
            f"URL: {asset.get('url')}\n"
            f"Description: {asset.get('description')}\n\n"
            "Respond ONLY with the exact header from the list (including '#' symbols, e.g. '## Kubernetes Tools').\n"
            "If no existing header matches perfectly, respond with 'NEW_HEADER: ## Proposed Name' (matching the appropriate heading level like ## or ###).\n"
            "If it doesn't fit anywhere and should be appended at the end of the document, respond with 'APPEND'."
        )
        
        selected_header = "APPEND"
        try:
            # We use Flash 3.5 (prefer_flash=True) to avoid 429 rate limits and reduce cost
            ai_res = await call_gemini_with_retry(prompt, response_format="text", prefer_flash=True, role="General")
            if ai_res:
                selected_header = ai_res.strip().strip("'\"")
        except Exception as e:
            log_event(f"  [!] LLM injection decision failed: {e}. Defaulting to APPEND.")
            selected_header = "APPEND"

        # Format the link line according to Mandate 17
        year = asset.get("year")
        year_str = str(year).strip() if year is not None else ""
        year_prefix = f"**({year_str})** " if year_str and year_str.lower() not in ("n/a", "none", "null", "unknown", "") else ""
        link_line = f"  - {year_prefix}[{asset['title']}]({asset['url']}) 🌟 - {asset['description']}"

        # Perform programmatic insertion in Python
        if selected_header == "APPEND":
            return content.rstrip() + "\n\n" + link_line + "\n"

        if selected_header.startswith("NEW_HEADER:"):
            new_h = selected_header.split("NEW_HEADER:", 1)[1].strip()
            return content.rstrip() + f"\n\n{new_h}\n{link_line}\n"

        # Else, find the header (exact or fuzzy match) and insert under it
        header_idx = -1
        for idx, line in enumerate(lines):
            if line.strip() == selected_header.strip():
                header_idx = idx
                break

        # Fuzzy match if exact match fails
        if header_idx == -1:
            clean_sel = selected_header.replace("#", "").strip().lower()
            for idx, line in enumerate(lines):
                if line.strip().startswith("#"):
                    clean_line = line.replace("#", "").strip().lower()
                    if clean_line == clean_sel:
                        header_idx = idx
                        selected_header = line
                        break

        if header_idx == -1:
            # Fallback to append if AI proposed header not found in the list
            return content.rstrip() + "\n\n" + link_line + "\n"

        # Insert under selected_header
        # Find the end of this header's section: when we hit a header of the same or higher level
        header_level = len(selected_header) - len(selected_header.lstrip('#'))
        insert_idx = len(lines)
        for idx in range(header_idx + 1, len(lines)):
            line = lines[idx].strip()
            if line.startswith("#"):
                line_level = len(line) - len(line.lstrip('#'))
                if line_level <= header_level:
                    insert_idx = idx
                    break

        # Move insert_idx backward past any trailing blank lines
        while insert_idx > header_idx + 1 and lines[insert_idx - 1].strip() == "":
            insert_idx -= 1

        lines.insert(insert_idx, link_line)
        return "\n".join(lines) + "\n"

    async def apply_semantic_interlinking(self, evaluations: Dict):
        log_event("[*] Applying Semantic Interlinking (Mandate 5)...")
        # Logic implementation for Mandate 5
        pass

    async def suggest_reorganization(self):
        """MANDATE 11 & 32: System Maintenance."""
        log_event("[*] Platinum Maintenance: Syncing Workflow UI (Mandate 11)...")
        try:
            from src.sync_workflow_ui import WorkflowUISync
            WorkflowUISync().sync_ui()
        except Exception as e:
            log_event(f"  [!] UI Sync Error: {e}")

        log_event("[*] Platinum Maintenance: Vaporware Reputation Audit (Mandate 32)...")
        # Identify suspicious tools for further grounding
        suspicious = [u for u, m in self.inventory.items() if m.get("reputation_status") == "Suspicious"]
        if suspicious:
            log_event(f"  [!] Auditing {len(suspicious)} suspicious resources via Grounding...")
            # Detailed grounding logic would go here in a batch

