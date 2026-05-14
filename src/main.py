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

from src.gemini_utils import call_gemini_with_retry, resolve_url

async def master_orchestrator():
    git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
    start_time = datetime.now(MADRID_TZ)
    
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
        # Modo Normal: Usar CURATION_START_DATE si existe, si no state.json
        env_start = os.getenv("CURATION_START_DATE")
        if env_start:
            try:
                since_date = datetime.fromisoformat(env_start).replace(tzinfo=MADRID_TZ)
                log_event(f"[*] Modo Normal: Desde fecha manual del workflow {since_date.date()}")
            except:
                since_date = get_last_date()
                log_event(f"[*] Modo Normal: Error parseando fecha manual, usando state.json {since_date.date()}")
        else:
            since_date = get_last_date()
            log_event(f"[*] Modo Normal: Desde la última fecha guardada {since_date.date()}")

    # 2. Ingesta Multi-fuente
    backup_file = os.getenv("BACKUP_FILE")
    x_audit_trail = []
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
    if not all_raw_assets:
        log_event("[!] No se encontraron nuevos enlaces para procesar.")
        return

    # 3. Expansión y Deduplicación Inicial
    log_event(f"[*] Expandiendo y deduplicando {len(all_raw_assets)} enlaces brutos...")
    
    semaphore = asyncio.Semaphore(20) # Máximo 20 peticiones simultáneas

    async def process_asset(asset):
        async with semaphore:
            expanded_url = await resolve_url(asset["url"])
            asset["url"] = expanded_url
            return asset

    all_raw_assets = await asyncio.gather(*[process_asset(a) for a in all_raw_assets])
    
    unique_assets_map = {}
    for asset in all_raw_assets:
        clean_url = asset["url"].split('#')[0].rstrip('/').lower()
        if clean_url not in unique_assets_map:
            unique_assets_map[clean_url] = asset
        else:
            if len(asset.get("context", "")) > len(unique_assets_map[clean_url].get("context", "")):
                unique_assets_map[clean_url] = asset

    all_raw_assets = list(unique_assets_map.values())
    log_event(f"[*] Total tras deduplicación inicial: {len(all_raw_assets)} enlaces únicos.")

    # 4. Evaluación y Registro (Deduplicación Global Robusta)
    existing_urls = set()
    for root, dirs, files in os.walk("docs"):
        for file in files:
            if file.endswith(".md"):
                try:
                    with open(os.path.join(root, file), 'r') as f:
                        content = f.read()
                        found = re.findall(r'\]\((https?://[^\)]+)\)', content)
                        for url in found:
                            existing_urls.add(url.split('#')[0].rstrip('/').lower())
                except: pass
    
    log_event(f"[*] Deduplicación Global: {len(existing_urls)} URLs existentes cargadas.")

    # --- INICIO PROCESAMIENTO POR LOTES ---
    BATCH_SIZE = 40
    all_raw_assets_batches = [all_raw_assets[i:i + BATCH_SIZE] for i in range(0, len(all_raw_assets), BATCH_SIZE)]
    
    curator_agent = AgenticCurator()
    total_processed = 0
    max_tweet_date = since_date
    full_report_metrics = []
    modified_files_content = {}

    for batch_index, batch_assets in enumerate(all_raw_assets_batches):
        log_event(f">>> INICIANDO LOTE {batch_index + 1}/{len(all_raw_assets_batches)} ({len(batch_assets)} enlaces)", section_break=True)
        
        assets_to_evaluate = []
        for asset in batch_assets:
            url = asset["url"]
            clean_url = url.split('#')[0].rstrip('/').lower()
            
            # Trackear fecha máxima
            try:
                ts = asset.get('timestamp')
                asset_date = None
                if ts:
                    if isinstance(ts, str):
                        try:
                            # Twitter format: 'Tue Oct 01 19:56:51 +0000 2024'
                            asset_date = datetime.strptime(ts, '%a %b %d %H:%M:%S +0000 %Y').replace(tzinfo=MADRID_TZ)
                        except:
                            try: asset_date = datetime.fromisoformat(ts.replace('Z', '+00:00'))
                            except: pass
                    
                if asset_date and asset_date > max_tweet_date:
                    max_tweet_date = asset_date
            except: pass

            if clean_url in existing_urls:
                log_event(f"  [=] SALTADO: {url[:60]}... (Ya existe)")
                full_report_metrics.append({
                    "url": url, "status": "DUPLICATE", "reason": "Ya existe en repositorio",
                    "category": "N/A", "post_date": ts, "source": asset.get("source_type", "Social")
                })
                continue
            assets_to_evaluate.append(asset)

        if not assets_to_evaluate:
            log_event("  [*] El lote completo consiste en duplicados. Siguiente lote.")
            continue

        evaluations = await evaluate_extracted_assets(assets_to_evaluate)
        unique_new_assets = []
        
        for asset in assets_to_evaluate:
            url = asset["url"]
            evaluation = evaluations.get(url, {"status": "FILTERED", "reason": "No evaluado por IA"})
            
            full_report_metrics.append({
                "url": url, "status": evaluation["status"], "reason": evaluation.get("reason", "Aceptado"),
                "category": evaluation.get("category", "N/A"), "post_date": asset.get("timestamp"),
                "source": asset.get("source_type", "Social")
            })

            if evaluation["status"] == "INCLUDED":
                unique_new_assets.append({
                    "url": url, "title": evaluation["title"],
                    "description": evaluation["description"], "category": evaluation.get("category", "kubernetes-tools"),
                    "impact_score": evaluation["impact_score"],
                    "reasoning": evaluation.get("reasoning")
                })
                existing_urls.add(url.split('#')[0].rstrip('/').lower())

        # Inyección inmediata
        if unique_new_assets:
            log_event(f">>> APLICANDO {len(unique_new_assets)} INYECCIONES EN MARKDOWN...", section_break=True)
            for asset in unique_new_assets:
                category = asset["category"]
                file_path = f"docs/{category}.md"
                try:
                    if file_path in modified_files_content:
                        content = modified_files_content[file_path]
                    else:
                        if not os.path.exists(file_path):
                            content = f"# {category.capitalize()}\n\n"
                        else:
                            with open(file_path, 'r') as f: content = f.read()
                    
                    new_content = await curator_agent.decide_smart_injection(content, asset)
                    
                    if len(new_content) > len(content):
                        modified_files_content[file_path] = new_content
                        with open(file_path, 'w') as f: f.write(new_content)
                        log_event(f"  [>>>] ÉXITO: Inyectado en docs/{category}.md -> {asset['url']}")
                    else:
                        log_event(f"  [!] ADVERTENCIA: La inyección no modificó el archivo para {asset['url']}")
                except Exception as e:
                    log_event(f"  [!] Error inyectando {asset['url']}: {e}")

        total_processed += len(batch_assets)
        if batch_index < len(all_raw_assets_batches) - 1:
            log_event(f"[*] Pausa de seguridad: 5s para el siguiente lote...")
            await asyncio.sleep(5)

    # 4. Finalización y PR
    if modified_files_content:
        log_event(">>> GENERANDO PULL REQUEST...", section_break=True)
        metrics = {
            "total_extracted": len(all_raw_assets),
            "start_date": since_date.isoformat(),
            "end_date": datetime.now(MADRID_TZ).isoformat(),
            "full_report": full_report_metrics,
            "x_audit": x_audit_trail
        }
        try:
            git_controller.apply_multi_file_changes(modified_files_content, metrics)
        except Exception as e:
            log_event(f"[!] Error creando PR: {e}")

    # Auditoría de reorganización
    await curator_agent.suggest_reorganization()

    # Actualizar estado
    if max_tweet_date > since_date:
        save_state(max_tweet_date + timedelta(seconds=1))

    # Lógica de re-disparo para Modo Histórico en GitHub Actions
    if is_historical and since_date > final_stop_date:
        # Imprimir para que el YAML lo capture
        print(f"\nNEXT_CHUNK_START: {since_date.isoformat()}")
        log_event(f"[*] TRAMO FINALIZADO. Sugiriendo siguiente tramo desde: {since_date.date()}", section_break=True)

    log_event("PROCESO FINALIZADO CON ÉXITO.", section_break=True)



    log_event("PROCESO FINALIZADO CON ÉXITO.", section_break=True)

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
