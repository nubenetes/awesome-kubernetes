import httpx
import asyncio
import random
import json
import re
import os
from typing import Dict, Any, List, Optional
from src.config import GEMINI_API_KEYS, GEMINI_API_VERSION
from src.logger import log_event

# Global para mantener el índice de la API Key actual y los modelos descubiertos
CURRENT_KEY_INDEX = 0
DISCOVERED_MODELS = []

async def discover_optimal_models():
    """
    Queries the Google Model Service to find available models for the current keys.
    Ranks them by capability (Pro > Flash) and version (3.1 > 2.5 > 1.5).
    """
    global DISCOVERED_MODELS
    if DISCOVERED_MODELS: return DISCOVERED_MODELS
    
    log_event("[*] Starting AI Model Auto-Discovery...", section_break=True)
    all_supported = []
    
    # Try all keys to get a union of available models
    for key in GEMINI_API_KEYS:
        try:
            async with httpx.AsyncClient() as client:
                # Use v1beta for discovery as it lists more models
                url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
                resp = await client.get(url, timeout=10)
                if resp.status_code == 200:
                    models_data = resp.json().get("models", [])
                    for m in models_data:
                        name = m.get("name", "").replace("models/", "")
                        # Filter only models that support content generation
                        if "generateContent" in m.get("supportedGenerationMethods", []):
                            if name not in all_supported:
                                all_supported.append(name)
                elif resp.status_code == 429:
                    log_event(f"  [!] Discovery Key is rate-limited (429). Skipping this key for discovery.")
        except: pass

    if not all_supported:
        log_event("  [!] Discovery failed or keys limited. Falling back to safe defaults.")
        # Fallback to absolute stables
        DISCOVERED_MODELS = ["gemini-1.5-flash-latest", "gemini-1.5-flash", "gemini-1.5-pro"]
        return DISCOVERED_MODELS

    # SCORING ALGORITHM
    def score_model(name: str) -> float:
        score = 0.0
        # 1. Version Score (Prioritize 3.x series in 2026)
        if "3.1" in name: score += 100
        elif "3.0" in name: score += 80
        elif "2.5" in name: score += 60
        elif "2.0" in name: score += 40
        elif "1.5" in name: score += 20
        
        # 2. Tier Score
        if "-pro" in name: score += 50
        elif "-flash" in name: score += 25
        elif "-lite" in name: score += 10
        
        # 3. Latest/Stable Bonus
        if "-latest" in name: score += 5
        if "experimental" in name or "exp" in name: score -= 15
        
        return score

    # Sort by score descending
    DISCOVERED_MODELS = sorted(all_supported, key=score_model, reverse=True)
    log_event(f"  [+] Discovered {len(DISCOVERED_MODELS)} suitable models.")
    log_event(f"  [+] Top Tier AI: {', '.join(DISCOVERED_MODELS[:3])}")
    return DISCOVERED_MODELS

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
    """Sigue las redirecciones para obtener la URL larga final."""
    shorteners = ['t.co', 'bit.ly', 'buff.ly', 'goo.gl', 'tinyurl.com', 't.ly', 'rb.gy', 'is.gd', 'drp.li', 't.me', 'lnkd.in']
    try: domain = url.split("//")[-1].split("/")[0].lower()
    except: return url
    
    final_url, max_hops, current_hop = url, 5, 0
    async with httpx.AsyncClient(follow_redirects=True, timeout=8) as client:
        while current_hop < max_hops:
            try:
                current_domain = final_url.split("//")[-1].split("/")[0].lower()
                if current_hop > 0 and current_domain not in shorteners: break
                resp = await client.head(final_url, timeout=5)
                new_url = str(resp.url)
                if new_url == final_url: break
                final_url, current_hop = new_url, current_hop + 1
            except: break
    return final_url

def is_fuzzy_duplicate(url_a: str, url_b: str) -> bool:
    """Detecta si dos URLs son iguales ignorando parámetros de tracking comunes."""
    def clean(u):
        u = u.split('#')[0].rstrip('/').lower()
        u = re.sub(r'(\?|&)(utm_[^&]+|s=[^&]+|t=[^&]+|ref=[^&]+)', '', u)
        return u[:-1] if u.endswith('?') else u
    return clean(url_a) == clean(url_b)

async def call_gemini_with_retry(prompt: str, response_format: str = "json", max_retries: int = 3):
    """
    Calls Gemini API using dynamic discovery and intelligent rotation.
    Optimizes for cost (Pay-as-you-go) and quality (Pro vs Flash).
    """
    global CURRENT_KEY_INDEX
    if not GEMINI_API_KEYS:
        raise ValueError("No GEMINI_API_KEYS configured.")

    # Ensure models are discovered
    models = await discover_optimal_models()
    diagnostics = GeminiDiagnostics()
    
    # Try rotating through all available keys
    for key_attempt in range(len(GEMINI_API_KEYS)):
        api_key = GEMINI_API_KEYS[CURRENT_KEY_INDEX]
        
        async with httpx.AsyncClient() as client:
            for model in models:
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
                                    break # Try next model
                                return text_resp
                            diagnostics.add_attempt(model, 200, "No candidates")
                            break # Try next model
                        
                        elif response.status_code == 429:
                            log_event(f"  [!] API 429 (Rate Limit) on Key {CURRENT_KEY_INDEX+1}. Rotating Key...")
                            CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(GEMINI_API_KEYS)
                            # On 429, we recursive call to start over with next key and top model
                            return await call_gemini_with_retry(prompt, response_format, max_retries)
                        
                        elif response.status_code == 404:
                            # Model not found for this key or deprecated
                            diagnostics.add_attempt(model, 404, "Not Found/Unsupported")
                            break # Try next model (Pro -> Flash fallback)
                            
                        elif response.status_code in [500, 503, 504]:
                            await asyncio.sleep(2 * (attempt + 1))
                            continue
                        
                        else:
                            diagnostics.add_attempt(model, response.status_code, "API Error", response.text)
                            break
                            
                    except Exception as e:
                        diagnostics.add_attempt(model, 0, str(e))
                        break
            
            # If no model worked for this key, rotate for the next global call
            CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(GEMINI_API_KEYS)

    raise Exception(f"Critical Gemini failure after key and model rotation.\n{diagnostics.get_report()}")
