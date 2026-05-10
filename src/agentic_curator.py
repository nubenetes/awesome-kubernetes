import os
import re
import json
import asyncio
import httpx
from bs4 import BeautifulSoup
from typing import List, Dict, Set, Optional
from src.config import GEMINI_API_KEY, GH_TOKEN, TARGET_REPO, NUBENETES_CATEGORIES
from src.gitops_manager import RepositoryController

async def _deep_fetch_content(url: str) -> str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, timeout=10, headers=headers)
            if resp.status_code == 200:
                html = resp.text
                soup = BeautifulSoup(html, 'html.parser')
                for s in soup(['script', 'style', 'nav', 'footer']):
                    s.decompose()
                return soup.get_text(separator=' ', strip=True)[:3000]
    except: return ""
    return ""

async def evaluate_extracted_assets(raw_assets: List[Dict]) -> List[Dict]:
    curated_assets = []
    api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    
    # Cargar reputación de dominios para filtrado rápido
    memory_file = "src/memory/health_learning.json"
    domain_blacklist = set()
    if os.path.exists(memory_file):
        try:
            with open(memory_file, 'r') as f:
                memory_data = json.load(f)
                domain_blacklist = set(memory_data.get("blacklisted_domains", []))
        except: pass

    for asset in raw_assets:
        domain = asset['url'].split("//")[-1].split("/")[0]
        if domain in domain_blacklist:
            print(f"[~] Saltando {domain} (Baja reputación en memoria)")
            continue

        web_content = await _deep_fetch_content(asset['url'])
        
        prompt = (
            "Actúas como Ingeniero Curador Senior de 'nubenetes/awesome-kubernetes'. "
            f"Filtra este recurso para estas categorías: {', '.join(NUBENETES_CATEGORIES)}. "
            "Si es sobre Model Context Protocol (MCP), asígnalo a 'ai-agents-mcp'.\n"
            f"URL: {asset['url']}\nContexto: {asset['context']}\nWeb: {web_content}\n\n"
            "Evalúa el IMPACTO SOCIAL y PROFUNDIDAD (1-100):\n"
            "- >80: Recurso excepcional, disruptivo (añadir estrella 🌟).\n"
            "- <20: Contenido pobre, clickbait o marketing puro (descartar).\n\n"
            "Responde SOLAMENTE un JSON: {\"is_exceptional\": bool, \"impact_score\": int, \"categories\": [\"cat1\"], \"title\": \"...\", \"desc\": \"...\"}"
        )

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(api_url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=30)
                if response.status_code == 200:
                    text_resp = response.json()['candidates'][0]['content']['parts'][0]['text']
                    match = re.search(r'\{.*\}', text_resp, re.DOTALL)
                    if match:
                        data = json.loads(match.group(0))
                        score = data.get("impact_score", 50)
                        
                        if score < 20:
                            # Añadir a blacklist si es muy malo
                            domain_blacklist.add(domain)
                            continue
                            
                        if data.get("is_exceptional") or score > 40:
                            title = data["title"]
                            if score > 80: title += " 🌟"
                            
                            for cat in data.get("categories", []):
                                if cat in NUBENETES_CATEGORIES:
                                    curated_assets.append({
                                        "url": asset["url"], "title": title,
                                        "description": data["desc"], "category": cat
                                    })
        except Exception as e:
            print(f"[!] Error evaluando {asset['url']}: {e}")
            
    # Guardar blacklist actualizada
    if domain_blacklist:
        try:
            with open(memory_file, 'r+') as f:
                mem = json.load(f)
                mem["blacklisted_domains"] = list(domain_blacklist)
                f.seek(0); json.dump(mem, f, indent=2); f.truncate()
        except: pass

    return curated_assets

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
        for orphan in orphans:
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
            f"Archivo: '{filename}'\nContenido: {content}\n\n"
            f"Menú actual:\n{nav_context}\n\n"
            "Responde JSON: {\"category\": \"Sección nav\", \"title\": \"Título\", \"index_section\": \"Sección index\"}"
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
        """
        Analiza la estructura de los documentos para mejorar la jerarquía interna.
        En lugar de dividir por número de links, busca coherencia temática y 
        propone subsecciones (##, ###) o nuevas páginas solo si el tema es 
        completamente disruptivo, manteniendo la navegación limpia.
        """
        print("[*] Analizando coherencia y jerarquía de categorías...")
        for category in NUBENETES_CATEGORIES:
            file_path = os.path.join(self.docs_dir, f"{category}.md")
            if not os.path.exists(file_path): continue
            
            # Solo analizamos archivos grandes para optimizar su estructura interna
            if os.path.getsize(file_path) > 50000: # >50KB suele indicar mucha densidad
                print(f"    [~] Analizando optimización jerárquica para '{category}'...")
                await self._optimize_file_hierarchy(category, file_path)

    async def _optimize_file_hierarchy(self, category: str, file_path: str):
        with open(file_path, 'r') as f:
            content = f.read()

        prompt = (
            f"Actúas como Arquitecto de Información para Nubenetes.\n"
            f"El documento '{category}.md' tiene mucha información. No quiero dividirlo en muchos archivos pequeños.\n"
            f"Prefiero una jerarquía profunda (Secciones ##, Subsecciones ###) dentro del mismo archivo.\n"
            "Analiza este contenido y propón una nueva estructura de encabezados que agrupe mejor los links.\n"
            "Si detectas un subtema que REALMENTE merece su propia página por ser muy distinto, dímelo.\n"
            "Responde JSON: {\"internal_structure\": \"...contenido completo con nuevos encabezados...\", \"new_pages\": [{\"name\": \"...\", \"title\": \"...\", \"content\": \"...\", \"nav_parent\": \"...\"}]}"
        )
        
        api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(api_url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=60)
                if resp.status_code == 200:
                    raw_text = resp.json()['candidates'][0]['content']['parts'][0]['text']
                    data = json.loads(re.search(r'\{.*\}', raw_text, re.DOTALL).group(0))
                    
                    # 1. Aplicar reestructuración interna
                    if data.get("internal_structure"):
                        with open(file_path, 'w') as f:
                            f.write(data["internal_structure"])
                        print(f"    [+] Jerarquía interna optimizada en {category}.md")

                    # 2. Gestionar nuevas páginas (solo si son estrictamente necesarias)
                    for new_pg in data.get("new_pages", []):
                        await self._create_and_link_new_page(new_pg)
        except Exception as e:
            print(f"    [!] Error en optimización jerárquica: {e}")

    async def _create_and_link_new_page(self, page_data: Dict):
        name = page_data["name"]
        if not name.endswith(".md"): name += ".md"
        path = os.path.join(self.docs_dir, name)
        
        # Crear el archivo
        with open(path, 'w') as f:
            f.write(f"# {page_data['title']}\n\n{page_data['content']}")
        
        print(f"    [+] Nueva página disruptiva creada: {name}")
        
        # Vincular de forma autónoma en mkdocs.yml (bajo el padre sugerido o sección lógica)
        await self._apply_placement(name, {
            "category": page_data.get("nav_parent", "More Resources"),
            "title": page_data["title"],
            "index_section": page_data.get("nav_parent", "Miscellaneous")
        })
        self.stats["structural_improvements"] += 1

    def validate_changes(self) -> bool:
        try:
            with open(self.mkdocs_path, 'r') as f:
                if "nav:" not in f.read(): return False
            return True
        except: return False


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
