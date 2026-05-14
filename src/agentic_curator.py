import os
import re
import json
import asyncio
import httpx
import random
from datetime import datetime
from typing import List, Dict, Set, Optional
from src.config import GEMINI_API_KEYS, GH_TOKEN, TARGET_REPO, NUBENETES_CATEGORIES
from src.gitops_manager import RepositoryController
from src.gemini_utils import call_gemini_with_retry

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

from src.logger import log_event

async def evaluate_extracted_assets(raw_assets: List[Dict]) -> Dict[str, Dict]:
    evaluations = {}
    if not GEMINI_API_KEYS:
        log_event("[!] ERROR CRÍTICO: GEMINI_API_KEYS no encontrada en el entorno.")
        return {a["url"]: {"status": "FILTERED", "reason": "Configuración: API KEY faltante"} for a in raw_assets}

    memory_file = "src/memory/health_learning.json"
    domain_blacklist = set()
    if os.path.exists(memory_file):
        try:
            with open(memory_file, 'r') as f:
                memory_data = json.load(f)
                domain_blacklist = set(memory_data.get("blacklisted_domains", []))
        except: pass

    for i, asset in enumerate(raw_assets):
        post_date = asset.get('timestamp', 'Fecha desconocida')
        log_event(f"--- EVALUANDO {i+1}/{len(raw_assets)} ---")
        log_event(f"  - URL: {asset['url']}\n  - Post Date: {post_date}")

        domain = asset['url'].split("//")[-1].split("/")[0]
        if domain in domain_blacklist:
            eval_res = {"status": "FILTERED", "reason": "Dominio en lista negra de reputación"}
            evaluations[asset["url"]] = eval_res
            log_event(f"  [-] RECHAZADO: {eval_res['reason']}")
            continue

        web_content = await _deep_fetch_content(asset['url'])
        context = asset.get('context', asset.get('description', 'Sin contexto adicional'))
        
        prompt = (
            "Actúas como Ingeniero Curador Senior de 'nubenetes/awesome-kubernetes'.\n"
            "Tu misión es catalogar contenido TÉCNICO sobre Kubernetes y Cloud Native compartido por el usuario.\n"
            "REGLA DE ORO: Si el enlace está en el feed, es porque el usuario lo considera útil. NO lo descartes a menos que sea ruido total.\n\n"
            f"Categorías válidas: {', '.join(NUBENETES_CATEGORIES)}.\n\n"
            "INSTRUCCIONES:\n"
            "1. YOUTUBE: Acepta videos técnicos o tutoriales. Categorízalos.\n"
            "2. RESUMEN: Crea un resumen conciso (1 frase). Usa prioritariamente el 'Contexto' (que es el post de X).\n"
            "3. ASIGNACIÓN: Si es sobre Model Context Protocol (MCP), asígnalo a 'ai-agents-mcp'. Si es técnico pero no sabes dónde, usa 'kubernetes-tools'.\n\n"
            f"URL: {asset['url']}\nContexto de X: {context}\nContenido Web Extraído: {web_content[:1500]}\n\n"
            "Evalúa (1-100):\n"
            "- >80: Recurso excepcional (🌟).\n"
            "- >1: Aceptar (si es técnico o útil).\n\n"
            "Responde SOLAMENTE un JSON: {\"impact_score\": int, \"categories\": [\"cat1\"], \"title\": \"...\", \"desc\": \"...\", \"reasoning\": \"Breve explicación de por qué esta categoría y score\", \"rejection_reason\": \"... (si aplica)\"}"
        )

        try:
            data = await call_gemini_with_retry(prompt)
            score = data.get("impact_score", 50)
            valid_cats = [c for c in data.get("categories", []) if c in NUBENETES_CATEGORIES]
            
            if score < 1:
                reason = data.get("rejection_reason", "Bajo impacto técnico")
                evaluations[asset["url"]] = {"status": "FILTERED", "reason": reason}
                log_event(f"  [-] RECHAZADO: {reason} (Score: {score})\n      Motivo IA: {data.get('reasoning')}")
            elif not valid_cats:
                evaluations[asset["url"]] = {"status": "FILTERED", "reason": "No se encontró categoría técnica válida"}
                log_event(f"  [-] RECHAZADO: Sin categoría válida (Cats sugeridas: {data.get('categories')})\n      Motivo IA: {data.get('reasoning')}")
            else:
                evaluations[asset["url"]] = {
                    "status": "INCLUDED", "title": data["title"], "description": data["desc"],
                    "category": valid_cats[0], "impact_score": score, "is_exceptional": score > 80,
                    "reasoning": data.get("reasoning")
                }
                log_event(f"  [+] ACEPTADO: {data['title']} -> {valid_cats[0]} (Score: {score})\n      Desc: {data['desc']}\n      Motivo IA: {data.get('reasoning')}")

        except Exception as e:
            err_msg = str(e)
            if "Rate Limit" in err_msg or "429" in err_msg:
                log_event(f"  [!] RATE LIMIT DETECTADO. Entrando en modo COOL DOWN (2 min)...")
                await asyncio.sleep(120) 
            
            err_log = f"  [!] ERROR GEMINI: {err_msg[:200]}"
            evaluations[asset["url"]] = {"status": "FILTERED", "reason": err_log}
            log_event(err_log)
        
        await asyncio.sleep(5.0) 
            
    if domain_blacklist:
        try:
            os.makedirs(os.path.dirname(memory_file), exist_ok=True)
            with open(memory_file, 'w') as f:
                json.dump({"blacklisted_domains": list(domain_blacklist)}, f)
        except: pass
    return evaluations

class AgenticCurator:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.docs_dir = "docs"
        self.index_path = os.path.join(self.docs_dir, "index.md")
        self.mkdocs_path = "mkdocs.yml"
        self.stats = {"orphans_found": 0, "orphans_linked": 0, "structural_improvements": 0, "orphan_details": []}

    async def decide_smart_injection(self, markdown_content: str, asset: Dict) -> str:
        """Usa Gemini para decidir dónde y cómo inyectar el enlace dentro del markdown."""
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
            "Responde JSON: {\"header\": \"Nombre exacto del ## o ###\", \"formatted_line\": \"  - [==Título==](url) 🌟 - Descripción\", \"reasoning\": \"Breve por qué de esta ubicación/formato\"}"
        )

        try:
            data = await call_gemini_with_retry(prompt)
            header = data.get("header")
            new_line = data.get("formatted_line")
            reasoning = data.get("reasoning", "Sin motivo especificado")
            
            if header and new_line:
                log_event(f"  [>>>] UBICACIÓN: Header '{header}'\n      Formato: {new_line}\n      Motivo IA: {reasoning}")

                new_lines = []
                inserted = False
                for line in lines:
                    new_lines.append(line)
                    if not inserted and header.lower() in line.lower() and line.strip().startswith("#"):
                        new_lines.append(new_line)
                        inserted = True
                if inserted: return "\n".join(new_lines)
        except Exception as e:
            log_event(f"[!] Error en decide_smart_injection: {e}")
            pass
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
