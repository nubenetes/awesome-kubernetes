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
from src.config import GH_TOKEN, TARGET_REPO, GEMINI_API_KEY, NUBENETES_CATEGORIES, MADRID_TZ, INVENTORY_PATH
from src.gitops_manager import RepositoryController
from src.markdown_ast import MarkdownSanitizer
from src.agentic_curator import AgenticCurator
from src.logger import log_event
from src.gemini_utils import call_gemini_with_retry, normalize_url

# Configuración de Excepciones
CORE_FILES = ["docs/index.md", "README.md", "docs/about.md"]
MEMORY_FILE = "src/memory/health_learning.json"

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
        self.full_report_metrics = [] 
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
        # 1. Map all links and Importance Markers
        for root, _, files in os.walk("docs"):
            for f in files:
                if f.endswith(".md"):
                    path = os.path.join(root, f)
                    content = open(path, "r").read()
                    lines = content.splitlines()
                    for idx, line in enumerate(lines):
                        matches = re.finditer(r'(\*\*|==)?\s*\[(.*?)\]\((https?://.*?)\)\s*(\*\*|==)?\s*(.*)', line)
                        for m in matches:
                            fmt_pre, title, url, fmt_post, desc = m.groups()
                            nu = normalize_url(url)
                            is_important = False
                            if fmt_pre or fmt_post: is_important = True
                            if "🌟" in title or "🌟" in (desc or ""): is_important = True
                            if desc and len(desc.strip()) > 100: is_important = True
                            if path in CORE_FILES: is_important = True
                            
                            self.link_registry.setdefault(nu, []).append({
                                "file": path, "line_index": idx, "url": url, 
                                "is_important": is_important
                            })
        
        unique_urls = list(self.link_registry.keys())
        random.shuffle(unique_urls)
        
        to_check = []
        for u in unique_urls:
            nu = normalize_url(u); entry = self.inventory.get(nu, {})
            is_suspicious = False
            if entry.get("status") == "online":
                path = nu.split("://")[-1].rstrip("/")
                if path.count("/") <= 1 or any(kw in path for kw in ["/about", "/products", "/index", "/whats-new"]):
                    is_suspicious = True
            
            if is_suspicious or entry.get("needs_ai_refresh") or os.getenv("FORCE_FULL_CHECK") == "true":
                to_check.append(u)
            elif (datetime.now().timestamp() - entry.get("last_checked", 0)) > (86400 * 21):
                to_check.append(u)

        log_event(f"[*] Queue: {len(to_check)} links prioritized for validation.")

        # 2. Parallel Network Checks
        BATCH_SIZE = 20
        check_results = {}
        for i in range(0, len(to_check), BATCH_SIZE):
            batch = to_check[i:i+BATCH_SIZE]
            tasks = [self._check_url_logic(url) for url in batch]
            results = await asyncio.gather(*tasks)
            for url, res in zip(batch, results): check_results[url] = res
            if i % 100 == 0: log_event(f"  [>] Progress: {i}/{len(to_check)} checked...")

        # 2.5. UNIVERSAL AI RESCUE
        to_rescue = [u for u, res in check_results.items() if not res[0] or res[1] == "generic_redirect_loss"]
        if to_rescue:
            AI_BATCH_SIZE = 10
            for i in range(0, len(to_rescue), AI_BATCH_SIZE):
                batch = to_rescue[i:i+AI_BATCH_SIZE]
                batch_info = []
                for u in batch:
                    entry = self.inventory.get(normalize_url(u), {})
                    batch_info.append({"url": u, "title": entry.get("title", u), "context": entry.get("description", "")})

                prompt = (
                    "You act as a Technical Librarian. Rescue missing resources based on title and description.\n"
                    "Consider acquisitions (Ansible->RedHat, Nginx->F5) and cross-domain moves.\n"
                    "Return ONLY JSON list: [{\"old_url\": \"...\", \"new_url\": \"...\"}, ...]\n\n"
                    "RESOURCES:\n" + "\n".join([f"- {d['title']} | {d['url']}" for d in batch_info])
                )
                
                try:
                    async with self.ai_semaphore:
                        ai_results = await call_gemini_with_retry(prompt, prefer_flash=False)
                        if isinstance(ai_results, list):
                            res_map = {normalize_url(r.get("old_url", "")): r.get("new_url") for r in ai_results}
                            for u in batch:
                                new_loc = res_map.get(normalize_url(u))
                                if new_loc and new_loc.startswith("http") and "NONE" not in new_loc.upper():
                                    try:
                                        async with httpx.AsyncClient(timeout=10, follow_redirects=True, verify=False) as client:
                                            if (await client.get(new_loc)).status_code < 400:
                                                log_event(f"  [✨] RESCUED: {u} -> {new_loc}")
                                                check_results[u] = (True, "resurrected", new_loc)
                                    except: pass
                except: pass

        # 2.8. Finalize Status
        for url, (alive, reason, final) in check_results.items():
            nu = normalize_url(url); entry = self.inventory.get(nu, {})
            score = entry.get("health_score", 100)
            score = (score * 0.8) + (100 if alive else 0) * 0.2
            entry["health_score"] = round(score, 1); entry["last_checked"] = datetime.now().timestamp()
            
            # --- MANDATE 22: SEMANTIC DRIFT (SHA256) ---
            if alive:
                try:
                    from src.agentic_curator import _deep_fetch_content
                    text, _ = await _deep_fetch_content(url if not final else final)
                    if text:
                        new_hash = hashlib.sha256(text.encode()).hexdigest()
                        old_hash = entry.get("content_hash", "N/A")
                        if old_hash != "N/A" and new_hash != old_hash:
                            log_event(f"  [!] DRIFT DETECTED: {url}")
                            entry["needs_ai_refresh"] = True
                        entry["content_hash"] = new_hash
                except: pass

            is_important = any(occ.get("is_important") for occ in self.link_registry.get(nu, []))
            if entry.get("stars", 0) >= 3: is_important = True

            status, final_reason = ("INCLUDED", reason) if alive else ("FILTERED", reason)
            
            if not alive or reason == "generic_redirect_loss":
                if is_important:
                    entry["status"] = "review_required"
                    entry["review_metadata"] = {
                        "original_url": url, "proposed_url": final if final else "NONE",
                        "reason": f"High-Value Protection: {reason}", "timestamp": datetime.now().isoformat()
                    }
                    log_event(f"  [⚠️] REVIEW STORED: {url}")
                    status, final_reason = "INCLUDED", f"Preserved for Review ({reason})"
                elif score < 20: 
                    entry["status"] = "dead"; self.dead_links[url] = (None, reason)
                    status, final_reason = "FILTERED", f"Dead: {reason}"
            elif final and alive:
                self.dead_links[url] = (f"CANONICAL:{final}", "Redirect/Resurrection")
                final_reason = "Updated (Canonical)"
            
            self.full_report_metrics.append({
                "url": url, "status": status, "reason": final_reason,
                "category": entry.get("category", "N/A"), "post_date": entry.get("pub_date"),
                "source": "Health Checker", "impact_score": entry.get("stars", 0) * 20,
                "language": entry.get("language", "EN"), "type": entry.get("resource_type", "Ref")
            })
            self.inventory[nu] = entry

        await self.apply_changes()

    async def _check_url_logic(self, url: str) -> Tuple[bool, str, Optional[str]]:
        headers = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.5"}
        parked = ["buy this domain", "parked free", "domain is for sale"]
        try:
            async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=12) as client:
                resp = await client.get(url)
                if resp.status_code < 400:
                    text = resp.text.lower(); final_url = str(resp.url)
                    if any(kw in text for kw in parked): return False, "parked", None
                    if final_url != url:
                        u_p = url.split("://")[-1].rstrip("/"); f_p = final_url.split("://")[-1].rstrip("/")
                        if u_p.count("/") >= 3 and (f_p.count("/") <= 2 or any(kw in f_p for kw in ["/about", "/products", "/home"])):
                            return False, "generic_redirect_loss", None
                    return True, "OK", final_url if final_url != url else None
                if resp.status_code in [404, 410]:
                    if "github.com" in url:
                        if "/master/" in url:
                            h = url.replace("/master/", "/main/")
                            try:
                                if (await client.get(h)).status_code < 200: return True, "healed", h
                            except: pass
                        m = re.search(r'(https?://github\.com/[^/]+/[^/]+)', url)
                        if m and (await client.get(m.group(1))).status_code < 400: return True, "consolidated", m.group(1)
                    return False, "404", None
                return True, f"Soft Block {resp.status_code}", None
        except: return True, "Error", None

    async def apply_changes(self):
        log_event("APPLYING CLEANING CHANGES...", section_break=True)
        file_updates = {}
        for url, (fallback, reason) in self.dead_links.items():
            nu = normalize_url(url); paths = self.inventory.get(nu, {}).get("v1_locations", [])
            if not paths: paths = [occ["file"] for occ in self.link_registry.get(nu, [])]
            for path in set(paths):
                if not os.path.exists(path): continue
                if path not in file_updates: file_updates[path] = open(path, "r").readlines()
                for i, line in enumerate(file_updates[path]):
                    if url in line:
                        if fallback and fallback.startswith("CANONICAL:"):
                            file_updates[path][i] = line.replace(url, fallback.replace("CANONICAL:", ""))
                        else: file_updates[path][i] = None 

        final_payload = {p: "".join([l for l in lines if l is not None]) for p, lines in file_updates.items()}
        await self.prune_orphaned_metadata(); self._save_inventory()
        final_payload[INVENTORY_PATH] = yaml.dump(self.inventory, sort_keys=False, allow_unicode=True)

        from src.safety_guard import SafetyGuard
        report = SafetyGuard().generate_audit_report()
        metrics = {"total_extracted": len(self.link_registry), "full_report": self.full_report_metrics, "end_date": datetime.now().isoformat()}
        if final_payload: self.git_controller.apply_multi_file_changes(final_payload, metrics, safety_report=report)

    async def prune_orphaned_metadata(self):
        valid_map = {}
        for root, _, files in os.walk("docs"):
            for f in files:
                if f.endswith(".md"):
                    p = os.path.join(root, f); c = open(p, "r").read()
                    for u in re.findall(r'\[.*?\]\((https?://.*?)\)', c): valid_map.setdefault(normalize_url(u), []).append(p)
        new_inv = {}
        for u, m in self.inventory.items():
            if u.startswith("INTRO:") or u in valid_map:
                if u in valid_map: m["v1_locations"] = sorted(list(set(valid_map[u])))
                new_inv[u] = m
        self.inventory = new_inv

if __name__ == "__main__":
    cleaner = IntelligentLinkCleaner()
    asyncio.run(cleaner.execute_clean_cycle())
