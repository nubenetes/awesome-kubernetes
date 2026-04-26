import aiohttp
import json
import httpx
import re
from src.config import GEMINI_API_KEY, NUBENETES_CATEGORIES

async def fetch_github_trending_cloud_native() -> list[dict]:
    queries = [
        "topic:kubernetes+stars:>1000", 
        "topic:mcp-server+stars:>0", 
        "topic:model-context-protocol+stars:>0",
        "topic:ai-agents+stars:>50"
    ]
    all_repos = []
    headers = {'Accept': 'application/vnd.github.v3+json'}
    async with aiohttp.ClientSession(headers=headers) as session:
        for q in queries:
            url = f"https://api.github.com/search/repositories?q={q}&sort=updated&order=desc"
            try:
                async with session.get(url, timeout=10) as resp:
                    if resp.status == 200:
                        data = await resp.json()
                        for repo in data.get('items', [])[:10]:
                            all_repos.append({
                                "name": repo['name'],
                                "url": repo['html_url'],
                                "desc": repo['description'] or "No description provided."
                            })
            except: continue
    return all_repos

async def discover_trending_assets() -> list[dict]:
    repos = await fetch_github_trending_cloud_native()
    if not repos:
        return []

    # Intentar clasificar con Gemini vía REST
    api_url = f"https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent?key={GEMINI_API_KEY}"
    prompt = (
        "Analiza estos repositorios y selecciona los 4 mejores.\n"
        f"Categorías: {', '.join(NUBENETES_CATEGORIES)}\n"
        f"Repos: {json.dumps(repos)}\n\n"
        "Responde SOLAMENTE una lista JSON: [{\"title\": \"...\", \"url\": \"...\", \"description\": \"...\", \"category\": \"...\"}]"
    )
    
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(api_url, json={"contents": [{"parts": [{"text": prompt}]}]}, timeout=30)
            if response.status_code == 200:
                text_resp = response.json()['candidates'][0]['content']['parts'][0]['text']
                match = re.search(r'\[.*\]', text_resp, re.DOTALL)
                if match:
                    results = json.loads(match.group(0))
                    return [res for res in results if res.get("category") in NUBENETES_CATEGORIES]
    except Exception as e:
        print(f"[~] Gemini REST falló, usando clasificación heurística: {e}")

    # --- FALLBACK HEURÍSTICO (Si Gemini falla) ---
    fallback_results = []
    for r in repos[:5]:
        category = "kubernetes-tools" # Default
        desc_lower = r['desc'].lower()
        name_lower = r['name'].lower()
        
        if "mcp" in desc_lower or "context-protocol" in desc_lower or "mcp" in name_lower:
            category = "ai-agents-mcp"
        elif "ai" in desc_lower or "agent" in desc_lower:
            category = "ai"
        elif "security" in desc_lower:
            category = "kubernetes-security"
        
        fallback_results.append({
            "title": r['name'],
            "url": r['url'],
            "description": r['desc'],
            "category": category
        })
    return fallback_results
