import asyncio
import sys
import os
import json
import re
from datetime import datetime, timedelta
from src.config import TARGET_REPO, MADRID_TZ, GH_TOKEN, NUBENETES_CATEGORIES
from src.ingestion_twikit import SocialDataExtractor
from src.markdown_ast import MarkdownSanitizer
from src.agentic_curator import evaluate_extracted_assets, AgenticCurator
from src.autonomous_discovery import discover_trending_assets
from src.gitops_manager import RepositoryController

async def master_orchestrator():
    git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
    
    print("[*] INICIANDO CURADURÍA AGÉNTICA (CRONOLOGÍA Y TRANSPARENCIA)")
    
    # 1. Horizonte Temporal Fijo (Octubre 2024) - Requisito de Curaduría Histórica
    time_horizon = datetime(2024, 10, 1, 0, 0, tzinfo=MADRID_TZ)
    print(f"[*] FORZANDO CURADURÍA HISTÓRICA desde: {time_horizon.date()}")

    # 2. Ingesta Multi-fuente
    twitter_client = SocialDataExtractor()
    raw_social = await twitter_client.fetch_links_since(time_horizon)
    x_audit_trail = twitter_client.audit_trail
    
    print("[*] Buscando novedades en GitHub Trending...")
    trending = await discover_trending_assets()
    for t in trending: 
        t["source_type"] = "GitHub Trending"
        t["timestamp"] = datetime.now(MADRID_TZ).isoformat()
    
    all_raw_assets = raw_social + trending
    
    # 3. Evaluación y Registro de Auditoría (Uso de archivos locales)
    existing_urls = set()
    for doc in os.listdir("docs"):
        if doc.endswith(".md"):
            try:
                with open(os.path.join("docs", doc), 'r') as f:
                    existing_urls.update(re.findall(r'\]\((https?://[^\)]+)\)', f.read()))
            except: pass

    full_extraction_report = []
    unique_new_assets = []
    
    if all_raw_assets:
        print(f"[*] Evaluando {len(all_raw_assets)} candidatos con Gemini...")
        curated = await evaluate_extracted_assets(all_raw_assets)
        
        curated_urls = {a["url"]: a for a in curated}
        for asset in all_raw_assets:
            url = asset["url"]
            clean_url = url.split('#')[0].rstrip('/')
            
            status = "INCLUDED"
            reason = "Aceptado"
            
            if clean_url in [u.split('#')[0].rstrip('/') for u in existing_urls]:
                status = "DUPLICATE"
                reason = "Ya existe en Nubenetes.com"
            elif url not in curated_urls:
                status = "FILTERED"
                reason = "Bajo impacto o contenido no bookmark"
            
            if status == "INCLUDED":
                unique_new_assets.append(curated_urls[url])
            
            full_extraction_report.append({
                "url": url,
                "status": status,
                "reason": reason,
                "category": curated_urls[url]["category"] if url in curated_urls else "N/A",
                "source": asset.get("source_type", "Unknown"),
                "post_date": asset.get("timestamp")
            })

    # 4. Inyección en Markdowns (Uso de archivos locales)
    file_updates = {}
    stats = {"added_details": [], "categories_updated": set()}
    curator_agent = AgenticCurator()

    for asset in unique_new_assets:
        category = asset["category"]
        file_path = f"docs/{category}.md"
        try:
            # Leer localmente si no está en file_updates
            content = file_updates.get(file_path)
            if not content:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f:
                        content = f.read()
                else:
                    print(f"[!] Archivo no encontrado localmente: {file_path}")
                    continue
            
            new_content = await curator_agent.decide_smart_injection(content, asset)
            if len(new_content) > len(content):
                file_updates[file_path] = new_content
                stats["added_details"].append(asset)
                stats["categories_updated"].add(category)
        except Exception as e:
            print(f"[!] Error inyectando en {file_path}: {e}")
            continue

    # 5. GitOps con Reporte Matricial
    metrics = {
        "social_injections": len([a for a in unique_new_assets if "X.com" in a.get("source_type", "")]),
        "total_extracted": len(all_raw_assets),
        "full_report": full_extraction_report,
        "x_audit": x_audit_trail,
        "added_list": stats["added_details"],
        "categories": list(stats["categories_updated"]),
        "start_date": time_horizon.isoformat(),
        "end_date": datetime.now(MADRID_TZ).isoformat()
    }
    
    if file_updates or full_extraction_report:
        print(f"[+] Generando PR con auditoría completa.")
        git_controller.apply_multi_file_changes(file_updates, metrics)

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
