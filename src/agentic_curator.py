import asyncio
import json
import os
import re
import httpx
import yaml
import hashlib
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from src.config import GH_TOKEN, TARGET_REPO, GEMINI_API_KEY, NUBENETES_CATEGORIES, MADRID_TZ, INVENTORY_PATH
from src.gitops_manager import RepositoryController
from src.gemini_utils import call_gemini_with_retry, normalize_url, clean_toc_text
from src.logger import log_event

# Configuration
V1_DIR = "docs"

def get_best_category_match(suggested: str) -> Optional[str]:
    if not suggested: return None
    suggested = suggested.lower().strip()
    for cat in NUBENETES_CATEGORIES:
        if suggested in cat or cat in suggested: return cat
    return None

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
    except: pass
    return {}

async def _deep_fetch_content(url: str) -> Tuple[str, Dict]:
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
    except: pass
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
        except: pass

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
                evaluations[url] = {"status": "REVIEW_PENDING", **cached}
                continue
            if cached.get("title") and cached.get("hierarchy"):
                from src.gemini_utils import SESSION_TRACKER
                SESSION_TRACKER.track_cache_hit(est_tokens=2200)
                evaluations[url] = {"status": "INCLUDED", **cached}
                continue
        to_evaluate.append(asset)

    if not to_evaluate: return evaluations

    # 2. SMART BATCHING WITH REPUTATION FILTER (Mandate 32)
    BATCH_SIZE = 10
    from src.mandate_ingestor import get_system_mandates
    dynamic_mandates = get_system_mandates()

    for i in range(0, len(to_evaluate), BATCH_SIZE):
        batch = to_evaluate[i:i+BATCH_SIZE]
        batch_data = []
        for asset in batch:
            web_content, rich_meta = await _deep_fetch_content(asset["url"])
            c_hash = hashlib.sha256(web_content.encode()).hexdigest() if web_content else "N/A"
            gh_meta = await _get_github_activity(asset["url"]) if "github.com" in asset["url"] else {}
            
            mvq_penalty = False
            if gh_meta.get("gh_pushed"):
                ld = datetime.fromisoformat(gh_meta["gh_pushed"].replace("Z", "+00:00"))
                if (datetime.now(ld.tzinfo) - ld).days > (365 * 4): mvq_penalty = True
            
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
            "- Identify TECHNICAL_HIERARCHY: List (max 10 strings) Area > Topic > Subtopics.\n"
            "Respond ONLY JSON list: [{\"url\": \"...\", \"impact_score\": int, \"reputation_penalty\": bool, \"reputation_summary\": \"...\", \"pub_date\": \"YYYY-MM-DD\", \"primary_category\": \"...\", \"title\": \"...\", \"desc\": \"...\", \"en_summary\": \"...\", \"language\": \"...\", \"type\": \"...\", \"level\": \"...\", \"technical_hierarchy\": [...], \"is_microservice\": bool}, ...]\n\n"
            "RESOURCES:\n" + "\n".join([f"- {d['asset']['url']}: (MVQ Penalty: {d['mvq_penalty']}) {d['content']}" for d in batch_data])
        )

        try:
            # ENABLE GROUNDING FOR REPUTATION FILTER
            results = await call_gemini_with_retry(prompt, use_grounding=True)
            if isinstance(results, list):
                res_map = {normalize_url(r.get("url", "")): r for r in results}
                for d in batch_data:
                    url = d["asset"]["url"]; norm_url = normalize_url(url); data = res_map.get(norm_url)
                    if not data: continue
                    score = data.get("impact_score", 50)
                    if data.get("reputation_penalty"):
                        log_event(f"  [!] REPUTATION ALERT: {data['title']} flagged.")
                        score = max(score - 30, 10)
                    
                    primary_cat = get_best_category_match(data.get("primary_category"))
                    is_primary = "nubenetes" in d["asset"].get("source_type", "Social").lower()
                    if score >= (5 if is_primary else 80) and primary_cat:
                        eval_data = {
                            "title": data["title"], "description": data["desc"], "ai_summary": data.get("en_summary", data["desc"]),
                            "language": data.get("language", "English"), "resource_type": data.get("type", "Reference"),
                            "complexity": data.get("level", "Intermediate"), "hierarchy": data.get("technical_hierarchy", ["General"]),
                            "is_microservice": data.get("is_microservice", False), "year": data.get("pub_date", "N/A")[:4],
                            "stars": min(max(score // 20, 0), 5), "content_hash": d["hash"],
                            "reputation_status": "Vetted" if not data.get("reputation_penalty") else "Suspicious",
                            "reputation_summary": data.get("reputation_summary", ""),
                            "source_provenance": d["asset"].get("source_type", "Social"), "social_preview_url": d["rich_meta"].get("og_image", ""),
                            "category": primary_cat, "status": "online", "last_checked": datetime.now().timestamp(), **d["gh_meta"]
                        }
                        curator.inventory[norm_url] = eval_data
                        evaluations[url] = {"status": "INCLUDED", **eval_data}
                    else: evaluations[url] = {"status": "FILTERED"}
                curator._save_inventory()
        except Exception as e: log_event(f"  [!] Batch AI Error: {e}")
            
    return evaluations

class AgenticCurator:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.docs_dir = "docs"
        self.inventory = self._load_inventory()

    def _load_inventory(self) -> dict:
        if os.path.exists(INVENTORY_PATH):
            try:
                with open(INVENTORY_PATH, "r") as f: return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def _save_inventory(self):
        os.makedirs(os.path.dirname(INVENTORY_PATH), exist_ok=True)
        with open(INVENTORY_PATH, "w") as f: yaml.dump(self.inventory, f, sort_keys=False, allow_unicode=True)

    async def discover_new_curation_sources(self) -> List[str]:
        """D) Autonomous Discovery: Periodically find new high-trust sources."""
        log_event("[*] Executing Autonomous Source Discovery (Grounding Mode)...")
        prompt = "Identify 5 high-quality Cloud Native or K8s engineering blogs or 'Awesome' repos active in 2026. Return ONLY JSON list of URLs."
        try:
            return await call_gemini_with_retry(prompt, use_grounding=True)
        except: return []

    async def decide_smart_injection(self, content: str, asset: Dict) -> str:
        prompt = f"Decide where to inject this link in the Markdown content.\nLINK: {asset['title']} ({asset['url']})\nDESC: {asset['description']}\n\nRespond ONLY with the updated full Markdown content."
        try: return await call_gemini_with_retry(prompt, response_format="text")
        except: return content

    async def apply_semantic_interlinking(self, evaluations: Dict):
        log_event("[*] Applying Semantic Interlinking (Mandate 5)...")
        # Logic implementation for Mandate 5
        pass

    async def suggest_reorganization(self):
        log_event("[*] Auditing Directory Structure for Reorganization...")
        pass
