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
        context = asset.get('context', asset.get('description', 'Sin contexto adicional'))
        
        log_event(f"--- EVALUANDO {i+1}/{len(raw_assets)} ---", section_break=False)
        log_event(f"  - URL: {asset['url']}")
        log_event(f"  - Post Date: {post_date}")
        log_event(f"  - Contexto del Post: \"{context[:300]}...\"")

        domain = asset['url'].split("//")[-1].split("/")[0]
        if domain in domain_blacklist:
            log_event(f"  [-] RECHAZADO: Dominio en lista negra ({domain})")
            evaluations[asset["url"]] = {"status": "FILTERED", "reason": "Dominio en lista negra"}
            continue

        web_content = await _deep_fetch_content(asset['url'])
        
        prompt = (
            "Actúas como Ingeniero Curador Senior de 'nubenetes/awesome-kubernetes'.\n"
            "Tu misión es catalogar contenido TÉCNICO sobre Kubernetes y Cloud Native compartido por el usuario.\n"
            "REGLA DE ORO: Si el enlace está en el feed, es porque el usuario lo considera útil. NO lo descartes a menos que sea ruido total (publicidad agresiva, error 404, o contenido no técnico).\n\n"
            f"Categorías válidas: {', '.join(NUBENETES_CATEGORIES)}.\n\n"
            "INSTRUCCIONES:\n"
            "1. YOUTUBE: Acepta videos técnicos o tutoriales. Categorízalos según su temática.\n"
            "2. RESUMEN: Crea un resumen conciso (1 frase). Usa prioritariamente el 'Contexto' (que es el post de X) ya que suele explicar por qué se compartió.\n"
            "3. ASIGNACIÓN: Si es sobre Model Context Protocol (MCP), asígnalo a 'ai-agents-mcp'.\n\n"
            f"URL: {asset['url']}\nContexto de X: {context}\nContenido Web Extraído: {web_content[:2000]}\n\n"
            "Evalúa el IMPACTO TÉCNICO (1-100):\n"
            "- >80: Recurso excepcional (🌟).\n"
            "- >5: Aceptar (si encaja en alguna categoría).\n"
            "- <5: Descartar (Ruido absoluto).\n\n"
            "Responde SOLAMENTE un JSON: {\"impact_score\": int, \"categories\": [\"cat1\"], \"title\": \"...\", \"desc\": \"...\", \"reasoning\": \"Breve explicación de por qué esta categoría y score\", \"rejection_reason\": \"... (si aplica)\"}"
        )

        try:
            data = await call_gemini_with_retry(prompt)
            score = data.get("impact_score", 50)
            valid_cats = [c for c in data.get("categories", []) if c in NUBENETES_CATEGORIES]
            reasoning = data.get("reasoning", "Sin motivo especificado")
            
            if score < 5:
                reason = data.get("rejection_reason", "Bajo impacto técnico")
                evaluations[asset["url"]] = {"status": "FILTERED", "reason": reason}
                log_event(f"  [-] RECHAZADO: {reason} (Score: {score})")
                log_event(f"      Motivo IA: {reasoning}")
                
                if score < 1 and domain not in domain_blacklist:
                    domain_blacklist.add(domain)
                    log_event(f"  [!] Dominio {domain} añadido a lista negra.")
            elif not valid_cats:
                evaluations[asset["url"]] = {"status": "FILTERED", "reason": "Sin categoría técnica válida"}
                log_event(f"  [-] RECHAZADO: No se encontró categoría válida (Sugeridas: {data.get('categories')})")
                log_event(f"      Motivo IA: {reasoning}")
            else:
                evaluations[asset["url"]] = {
                    "status": "INCLUDED", "title": data["title"], "description": data["desc"],
                    "category": valid_cats[0], "impact_score": score, "is_exceptional": score > 80,
                    "reasoning": reasoning
                }
                log_event(f"  [+] ACEPTADO: \"{data['title']}\" (Score: {score})")
                log_event(f"      Destino: docs/{valid_cats[0]}.md")
                log_event(f"      Descripción: {data['desc']}")
                log_event(f"      Motivo IA: {reasoning}")

        except Exception as e:
            log_event(f"  [!] ERROR CRÍTICO EVALUANDO {asset['url']}: {e}")
            evaluations[asset["url"]] = {"status": "FILTERED", "reason": f"Fallo Evaluación: {str(e)[:100]}"}
        
        await asyncio.sleep(2.0) # Ritmo estable
            
    # Guardar blacklist actualizada
    try:
        os.makedirs(os.path.dirname(memory_file), exist_ok=True)
        with open(memory_file, 'w') as f:
            json.dump({"blacklisted_domains": list(domain_blacklist)}, f, indent=2)
    except: pass
    return evaluations

class AgenticCurator:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.docs_dir = "docs"
        self.mkdocs_path = "mkdocs.yml"

    async def decide_smart_injection(self, markdown_content: str, asset: Dict) -> str:
        lines = markdown_content.splitlines()
        structure = "\n".join([l for l in lines if l.startswith("#")])
        
        prompt = (
            "Actúas como Arquitecto de Contenidos.\n"
            f"Enlace: [{asset['title']}]({asset['url']}) - {asset['description']}\n"
            f"Impacto: {asset['impact_score']}/100.\n\n"
            "Estructura:\n"
            f"{structure[:1500]}\n\n"
            "Responde JSON: {\"header\": \"## ...\", \"formatted_line\": \"  - [Título](url) - Desc\", \"reasoning\": \"...\"}"
        )

        try:
            data = await call_gemini_with_retry(prompt)
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

    async def suggest_reorganization(self):
        """Detecta categorías con >15 links y propone/realiza el split."""
        log_event("[*] Iniciando Auditoría de Reorganización Estructural...", section_break=True)
        
        bloated_files = []
        for file in os.listdir(self.docs_dir):
            if file.endswith(".md") and file != "index.md":
                path = os.path.join(self.docs_dir, file)
                with open(path, 'r') as f:
                    content = f.read()
                    links = re.findall(r'^\s*-\s*\[', content, re.MULTILINE)
                    if len(links) > 15:
                        bloated_files.append((file, len(links), content))

        for file, count, content in bloated_files:
            log_event(f"  [!] CATEGORÍA SATURADA: {file} tiene {count} enlaces. Proponiendo subdivisión...")
            
            prompt = (
                f"El archivo '{file}' tiene demasiados enlaces ({count}).\n"
                "Propón una subdivisión semántica en 2 o 3 subcategorías nuevas.\n"
                "Responde JSON: {\"subcategories\": [{\"name\": \"nombre-slug\", \"title\": \"Título Legible\", \"links_indices\": [int]}]}"
                "Nota: Para simplificar, solo propón los nombres de las subcategorías por ahora."
            )
            # Por ahora, solo logueamos la intención para no romper el flujo principal
            # En una fase futura, implementaremos el split físico de archivos.
            log_event(f"  [>>>] SUGERENCIA: Subdividir {file} para mejorar legibilidad.")

    def validate_changes(self) -> bool:
        return True
