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
    """Sigue las redirecciones para obtener la URL larga final, consolidando repositorios y evitando bucles."""
    shorteners = ['t.co', 'bit.ly', 'buff.ly', 'goo.gl', 'tinyurl.com', 't.ly', 'rb.gy', 'is.gd', 'drp.li', 't.me', 'lnkd.in']
    try:
        domain = url.split("//")[-1].split("/")[0].lower()
    except:
        return url
    
    # 1. Expansión Multi-salto (evita intermediarios de tracking)
    final_url = url
    max_hops = 5
    current_hop = 0
    
    async with httpx.AsyncClient(follow_redirects=True, timeout=8) as client:
        while current_hop < max_hops:
            try:
                # Si no es un acortador conocido y ya tenemos una URL larga, paramos
                current_domain = final_url.split("//")[-1].split("/")[0].lower()
                if current_hop > 0 and current_domain not in shorteners:
                    break
                    
                resp = await client.head(final_url, timeout=5)
                new_url = str(resp.url)
                if new_url == final_url: break
                
                final_url = new_url
                current_hop += 1
            except:
                break

    # 2. Consolidación de Repositorios (GitHub/GitLab) con chequeo de MVQ (vía REST si es necesario)
    repo_domains = ['github.com', 'gitlab.com']
    current_domain = final_url.split("//")[-1].split("/")[0].lower()
    
    if any(d in current_domain for d in repo_domains):
        try:
            async with httpx.AsyncClient(follow_redirects=True) as client:
                resp = await client.head(final_url, timeout=5)
                if resp.status_code != 200:
                    parts = final_url.split('/')
                    if len(parts) > 4: 
                        root_repo = "/".join(parts[:5])
                        resp_root = await client.head(root_repo, timeout=5)
                        if resp_root.status_code == 200:
                            log_event(f"  [📦] Consolidación: {final_url} -> {root_repo}")
                            final_url = root_repo
        except:
            pass
            
    return final_url

def is_fuzzy_duplicate(url_a: str, url_b: str) -> bool:
    """Detecta si dos URLs son iguales ignorando parámetros de tracking comunes."""
    def clean(u):
        u = u.split('#')[0].rstrip('/').lower()
        # Eliminar parámetros utm_* y otros comunes
        u = re.sub(r'(\?|&)(utm_[^&]+|s=[^&]+|t=[^&]+|ref=[^&]+)', '', u)
        if u.endswith('?'): u = u[:-1]
        return u
    return clean(url_a) == clean(url_b)

async def call_gemini_with_retry(prompt: str, response_format: str = "json", max_retries: int = 3):
    """
    Calls Gemini API optimizing for quota usage (pay-per-use).
    Rotates keys immediately on 429 and uses smart exponential backoff.
    """
    global CURRENT_KEY_INDEX
    if not GEMINI_API_KEYS:
        raise ValueError("No GEMINI_API_KEYS configured.")

    diagnostics = GeminiDiagnostics()
    
    # Try rotating through all available keys before failing
    for key_attempt in range(len(GEMINI_API_KEYS)):
        api_key = GEMINI_API_KEYS[CURRENT_KEY_INDEX]
        
        async with httpx.AsyncClient() as client:
            for model in GEMINI_MODELS:
                full_model_name = f"models/{model}"
                api_url = f"https://generativelanguage.googleapis.com/{GEMINI_API_VERSION}/{full_model_name}:generateContent?key={api_key}"
                
                for attempt in range(max_retries):
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
                                    diagnostics.add_attempt(model, 200, "JSON not found", text_resp)
                                    break 
                                return text_resp
                            diagnostics.add_attempt(model, 200, "No candidates")
                            break
                        
                        elif response.status_code == 429:
                            # 429: Rotate key immediately to save time
                            log_event(f"  [!] API 429 on key {CURRENT_KEY_INDEX+1}. Rotating...")
                            CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(GEMINI_API_KEYS)
                            # Break current model loop and move to next key
                            break 
                        
                        elif response.status_code in [500, 503, 504]:
                            await asyncio.sleep(2 * (attempt + 1))
                            continue
                        
                        else:
                            diagnostics.add_attempt(model, response.status_code, "API Error", response.text)
                            break
                            
                    except Exception as e:
                        diagnostics.add_attempt(model, 0, f"Exception: {str(e)}")
                        break
            
            # If we finished all models for a key with 429, skip to next key
            if response.status_code == 429:
                continue
            
            # If we are here and didn't succeed, try next key after a brief pause
            CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(GEMINI_API_KEYS)
            await asyncio.sleep(1)

    raise Exception(f"Critical Gemini failure after key rotation.\n{diagnostics.get_report()}")

