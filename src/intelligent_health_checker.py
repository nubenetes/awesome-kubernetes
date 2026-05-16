import asyncio
import json
import os
import re
import httpx
import random
from datetime import datetime
from typing import Dict, List, Set, Tuple, Optional, Any
from src.config import GH_TOKEN, TARGET_REPO, GEMINI_API_KEY, NUBENETES_CATEGORIES, MADRID_TZ
from src.gitops_manager import RepositoryController
from src.markdown_ast import MarkdownSanitizer
from src.agentic_curator import AgenticCurator
from src.logger import log_event

def normalize_url(url: str) -> str:
    url = url.split("#")[0].split("?")[0].rstrip("/")
    if url.startswith("http://"): url = "https://" + url[7:]
    return url.lower()

# Configuración de Excepciones
CORE_FILES = ["docs/index.md", "README.md"]
MEMORY_FILE = "src/memory/health_learning.json"
INVENTORY_PATH = "data/inventory.yaml"
STRUCTURE_MAP_PATH = "data/structure_map.yaml"

class IntelligentLinkCleaner:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.sanitizer = MarkdownSanitizer()
        self.curator = AgenticCurator()
        self.link_registry: Dict[str, List[Dict]] = {}
        self.dead_links: Dict[str, Tuple[str, str]] = {} 
        self.description_updates: Dict[str, str] = {}
        self.learning_data = self._load_memory()
        self.inventory = self._load_inventory()
        self.structure_map = self._load_structure_map()
        self.action_log: List[Dict] = [] 
        self.detailed_stats = {
            "total_scanned": 0,
            "skipped_recent": 0,
            "by_file": {}, 
            "by_category": {}, 
            "operation_types": {"removals": 0, "consolidated": 0, "orphans": 0, "enriched": 0}
        }
        self.stats = {"total_links": 0, "dead_links_removed": 0, "duplicates_pruned": 0, "ai_decisions": 0, "orphans_fixed": 0, "enriched_descriptions": 0}

    def _load_memory(self) -> Dict:
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, 'r') as f: return json.load(f)
            except: pass
        return {"domains": {}, "link_cache": {}, "known_soft_404_patterns": []}

    def _save_memory(self):
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        with open(MEMORY_FILE, "w") as f: json.dump(self.learning_data, f, indent=2)

    def _load_inventory(self) -> dict:
        if os.path.exists(INVENTORY_PATH):
            try:
                with open(INVENTORY_PATH, "r") as f:
                    import yaml
                    return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def _save_inventory(self):
        os.makedirs(os.path.dirname(INVENTORY_PATH), exist_ok=True)
        with open(INVENTORY_PATH, "w") as f:
            import yaml
            yaml.dump(self.inventory, f, sort_keys=False, allow_unicode=True)

    def _load_structure_map(self) -> dict:
        if os.path.exists(STRUCTURE_MAP_PATH):
            try:
                with open(STRUCTURE_MAP_PATH, "r") as f:
                    import yaml
                    return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def _save_structure_map(self):
        os.makedirs(os.path.dirname(STRUCTURE_MAP_PATH), exist_ok=True)
        with open(STRUCTURE_MAP_PATH, "w") as f:
            import yaml
            yaml.dump(self.structure_map, f, sort_keys=False, allow_unicode=True)

    async def _fetch_github_metadata(self, url: str) -> Dict:
        match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
        if not match: return {}
        owner, repo = match.groups()
        repo = repo.split("#")[0].split("?")[0].rstrip(".git")
        
        headers = {"Authorization": f"token {GH_TOKEN}"} if GH_TOKEN else {}
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        
        try:
            async with httpx.AsyncClient(timeout=10.0) as client:
                resp = await client.get(api_url, headers=headers)
                if resp.status_code == 200:
                    data = resp.json()
                    pushed_at = data.get("pushed_at", "")
                    years_inactive = 0
                    if pushed_at:
                        last_date = datetime.fromisoformat(pushed_at.replace('Z', '+00:00'))
                        years_inactive = (datetime.now(last_date.tzinfo) - last_date).days / 365
                    
                    return {
                        "stars": data.get("stargazers_count", 0),
                        "pushed_at": pushed_at, "created_at": data.get("created_at", ""),
                        "years_inactive": years_inactive,
                        "is_abandoned": years_inactive > 4
                    }
        except: pass
        return {}

    async def _check_url_with_retries(self, url: str, max_retries=5) -> Tuple[str, bool, Optional[str], str]:
        now = datetime.now().timestamp()

        # 0. Policy Enforcement: No archive.org links allowed
        if "archive.org" in url.lower():
            return url, False, None, "Archive.org link (Forbidden by policy)"
        
        # 1. NOTE: V1 Exhaustiveness Mandate
        # We fetch GitHub metadata for logging/metrics, but we DO NOT delete based on activity.
        # Only definitively dead links are removed in V1.
        if "github.com" in url:
            gh_meta = await self._fetch_github_metadata(url)
            # Metadata is stored in cache/logs but not used for deletion here.

        cache_entry = self.learning_data.get("link_cache", {}).get(url)
        if cache_entry and cache_entry.get("status") == "ALIVE":
            if now - cache_entry.get("last_checked", 0) < (21 * 24 * 3600):
                self.detailed_stats["skipped_recent"] += 1
                return url, True, None, "Cached (Recent)"

        domain = url.split("//")[-1].split("/")[0]
        domain_info = self.learning_data.get("domains", {}).get(domain, {})
        strategies = [
            {"type": "http", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36", "ref": "https://www.google.com/", "desc": "Desktop/Google"},
            {"type": "http", "ua": "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1", "ref": "https://t.co/", "desc": "Mobile/Twitter"},
            {"type": "playwright", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36", "ref": "https://www.linkedin.com/", "desc": "PW Desktop/LinkedIn"},
            {"type": "http", "ua": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36", "ref": "https://www.google.com/", "desc": "Linux/Chrome"},
            {"type": "playwright", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36", "ref": "https://www.reddit.com/", "desc": "PW Windows/Reddit"}
        ]
        
        # PRIORIZACIÓN INTELIGENTE: Si ya sabemos qué funciona para este dominio, empezar por ahí.
        best_strat_idx = domain_info.get("best_strategy_idx")
        if best_strat_idx is not None and best_strat_idx < len(strategies):
            # Mover la mejor estrategia al inicio
            best_strat = strategies.pop(best_strat_idx)
            strategies.insert(0, best_strat)

        for attempt in range(min(max_retries, len(strategies))):
            strategy = strategies[attempt]
            try:
                if attempt > 0: await asyncio.sleep((2 ** attempt) + random.random())
                is_alive, reason = await self._check_url_logic(url, strategy)
                if is_alive:
                    if "domains" not in self.learning_data: self.learning_data["domains"] = {}
                    if domain not in self.learning_data["domains"]: self.learning_data["domains"][domain] = {}
                    
                    # Guardar el índice REAL de la estrategia que funcionó
                    original_idx = attempt if best_strat_idx is None else (best_strat_idx if attempt == 0 else (attempt if attempt < best_strat_idx else attempt))
                    self.learning_data["domains"][domain]["best_strategy_idx"] = original_idx
                    
                    # Enrichment: If link is ALIVE but lacks description in V1, generate one
                    await self._enrich_description_if_needed(url)
                    
                    if "link_cache" not in self.learning_data: self.learning_data["link_cache"] = {}
                    self.learning_data["link_cache"][url] = {"status": "ALIVE", "last_checked": now}
                    return url, True, None, f"Alive ({strategy['desc']}) - {reason}"

                if reason in ["404", "soft_404", "redirect_to_home"]:
                    fallback_result = None
                    if any(git_host in url for git_host in ["github.com", "gitlab.com", "bitbucket.org"]):
                        parts = url.split("/"); repo_root = "/".join(parts[:5]) if len(parts) > 4 else None
                        if repo_root:
                            root_alive, _ = await self._check_url_logic(repo_root, strategies[0])
                            if root_alive: fallback_result = f"REPO_ROOT:{repo_root}"
                    
                    # Cache DEAD status for resumption
                    if "link_cache" not in self.learning_data: self.learning_data["link_cache"] = {}
                    self.learning_data["link_cache"][url] = {
                        "status": "DEAD", "reason": reason, "fallback": fallback_result, "last_checked": now
                    }
                    
                    if fallback_result: return url, False, fallback_result, f"Consolidated (Original: {reason})"
                    if attempt == max_retries - 1:
                        return url, False, None, reason
            except: pass
        return url, True, None, "Conservative Keep"

    async def _enrich_description_if_needed(self, url: str):
        """
        Policy Update: We NO LONGER enrich existing V1 descriptions in the repo 
        to respect manual curation. However, we ensure the INVENTORY has a 
        description for the V2 Elite portal.
        """
        norm_url = normalize_url(url)
        if norm_url not in self.inventory: self.inventory[norm_url] = {}
        
        # If inventory already has a description, we are done
        if self.inventory[norm_url].get("ai_summary"): return

        log_event(f"    [✨] INVENTORY: Generating summary for {url} (V2 Only)")
        try:
            from src.agentic_curator import _deep_fetch_content
            from src.gemini_utils import call_gemini_with_retry
            web_content = await _deep_fetch_content(url)
            if not web_content: return
            
            prompt = f"""Analyze this resource: {url}
Technical Content Snippet: {web_content[:1500]}
Provide: 1) A professional 1-sentence English description. 2) The precise original PUBLICATION DATE (YYYY-MM-DD or YYYY if possible).
Format: JSON: {\"desc\": \"...\", \"pub_date\": \"...\"}"""
            ai_data = await call_gemini_with_retry(prompt)
            if ai_data:
                self.inventory[norm_url]["ai_summary"] = ai_data.get("desc", "").strip()
                self.inventory[norm_url]["pub_date"] = ai_data.get("pub_date", "N/A")
                self.stats["enriched_descriptions"] += 1
                log_event(f"    [OK] Cached for V2: {ai_data.get("desc", "")[:50]}...")
        except Exception as e:
            log_event(f"    [!] Enrichment error: {e}")

    async def _check_url_logic(self, url: str, strategy: Dict) -> Tuple[bool, str]:
        # RESILIENT LOGIC: Mimic user behavior and handle blocks gracefully
        headers = {
            "User-Agent": strategy["ua"], 
            "Referer": strategy["ref"], 
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Connection": "keep-alive"
        }
        
        # Immediate pass for high-trust domains to avoid over-cleaning
        if any(trusted in url.lower() for trusted in ["github.com", "gitlab.com", "microsoft.com", "google.com", "aws.amazon.com"]):
            return True, "Trusted Domain"

        paywall_indicators = ["sign in", "create free account", "member-only story", "página de suscripción", "inicia sesión"]
        
        if strategy["type"] == "http":
            try:
                # Use GET as primary (HEAD is often blocked)
                async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=15, verify=False) as client:
                    resp = await client.get(url)
                    if resp.status_code < 400: return True, "HTTP OK"
                    
                    # Definitive Failures
                    if resp.status_code in [404, 410]: return False, "404"
                    
                    # Soft Failures (Keep but flag)
                    if resp.status_code in [403, 429, 401, 500, 502, 503]: 
                        return True, f"Soft Block/Error ({resp.status_code})"
            except Exception as e:
                return True, f"Connection Timeout/Error (Preserving)"
        else:
            # Playwright Logic for JS-Heavy/Protected Sites
            try:
                from playwright.async_api import async_playwright
                async with async_playwright() as p:
                    browser = await p.chromium.launch(headless=True)
                    context = await browser.new_context(user_agent=strategy["ua"], extra_http_headers={"Referer": strategy["ref"]})
                    page = await context.new_page()
                    try:
                        response = await page.goto(url, wait_until="domcontentloaded", timeout=30000)
                        if not response: return True, "JS Timeout (Preserving)"
                        if response.status in [404, 410]: return False, "404"
                        
                        content = (await page.content()).lower()
                        title = (await page.title()).lower()
                        
                        if any(kw in content for kw in paywall_indicators): return True, "Paywall (Preserving)"
                        
                        soft_404_keywords = ["page not found", "404 not found", "artículo no encontrado", "página no encontrada"]
                        if any(kw in title for kw in soft_404_keywords) or (("404" in title) and any(kw in content for kw in soft_404_keywords)): 
                            return False, "soft_404"
                            
                        return True, "Render OK"
                    finally: await browser.close()
            except: 
                return True, "Browser Engine Error (Preserving)"
        
        return True, "Conservative Keep"

    async def build_global_registry(self):
        log_event("STARTING GLOBAL LINK DISCOVERY...", section_break=True)
        all_files = CORE_FILES + [f"docs/{cat}.md" for cat in NUBENETES_CATEGORIES]
        for file_path in all_files:
            try:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f: content = f.read()
                    lines = content.splitlines()
                    for i, line in enumerate(lines):
                        match = self.sanitizer.link_pattern.search(line)
                        if match:
                            title, url = match.groups(); clean_url = url.split('#')[0].rstrip('/')
                            if clean_url not in self.link_registry: self.link_registry[clean_url] = []
                            self.link_registry[clean_url].append({"file": file_path, "line_index": i, "content": line, "title": title})
                            self.stats["total_links"] += 1
            except: pass
        log_event(f"[*] Discovery: Registered {self.stats['total_links']} links from {len(all_files)} files.")

    async def validate_links_tiered(self):
        log_event(f"[*] Validating {len(self.link_registry)} unique URLs (Randomized Tiered Batching)...", section_break=True)
        
        # Recover DEAD links from cache to enable resumption
        for url, cache in self.learning_data.get("link_cache", {}).items():
            if cache.get("status") == "DEAD" and url in self.link_registry:
                self.dead_links[url] = (cache.get("fallback"), cache.get("reason"))
                log_event(f"    [M] Recovered from memory: {url} (DEAD)")

        unique_urls = [u for u in self.link_registry.keys() if u not in self.dead_links]
        random.shuffle(unique_urls)
        total_unique = len(unique_urls)
        for i in range(0, total_unique, 40):
            batch = unique_urls[i:i+40]
            log_event(f"    [>] Processing batch {i//40 + 1}/{(total_unique-1)//40 + 1} ({min(i+40, total_unique)}/{total_unique})...")
            tasks = [self._check_url_with_retries(url) for url in batch]
            results = await asyncio.gather(*tasks)
            for url, is_alive, fallback, reason in results:
                if not is_alive: 
                    self.dead_links[url] = (fallback if fallback else "DEAD", reason)
                    log_event(f"        [!] DEAD: {url} -> {reason} {'(Fallback: ' + fallback + ')' if fallback else ''}")
            self._save_memory(); self._save_inventory(); self._save_structure_map()

    async def apply_changes(self):
        log_event("APPLYING INTELLIGENT CLEANING & PR GENERATION...", section_break=True)
        file_updates = {}
        def track(file, op, url, reason, cat=None):
            if file not in self.detailed_stats["by_file"]: self.detailed_stats["by_file"][file] = {"removed": 0, "modified": 0, "created": 0}
            self.detailed_stats["by_file"][file][op] += 1
            if not cat: cat = file.replace("docs/", "").replace(".md", "")
            if cat not in self.detailed_stats["by_category"]: self.detailed_stats["by_category"][cat] = {"removed": 0, "modified": 0, "created": 0}
            self.detailed_stats["by_category"][cat][op] += 1
            self.action_log.append({"file": file, "url": url, "action": op, "reason": reason})

        for url, (fallback, reason) in self.dead_links.items():
            occurrences = self.link_registry.get(url, [])
            for occ in occurrences:
                file_path = occ["file"]
                if file_path not in file_updates:
                    with open(file_path, 'r') as f: file_updates[file_path] = f.readlines()
                line_idx = occ["line_index"]
                if fallback and fallback.startswith("REPO_ROOT:"):
                    real_f = fallback.replace("REPO_ROOT:", "")
                    file_updates[file_path][line_idx] = file_updates[file_path][line_idx].replace(url, real_f)
                    track(file_path, "modified", url, reason); self.detailed_stats["operation_types"]["consolidated"] += 1
                else:
                    if file_path not in CORE_FILES:
                        file_updates[file_path][line_idx] = None
                        track(file_path, "removed", url, reason); self.detailed_stats["operation_types"]["removals"] += 1

        # 2. APPLY DESCRIPTION ENRICHMENT (Disabled for V1 repo files per policy)

        orphans_linked = getattr(self.curator, "stats", {}).get("orphans_linked", 0)
        if orphans_linked > 0:
            track("Navigation", "created", "Orphan Audit", "Linked via Curator")
            self.detailed_stats["operation_types"]["orphans"] = orphans_linked

        final_payload = {p: "".join([l for l in lines if l is not None]) for p, lines in file_updates.items()}
        if orphans_linked > 0:
            with open(getattr(self.curator, "index_path", "docs/index.md"), 'r') as f: 
                final_payload[getattr(self.curator, "index_path", "docs/index.md")] = f.read()
            with open(getattr(self.curator, "mkdocs_path", "mkdocs.yml"), 'r') as f: 
                final_payload[getattr(self.curator, "mkdocs_path", "mkdocs.yml")] = f.read()
        if final_payload: self._create_pr(final_payload)

    def _create_pr(self, updates: Dict[str, str], report_content: str = None):
        timestamp = datetime.now().strftime("%Y%m%d-%H%M"); branch_name = f"bot/autonomous-health-{timestamp}"
        if not report_content: report_content = self._build_report_body()
        self.git_controller._create_feature_branch(branch_name)
        for path, content in updates.items():
            try:
                file_meta = self.git_controller.repository.get_contents(path)
                self.git_controller.repository.update_file(path=path, message=f"fix(autonomous): engine update in {path}", content=content, sha=file_meta.sha, branch=branch_name)
            except: pass
        safe_report = report_content[:65000]
        self.git_controller.repository.create_pull(title=f"🧹 Autonomous Engine Health Report: {datetime.now().strftime('%d %b %Y')}", body=safe_report, head=branch_name, base=self.git_controller.default_branch_name)

    def _build_report_body(self) -> str:
        report = "## 🧠 Nubenetes Autonomous Health & Curation Engine\n\n"
        report += "### 📊 Distribución de Operaciones\n"
        report += "```mermaid\npie title Operaciones de Mantenimiento\n"
        report += f"    \"Eliminados\" : {self.detailed_stats['operation_types']['removals']}\n"
        report += f"    \"Consolidados\" : {self.detailed_stats['operation_types']['consolidated']}\n"
        report += f"    \"Nuevos\" : {self.detailed_stats['operation_types']['orphans']}\n```\n\n"
        report += "### 📈 Resumen de Eficiencia\n"
        report += "| Métrica | Cantidad | Detalle |\n| :--- | :---: | :--- |\n"
        report += f"| ⏩ Omitidos (Cache) | **{self.detailed_stats['skipped_recent']}** | Verificados hace menos de 21 días |\n"
        report += f"| 💀 Eliminados | **{self.detailed_stats['operation_types']['removals']}** | 404 definitivos |\n"
        report += f"| 🎯 Consolidados | **{self.detailed_stats['operation_types']['consolidated']}** | Raíz de Repositorio Git |\n"
        report += f"| 🖇️ Nuevos | **{self.detailed_stats['operation_types']['orphans']}** | Páginas vinculadas |\n\n"
        report += "### 🧮 Matriz de Mantenimiento\n"
        report += "| Documento | 🔴 Elim | 🟡 Mod | 🟢 Crea | Estado |\n| :--- | :---: | :---: | :---: | :---: |\n"
        for file, s in sorted(self.detailed_stats["by_file"].items()):
            status = "🧹 Limpio" if s['removed'] + s['modified'] < 3 else "🛠️ Refactor"
            if s['removed'] > 5: status = "⚠️ Crítico"
            report += f"| `{file}` | {s['removed']} | {s['modified']} | {s['created']} | {status} |\n"
        report += "\n### 📝 Registro de Acciones\n<details><summary>Ver detalle de cambios</summary>\n\n"
        report += "| Archivo | Acción | Recurso (Acortado) | Motivo |\n| :--- | :---: | :--- | :--- |\n"
        is_compressed = False; current_len = len(report); processed_logs = 0
        from collections import defaultdict; logs_by_file = defaultdict(list)
        for log in self.action_log: logs_by_file[log["file"]].append(log)
        for file_path, actions in sorted(logs_by_file.items()):
            if current_len > 55000:
                is_compressed = True; summary = f"| `{file_path}` | 🛠️ | *Múltiples enlaces* | Se procesaron {len(actions)} cambios en este archivo. |\n"
                report += summary; current_len += len(summary); continue
            for log in actions:
                emoji = {"removed": "❌", "modified": "🔄", "created": "✨"}.get(log["action"], "❓")
                short_url = (log["url"][:50] + "...") if current_len > 45000 and len(log["url"]) > 53 else log["url"]
                entry = f"| `{log['file']}` | {emoji} | {short_url} | {log['reason']} |\n"
                if current_len + len(entry) > 62000: is_compressed = True; break
                report += entry; current_len += len(entry); processed_logs += 1
        if is_compressed: report += f"\n> 💡 **Nota**: Log comprimido para límites de GitHub ({processed_logs}/{len(self.action_log)} detallados).\n"
        report += "</details>\n\n---\n*📈 Inteligencia acumulada: `{len(self.learning_data['domains'])}`*"
        return report

async def main():
    try:
        cleaner = IntelligentLinkCleaner()
        await cleaner.build_global_registry()
        await cleaner.validate_links_tiered()
        
        log_event("STARTING NAVIGATION & REORGANIZATION AUDIT...", section_break=True)
        await cleaner.curator.suggest_reorganization()
        
        await cleaner.apply_changes()
        log_event("INTELLIGENT CLEANING COMPLETED SUCCESSFULLY.", section_break=True)
    except Exception as e:
        import traceback
        error_msg = f"[CRITICAL ERROR]: {e}"
        log_event(error_msg)
        print(traceback.format_exc())
        exit(1)

if __name__ == "__main__": asyncio.run(main())
