import asyncio
import json
import os
import re
import httpx
from datetime import datetime
from typing import Dict, List, Set, Tuple
from src.config import GH_TOKEN, TARGET_REPO, GEMINI_API_KEY, NUBENETES_CATEGORIES, MADRID_TZ
from src.gitops_manager import RepositoryController
from src.markdown_ast import MarkdownSanitizer

# Configuración de Excepciones (Archivos que no se podan)
CORE_FILES = ["docs/index.md", "README.md"]

class IntelligentLinkCleaner:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.sanitizer = MarkdownSanitizer()
        self.link_registry: Dict[str, List[Dict]] = {} # URL -> List of {file, line_content, score}
        self.dead_links: Set[str] = set()
        self.stats = {
            "total_links": 0,
            "dead_links_removed": 0,
            "duplicates_pruned": 0,
            "ai_decisions": 0
        }

    async def build_global_registry(self):
        print("[*] Construyendo registro global de enlaces...")
        # Incluimos archivos core + categorías
        all_files = CORE_FILES + [f"docs/{cat}.md" for cat in NUBENETES_CATEGORIES]
        
        for file_path in all_files:
            try:
                if not os.path.exists(file_path):
                    # Intentar obtener del repo si no está local (aunque debería estar)
                    repo_file = self.git_controller.repository.get_contents(file_path)
                    content = repo_file.decoded_content.decode("utf-8")
                else:
                    with open(file_path, 'r') as f:
                        content = f.read()
                
                lines = content.splitlines()
                for i, line in enumerate(lines):
                    match = self.sanitizer.link_pattern.search(line)
                    if match:
                        title, url = match.groups()
                        clean_url = url.split('#')[0].rstrip('/')
                        if "github.com" in clean_url and "/blob/" in clean_url:
                            continue # Evitar validar enlaces internos profundos de git por ahora
                        
                        score = self.sanitizer._calculate_link_score(line)
                        if clean_url not in self.link_registry:
                            self.link_registry[clean_url] = []
                        
                        self.link_registry[clean_url].append({
                            "file": file_path,
                            "line_index": i,
                            "content": line,
                            "score": score,
                            "title": title
                        })
                        self.stats["total_links"] += 1
            except Exception as e:
                print(f"[!] Error procesando {file_path}: {e}")

    async def validate_links_tiered(self):
        """Validación en dos niveles: HTTP -> Playwright"""
        print(f"[*] Validando {len(self.link_registry)} URLs únicas...")
        
        unique_urls = list(self.link_registry.keys())
        # Para evitar saturar, validamos en batches
        batch_size = 50
        for i in range(0, len(unique_urls), batch_size):
            batch = unique_urls[i:i+batch_size]
            tasks = [self._check_url_sophisticated(url) for url in batch]
            results = await asyncio.gather(*tasks)
            for url, is_alive in results:
                if not is_alive:
                    self.dead_links.add(url)
            print(f"    - Progreso: {min(i+batch_size, len(unique_urls))}/{len(unique_urls)}")

    async def _check_url_sophisticated(self, url: str) -> Tuple[str, bool]:
        # TIER 1: HTTP Fast
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"
        }
        try:
            async with httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=10) as client:
                resp = await client.get(url)
                if resp.status_code < 400:
                    return url, True
                if resp.status_code not in [403, 429, 401]:
                    return url, False # 404, 500 etc son muertos
        except Exception:
            pass # Errores de conexión pasan a Tier 2

        # TIER 2: Playwright (Solo si Tier 1 falla con sospecha de bloqueo)
        try:
            from playwright.async_api import async_playwright
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                page = await browser.new_page()
                # User agent real para Playwright
                await page.set_extra_http_headers({"User-Agent": headers["User-Agent"]})
                response = await page.goto(url, wait_until="networkidle", timeout=20000)
                is_alive = response.status < 400 if response else False
                await browser.close()
                return url, is_alive
        except Exception as e:
            # Si Playwright también falla, asumimos que puede estar muerto o es inaccesible
            # pero para ser conservadores, solo marcamos como muerto si es un error claro
            return url, True # Conservador: Si todo falla, no lo borramos todavía

    async def resolve_duplicates_with_ai(self):
        print("[*] Resolviendo duplicados globales con Gemini...")
        for url, occurrences in self.link_registry.items():
            if len(occurrences) <= 1 or url in self.dead_links:
                continue
            
            # Si alguna ocurrencia está en CORE_FILES, esa manda pero no borra el resto necesariamente
            # a menos que Gemini diga que es redundante.
            
            # Filtrar ocurrencias que NO están en archivos core para ver qué podemos podar
            prunable = [occ for occ in occurrences if occ["file"] not in CORE_FILES]
            if len(prunable) <= 1 and len(occurrences) - len(prunable) >= 1:
                # Ya está en un CORE_FILE y solo en un sitio más, lo dejamos estar
                continue

            if len(prunable) > 1:
                # Preguntar a Gemini
                decision = await self._ask_gemini_dedup(url, occurrences)
                self.stats["ai_decisions"] += 1
                
                # 'decision' debería decirnos qué archivos mantener
                files_to_keep = decision.get("keep_in_files", [])
                for occ in prunable:
                    if occ["file"] not in files_to_keep:
                        occ["should_prune"] = True
                        self.stats["duplicates_pruned"] += 1

    async def _ask_gemini_dedup(self, url: str, occurrences: List[Dict]) -> Dict:
        api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        contexts = "\n".join([f"- Archivo: {occ['file']}, Contexto: {occ['content']}" for occ in occurrences])
        prompt = (
            f"El enlace {url} aparece en múltiples archivos de mi repositorio de Kubernetes.\n"
            f"Ocurrencias:\n{contexts}\n\n"
            "Analiza si el enlace es fundamental en todos esos contextos o si es redundante y debería estar solo en el más relevante.\n"
            "Responde en JSON: {\"keep_in_files\": [\"lista de archivos donde mantenerlo\"], \"reason\": \"...\"}"
        )
        
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(api_url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=20)
                if resp.status_code == 200:
                    text = resp.json()['candidates'][0]['content']['parts'][0]['text']
                    match = re.search(r'\{.*\}', text, re.DOTALL)
                    if match:
                        return json.loads(match.group(0))
        except: pass
        # Fallback: Mantener solo el que tiene mayor score
        best_file = max(occurrences, key=lambda x: x["score"])["file"]
        return {"keep_in_files": [best_file]}

    async def apply_changes(self):
        print("[*] Aplicando limpieza a los archivos...")
        file_updates = {}
        
        # Agrupar podas por archivo
        prunes_by_file = {}
        for url, occurrences in self.link_registry.items():
            is_dead = url in self.dead_links
            for occ in occurrences:
                if is_dead or occ.get("should_prune"):
                    if occ["file"] not in prunes_by_file:
                        prunes_by_file[occ["file"]] = []
                    # Guardamos si es por muerto para la lógica de excepciones
                    prunes_by_file[occ["file"]].append({
                        "idx": occ["line_index"],
                        "is_dead": is_dead,
                        "url": url
                    })

        for file_path, tasks in prunes_by_file.items():
            try:
                with open(file_path, 'r') as f:
                    lines = f.readlines()
                
                original_count = len(lines)
                # Borrar de atrás hacia adelante para no arruinar índices
                for task in sorted(tasks, key=lambda x: x["idx"], reverse=True):
                    idx = task["idx"]
                    is_dead = task["is_dead"]
                    
                    # Regla: Solo borramos de CORE_FILES si el link está MUERTO.
                    # Los duplicados se permiten en CORE_FILES.
                    if file_path not in CORE_FILES or is_dead:
                        if idx < len(lines):
                            lines.pop(idx)
                            if is_dead: 
                                self.stats["dead_links_removed"] += 1
                            else:
                                self.stats["duplicates_pruned"] += 1

                if len(lines) < original_count:
                    file_updates[file_path] = "".join(lines)
                    print(f"    - {file_path}: {original_count - len(lines)} líneas eliminadas.")
            except Exception as e:
                print(f"[!] Error al procesar limpieza en {file_path}: {e}")

        if file_updates:
            print(f"[+] Generando PR con {len(file_updates)} archivos modificados.")
            metrics = {
                "total_cleaned": self.stats["dead_links_removed"] + self.stats["duplicates_pruned"],
                "dead_removed": self.stats["dead_links_removed"],
                "duplicates_pruned": self.stats["duplicates_pruned"],
                "ai_decisions": self.stats["ai_decisions"],
                "files_impacted": list(file_updates.keys())
            }
            self._create_pr(file_updates, metrics)
        else:
            print("[~] No se encontraron mejoras necesarias (todo limpio).")

    def _create_pr(self, updates: Dict[str, str], metrics: Dict):
        # Usamos el git_controller para aplicar cambios
        # (Modificado para este script específico)
        timestamp = datetime.now().strftime("%Y%m%d-%H%M")
        branch_name = f"bot/intelligent-clean-{timestamp}"
        self.git_controller._create_feature_branch(branch_name)

        for path, content in updates.items():
            file_meta = self.git_controller.repository.get_contents(path)
            self.git_controller.repository.update_file(
                path=path,
                message=f"fix(clean): limpieza inteligente de enlaces en {path}",
                content=content,
                sha=file_meta.sha,
                branch=branch_name
            )

        body = (
            f"## 🤖 Limpieza Inteligente de Enlaces (May 2026)\n\n"
            f"He completado un ciclo de revisión global utilizando **Playwright** para evasión de bloqueos y **Gemini** para deduplicación inteligente.\n\n"
            f"### 📊 Resumen de Ejecución:\n"
            f"- 💀 Enlaces muertos eliminados: `{metrics['dead_removed']}`\n"
            f"- ✂️ Duplicados globales podados: `{metrics['duplicates_pruned']}`\n"
            f"- 🧠 Decisiones asistidas por IA: `{metrics['ai_decisions']}`\n\n"
            f"### 📂 Archivos Optimizados:\n" + 
            "\n".join([f"- `{f}`" for f in metrics['files_impacted']])
        )
        
        self.git_controller.repository.create_pull(
            title=f"🧹 Intelligent Link Clean & Dedup: {datetime.now().strftime('%d %b %Y')}",
            body=body,
            head=branch_name,
            base="master"
        )

async def main():
    cleaner = IntelligentLinkCleaner()
    await cleaner.build_global_registry()
    await cleaner.validate_links_tiered()
    await cleaner.resolve_duplicates_with_ai()
    await cleaner.apply_changes()

if __name__ == "__main__":
    asyncio.run(main())
