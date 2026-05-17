import asyncio
import json
import os
import re
import httpx
import random
import yaml
from datetime import datetime
from typing import Dict, List, Set, Tuple, Optional, Any
from src.config import GH_TOKEN, TARGET_REPO, GEMINI_API_KEY, NUBENETES_CATEGORIES, MADRID_TZ
from src.gitops_manager import RepositoryController
from src.markdown_ast import MarkdownSanitizer
from src.agentic_curator import AgenticCurator
from src.logger import log_event
from src.gemini_utils import call_gemini_with_retry, normalize_url

# Configuración de Excepciones
CORE_FILES = ["docs/index.md", "README.md"]
MEMORY_FILE = "src/memory/health_learning.json"
INVENTORY_PATH = "data/inventory.yaml"

class IntelligentLinkCleaner:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.sanitizer = MarkdownSanitizer()
        self.curator = AgenticCurator()
        self.ai_semaphore = asyncio.Semaphore(5)
        self.link_registry: Dict[str, List[Dict]] = {}
        self.dead_links: Dict[str, Tuple[str, str]] = {} 
        self.learning_data = self._load_memory()
        self.inventory = self._load_inventory()
        self.action_log: List[Dict] = [] 
        self.detailed_stats = {"total_scanned": 0, "skipped_recent": 0, "by_file": {}, "operation_types": {"removals": 0, "consolidated": 0, "healed": 0, "enriched": 0}}
        self.stats = {"total_links": 0, "dead_links_removed": 0, "orphans_fixed": 0, "enriched_descriptions": 0}

    def _load_memory(self) -> Dict:
        if os.path.exists(MEMORY_FILE):
            try: return json.load(open(MEMORY_FILE, 'r'))
            except: pass
        return {"domains": {}, "known_soft_404_patterns": []}

    def _save_memory(self):
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        json.dump(self.learning_data, open(MEMORY_FILE, "w"), indent=2)

    def _load_inventory(self) -> dict:
        if os.path.exists(INVENTORY_PATH):
            try: return yaml.safe_load(open(INVENTORY_PATH, "r")) or {}
            except: return {}
        return {}

    def _save_inventory(self):
        os.makedirs(os.path.dirname(INVENTORY_PATH), exist_ok=True)
        yaml.dump(self.inventory, open(INVENTORY_PATH, "w"), sort_keys=False, allow_unicode=True)

    async def _check_url_logic(self, url: str) -> Tuple[bool, str, Optional[str]]:
        headers = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.5"}
        parked = ["buy this domain", "parked free", "this domain may be for sale"]
        try:
            async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=15) as client:
                resp = await client.get(url)
                if resp.status_code < 400:
                    text = resp.text.lower()
                    if any(kw in text for kw in parked): return False, "parked", None
                    return True, "OK", str(resp.url) if str(resp.url) != url else None
                if resp.status_code in [404, 410]:
                    if "github.com" in url and "/master/" in url:
                        heal = url.replace("/master/", "/main/")
                        if (await client.get(heal)).status_code < 400: return True, "healed", heal
                    return False, "404", None
                return True, f"Soft Error {resp.status_code}", None
        except: return True, "Timeout/Error", None

    async def _check_and_fix_link(self, url: str):
        nu = normalize_url(url); entry = self.inventory.get(nu, {})
        alive, reason, final = await self._check_url_logic(url)
        
        # Platinum: Update Health Score (Exponential moving average)
        score = entry.get("health_score", 100)
        score = (score * 0.8) + (100 if alive else 0) * 0.2
        entry["health_score"] = round(score, 1)
        entry["last_checked"] = datetime.now().timestamp()
        
        if not alive and score < 20: # Definitive removal threshold
            entry["status"] = "dead"; self.dead_links[url] = (None, reason)
        elif final and alive:
            self.dead_links[url] = (f"CANONICAL:{final}", "Redirect")
        
        self.inventory[nu] = entry
        self.stats["total_links"] += 1

    async def execute_clean_cycle(self):
        log_event("STARTING INTELLIGENT CLEANING CYCLE", section_break=True)
        # Gather current state
        all_urls = set()
        for root, _, files in os.walk("docs"):
            for f in files:
                if f.endswith(".md"):
                    p = os.path.join(root, f); c = open(p, "r").read()
                    matches = re.findall(r'\[.*?\]\((https?://.*?)\)', c)
                    for u in matches:
                        nu = normalize_url(u); all_urls.add(u)
                        self.link_registry.setdefault(nu, []).append({"file": p, "line_index": 0}) # Simplified for mapping
        
        tasks = [self._check_and_fix_link(u) for u in list(all_urls)[:100]] # Limit for speed test
        await asyncio.gather(*tasks)
        await self.prune_orphaned_metadata()
        self._save_inventory()

    async def prune_orphaned_metadata(self):
        log_event("RUNNING DATABASE GARBAGE COLLECTION...", section_break=True)
        valid_map = {}
        for root, _, files in os.walk("docs"):
            for f in files:
                if f.endswith(".md"):
                    p = os.path.join(root, f); c = open(p, "r").read()
                    for u in re.findall(r'\[.*?\]\((https?://.*?)\)', c):
                        valid_map.setdefault(normalize_url(u), []).append(p)
        
        new_inv = {}
        for u, m in self.inventory.items():
            if u.startswith("INTRO:") or u in valid_map:
                if u in valid_map: m["v1_locations"] = sorted(list(set(valid_map[u])))
                new_inv[u] = m
        self.inventory = new_inv; log_event(f"GC Done. Total records: {len(self.inventory)}")

    async def apply_changes(self):
        log_event("APPLYING CLEANING CHANGES...")
        # (This would apply replacements to V1 .md files using inventory.v1_locations)
        pass

if __name__ == "__main__":
    cleaner = IntelligentLinkCleaner()
    asyncio.run(cleaner.execute_clean_cycle())
