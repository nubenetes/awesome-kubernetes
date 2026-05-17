import asyncio
import json
import os
import re
import httpx
import random
import yaml
import hashlib
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

    async def execute_clean_cycle(self):
        log_event("STARTING INTELLIGENT CLEANING CYCLE", section_break=True)
        # 1. Map all links in V1
        for root, _, files in os.walk("docs"):
            for f in files:
                if f.endswith(".md"):
                    path = os.path.join(root, f)
                    content = open(path, "r").read()
                    lines = content.splitlines()
                    for idx, line in enumerate(lines):
                        urls = re.findall(r'\[.*?\]\((https?://.*?)\)', line)
                        for url in urls:
                            nu = normalize_url(url)
                            self.link_registry.setdefault(nu, []).append({"file": path, "line_index": idx, "url": url})
        
        unique_urls = list(self.link_registry.keys())
        random.shuffle(unique_urls)
        
        # 1.5. INCREMENTAL SELF-CORRECTION: Identify 'Suspicious' URLs in BBDD
        # If a link is 'online' but looks too generic compared to its V1 title, force check.
        to_check = []
        for u in unique_urls:
            nu = normalize_url(u)
            entry = self.inventory.get(nu, {})
            # If it's a home/about page but has a specific technical title, it's suspicious
            is_suspicious = False
            if entry.get("status") == "online":
                path = nu.split("://")[-1].rstrip("/")
                # Generic redirect indicators
                if path.count("/") <= 1 or any(kw in path for kw in ["/about", "/products", "/index", "/whats-new"]):
                    is_suspicious = True
            
            if is_suspicious or entry.get("needs_ai_refresh") or os.getenv("FORCE_FULL_CHECK") == "true":
                to_check.append(u)
            elif (datetime.now().timestamp() - entry.get("last_checked", 0)) > (86400 * 21):
                to_check.append(u) # Standard 21-day rotation

        log_event(f"[*] Queue: {len(to_check)} links prioritized for validation (including {len([u for u in to_check if u not in unique_urls])} suspicious).")

        # 2. Resilient Check
        BATCH_SIZE = 20
        for i in range(0, len(to_check), BATCH_SIZE):
            batch = to_check[i:i+BATCH_SIZE]
            tasks = [self._check_and_fix_link(url) for url in batch]
            await asyncio.gather(*tasks)
            if i % 100 == 0: log_event(f"  [>] Progress: {i}/{len(to_check)} checked...")

        # 3. Finalize
        await self.apply_changes()

    async def _check_and_fix_link(self, url: str):
        nu = normalize_url(url); entry = self.inventory.get(nu, {})
        alive, reason, final = await self._check_url_logic(url)
        
        # --- MANDATE 31: RESCUE PROTOCOL (Universal) ---
        if (not alive or reason == "generic_redirect_loss"):
            log_event(f"  [🔍] RESCUE ATTEMPT: '{entry.get('title', url)}' is missing. Searching new location...")
            new_location = await self._try_rescue_link(url, entry.get("title", ""))
            if new_location:
                log_event(f"  [✨] RESCUED: Found at {new_location}")
                alive, reason, final = True, "resurrected", new_location

        # 1. Update Health Score
        score = entry.get("health_score", 100)
        score = (score * 0.8) + (100 if alive else 0) * 0.2
        entry["health_score"] = round(score, 1)
        entry["last_checked"] = datetime.now().timestamp()
        
        # 2. Semantic Drift Detection (SHA256)
        if alive:
            from src.agentic_curator import _deep_fetch_content
            text, _ = await _deep_fetch_content(url if not final else final)
            new_hash = hashlib.sha256(text.encode()).hexdigest() if text else "N/A"
            old_hash = entry.get("content_hash", "N/A")
            
            if old_hash != "N/A" and new_hash != old_hash:
                log_event(f"  [!] DRIFT DETECTED: {url} (Content changed). Marking for re-evaluation.")
                entry["needs_ai_refresh"] = True
                entry["content_hash"] = new_hash
            elif old_hash == "N/A":
                entry["content_hash"] = new_hash

        if not alive and score < 20: 
            entry["status"] = "dead"; self.dead_links[url] = (None, reason)
        elif final and alive:
            self.dead_links[url] = (f"CANONICAL:{final}", "Redirect")
        
        self.inventory[nu] = entry

    async def _try_rescue_link(self, old_url: str, title: str) -> Optional[str]:
        """
        Uses Gemini to identify the new home of a technical resource.
        Universal application for all links (Mandate 31).
        """
        if not title: return None
        prompt = (
            f"You act as a Technical Librarian. The resource '{title}' was at '{old_url}'.\n"
            "The site has migrated or restructured. Identify the NEW specific URL for this technical content.\n"
            "Search for the direct equivalent, not a home page.\n"
            "Return ONLY the raw URL. If not found, return 'NONE'."
        )
        try:
            async with self.ai_semaphore:
                new_url = await call_gemini_with_retry(prompt, response_format="text", prefer_flash=False)
                if new_url and new_url.startswith("http") and normalize_url(new_url) != normalize_url(old_url):
                    async with httpx.AsyncClient(timeout=10, follow_redirects=True) as client:
                        resp = await client.get(new_url)
                        if resp.status_code < 400: return new_url
        except: pass
        return None

    async def _check_url_logic(self, url: str) -> Tuple[bool, str, Optional[str]]:
        headers = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.5"}
        parked_indicators = ["buy this domain", "parked free", "domain is for sale"]
        try:
            async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=12) as client:
                resp = await client.get(url)
                if resp.status_code < 400:
                    text = resp.text.lower()
                    if any(kw in text for kw in parked_indicators): return False, "parked", None
                    
                    final_url = str(resp.url)
                    
                    # Mandate 31: Content-URL Precision (Generic Redirect Detection)
                    if final_url != url:
                        u_path = url.split("://")[-1].rstrip("/")
                        f_path = final_url.split("://")[-1].rstrip("/")
                        generic_segments = ["/about", "/home", "/index", "/whats-new", "/es/", "/en/", "/products/"]
                        is_deep_orig = u_path.count("/") >= 3
                        is_shallow_final = f_path.count("/") <= 2 or any(f_path.endswith(s) for s in generic_segments)
                        
                        if is_deep_orig and is_shallow_final:
                            return False, "generic_redirect_loss", None

                    return True, "OK", final_url if final_url != url else None
                
                if resp.status_code in [404, 410]:
                    if "github.com" in url and "/master/" in url:
                        heal = url.replace("/master/", "/main/")
                        try:
                            if (await client.get(heal)).status_code < 400: return True, "healed", heal
                        except: pass
                    
                    if "github.com" in url:
                        match = re.search(r'(https?://github\.com/[^/]+/[^/]+)', url)
                        if match:
                            root_url = match.group(1)
                            if root_url != url:
                                try:
                                    if (await client.get(root_url)).status_code < 400:
                                        return True, "consolidated_to_root", root_url
                                except: pass
                    return False, "404", None
                return True, f"Soft Block {resp.status_code}", None
        except: return True, "Connection Error", None

    async def apply_changes(self):
        log_event("APPLYING CLEANING CHANGES & PR GENERATION...", section_break=True)
        file_updates = {}
        for url, (fallback, reason) in self.dead_links.items():
            nu = normalize_url(url)
            paths = self.inventory.get(nu, {}).get("v1_locations", [])
            if not paths:
                paths = [occ["file"] for occ in self.link_registry.get(nu, [])]
            for path in set(paths):
                if not os.path.exists(path): continue
                if path not in file_updates: file_updates[path] = open(path, "r").readlines()
                for i, line in enumerate(file_updates[path]):
                    if url in line:
                        if fallback and fallback.startswith("CANONICAL:"):
                            new_url = fallback.replace("CANONICAL:", "")
                            file_updates[path][i] = line.replace(url, new_url)
                        else:
                            file_updates[path][i] = None 

        final_payload = {p: "".join([l for l in lines if l is not None]) for p, lines in file_updates.items()}
        await self.prune_orphaned_metadata()
        self._save_inventory()
        final_payload[INVENTORY_PATH] = yaml.dump(self.inventory, sort_keys=False, allow_unicode=True)

        from src.safety_guard import SafetyGuard
        guard = SafetyGuard()
        safety_report = guard.generate_audit_report()
        
        if final_payload:
            metrics = {"total_extracted": len(self.link_registry), "full_report": self.action_log}
            self.git_controller.apply_multi_file_changes(final_payload, metrics, safety_report=safety_report)

    async def prune_orphaned_metadata(self):
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
        self.inventory = new_inv

if __name__ == "__main__":
    cleaner = IntelligentLinkCleaner()
    asyncio.run(cleaner.execute_clean_cycle())
