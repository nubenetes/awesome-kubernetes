import httpx
import asyncio
import random
import json
import re
from typing import Dict, Any, List, Optional
from src.config import GEMINI_API_KEYS, GEMINI_API_VERSION, GEMINI_MODELS
from src.logger import log_event

# Global para mantener el índice de la API Key actual
CURRENT_KEY_INDEX = 0

class GeminiDiagnostics:
    def __init__(self):
        self.attempts = []

    def add_attempt(self, model: str, status: int, error: str = None, response_text: str = None):
        self.attempts.append({
            "model": model,
            "status": status,
            "error": error,
            "response_preview": response_text[:200] if response_text else None
        })

    def get_report(self) -> str:
        report = "DIAGNÓSTICO GEMINI:\n"
        for i, a in enumerate(self.attempts):
            report += f"  {i+1}. [{a['model']}] Status: {a['status']}"
            if a['error']: report += f" | Error: {a['error']}"
            if a['response_preview']: report += f" | Resp: {a['response_preview']}"
            report += "\n"
        return report

async def resolve_url(url: str) -> str:
    """Sigue las redirecciones para obtener la URL larga final y consolida repositorios si fallan."""
    shorteners = ['t.co', 'bit.ly', 'buff.ly', 'goo.gl', 'tinyurl.com', 't.ly', 'rb.gy', 'is.gd', 'drp.li', 't.me']
    try:
        domain = url.split("//")[-1].split("/")[0].lower()
    except:
        return url
    
    # 1. Expansión inicial
    final_url = url
    if domain in shorteners or url.endswith('…'):
        try:
            async with httpx.AsyncClient(follow_redirects=True) as client:
                resp = await client.head(url, timeout=5)
                final_url = str(resp.url)
                if final_url != url:
                    log_event(f"  [🔗] URL Expandida: {url} -> {final_url}")
        except:
            pass

    # 2. Consolidación de Repositorios (GitHub/GitLab)
    repo_domains = ['github.com', 'gitlab.com']
    current_domain = final_url.split("//")[-1].split("/")[0].lower()
    
    if any(d in current_domain for d in repo_domains):
        # Intentar validar si el enlace profundo funciona
        try:
            async with httpx.AsyncClient(follow_redirects=True) as client:
                resp = await client.head(final_url, timeout=5)
                if resp.status_code == 200:
                    return final_url
                
                # Si falla, intentar consolidar a la raíz del repo
                # Formato esperado: https://github.com/user/repo/...
                parts = final_url.split('/')
                if len(parts) > 4: # https: , , domain, user, repo
                    root_repo = "/".join(parts[:5])
                    resp_root = await client.head(root_repo, timeout=5)
                    if resp_root.status_code == 200:
                        log_event(f"  [📦] Consolidación: {final_url} -> {root_repo} (Raíz validada)")
                        return root_repo
        except:
            pass
            
    return final_url

async def call_gemini_with_retry(prompt: str, response_format: str = "json", max_retries: int = 3):
    """
    Llama a la API de Gemini con rotación exhaustiva y REINTENTO REAL en 429.
    """
    global CURRENT_KEY_INDEX
    if not GEMINI_API_KEYS:
        raise ValueError("No hay GEMINI_API_KEYS configuradas.")

    diagnostics = GeminiDiagnostics()
    
    async with httpx.AsyncClient() as client:
        for key_attempt in range(len(GEMINI_API_KEYS)):
            api_key = GEMINI_API_KEYS[CURRENT_KEY_INDEX]
            
            for model in GEMINI_MODELS:
                full_model_name = f"models/{model}"
                api_url = f"https://generativelanguage.googleapis.com/{GEMINI_API_VERSION}/{full_model_name}:generateContent?key={api_key}"
                
                # Reintentos por modelo (incluyendo 429)
                for attempt in range(max_retries + 2):
                    try:
                        payload = {"contents": [{"parts": [{"text": prompt}]}]}
                        response = await client.post(api_url, json=payload, timeout=45)
                        
                        if response.status_code == 200:
                            resp_json = response.json()
                            if 'candidates' in resp_json and resp_json['candidates']:
                                text_resp = resp_json['candidates'][0]['content']['parts'][0]['text']
                                if response_format == "json":
                                    match = re.search(r'\{.*\}|\[.*\]', text_resp, re.DOTALL)
                                    if match:
                                        data = json.loads(match.group(0))
                                        return data[0] if isinstance(data, list) and len(data) > 0 else data
                                    diagnostics.add_attempt(model, 200, "JSON no encontrado", text_resp)
                                    break 
                                return text_resp
                            diagnostics.add_attempt(model, 200, "Sin candidates")
                            break
                        
                        elif response.status_code == 429:
                            wait_time = (10 * (attempt + 1)) + random.random() * 5
                            log_event(f"  [!] API 429 (Límite): Reintentando {model} en {wait_time:.1f}s... (Intento {attempt+1})")
                            await asyncio.sleep(wait_time)
                            continue # Reintentar el MISMO modelo
                        
                        elif response.status_code in [500, 503, 504]:
                            diagnostics.add_attempt(model, response.status_code, "Server Error")
                            await asyncio.sleep(5)
                            continue
                        
                        else:
                            diagnostics.add_attempt(model, response.status_code, "API Error", response.text)
                            break
                            
                    except Exception as e:
                        diagnostics.add_attempt(model, 0, f"Excepción: {str(e)}")
                        break
            
            CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(GEMINI_API_KEYS)
            await asyncio.sleep(2)

    raise Exception(f"Fallo crítico Gemini tras rotación exhaustiva.\n{diagnostics.get_report()}")
