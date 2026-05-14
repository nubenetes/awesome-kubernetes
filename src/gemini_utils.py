import httpx
import asyncio
import random
import json
import re
from typing import Dict, Any, List, Optional
from src.config import GEMINI_API_KEYS, GEMINI_API_VERSION, GEMINI_MODELS

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

async def call_gemini_with_retry(prompt: str, response_format: str = "json", max_retries: int = 5):
    """
    Llama a la API de Gemini con rotación de modelos Y rotación de API Keys.
    """
    global CURRENT_KEY_INDEX
    if not GEMINI_API_KEYS:
        raise ValueError("No hay GEMINI_API_KEYS configuradas.")

    diagnostics = GeminiDiagnostics()
    
    async with httpx.AsyncClient() as client:
        # Intentamos con las llaves disponibles si una falla por cuota
        for _ in range(len(GEMINI_API_KEYS)):
            api_key = GEMINI_API_KEYS[CURRENT_KEY_INDEX]
            
            for model in GEMINI_MODELS:
                # Usamos el nombre completo del modelo como requiere la v1beta
                full_model_name = f"models/{model}"
                api_url = f"https://generativelanguage.googleapis.com/{GEMINI_API_VERSION}/{full_model_name}:generateContent?key={api_key}"
                
                for attempt in range(max_retries):
                    try:
                        payload = {"contents": [{"parts": [{"text": prompt}]}]}
                        response = await client.post(api_url, json=payload, timeout=35)
                        
                        if response.status_code == 200:
                            try:
                                resp_json = response.json()
                                if 'candidates' not in resp_json or not resp_json['candidates']:
                                    diagnostics.add_attempt(model, 200, "Respuesta vacía (no candidates)", response.text)
                                    break

                                text_resp = resp_json['candidates'][0]['content']['parts'][0]['text']
                                if response_format == "json":
                                    match = re.search(r'\{.*\}|\[.*\]', text_resp, re.DOTALL)
                                    if match:
                                        data = json.loads(match.group(0))
                                        if isinstance(data, list):
                                            return data[0] if len(data) > 0 else {}
                                        return data
                                    diagnostics.add_attempt(model, 200, "JSON no encontrado en texto", text_resp)
                                    break 
                                return text_resp
                            except Exception as e:
                                diagnostics.add_attempt(model, 200, f"Error parseo: {str(e)}", response.text)
                                break
                        
                        elif response.status_code == 404:
                            diagnostics.add_attempt(model, 404, f"Modelo {full_model_name} no encontrado")
                            break # Probar siguiente modelo
                        
                        elif response.status_code in [429, 503]:
                            # Si es un error de cuota (429), probamos a rotar la API Key inmediatamente
                            if response.status_code == 429:
                                reason = "Rate Limit / Quota Exceeded"
                                diagnostics.add_attempt(model, 429, reason)
                                # Loguear rotación en el log central
                                with open("/home/inafev/.gemini/tmp/awesome-kubernetes/curation_progress.log", "a") as log_f:
                                    log_f.write(f"  [!] Llave {CURRENT_KEY_INDEX + 1} agotada. Probando rotación...\n")
                                break # Rompe el bucle de reintentos para cambiar de llave o modelo
                            
                            reason = "Service Unavailable"
                            diagnostics.add_attempt(model, response.status_code, reason)
                            wait = (5 * (2 ** attempt)) + random.random() * 5
                            await asyncio.sleep(wait)
                            continue
                        
                        else:
                            diagnostics.add_attempt(model, response.status_code, "Error API", response.text)
                            break
                            
                    except Exception as e:
                        diagnostics.add_attempt(model, 0, f"Excepción: {str(e)}")
                        if attempt == max_retries - 1:
                            break
                        await asyncio.sleep(1)
                
                # Si llegamos aquí por un 429, el bucle 'attempt' se rompió. 
                # Salimos también del bucle 'model' para rotar la llave.
                if diagnostics.attempts and diagnostics.attempts[-1]['status'] == 429:
                    break

            # Si la última falla fue un 429, rotamos la llave y probamos el siguiente ciclo
            if diagnostics.attempts and diagnostics.attempts[-1]['status'] == 429:
                CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(GEMINI_API_KEYS)
                # Opcional: una pequeña espera antes de usar la nueva llave
                await asyncio.sleep(2)
                continue
            else:
                # Si no fue un 429 o éxito, salimos del bucle de llaves
                if diagnostics.attempts and diagnostics.attempts[-1]['status'] == 200:
                    # En caso de éxito (que devuelve directamente arriba), no llegamos aquí.
                    # Este break es para otros errores terminales.
                    pass
                break
        
    # Si logramos el éxito, la función ya habría retornado dentro del bucle de éxito (200)
    # Si llegamos aquí, es porque todas las llaves y modelos fallaron.
    raise Exception(f"Fallo crítico Gemini tras rotación.\n{diagnostics.get_report()}")
