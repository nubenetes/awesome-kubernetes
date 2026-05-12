import httpx
import asyncio
import random
import json
import re
from typing import Dict, Any, List, Optional
from src.config import GEMINI_API_KEY, GEMINI_API_VERSION, GEMINI_MODELS

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

async def call_gemini_with_retry(prompt: str, response_format: str = "json", max_retries: int = 3):
    """
    Llama a la API de Gemini con rotación de modelos y diagnóstico detallado.
    """
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY no configurada.")

    diagnostics = GeminiDiagnostics()
    
    async with httpx.AsyncClient() as client:
        for model in GEMINI_MODELS:
            api_url = f"https://generativelanguage.googleapis.com/{GEMINI_API_VERSION}/models/{model}:generateContent?key={GEMINI_API_KEY}"
            
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
                                    return json.loads(match.group(0))
                                diagnostics.add_attempt(model, 200, "JSON no encontrado en texto", text_resp)
                                break 
                            return text_resp
                        except Exception as e:
                            diagnostics.add_attempt(model, 200, f"Error parseo: {str(e)}", response.text)
                            break
                    
                    elif response.status_code == 404:
                        diagnostics.add_attempt(model, 404, "Modelo no encontrado")
                        break # Probar siguiente modelo
                    
                    elif response.status_code == 429:
                        diagnostics.add_attempt(model, 429, "Rate Limit")
                        wait = (2 ** attempt) + random.random()
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
        
    raise Exception(f"Fallo crítico Gemini.\n{diagnostics.get_report()}")
