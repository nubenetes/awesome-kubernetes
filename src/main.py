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
from src.logger import log_event

async def master_orchestrator():
    git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
    
    log_event("INICIANDO CURADURÍA AGÉNTICA (CRONOLOGÍA Y TRANSPARENCIA)", section_break=True)
    
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
            
        log_event(f"[*] MODO HISTÓRICO: Tramo {since_date.date()} -> {until_date.date()}")
    else:
        # Modo Normal (30 días)
        days_back = int(os.getenv("CURATION_DAYS_BACK", "30"))
        since_date = datetime.now(MADRID_TZ) - timedelta(days=days_back)
        until_date = None
        log_event(f"[*] Modo Normal: Desde {since_date.date()}")

    # 2. Ingesta Multi-fuente
    backup_file = os.getenv("BACKUP_FILE")
    if backup_file and os.path.exists(backup_file):
        from src.ingestion_backup import BackupDataExtractor
        extractor = BackupDataExtractor(backup_file)
        raw_social = await extractor.fetch_links()
        x_audit_trail = extractor.audit_trail
    else:
        strategy = os.getenv("EXTRACTION_STRATEGY", "search")
        twitter_client = SocialDataExtractor()
        raw_social = await twitter_client.fetch_links_since(since_date, until_date=until_date, strategy=strategy)
        x_audit_trail = twitter_client.audit_trail
    
    # GitHub Trending solo en modo normal (para no repetir)
    trending = []
    if not is_historical and not backup_file:
        log_event("[*] Buscando novedades en GitHub Trending...")
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

    # --- INICIO PROCESAMIENTO POR LOTES ---
    BATCH_SIZE = 50
    all_raw_assets_batches = [all_raw_assets[i:i + BATCH_SIZE] for i in range(0, len(all_raw_assets), BATCH_SIZE)]
    
    curator_agent = AgenticCurator()
    total_processed = 0

    for batch_index, batch_assets in enumerate(all_raw_assets_batches):
        log_event(f">>> INICIANDO LOTE {batch_index + 1}/{len(all_raw_assets_batches)} ({len(batch_assets)} enlaces)", section_break=True)
        
        full_extraction_report = []
        unique_new_assets = []
        
        evaluations = await evaluate_extracted_assets(batch_assets)
        
        for asset in batch_assets:
            url = asset["url"]
            clean_url = url.split('#')[0].rstrip('/')
            
            evaluation = evaluations.get(url, {"status": "FILTERED", "reason": "No evaluado por IA"})
            status = evaluation["status"]
            reason = evaluation.get("reason", "Aceptado")
            category = evaluation.get("category", "N/A")
            
            if clean_url in [u.split('#')[0].rstrip('/') for u in existing_urls]:
                status = "DUPLICATE"
                reason = "Ya existe en Nubenetes.com"
                log_event(f"  [=] DUPLICADO: El enlace ya está en el repositorio.")
            
            if status == "INCLUDED":
                unique_new_assets.append({
                    "url": url, "title": evaluation["title"],
                    "description": evaluation["description"], "category": category,
                    "impact_score": evaluation["impact_score"],
                    "reasoning": evaluation.get("reasoning")
                })

        # Inyección inmediata de este lote
        if unique_new_assets:
            log_event(">>> APLICANDO INYECCIONES EN MARKDOWN...", section_break=True)

            for asset in unique_new_assets:
                category = asset["category"]
                file_path = f"docs/{category}.md"
                try:
                    with open(file_path, 'r') as f: content = f.read()
                    
                    new_content = await curator_agent.decide_smart_injection(content, asset)
                    if len(new_content) > len(content):
                        # Actualizar archivo físico inmediatamente
                        with open(file_path, 'w') as f: f.write(new_content)
                except Exception as e:
                    log_event(f"  [!] Error inyectando {asset['url']}: {e}")

        total_processed += len(batch_assets)
        log_event(f"Fin del Lote {batch_index + 1}. Total procesado: {total_processed}/{len(all_raw_assets)}", section_break=True)
        
        # Pausa entre lotes para dejar respirar a la API
        if batch_index < len(all_raw_assets_batches) - 1:
            log_event("[*] Esperando 30 segundos para el siguiente lote...")
            await asyncio.sleep(30)

    log_event("PROCESO FINALIZADO CON ÉXITO.", section_break=True)

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
