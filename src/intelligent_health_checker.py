import asyncio
import json
import os
import re
import httpx
import random
import yaml
import hashlib
from datetime import datetime
import argparse
from typing import Dict, List, Set, Tuple, Optional, Any
from src.config import GH_TOKEN, TARGET_REPO, GEMINI_API_KEY, NUBENETES_CATEGORIES, MADRID_TZ
from src.gitops_manager import RepositoryController
from src.markdown_ast import MarkdownSanitizer
from src.agentic_curator import AgenticCurator
from src.logger import log_event
from src.gemini_utils import call_gemini_with_retry, normalize_url
from src.inventory_manager import load_inventory, get_shard_name, TOTAL_SHARDS

# Configuración de Excepciones
CORE_FILES = ["docs/index.md", "README.md", "docs/about.md"]
MEMORY_FILE = "src/memory/health_learning.json"

class IntelligentLinkCleaner:
    def __init__(self, shard_index: int = None, total_shards: int = TOTAL_SHARDS):
        self.shard_index = shard_index
        self.total_shards = total_shards
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.sanitizer = MarkdownSanitizer()
        self.curator = AgenticCurator()
        self.ai_semaphore = asyncio.Semaphore(5)
        self.link_registry: Dict[str, List[Dict]] = {}
        self.dead_links: Dict[str, Tuple[str, str]] = {} 
        self.learning_data = self._load_memory()
        
        # Determine the shard file if sharded mode
        self.shard_file = f"shard_{self.shard_index:02d}.yaml" if self.shard_index is not None else None
        self.inventory = load_inventory(self.shard_file)
        
        # Determine checkpoint file and load it
        self.checkpoint_file = f"checkpoint_{self.shard_index:02d}.json" if self.shard_index is not None else "health_check_checkpoint.json"
        self.checkpoint_data = self._load_checkpoint()
        
        self.full_report_metrics = [] 
        self.detailed_stats = {"total_scanned": 0, "skipped_recent": 0, "by_file": {}, "operation_types": {"removals": 0, "consolidated": 0, "healed": 0, "enriched": 0}}
        self.stats = {"total_links": 0, "dead_links_removed": 0, "orphans_fixed": 0, "enriched_descriptions": 0}

    def _load_memory(self) -> Dict:
        if os.path.exists(MEMORY_FILE):
            try: return json.load(open(MEMORY_FILE, 'r'))
            except Exception as e:
                log_event(f"[WARN] load health learning memory: {str(e)[:100]}")
        return {"domains": {}, "known_soft_404_patterns": []}

    def _save_memory(self):
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        json.dump(self.learning_data, open(MEMORY_FILE, "w"), indent=2)

    def _load_checkpoint(self) -> Dict:
        if os.path.exists(self.checkpoint_file) and os.path.getsize(self.checkpoint_file) > 0:
            try:
                with open(self.checkpoint_file, "r") as f:
                    data = json.load(f)
                log_event(f"[*] Resuming from checkpoint file: {self.checkpoint_file}")
                # Restore checkpoint data into self variables
                self.inventory.update(data.get("inventory_updates", {}))
                return data
            except Exception as e:
                log_event(f"[WARN] Failed to load checkpoint {self.checkpoint_file}: {str(e)[:100]}")
        return {
            "checked_urls": {}, # url -> [alive, reason, final_url]
            "inventory_updates": {}, # url -> inventory_entry
            "rescued_urls": [] # list of URLs that we attempted to rescue
        }

    def _save_checkpoint(self):
        try:
            with open(self.checkpoint_file, "w") as f:
                json.dump(self.checkpoint_data, f, indent=2)
        except Exception as e:
            log_event(f"[WARN] Failed to save checkpoint {self.checkpoint_file}: {str(e)[:100]}")

    def _delete_checkpoint(self):
        if os.path.exists(self.checkpoint_file):
            try:
                os.remove(self.checkpoint_file)
                log_event(f"[*] Cleaned up checkpoint file: {self.checkpoint_file}")
            except Exception as e:
                log_event(f"[WARN] Failed to delete checkpoint {self.checkpoint_file}: {str(e)[:100]}")



    async def execute_clean_cycle(self):
        log_event("STARTING INTELLIGENT CLEANING CYCLE", section_break=True)
        # 1. Map all links and Importance Markers
        for root, _, files in os.walk("docs"):
            for f in files:
                if f.endswith(".md"):
                    path = os.path.join(root, f)
                    content = open(path, "r").read()
                    
                    # Mandate 23: Detect Mosaic boundaries in index.md
                    mosaic_lines = set()
                    if path == "docs/index.md":
                        # Find all center blocks and identify the one that looks like the YouTube mosaic
                        mosaics = list(re.finditer(r'<center markdown="1">\s*\n(.*?)\n\s*</center>', content, re.DOTALL))
                        target_mosaic = None
                        max_yt_links = 0
                        
                        for m in mosaics:
                            yt_count = m.group(1).count("youtube.com")
                            if yt_count > max_yt_links:
                                max_yt_links = yt_count
                                target_mosaic = m
                        
                        if target_mosaic:
                            mosaic_text = target_mosaic.group(1)
                            # We find the start line of this specific block
                            start_pos = target_mosaic.start(1)
                            start_line = content[:start_pos].count('\n')
                            line_count = mosaic_text.count('\n') + 1
                            for i in range(start_line, start_line + line_count):
                                mosaic_lines.add(i)
                            log_event(f"[*] YouTube Mosaic identified in docs/index.md (Lines {start_line}-{start_line+line_count})")

                    lines = content.splitlines()
                    for idx, line in enumerate(lines):
                        # Detect standard markdown links
                        matches = list(re.finditer(r'(\*\*|==)?\s*\[(.*?)\]\((https?://.*?)\)\s*(\*\*|==)?\s*(.*)', line))
                        
                        # MANDATE 23: Also detect YouTube links in iframes for the videos section
                        if path == "docs/index.md" and "iframe" in line and "youtube.com" in line:
                            iframe_match = re.search(r'src="(https?://www\.youtube\.com/.*?)"', line)
                            if iframe_match:
                                url = iframe_match.group(1)
                                nu = normalize_url(url)
                                # We treat iframes as non-important by default but they must be checked
                                self.link_registry.setdefault(nu, []).append({
                                    "file": path, "line_index": idx, "url": url, 
                                    "is_important": False, "is_iframe": True
                                })

                        for m in matches:
                            fmt_pre, title, url, fmt_post, desc = m.groups()
                            nu = normalize_url(url)

                            # MANDATE 23: Skip YouTube Mosaic links in docs/index.md
                            if path == "docs/index.md" and idx in mosaic_lines and "youtube.com" in nu:
                                continue

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
            nu = normalize_url(u)
            
            # Shard filtering
            if self.shard_index is not None:
                if get_shard_name(nu) != self.shard_file:
                    continue

            # Checkpoint filtering: skip if already checked in checkpoint
            if nu in self.checkpoint_data["checked_urls"]:
                continue

            entry = self.inventory.get(nu, {})
            is_suspicious = False
            if entry.get("status") == "online":
                path = nu.split("://")[-1].rstrip("/")
                if path.count("/") <= 1 or any(kw in path for kw in ["/about", "/products", "/index", "/whats-new"]):
                    is_suspicious = True
            
            if is_suspicious or entry.get("needs_ai_refresh") or os.getenv("FORCE_FULL_CHECK") == "true":
                to_check.append(u)
            elif (datetime.now().timestamp() - (entry.get("last_checked") or 0)) > (86400 * 21):
                to_check.append(u)

        total_to_check = len(to_check)
        log_event(f"[*] Queue: {total_to_check} links prioritized for validation (skipped {len(self.checkpoint_data['checked_urls'])} already checked).")

        # 2. Parallel Network Checks (Optimized with Mandate 22 & 33)
        BATCH_SIZE = 15 # Slightly smaller batch to accommodate deep fetch
        check_results = {}
        for nu, res in self.checkpoint_data["checked_urls"].items():
            check_results[nu] = tuple(res)

        for i in range(0, total_to_check, BATCH_SIZE):
            batch = to_check[i:i+BATCH_SIZE]
            tasks = [self._check_url_logic(url) for url in batch]
            results = await asyncio.gather(*tasks)
            for url, res in zip(batch, results):
                check_results[url] = res
                nu = normalize_url(url)
                self.checkpoint_data["checked_urls"][nu] = list(res)
                self.checkpoint_data["inventory_updates"][nu] = self.inventory.get(nu)
            
            self._save_checkpoint()
            if i % 45 == 0: log_event(f"  [>] Progress: [{i}/{total_to_check}] links validated...")

        # 2.5. UNIVERSAL AI RESCUE
        to_rescue = [u for u, res in check_results.items() if not res[0] or res[1] == "generic_redirect_loss"]
        to_rescue = [u for u in to_rescue if normalize_url(u) not in self.checkpoint_data["rescued_urls"]]
        
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
                        # Mandate 48: Use Flash/Lite for high-volume rescue to avoid Rate-Limits
                        ai_results = await call_gemini_with_retry(prompt, prefer_flash=True, use_grounding=True, role="Link-Rescue")
                        if isinstance(ai_results, list):
                            res_map = {normalize_url(r.get("old_url", "")): r.get("new_url") for r in ai_results}
                            for u in batch:
                                nu = normalize_url(u)
                                if nu not in self.checkpoint_data["rescued_urls"]:
                                    self.checkpoint_data["rescued_urls"].append(nu)
                                
                                new_loc = res_map.get(nu)
                                if new_loc and new_loc.startswith("http") and "NONE" not in new_loc.upper():
                                    try:
                                        async with httpx.AsyncClient(timeout=10, follow_redirects=True, verify=False) as client:
                                            resp_new = await client.get(new_loc)
                                            if resp_new.status_code < 400:
                                                from src.gemini_utils import sanitize_trailing_slashes, is_invalid_or_generic_redirect
                                                final_new = sanitize_trailing_slashes(str(resp_new.url))
                                                is_bad, bad_reason = is_invalid_or_generic_redirect(u, final_new, resp_new.text)
                                                if is_bad:
                                                    log_event(f"  [⚠️] AI proposed an invalid/generic redirect for {u} -> {final_new} ({bad_reason}). Rejecting.")
                                                else:
                                                    log_event(f"  [✨] RESCUED: {u} -> {final_new}")
                                                    check_results[u] = (True, "resurrected", final_new)
                                                    self.checkpoint_data["checked_urls"][nu] = [True, "resurrected", final_new]
                                    except Exception as e:
                                        log_event(f"[WARN] verify rescued URL {new_loc[:50]}: {str(e)[:100]}")
                            
                            self._save_checkpoint()
                except Exception as e:
                    log_event(f"[WARN] AI rescue batch: {str(e)[:100]}")

        # 2.8. Finalize Status
        log_event("FINALIZING STATUS AND METRICS...", section_break=True)
        for url, (alive, reason, final) in check_results.items():
            nu = normalize_url(url); entry = self.inventory.get(nu, {})
            score = entry.get("health_score")
            if score is None:
                score = 100.0
            score = (score * 0.8) + (100 if alive else 0) * 0.2
            entry["health_score"] = round(score, 1); entry["last_checked"] = datetime.now().timestamp()
            
            # Mandate 22 & 33 were handled in _check_url_logic to avoid sequential bottlenecks
            is_important = any(occ.get("is_important") for occ in self.link_registry.get(nu, []))
            if (entry.get("stars") or 0) >= 3: is_important = True

            status, final_reason = ("INCLUDED", reason) if alive else ("FILTERED", reason)
            
            if not alive or reason == "generic_redirect_loss" or reason.startswith("soft_404") or reason == "parked_domain":
                if is_important:
                    orig_metadata = entry.get("review_metadata") or {}
                    orig_timestamp = orig_metadata.get("timestamp")
                    
                    is_expired = False
                    if orig_timestamp:
                        try:
                            dt = datetime.fromisoformat(orig_timestamp)
                            age_days = (datetime.now() - dt).days
                            if age_days >= 30:
                                is_expired = True
                                log_event(f"  [❌] REVIEW EXPIRED (Age: {age_days} days): {url} has been dead for too long. Pruning.")
                        except Exception as e:
                            log_event(f"[WARN] Parse review timestamp {orig_timestamp}: {e}")
                    
                    if is_expired:
                        entry["status"] = "dead"
                        self.dead_links[url] = (None, "review_expired")
                        status, final_reason = "FILTERED", "Review expired (30-day TTL)"
                    else:
                        entry["status"] = "review_required"
                        entry["review_metadata"] = {
                            "original_url": url,
                            "proposed_url": final if final else "NONE",
                            "reason": f"High-Value Protection: {reason}",
                            "timestamp": orig_timestamp if orig_timestamp else datetime.now().isoformat()
                        }
                        log_event(f"  [⚠️] REVIEW STORED/MAINTAINED: {url}")
                        status, final_reason = "INCLUDED", f"Preserved for Review ({reason})"
                else:
                    entry["status"] = "dead"; self.dead_links[url] = (None, reason)
                    status, final_reason = "FILTERED", f"Dead: {reason}"
            elif final and alive:
                self.dead_links[url] = (f"CANONICAL:{final}", "Redirect/Resurrection")
                final_reason = "Updated (Canonical)"
            
            self.full_report_metrics.append({
                "url": url, "status": status, "reason": final_reason,
                "category": entry.get("category", "N/A"), "post_date": entry.get("pub_date"),
                "source": "Health Checker", "impact_score": (entry.get("stars") or 0) * 20,
                "language": entry.get("language", "EN"), "type": entry.get("resource_type", "Ref")
            })
            self.inventory[nu] = entry

        await self.apply_changes()
        self._delete_checkpoint()

    async def apply_changes(self):
        # Export JSON artifact for the reducer instead of applying Git changes directly
        output_payload = {
            "shard_index": self.shard_index,
            "inventory_updates": self.inventory,
            "dead_links": self.dead_links,
            "full_report_metrics": self.full_report_metrics
        }
        
        out_name = f"shard_result_{self.shard_index:02d}.json" if self.shard_index is not None else "shard_result.json"
        with open(out_name, "w") as f:
            json.dump(output_payload, f, indent=2)
            
        log_event(f"EXPORTED SHARD RESULTS TO {out_name}", section_break=True)
        
        # --- AUTOMATED TRIAGE REPORT GENERATION ---
        triage_links = []
        for url, meta in self.inventory.items():
            if meta.get('status') == 'review_required':
                triage_links.append({"url": url, "stars": meta.get('stars') or 0, "desc": meta.get('description', 'N/A')})
        
        if triage_links:
            # Sort by stars (impact) DESC
            triage_links.sort(key=lambda x: x['stars'], reverse=True)
            with open("triage_report.md", "w") as f:
                f.write(f"### 🚨 Manual Triage Required ({len(triage_links)} High-Value Links)\n\n")
                f.write("The following resources were flagged for manual review because they failed health checks but are considered high-value assets.\n\n")
                f.write("| Impact | Resource | Description |\n| :---: | :--- | :--- |\n")
                for item in triage_links:
                    f.write(f"| {'🌟'*item['stars']} | {item['url']} | {item['desc']} |\n")

    async def _check_url_logic(self, url: str) -> Tuple[bool, str, Optional[str]]:
        headers = {"User-Agent": "Mozilla/5.0", "Accept-Language": "en-US,en;q=0.5"}
        nu = normalize_url(url); entry = self.inventory.get(nu, {})
        
        try:
            async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=12) as client:
                resp = await client.get(url)
                if resp.status_code < 400:
                    from src.gemini_utils import sanitize_trailing_slashes, is_invalid_or_generic_redirect
                    final_url = sanitize_trailing_slashes(str(resp.url))
                    
                    is_bad, bad_reason = is_invalid_or_generic_redirect(url, final_url, resp.text)
                    if is_bad:
                        return False, bad_reason, None
                    
                    # Mandate 22: Content Drift detection (SHA256) - Integrated here for speed
                    new_hash = hashlib.sha256(resp.text.encode()).hexdigest()
                    old_hash = entry.get("content_hash", "N/A")
                    if old_hash != "N/A" and new_hash != old_hash:
                        log_event(f"  [!] DRIFT DETECTED: {url}")
                        entry["needs_ai_refresh"] = True
                    entry["content_hash"] = new_hash

                    # Mandate 33: License Guard for GitHub
                    if "github.com" in url:
                        try:
                            from src.agentic_curator import _get_github_activity
                            gh_meta = await _get_github_activity(url)
                            if gh_meta.get("gh_license"):
                                old_lic = entry.get("gh_license", "N/A")
                                new_lic = gh_meta["gh_license"]
                                if old_lic != "N/A" and old_lic != new_lic:
                                    if any(x in new_lic.upper() for x in ["BSL", "SSPL", "PROPRIETARY"]):
                                        log_event(f"  [⚖️] LICENSE ALERT: {url} -> {new_lic}")
                                        entry["status"] = "review_required"
                                entry["gh_license"] = new_lic
                        except Exception as e:
                            log_event(f"[WARN] license guard check for {url}: {str(e)[:100]}")

                    if final_url != url:
                        u_p = url.split("://")[-1].rstrip("/"); f_p = final_url.split("://")[-1].rstrip("/")
                        if u_p == f_p: return True, "normalized_slashes", final_url
                    
                    return True, "OK", final_url if final_url != url else None
                
                if resp.status_code in [404, 410, 451]:
                    if "github.com" in url:
                        if "/master/" in url:
                            h = url.replace("/master/", "/main/")
                            try:
                                if (await client.get(h)).status_code < 400: return True, "healed", h
                            except Exception as e:
                                log_event(f"[WARN] heal master->main for {url}: {str(e)[:100]}")
                        m = re.search(r'(https?://github\.com/[^/]+/[^/]+)', url)
                        if m and (await client.get(m.group(1))).status_code < 400: return True, "consolidated", m.group(1)
                    return False, str(resp.status_code), None
                return True, f"Soft Block {resp.status_code}", None
        except httpx.ConnectError as e:
            log_event(f"[WARN] Connect/DNS error for {url}: {str(e)[:100]}")
            return False, "connect_or_dns_error", None
        except Exception as e:
            log_event(f"[WARN] URL check logic for {url}: {str(e)[:100]}")
            return True, "Error", None

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
    parser = argparse.ArgumentParser()
    parser.add_argument("--shard-index", type=int, default=None, help="Index of the shard (0-63)")
    parser.add_argument("--total-shards", type=int, default=TOTAL_SHARDS, help="Total number of shards")
    args = parser.parse_args()

    cleaner = IntelligentLinkCleaner(shard_index=args.shard_index, total_shards=args.total_shards)
    asyncio.run(cleaner.execute_clean_cycle())
