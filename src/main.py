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
    
    # 1. Horizonte Temporal Dinámico / Histórico
    is_historical = os.getenv("HISTORICAL_MODE", "false").lower() == "true"
    
    if is_historical:
        # Modo Histórico por Tramos (Ej: tramos de 180 días)
        final_stop_date = datetime(2024, 10, 1, 0, 0, tzinfo=MADRID_TZ)
        chunk_days = int(os.getenv("HISTORICAL_CHUNK_DAYS", "180"))
        
        # El tramo actual termina donde el anterior empezó (o en 'ahora' si es el primero)
        until_str = os.getenv("HISTORICAL_UNTIL_DATE")
        if until_str:
            until_date = datetime.fromisoformat(until_str).replace(tzinfo=MADRID_TZ)
        else:
            until_date = datetime.now(MADRID_TZ)
            
        since_date = until_date - timedelta(days=chunk_days)
        if since_date < final_stop_date:
            since_date = final_stop_date
            
        print(f"[*] MODO HISTÓRICO: Tramo {since_date.date()} -> {until_date.date()}")
    else:
        # Modo Normal (30 días)
        days_back = int(os.getenv("CURATION_DAYS_BACK", "30"))
        since_date = datetime.now(MADRID_TZ) - timedelta(days=days_back)
        until_date = None
        print(f"[*] Modo Normal: Desde {since_date.date()}")

    # 2. Ingesta Multi-fuente
    strategy = os.getenv("EXTRACTION_STRATEGY", "search")
    twitter_client = SocialDataExtractor()
    raw_social = await twitter_client.fetch_links_since(since_date, until_date=until_date, strategy=strategy)
    x_audit_trail = twitter_client.audit_trail
    
    # GitHub Trending solo en modo normal (para no repetir)
    trending = []
    if not is_historical:
        print("[*] Buscando novedades en GitHub Trending...")
        trending = await discover_trending_assets()
        for t in trending: 
            t["source_type"] = "GitHub Trending"
            t["timestamp"] = datetime.now(MADRID_TZ).isoformat()
    
    all_raw_assets = raw_social + trending
    
    # 3. Evaluación y Registro (Ignorar duplicados locales)
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
        evaluations = await evaluate_extracted_assets(all_raw_assets)
        
        for asset in all_raw_assets:
            url = asset["url"]
            clean_url = url.split('#')[0].rstrip('/')
            
            evaluation = evaluations.get(url, {"status": "FILTERED", "reason": "No evaluado por IA"})
            status = evaluation["status"]
            reason = evaluation.get("reason", "Aceptado")
            category = evaluation.get("category", "N/A")
            
            if clean_url in [u.split('#')[0].rstrip('/') for u in existing_urls]:
                status = "DUPLICATE"
                reason = "Ya existe en Nubenetes.com"
            
            if status == "INCLUDED":
                unique_new_assets.append({
                    "url": url, "title": evaluation["title"],
                    "description": evaluation["description"], "category": category,
                    "impact_score": evaluation["impact_score"]
                })
            
            full_extraction_report.append({
                "url": url,
                "status": status,
                "reason": reason,
                "category": category,
                "source": asset.get("source_type", "Unknown"),
                "post_date": asset.get("timestamp")
            })

    # 4. Inyección en Markdowns (Local)
    file_updates = {}
    stats = {"added_details": [], "categories_updated": set()}
    curator_agent = AgenticCurator()

    for asset in unique_new_assets:
        category = asset["category"]
        file_path = f"docs/{category}.md"
        try:
            content = file_updates.get(file_path)
            if not content:
                if os.path.exists(file_path):
                    with open(file_path, 'r') as f: content = f.read()
                else: continue
            
            new_content = await curator_agent.decide_smart_injection(content, asset)
            if len(new_content) > len(content):
                file_updates[file_path] = new_content
                stats["added_details"].append(asset)
                stats["categories_updated"].add(category)
        except: continue

    # 5. Gestión de Métricas Acumulativas (Para reporte final)
    metrics_file = "src/memory/historical_metrics.json"
    accumulated_report = full_extraction_report
    if is_historical and os.path.exists(metrics_file):
        try:
            with open(metrics_file, 'r') as f:
                prev_metrics = json.load(f)
                accumulated_report.extend(prev_metrics.get("full_report", []))
        except: pass

    metrics = {
        "total_extracted": len(accumulated_report),
        "full_report": accumulated_report,
        "x_audit": x_audit_trail,
        "start_date": since_date.isoformat() if is_historical else (datetime.now(MADRID_TZ) - timedelta(days=30)).isoformat(),
        "end_date": until_date.isoformat() if until_date else datetime.now(MADRID_TZ).isoformat()
    }
    
    if is_historical:
        # En modo histórico, guardamos métricas para el siguiente tramo
        file_updates[metrics_file] = json.dumps(metrics, indent=2)
        
        # Si aún no hemos llegado al stop_date, señalamos que hay que seguir
        has_more = since_date > datetime(2024, 10, 1, 0, 0, tzinfo=MADRID_TZ)
        
        if has_more:
            # Commit y trigger siguiente (esto se gestiona mejor en el YAML del workflow)
            print(f"NEXT_CHUNK_START: {since_date.isoformat()}")
            git_controller.apply_historical_chunk(file_updates, since_date.isoformat())
        else:
            # Último tramo: Crear el PR final
            print("[+] Todos los tramos completados. Generando PR final...")
            git_controller.apply_multi_file_changes(file_updates, metrics)
            # Borrar el archivo de métricas temporal en el commit final
            if os.path.exists(metrics_file):
                os.remove(metrics_file)
    else:
        # Modo Normal: PR inmediato
        if file_updates or full_extraction_report:
            git_controller.apply_multi_file_changes(file_updates, metrics)

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
