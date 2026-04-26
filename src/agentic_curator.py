import json
import re
import aiohttp
import httpx
from bs4 import BeautifulSoup
from pydantic import BaseModel
from typing import List, Optional
from src.config import GEMINI_API_KEY, NUBENETES_CATEGORIES

async def _deep_fetch_content(url: str) -> str:
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'}
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url, timeout=10, headers=headers) as resp:
                if resp.status == 200:
                    html = await resp.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    for s in soup(['script', 'style', 'nav', 'footer']):
                        s.decompose()
                    return soup.get_text(separator=' ', strip=True)[:3000]
    except: return ""
    return ""

async def evaluate_extracted_assets(raw_assets: list[dict]) -> list[dict]:
    curated_assets = []
    
    # URL de la API REST Directa (v1 estable)
    api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"

    for asset in raw_assets:
        web_content = await _deep_fetch_content(asset['url'])
        
        prompt = (
            "Actúas como Ingeniero Curador de 'nubenetes/awesome-kubernetes'. "
            f"Filtra este recurso para estas categorías: {', '.join(NUBENETES_CATEGORIES)}. "
            "Si es sobre Model Context Protocol (MCP), asígnalo a 'ai-agents-mcp'. "
            f"URL: {asset['url']}\nContexto: {asset['context']}\nWeb: {web_content}\n\n"
            "Responde SOLAMENTE un JSON: {\"is_exceptional\": bool, \"categories\": [\"cat1\"], \"title\": \"...\", \"desc\": \"...\"}"
        )

        payload = {"contents": [{"parts": [{"text": prompt}]}]}

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(api_url, json=payload, timeout=30)
                if response.status_code == 200:
                    res_data = response.json()
                    text_resp = res_data['candidates'][0]['content']['parts'][0]['text']
                    # Extraer JSON del texto
                    match = re.search(r'\{.*\}', text_resp, re.DOTALL)
                    if match:
                        data = json.loads(match.group(0))
                        if data.get("is_exceptional"):
                            for cat in data.get("categories", []):
                                if cat in NUBENETES_CATEGORIES:
                                    curated_assets.append({
                                        "url": asset["url"], "title": data["title"],
                                        "description": data["desc"], "category": cat
                                    })
        except Exception as e:
            print(f"[!] Error REST Gemini: {e}")
            
    return curated_assets
