import os
import re
import json
import asyncio
import httpx
import random
from typing import List, Dict, Set, Optional
from src.config import GEMINI_API_KEY, GH_TOKEN, TARGET_REPO, NUBENETES_CATEGORIES
from src.gitops_manager import RepositoryController

# Silenciar advertencias de XML/HTML
import warnings
from bs4 import XMLParsedAsHTMLWarning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

async def _deep_fetch_content(url: str) -> str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(url, timeout=12, headers=headers, follow_redirects=True)
            if resp.status_code == 200:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(resp.text, 'html.parser')
                for s in soup(['script', 'style', 'nav', 'footer', 'aside']):
                    s.decompose()
                return soup.get_text(separator=' ', strip=True)[:4000]
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
            "- >80: Recurso excepcional, disruptivo.\n"
            "- <20: Contenido pobre o irrelevante.\n\n"
            "Responde SOLAMENTE un JSON: {\"is_exceptional\": bool, \"impact_score\": int, \"categories\": [\"cat1\"], \"title\": \"...\", \"desc\": \"...\"}"
        )

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(api_url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=35)
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
                            for cat in data.get("categories", []):
                                if cat in NUBENETES_CATEGORIES:
                                    curated_assets.append({
                                        "url": asset["url"], "title": data["title"],
                                        "description": data["desc"], "category": cat,
                                        "impact_score": score, "is_exceptional": data.get("is_exceptional", False)
                                    })
        except: pass
            
    if domain_blacklist:
        try:
            os.makedirs(os.path.dirname(memory_file), exist_ok=True)
            with open(memory_file, 'w') as f:
                json.dump({"blacklisted_domains": list(domain_blacklist)}, f)
        except: pass
    return curated_assets

class AgenticCurator:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.docs_dir = "docs"
        self.index_path = os.path.join(self.docs_dir, "index.md")
        self.mkdocs_path = "mkdocs.yml"
        self.stats = {"orphans_found": 0, "orphans_linked": 0, "structural_improvements": 0, "orphan_details": []}

    async def decide_smart_injection(self, markdown_content: str, asset: Dict) -> str:
        """Usa Gemini para decidir dónde y cómo inyectar el enlace dentro del markdown."""
        api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
        lines = markdown_content.splitlines()
        structure = "\n".join([l for l in lines if l.startswith("#")])
        
        prompt = (
            "Actúas como Arquitecto de Contenidos para Nubenetes.com.\n"
            f"Enlace: [{asset['title']}]({asset['url']}) - {asset['description']}\n"
            f"Impacto: {asset['impact_score']}/100.\n\n"
            "Estructura del archivo:\n"
            f"{structure[:2000]}\n\n"
            "1. Encuentra el ## o ### más semántico.\n"
            "2. Decide formato: si es excelente, añade estrellas (🌟, 🌟🌟 o 🌟🌟🌟).\n"
            "3. Decide si usar negritas (==enlace== o **texto**).\n"
            "Responde JSON: {\"header\": \"Nombre exacto del ## o ###\", \"formatted_line\": \"  - [==Título==](url) 🌟 - Descripción\"}"
        )

        try:
            async with httpx.AsyncClient() as client:
                resp = await client.post(api_url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=30)
                if resp.status_code == 200:
                    data = json.loads(re.search(r'\{.*\}', resp.json()['candidates'][0]['content']['parts'][0]['text'], re.DOTALL).group(0))
                    header = data.get("header")
                    new_line = data.get("formatted_line")
                    if header and new_line:
                        new_lines = []
                        inserted = False
                        for line in lines:
                            new_lines.append(line)
                            if not inserted and header.lower() in line.lower() and line.strip().startswith("#"):
                                new_lines.append(new_line)
                                inserted = True
                        if inserted: return "\n".join(new_lines)
        except: pass
        return self._manual_fallback_injection(markdown_content, asset)

    def _manual_fallback_injection(self, content: str, asset: Dict) -> str:
        stars = " 🌟" if asset['impact_score'] > 80 else ""
        line = f"  - [{asset['title']}]({asset['url']}){stars} - {asset['description']}"
        return content + f"\n{line}"

    async def audit_navigation(self):
        pass

    async def suggest_reorganization(self):
        pass

    def validate_changes(self) -> bool:
        return True
