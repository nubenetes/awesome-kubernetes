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

# Configuración de Excepciones
CORE_FILES = ["docs/index.md", "README.md"]
MEMORY_FILE = "src/memory/health_learning.json"

class IntelligentLinkCleaner:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.sanitizer = MarkdownSanitizer()
        self.curator = AgenticCurator()
        self.link_registry: Dict[str, List[Dict]] = {}
        self.dead_links: Dict[str, Tuple[str, str]] = {} 
        self.learning_data = self._load_memory()
        self.action_log: List[Dict] = [] 
        self.detailed_stats = {
            "total_scanned": 0,
            "skipped_recent": 0,
            "by_file": {}, 
            "by_category": {}, 
            "operation_types": {"removals": 0, "archived": 0, "consolidated": 0, "orphans": 0}
        }
        self.stats = {"total_links": 0, "dead_links_removed": 0, "duplicates_pruned": 0, "ai_decisions": 0, "archived_fallbacks": 0, "orphans_fixed": 0}

    def _load_memory(self) -> Dict:
        if os.path.exists(MEMORY_FILE):
            try:
                with open(MEMORY_FILE, 'r') as f: return json.load(f)
            except: pass
        return {"domains": {}, "link_cache": {}, "known_soft_404_patterns": []}

    def _save_memory(self):
        os.makedirs(os.path.dirname(MEMORY_FILE), exist_ok=True)
        with open(MEMORY_FILE, 'w') as f: json.dump(self.learning_data, f, indent=2)

    async def _check_wayback(self, url: str) -> Optional[str]:
        api_url = f"https://archive.org/wayback/available?url={url}"
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                resp = await client.get(api_url)
                if resp.status_code == 200:
                    data = resp.json()
                    if data.get("archived_snapshots", {}).get("closest"): return data["archived_snapshots"]["closest"]["url"]
        except: pass
        return None

    async def _check_url_with_retries(self, url: str, max_retries=5) -> Tuple[str, bool, Optional[str], str]:
        now = datetime.now().timestamp()
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
            {"type": "playwright", "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36", "ref": "https://www.linkedin.com/", "desc": "PW Desktop/LinkedIn"},
            {"type": "http", "ua": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/115.0", "ref": "https://news.ycombinator.com/", "desc": "Firefox/Reddit"},
            {"type": "playwright", "ua": "Mozilla/5.0 (Linux; Android 13; SM-S918B) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Mobile Safari/537.36", "ref": "https://www.google.com/", "desc": "PW Mobile/Google"}
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
                    
                    if "link_cache" not in self.learning_data: self.learning_data["link_cache"] = {}
                    self.learning_data["link_cache"][url] = {"status": "ALIVE", "last_checked": now}
                    return url, True, None, f"Alive ({strategy['desc']}) - {reason}"

                if reason in ["404", "soft_404", "redirect_to_home"]:
                    if any(git_host in url for git_host in ["github.com", "gitlab.com", "bitbucket.org"]):
                        parts = url.split("/"); repo_root = "/".join(parts[:5]) if len(parts) > 4 else None
                        if repo_root:
                            root_alive, _ = await self._check_url_logic(repo_root, strategies[0])
                            if root_alive: return url, False, f"REPO_ROOT:{repo_root}", f"Consolidated (Original: {reason})"
                    if attempt == max_retries - 1:
                        archived = await self._check_wayback(url)
                        if archived: return url, False, f"ARCHIVE:{archived}", f"Archived (Original: {reason})"
                        return url, False, None, reason
            except: pass
        return url, True, None, "Conservative Keep"

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
        print("[*] Construyendo registro global...")
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

    async def validate_links_tiered(self):
        print(f"[*] Validando {len(self.link_registry)} URLs...")
        unique_urls = list(self.link_registry.keys()); random.shuffle(unique_urls)
        for i in range(0, len(unique_urls), 40):
            batch = unique_urls[i:i+40]
            tasks = [self._check_url_with_retries(url) for url in batch]
            results = await asyncio.gather(*tasks)
            for url, is_alive, fallback, reason in results:
                if not is_alive: self.dead_links[url] = (fallback if fallback else "DEAD", reason)
            self._save_memory()

    async def apply_changes(self):
        print("[*] Aplicando cambios y generando métricas visuales...")
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
                if fallback and fallback.startswith("ARCHIVE:"):
                    real_f = fallback.replace("ARCHIVE:", "")
                    file_updates[file_path][line_idx] = file_updates[file_path][line_idx].replace(url, real_f)
                    if "[ARCHIVED]" not in file_updates[file_path][line_idx]: file_updates[file_path][line_idx] = file_updates[file_path][line_idx].replace("](", " [ARCHIVED]]( ")
                    track(file_path, "modified", url, reason); self.detailed_stats["operation_types"]["archived"] += 1
                elif fallback and fallback.startswith("REPO_ROOT:"):
                    real_f = fallback.replace("REPO_ROOT:", "")
                    file_updates[file_path][line_idx] = file_updates[file_path][line_idx].replace(url, real_f)
                    track(file_path, "modified", url, reason); self.detailed_stats["operation_types"]["consolidated"] += 1
                else:
                    if file_path not in CORE_FILES:
                        file_updates[file_path][line_idx] = None
                        track(file_path, "removed", url, reason); self.detailed_stats["operation_types"]["removals"] += 1

        if self.curator.stats["orphans_linked"] > 0:
            track("Navigation", "created", "Orphan Audit", "Linked via Curator")
            self.detailed_stats["operation_types"]["orphans"] = self.curator.stats["orphans_linked"]

        final_payload = {p: "".join([l for l in lines if l is not None]) for p, lines in file_updates.items()}
        if self.curator.stats["orphans_linked"] > 0:
            with open(self.curator.index_path, 'r') as f: final_payload[self.curator.index_path] = f.read()
            with open(self.curator.mkdocs_path, 'r') as f: final_payload[self.curator.mkdocs_path] = f.read()
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
        self.git_controller.repository.create_pull(title=f"🧹 Autonomous Engine Health Report: {datetime.now().strftime('%d %b %Y')}", body=safe_report, head=branch_name, base="master")

    def _build_report_body(self) -> str:
        report = "## 🧠 Nubenetes Autonomous Health & Curation Engine\n\n"
        report += "### 📊 Distribución de Operaciones\n"
        report += "```mermaid\npie title Operaciones de Mantenimiento\n"
        report += f"    \"Eliminados\" : {self.detailed_stats['operation_types']['removals']}\n"
        report += f"    \"Archivados\" : {self.detailed_stats['operation_types']['archived']}\n"
        report += f"    \"Consolidados\" : {self.detailed_stats['operation_types']['consolidated']}\n"
        report += f"    \"Nuevos\" : {self.detailed_stats['operation_types']['orphans']}\n```\n\n"
        report += "### 📈 Resumen de Eficiencia\n"
        report += "| Métrica | Cantidad | Detalle |\n| :--- | :---: | :--- |\n"
        report += f"| ⏩ Omitidos (Cache) | **{self.detailed_stats['skipped_recent']}** | Verificados hace menos de 21 días |\n"
        report += f"| 💀 Eliminados | **{self.detailed_stats['operation_types']['removals']}** | 404 definitivos |\n"
        report += f"| 🏛️ Archivados | **{self.detailed_stats['operation_types']['archived']}** | Vía Wayback Machine |\n"
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
        await cleaner.curator.audit_navigation()
        await cleaner.curator.suggest_reorganization()
        await cleaner.apply_changes()
    except Exception as e:
        import traceback; print(f"[CRITICAL ERROR]: {e}"); traceback.print_exc(); exit(1)

if __name__ == "__main__": asyncio.run(main())
