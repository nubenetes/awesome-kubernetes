import asyncio
import sys
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
    state_file = "src/memory/state.json"
    
    print("[*] INICIANDO CURADURÍA AGÉNTICA (SOLO INYECCIÓN DE NOVEDADES)")
    
    # 1. Cargar Estado y Horizonte Temporal
    try:
        with open(state_file, 'r') as f:
            state = json.load(f)
            time_horizon = datetime.fromisoformat(state["last_processed_tweet_date"]).replace(tzinfo=MADRID_TZ)
    except:
        time_horizon = datetime(2024, 10, 1, 0, 0, tzinfo=MADRID_TZ)

    print(f"[*] Buscando novedades desde: {time_horizon}")

    # 2. Ingesta Multi-fuente
    twitter_client = SocialDataExtractor()
    raw_social = await twitter_client.fetch_links_since(time_horizon)
    
    print("[*] Buscando novedades en GitHub Trending...")
    trending = await discover_trending_assets()
    
    # 3. Evaluación con IA
    curated = []
    if raw_social:
        print(f"[*] Evaluando {len(raw_social)} candidatos de X con Gemini...")
        curated = await evaluate_extracted_assets(raw_social)
    
    all_new_assets = curated + trending
    
    # 4. Deduplicación Global (Pre-escaneo de todos los .md)
    print("[*] Escaneando repositorio para deduplicación global...")
    existing_urls = set()
    for doc in os.listdir("docs"):
        if doc.endswith(".md"):
            try:
                with open(os.path.join("docs", doc), 'r') as f:
                    existing_urls.update(re.findall(r'\]\((https?://[^\)]+)\)', f.read()))
            except: pass
    
    # Filtrar solo los que no existen
    unique_new_assets = []
    for asset in all_new_assets:
        clean_url = asset["url"].split('#')[0].rstrip('/')
        if any(clean_url in ex for ex in existing_urls):
            continue
        unique_new_assets.append(asset)
    
    print(f"[*] Total candidatos únicos a inyectar: {len(unique_new_assets)}")

    # 5. Inyección en Markdowns
    file_updates = {}
    stats = {
        "new_links": 0, 
        "categories_updated": set(),
        "added_details": [],
        "removed_details": [],
        "start_date": time_horizon.isoformat(),
        "end_date": datetime.now(MADRID_TZ).isoformat()
    }

    for category in NUBENETES_CATEGORIES:
        file_path = f"docs/{category}.md"
        try:
            repo_file = git_controller.repository.get_contents(file_path)
            content = repo_file.decoded_content.decode("utf-8")
            final_content, doc_stats = await markdown_sanitizer.sanitize_document(content)
            
            original_content = final_content
            for asset in unique_new_assets:
                if asset["category"] == category:
                    prev_len = len(final_content)
                    final_content = markdown_sanitizer.inject_curated_link(
                        final_content, category, asset["title"], asset["url"], asset["description"]
                    )
                    if len(final_content) > prev_len:
                        stats["added_details"].append({
                            "title": asset["title"],
                            "url": asset["url"],
                            "category": category
                        })
            
            if final_content.strip() != original_content.strip():
                file_updates[file_path] = final_content
                stats["new_links"] += (final_content.count("  - [") - original_content.count("  - ["))
                stats["categories_updated"].add(category)
        except: continue

    # 6. Actualizar Estado de Tiempo
    if raw_social:
        new_horizon = max([datetime.fromisoformat(t["timestamp"]) for t in raw_social]) + timedelta(seconds=1)
        with open(state_file, 'w') as f:
            json.dump({"last_processed_tweet_date": new_horizon.isoformat()}, f)

    # 7. GitOps
    if file_updates:
        metrics = {
            "social_injections": len(curated),
            "trending_injections": len(trending),
            "total_new": stats["new_links"],
            "categories": list(stats["categories_updated"]),
            "added_list": stats["added_details"],
            "removed_list": stats["removed_details"],
            "start_date": stats["start_date"],
            "end_date": stats["end_date"]
        }
        git_controller.apply_multi_file_changes(file_updates, metrics)
    else:
        print("[~] No se han encontrado novedades relevantes.")

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
