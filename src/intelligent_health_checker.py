import asyncio
import json
import os
import re
import httpx
import random
from datetime import datetime
from typing import Dict, List, Set, Tuple, Optional
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
        return {"domains": {}, "known_soft_404_patterns": []}

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

    async def _check_url_with_retries(self, url: str, max_retries=3) -> Tuple[str, bool, Optional[str], str]:
        domain = url.split("//")[-1].split("/")[0]
        domain_info = self.learning_data["domains"].get(domain, {})
        use_playwright_first = domain_info.get("requires_playwright", False)
        
        for attempt in range(max_retries):
            try:
                if attempt > 0: await asyncio.sleep((2 ** attempt) + random.random())
                is_alive, reason = await self._check_url_logic(url, use_playwright_first)
                if is_alive:
                    if domain not in self.learning_data["domains"]: self.learning_data["domains"][domain] = {"success_count": 0, "fail_count": 0}
                    self.learning_data["domains"][domain]["success_count"] += 1
                    return url, True, None, "Alive"
                if reason in ["404", "soft_404", "redirect_to_home"]:
                    if any(git_host in url for git_host in ["github.com", "gitlab.com", "bitbucket.org"]):
                        parts = url.split("/")
                        if len(parts) > 4:
                            repo_root = "/".join(parts[:5])
                            root_alive, _ = await self._check_url_logic(repo_root, False)
                            if root_alive: return url, False, f"REPO_ROOT:{repo_root}", f"Consolidated (Original: {reason})"
                    archived = await self._check_wayback(url)
                    if archived: return url, False, f"ARCHIVE:{archived}", f"Archived (Original: {reason})"
                    return url, False, None, reason
            except: pass
        return url, True, None, "Keep (Error)"

    async def _check_url_logic(self, url: str, force_playwright: bool) -> Tuple[bool, str]:
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36", "Referer": "https://www.google.com/"}
        if not force_playwright:
            try:
                async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=12) as client:
                    resp = await client.get(url)
                    if resp.status_code in [404, 410]: return False, "404"
                    if resp.status_code < 300:
                        final_url = str(resp.url).rstrip('/')
                        original_base = "/".join(url.split("/")[:3])
                        if len(url) > len(original_base) + 10 and final_url == original_base: pass
                        else: return True, "ok"
                    if resp.status_code in [403, 429, 401]:
                        domain = url.split("//")[-1].split("/")[0]
                        if domain not in self.learning_data["domains"]: self.learning_data["domains"][domain] = {}
                        self.learning_data["domains"][domain]["requires_playwright"] = True
            except: pass
        try:
            from playwright.async_api import async_playwright
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page(user_agent=headers["User-Agent"])
                try:
                    response = await page.goto(url, wait_until="domcontentloaded", timeout=25000)
                    if not response: return True, "timeout"
                    if response.status in [404, 410]: return False, "404"
                    content = (await page.content()).lower(); title = (await page.title()).lower()
                    soft_404_keywords = ["page not found", "404 not found", "artículo no encontrado", "página no encontrada"]
                    if any(kw in title for kw in soft_404_keywords) or (("404" in title) and any(kw in content for kw in soft_404_keywords)): return False, "soft_404"
                    final_url = page.url.rstrip('/'); original_base = "/".join(url.split("/")[:3])
                    if len(url) > len(original_base) + 10 and final_url == original_base: return False, "redirect_to_home"
                    return True, "ok"
                finally: await browser.close()
        except: return True, "engine_error"

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
        for i in range(0, len(unique_urls), 20):
            batch = unique_urls[i:i+20]
            tasks = [self._check_url_with_retries(url) for url in batch]
            results = await asyncio.gather(*tasks)
            for url, is_alive, fallback, reason in results:
                if not is_alive: self.dead_links[url] = (fallback if fallback else "DEAD", reason)
            self._save_memory()

    async def apply_changes(self):
        print("[*] Aplicando cambios y métricas visuales...")
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
                    real_fallback = fallback.replace("ARCHIVE:", "")
                    file_updates[file_path][line_idx] = file_updates[file_path][line_idx].replace(url, real_fallback)
                    if "[ARCHIVED]" not in file_updates[file_path][line_idx]: file_updates[file_path][line_idx] = file_updates[file_path][line_idx].replace("](", " [ARCHIVED]]( ")
                    track(file_path, "modified", url, reason); self.detailed_stats["operation_types"]["archived"] += 1
                elif fallback and fallback.startswith("REPO_ROOT:"):
                    real_fallback = fallback.replace("REPO_ROOT:", "")
                    file_updates[file_path][line_idx] = file_updates[file_path][line_idx].replace(url, real_fallback)
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

    def _create_pr(self, updates: Dict[str, str]):
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        branch_name = f"bot/autonomous-health-{timestamp}"
        self.git_controller._create_feature_branch(branch_name)
        for path, content in updates.items():
            try:
                file_meta = self.git_controller.repository.get_contents(path)
                self.git_controller.repository.update_file(path=path, message=f"fix(autonomous): engine update in {path}", content=content, sha=file_meta.sha, branch=branch_name)
            except: pass

        report = "## 🧠 Nubenetes Autonomous Health & Curation Engine\n\n"
        
        # Mermaid Pie Chart
        report += "### 📊 Distribución de Operaciones\n"
        report += "```mermaid\npie title Operaciones de Mantenimiento\n"
        report += f"    \"Muertos (Eliminados)\" : {self.detailed_stats['operation_types']['removals']}\n"
        report += f"    \"Archivados (Wayback)\" : {self.detailed_stats['operation_types']['archived']}\n"
        report += f"|    \"Consolidados (Git)\" : {self.detailed_stats['operation_types']['consolidated']}\n"
        report += f"    \"Nuevos (Huérfanos)\" : {self.detailed_stats['operation_types']['orphans']}\n```\n\n"

        # Executive Summary
        report += "### 📈 Resumen de Operaciones\n"
        report += "| Operación | Cantidad | Impacto / Detalle |\n| :--- | :---: | :--- |\n"
        report += f"| 💀 Eliminados | **{self.detailed_stats['operation_types']['removals']}** | 404 definitivos (No recuperables) |\n"
        report += f"| 🏛️ Archivados | **{self.detailed_stats['operation_types']['archived']}** | Restaurados vía Wayback Machine |\n"
        report += f"| 🎯 Consolidados | **{self.detailed_stats['operation_types']['consolidated']}** | Deep-links Git movidos a la raíz |\n"
        report += f"| 🖇️ Nuevos | **{self.detailed_stats['operation_types']['orphans']}** | Páginas vinculadas automáticamente |\n\n"

        # Health Matrix (Documentos Críticos)
        report += "### 🧮 Matriz de Mantenimiento por Documento\n"
        report += "| Documento | 🔴 Elim | 🟡 Mod | 🟢 Crea | Estado |\n| :--- | :---: | :---: | :---: | :---: |\n"
        for file, s in sorted(self.detailed_stats["by_file"].items()):
            status = "🧹 Limpio" if s['removed'] + s['modified'] < 3 else "🛠️ Refactor"
            if s['removed'] > 5: status = "⚠️ Crítico"
            report += f"| `{file}` | {s['removed']} | {s['modified']} | {s['created']} | {status} |\n"

        # Action Log
        report += "\n### 📝 Registro Detallado (Log)\n<details><summary>Click para ver todas las acciones</summary>\n\n"
        report += "| Archivo | Acción | URL / Recurso | Motivo |\n| :--- | :---: | :--- | :--- |\n"
        for log in sorted(self.action_log, key=lambda x: x["file"]):
            emoji = {"removed": "❌", "modified": "🔄", "created": "✨"}.get(log["action"], "❓")
            report += f"| `{log['file']}` | {emoji} | {log['url']} | {log['reason']} |\n"
        report += "</details>\n\n"

        report += f"\n---\n*📈 Inteligencia de dominios acumulada: `{len(self.learning_data['domains'])}`*"
        self.git_controller.repository.create_pull(title=f"🧹 Autonomous Engine Health Report: {datetime.now().strftime('%d %b %Y')}", body=report, head=branch_name, base="master")

async def main():
    cleaner = IntelligentLinkCleaner()
    await cleaner.build_global_registry()
    await cleaner.validate_links_tiered()
    await cleaner.curator.audit_navigation()
    await cleaner.curator.suggest_reorganization()
    await cleaner.apply_changes()

if __name__ == "__main__": asyncio.run(main())
