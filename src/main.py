import asyncio
import sys
import os
import json
import re
from datetime import datetime, timedelta
from src.config import TARGET_REPO, MADRID_TZ, GH_TOKEN, NUBENETES_CATEGORIES
from src.ingestion_twikit import SocialDataExtractor
from src.markdown_ast import MarkdownSanitizer
from src.agentic_curator import evaluate_extracted_assets
from src.autonomous_discovery import discover_trending_assets
from src.gitops_manager import RepositoryController

async def master_orchestrator():
    git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
    markdown_sanitizer = MarkdownSanitizer()
    
    print("[*] INICIANDO CURADURÍA AGÉNTICA (ESTRATEGIA DE TRANSPARENCIA TOTAL)")
    
    # 1. Determinar Horizonte Temporal según el último MERGE
    time_horizon = datetime(2024, 10, 1, 0, 0, tzinfo=MADRID_TZ)
    try:
        # Buscamos PRs cerradas y merged del bot
        pulls = git_controller.repository.get_pulls(state='closed', sort='updated', direction='desc')
        for pr in pulls:
            if pr.merged and "💎 Knowledge Update" in pr.title:
                time_horizon = pr.merged_at.replace(tzinfo=MADRID_TZ) + timedelta(seconds=1)
                print(f"[+] Último PR mergeado encontrado ({pr.merged_at}). Retomando desde ahí.")
                break
    except Exception as e:
        print(f"[!] No se pudieron consultar PRs mergeadas: {e}. Usando fallback Oct 2024.")

    print(f"[*] Rango de búsqueda: {time_horizon} ➔ Ahora")

    # 2. Ingesta Multi-fuente
    twitter_client = SocialDataExtractor()
    raw_social = await twitter_client.fetch_links_since(time_horizon)
    x_audit_trail = twitter_client.audit_trail
    
    print("[*] Buscando novedades en GitHub Trending...")
    trending = await discover_trending_assets()
    for t in trending: t["source_type"] = "GitHub Trending"
    
    all_raw_assets = raw_social + trending
    
    # 3. Evaluación y Registro de Auditoría (Deduplicación Global Previa)
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
        
        # Mapear resultados para el reporte matricial
        curated_urls = {a["url"]: a for a in curated}
        for asset in all_raw_assets:
            url = asset["url"]
            clean_url = url.split('#')[0].rstrip('/')
            
            reason = "Aceptado"
            status = "INCLUDED"
            
            if clean_url in [u.split('#')[0].rstrip('/') for u in existing_urls]:
                status = "DUPLICATE"
                reason = "Ya existe en Nubenetes.com"
            elif url not in curated_urls:
                status = "FILTERED"
                reason = "Bajo impacto o no encaja en categorías"
            
            if status == "INCLUDED":
                unique_new_assets.append(curated_urls[url])
            
            full_extraction_report.append({
                "url": url,
                "status": status,
                "reason": reason,
                "category": curated_urls[url]["category"] if url in curated_urls else "N/A",
                "source": asset.get("source_type", "Unknown")
            })

    # 4. Inyección en Markdowns
    file_updates = {}
    stats = {"added_details": [], "categories_updated": set()}

    for asset in unique_new_assets:
        category = asset["category"]
        file_path = f"docs/{category}.md"
        try:
            # Leer contenido (usar caché local o git)
            content = file_updates.get(file_path)
            if not content:
                repo_file = git_controller.repository.get_contents(file_path)
                content = repo_file.decoded_content.decode("utf-8")
            
            final_content = markdown_sanitizer.inject_curated_link(
                content, category, asset["title"], asset["url"], asset["description"]
            )
            
            if len(final_content) > len(content):
                file_updates[file_path] = final_content
                stats["added_details"].append(asset)
                stats["categories_updated"].add(category)
        except: continue

    # 5. GitOps con Reporte Matricial
    metrics = {
        "social_injections": len(unique_new_assets),
        "total_extracted": len(raw_social),
        "full_report": full_extraction_report,
        "x_audit": x_audit_trail,
        "added_list": stats["added_details"],
        "categories": list(stats["categories_updated"]),
        "start_date": time_horizon.isoformat(),
        "end_date": datetime.now(MADRID_TZ).isoformat()
    }
    
    if file_updates or full_extraction_report:
        print(f"[+] Finalizado. Generando PR con auditoría completa.")
        git_controller.apply_multi_file_changes(file_updates, metrics)
    else:
        print("[~] Sin novedades ni reportes que generar.")

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
