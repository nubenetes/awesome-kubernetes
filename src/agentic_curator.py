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
        """
        Inyecta un enlace de forma inteligente buscando o creando la subsección (##) más adecuada.
        Sigue el mandato: "Priorizar secciones internas (## Headers) sobre nuevos archivos".
        """
        lines = markdown_content.splitlines()
        # Extraer solo los headers para dar contexto a la IA sin saturar
        structure = "\n".join([l for l in lines if l.startswith("#")])
        
        stars = " 🌟" if asset['impact_score'] > 80 else ""
        formatted_line = f"  - [{asset['title']}]({asset['url']}){stars} - {asset['description']}"

        prompt = (
            "Actúas como Arquitecto de Contenidos de Nubenetes.com.\n"
            f"Tu misión es inyectar este nuevo recurso en el archivo markdown de forma lógica:\n"
            f"RECURSO: {formatted_line}\n"
            f"RAZONAMIENTO IA: {asset.get('reasoning', 'N/A')}\n\n"
            "ESTRUCTURA ACTUAL DEL ARCHIVO:\n"
            f"{structure[:1500]}\n\n"
            "INSTRUCCIONES:\n"
            "1. Identifica el header (##) más adecuado para este recurso.\n"
            "2. Si no existe un header adecuado, PROPÓN UNO NUEVO que sea semánticamente correcto.\n"
            "3. Si el archivo está vacío o solo tiene un # Título, propón un ## Header inicial.\n\n"
            "Responde SOLAMENTE un JSON con este formato:\n"
            "{\n"
            "  \"target_header\": \"## Nombre del Header (existente o nuevo)\",\n"
            "  \"is_new_header\": true/false,\n"
            "  \"insert_after_header\": \"## Header de referencia (si es nuevo, ¿después de cuál lo pongo?)\",\n"
            "  \"reasoning\": \"Breve explicación\"\n"
            "}"
        )

        try:
            data = await call_gemini_with_retry(prompt)
            target_header = data.get("target_header")
            is_new = data.get("is_new_header", False)
            ref_header = data.get("insert_after_header")
            
            if not target_header:
                return self._manual_fallback_injection(markdown_content, asset)

            new_lines = []
            inserted = False
            
            if is_new:
                # Caso: Insertar un NUEVO header
                if not ref_header: # Si no hay referencia, al final
                    new_lines = lines + ["", target_header, formatted_line]
                    inserted = True
                else:
                    for line in lines:
                        new_lines.append(line)
                        if not inserted and ref_header.lower() in line.lower() and line.strip().startswith("#"):
                            # Buscar el final de la sección actual para insertar el nuevo header
                            new_lines.append("")
                            new_lines.append(target_header)
                            new_lines.append(formatted_line)
                            inserted = True
            else:
                # Caso: Insertar en un header EXISTENTE
                for line in lines:
                    new_lines.append(line)
                    if not inserted and target_header.lower() in line.lower() and line.strip().startswith("#"):
                        new_lines.append(formatted_line)
                        inserted = True
            
            if inserted:
                log_event(f"  [🏠] IA decidió: Secc '{target_header}' ({'NUEVA' if is_new else 'EXISTENTE'})")
                return "\n".join(new_lines)
                
        except Exception as e:
            log_event(f"  [!] Fallo en inyección inteligente: {e}")
            
        return self._manual_fallback_injection(markdown_content, asset)

    def _manual_fallback_injection(self, content: str, asset: Dict) -> str:
        stars = " 🌟" if asset['impact_score'] > 80 else ""
        line = f"  - [{asset['title']}]({asset['url']}){stars} - {asset['description']}"
        # Si no hay secciones, añadir un header genérico
        if "##" not in content:
            return content + f"\n\n## Herramientas y Recursos\n{line}"
        return content + f"\n{line}"

    async def suggest_reorganization(self):
        """
        Audita archivos con exceso de enlaces y los reorganiza INTERNAMENTE.
        Sigue el mandato: "No dividir en archivos, sino en secciones internas".
        """
        log_event("[*] Iniciando Auditoría de Reorganización Interna...", section_break=True)
        
        for file in os.listdir(self.docs_dir):
            if not file.endswith(".md") or file == "index.md": continue
            
            path = os.path.join(self.docs_dir, file)
            with open(path, 'r') as f: content = f.read()
            
            links = re.findall(r'^\s*-\s*\[', content, re.MULTILINE)
            headers = re.findall(r'^##\s+', content, re.MULTILINE)
            
            # Si tiene muchos links y pocos headers, reorganizar
            if len(links) > 25 and len(headers) < 3:
                log_event(f"  [!] REORGANIZANDO: {file} ({len(links)} links, {len(headers)} headers)")
                
                prompt = (
                    f"El archivo '{file}' tiene {len(links)} enlaces pero solo {len(headers)} secciones.\n"
                    "Está demasiado plano. Reorganiza el contenido en secciones (##) lógicas.\n"
                    "Devuelve el contenido COMPLETO del archivo markdown reorganizado.\n"
                    "MANTÉN TODOS LOS ENLACES. SOLO AGRÚPALOS BAJO HEADERS SEMÁNTICOS.\n\n"
                    "CONTENIDO ACTUAL:\n"
                    f"{content[:5000]}" # Limitar para no saturar context window
                )
                
                try:
                    new_content = await call_gemini_with_retry(prompt, response_format="text")
                    if len(new_content) > len(content) * 0.8: # Validación básica de que no borró todo
                        with open(path, 'w') as f: f.write(new_content)
                        log_event(f"  [OK] Reorganización aplicada a {file}")
                except Exception as e:
                    log_event(f"  [!] Error reorganizando {file}: {e}")

    def validate_changes(self) -> bool:
        return True
