import httpx
import asyncio
import random
import json
import re
from src.config import GEMINI_API_KEY, GEMINI_API_VERSION, GEMINI_MODELS

async def call_gemini_with_retry(prompt: str, response_format: str = "json", max_retries: int = 3):
    """
    Llama a la API de Gemini con rotación de modelos y reintentos ante 404 o 429.
    """
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY no configurada.")

    async with httpx.AsyncClient() as client:
        for model in GEMINI_MODELS:
            api_url = f"https://generativelanguage.googleapis.com/{GEMINI_API_VERSION}/models/{model}:generateContent?key={GEMINI_API_KEY}"
            
            for attempt in range(max_retries):
                try:
                    payload = {"contents": [{"parts": [{"text": prompt}]}]}
                    response = await client.post(api_url, json=payload, timeout=35)
                    
                    if response.status_code == 200:
                        try:
                            text_resp = response.json()['candidates'][0]['content']['parts'][0]['text']
                            if response_format == "json":
                                match = re.search(r'\{.*\}|\[.*\]', text_resp, re.DOTALL)
                                if match:
                                    return json.loads(match.group(0))
                                raise ValueError("No se encontró JSON en la respuesta")
                            return text_resp
                        except (KeyError, IndexError, json.JSONDecodeError) as e:
                            print(f"[!] Error parseando respuesta de {model}: {e}")
                            break # Probar siguiente modelo si el formato es basura
                    
                    elif response.status_code == 404:
                        print(f"[!] Modelo {model} no encontrado (404) en {api_url}. Probando siguiente...")
                        break # Ir al siguiente modelo en GEMINI_MODELS
                    
                    elif response.status_code == 429:
                        wait = (2 ** attempt) + random.random()
                        print(f"[*] Rate limit (429) para {model}. Reintentando en {wait:.2f}s...")
                        await asyncio.sleep(wait)
                        continue
                    
                    else:
                        print(f"[!] Error {response.status_code} de Gemini ({model}): {response.text[:200]}")
                        break # Probar siguiente modelo
                        
                except Exception as e:
                    print(f"[!] Excepción llamando a {model}: {e}")
                    if attempt == max_retries - 1:
                        break
                    await asyncio.sleep(1)
        
    raise Exception("Todos los modelos de Gemini fallaron o no están disponibles.")
