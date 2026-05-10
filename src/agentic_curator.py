import os
import re
import json
import asyncio
import httpx
from typing import List, Dict, Set
from src.config import GEMINI_API_KEY, GH_TOKEN, TARGET_REPO, NUBENETES_CATEGORIES
from src.gitops_manager import RepositoryController

class AgenticCurator:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.docs_dir = "docs"
        self.index_path = os.path.join(self.docs_dir, "index.md")
        self.mkdocs_path = "mkdocs.yml"
        self.stats = {
            "orphans_found": 0, 
            "orphans_linked": 0, 
            "structural_improvements": 0,
            "orphan_details": []
        }

    def _get_all_docs(self) -> Set[str]:
        return {f for f in os.listdir(self.docs_dir) if f.endswith('.md')}

    def _get_nav_files(self) -> Set[str]:
        with open(self.mkdocs_path, 'r') as f:
            content = f.read()
        # Captura archivos .md precedidos por ":" o espacio, terminando con salto de línea o espacio
        return set(re.findall(r'[:\s]([a-zA-Z0-9_\-\./]+\.md)', content))

    def _get_index_links(self) -> Set[str]:
        with open(self.index_path, 'r') as f:
            content = f.read()
        return set(re.findall(r'\]\(([^)]+\.md)\)', content))

    async def audit_navigation(self):
        print("[*] Iniciando auditoría de navegación...")
        all_docs = self._get_all_docs()
        nav_files = self._get_nav_files()
        index_links = self._get_index_links()

        orphans = all_docs - nav_files - index_links - {"index.md", "tags.md"}
        self.stats["orphans_found"] = len(orphans)

        if orphans:
            print(f"[!] Se encontraron {len(orphans)} archivos huérfanos: {orphans}")
            await self._resolve_orphans(list(orphans))
        else:
            print("[+] No se detectaron archivos huérfanos.")

    async def _resolve_orphans(self, orphans: List[str]):
        """Usa Gemini para decidir dónde colocar los huérfanos."""
        for orphan in orphans:
            print(f"[*] Buscando hogar para {orphan}...")
            try:
                with open(os.path.join(self.docs_dir, orphan), 'r') as f:
                    content = f.read(1000)
            except: content = "No content available"

            decision = await self._ask_gemini_placement(orphan, content)
            if decision:
                await self._apply_placement(orphan, decision)
                self.stats["orphans_linked"] += 1
                self.stats["orphan_details"].append({
                    "file": orphan, 
                    "title": decision.get("title"), 
                    "category": decision.get("category")
                })

    async def _ask_gemini_placement(self, filename: str, content: str) -> Dict:
        with open(self.mkdocs_path, 'r') as f:
            nav_context = f.read()
        
        prompt = (
            f"Tengo un archivo markdown llamado '{filename}' en mi repositorio de Kubernetes que no está enlazado.\n"
            f"Contenido (primeros caracteres):\n{content}\n\n"
            f"Estructura actual del menú (mkdocs.yml):\n{nav_context}\n\n"
            "Dime:\n"
            "1. ¿Bajo qué sección del menú (nav) debería estar?\n"
            "2. ¿Cuál sería un título descriptivo para el menú?\n"
            "3. ¿Bajo qué encabezado (##) del index.md debería aparecer?\n"
            "Responde en JSON: {\"category\": \"Nombre de la Sección en nav\", \"title\": \"Título para el link\", \"index_section\": \"Sección en index.md\"}"
        )

        api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(api_url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=20)
                if resp.status_code == 200:
                    text = resp.json()['candidates'][0]['content']['parts'][0]['text']
                    match = re.search(r'\{.*\}', text, re.DOTALL)
                    if match: return json.loads(match.group(0))
        except: pass
        return None

    async def _apply_placement(self, filename: str, decision: Dict):
        section = decision.get("index_section", "More References")
        title = decision.get("title", filename.replace(".md", ""))
        
        with open(self.index_path, 'r') as f:
            index_lines = f.readlines()

        section_found = False
        for i, line in enumerate(index_lines):
            if section.lower() in line.lower() and line.startswith("##"):
                index_lines.insert(i + 1, f"- [{title}]({filename})\n")
                section_found = True
                break
        
        if not section_found:
            index_lines.append(f"\n## {section}\n- [{title}]({filename})\n")

        with open(self.index_path, 'w') as f:
            f.writelines(index_lines)

        with open(self.mkdocs_path, 'r') as f:
            mkdocs_lines = f.readlines()
        
        for i, line in enumerate(mkdocs_lines):
            if line.strip().startswith("- About:"):
                mkdocs_lines.insert(i, f"  - {title}: {filename}\n")
                break
        
        with open(self.mkdocs_path, 'w') as f:
            f.writelines(mkdocs_lines)

    async def suggest_reorganization(self):
        """Analiza la densidad de archivos por categoría y sugiere mejoras."""
        print("[*] Analizando densidad de categorías...")
        with open(self.mkdocs_path, 'r') as f:
            content = f.read()
        
        sections = re.split(r'  - ', content)
        for section in sections:
            count = len(re.findall(r'\.md', section))
            if count > 15:
                lines = section.split('\n')
                if lines:
                    section_name = lines[0].split(':')[0].strip()
                    print(f"    [~] La sección '{section_name}' tiene muchos archivos ({count}).")
                    self.stats["structural_improvements"] += 1

    def validate_changes(self) -> bool:
        try:
            with open(self.mkdocs_path, 'r') as f:
                content = f.read()
                if "nav:" not in content: return False
            with open(self.index_path, 'r') as f:
                content = f.read()
                if not content.startswith("#"): return False
            return True
        except:
            return False

async def main():
    curator = AgenticCurator()
    await curator.audit_navigation()
    await curator.suggest_reorganization()
    if curator.validate_changes():
        print("[+] Estructura validada.")
    else:
        print("[!] Error en validación.")

if __name__ == "__main__":
    asyncio.run(main())
