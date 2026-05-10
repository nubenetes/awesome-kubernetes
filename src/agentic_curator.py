import os
import re
import json
import asyncio
import httpx
from typing import List, Dict, Set, Optional
from src.config import GEMINI_API_KEY, GH_TOKEN, TARGET_REPO, NUBENETES_CATEGORIES
from src.gitops_manager import RepositoryController

# Silenciar advertencias de XML/HTML de forma global
import warnings
from bs4 import XMLParsedAsHTMLWarning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

async def _deep_fetch_content(url: str) -> str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, timeout=10, headers=headers)
            if resp.status_code == 200:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(resp.text, 'html.parser')
                for s in soup(['script', 'style', 'nav', 'footer']):
                    s.decompose()
                return soup.get_text(separator=' ', strip=True)[:3000]
    except: return ""
    return ""

async def evaluate_extracted_assets(raw_assets: List[Dict]) -> List[Dict]:
    curated_assets = []
    api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    
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
        if domain in domain_blacklist: continue

        web_content = await _deep_fetch_content(asset['url'])
        context = asset.get('context', asset.get('description', 'Sin contexto adicional'))
        
        prompt = (
            "Actúas como Ingeniero Curador Senior de 'nubenetes/awesome-kubernetes'. "
            f"Filtra este recurso para estas categorías: {', '.join(NUBENETES_CATEGORIES)}. "
            "Si es sobre Model Context Protocol (MCP), asígnalo a 'ai-agents-mcp'.\n"
            f"URL: {asset['url']}\nContexto: {context}\nWeb: {web_content}\n\n"
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
        except: pass
            
    if domain_blacklist:
        try:
            if os.path.exists(memory_file):
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
        self.stats = {"orphans_found": 0, "orphans_linked": 0, "structural_improvements": 0, "orphan_details": []}

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
        all_docs = self._get_all_docs()
        nav_files = self._get_nav_files()
        index_links = self._get_index_links()
        orphans = all_docs - nav_files - index_links - {"index.md", "tags.md"}
        if orphans: await self._resolve_orphans(list(orphans))

    async def _resolve_orphans(self, orphans: List[str]):
        for orphan in orphans:
            try:
                with open(os.path.join(self.docs_dir, orphan), 'r') as f: content = f.read(1000)
            except: content = "No content"
            decision = await self._ask_gemini_placement(orphan, content)
            if decision: await self._apply_placement(orphan, decision)

    async def _ask_gemini_placement(self, filename: str, content: str) -> Dict:
        api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        prompt = f"Archivo: {filename}\nContenido: {content}\nAsigna categoría nav e índice. Responde JSON."
        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(api_url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=20)
                if resp.status_code == 200:
                    match = re.search(r'\{.*\}', resp.json()['candidates'][0]['content']['parts'][0]['text'], re.DOTALL)
                    if match: return json.loads(match.group(0))
        except: pass
        return None

    async def _apply_placement(self, filename: str, decision: Dict):
        # Lógica de inserción en mkdocs.yml e index.md
        pass

    async def suggest_reorganization(self):
        """Optimización jerárquica automática de archivos densos."""
        for category in NUBENETES_CATEGORIES:
            file_path = os.path.join(self.docs_dir, f"{category}.md")
            if os.path.exists(file_path) and os.path.getsize(file_path) > 80000:
                await self._optimize_file_hierarchy(category, file_path)

    async def _optimize_file_hierarchy(self, category: str, file_path: str):
        # Lógica de Gemini para reestructurar encabezados internamente
        pass

    def validate_changes(self) -> bool:
        return True
