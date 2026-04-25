import asyncio
from datetime import datetime, timedelta
from src.config import TARGET_REPO, MADRID_TZ, GH_TOKEN, NUBENETES_CATEGORIES
from src.ingestion_twikit import SocialDataExtractor
from src.markdown_ast import MarkdownSanitizer
from src.agentic_curator import evaluate_extracted_assets
from src.autonomous_discovery import discover_trending_assets
from src.gitops_manager import RepositoryController

async def master_orchestrator():
    git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
    
    try:
        commits = git_controller.repository.get_commits(path="docs")
        last_commit_date = commits[0].commit.committer.date.replace(tzinfo=MADRID_TZ)
        time_horizon = last_commit_date + timedelta(seconds=1)
    except:
        time_horizon = datetime(2024, 10, 5, 18, 36, tzinfo=MADRID_TZ)

    print(f"[*] Horizonte temporal: {time_horizon}")

    # 1. Ingesta Multi-fuente (Resiliente)
    twitter_client = SocialDataExtractor()
    raw_social = await twitter_client.fetch_links_since(time_horizon)
    
    print("[*] Buscando novedades en GitHub Trending...")
    trending = await discover_trending_assets()
    
    # 2. IA - Solo evaluamos si hay algo nuevo
    curated = []
    if raw_social:
        print(f"[*] Evaluando {len(raw_social)} candidatos de X con Gemini...")
        curated = await evaluate_extracted_assets(raw_social)
    
    all_new_assets = curated + trending
    
    # 3. Saneamiento y Aplicación Global
    markdown_sanitizer = MarkdownSanitizer()
    file_updates = {}
    global_stats = {"fixed": 0, "removed": 0, "duplicates": 0, "new": 0}

    print(f"[*] Auditando salud de {len(NUBENETES_CATEGORIES)} archivos Markdown...")
    for category in NUBENETES_CATEGORIES:
        file_path = f"docs/{category}.md"
        try:
            repo_file = git_controller.repository.get_contents(file_path)
            content = repo_file.decoded_content.decode("utf-8")
            
            # Saneamiento (Redirecciones + Borrado de muertos)
            purified, stats = await markdown_sanitizer.sanitize_document(content)
            
            # Inyectar si aplica
            final_content = purified
            for asset in all_new_assets:
                if asset["category"] == category:
                    prev_c = final_content
                    final_content = markdown_sanitizer.inject_curated_link(
                        final_content, category, asset["title"], asset["url"], asset["description"]
                    )
                    if final_content != prev_c:
                        global_stats["new"] += 1

            for k in ["fixed", "removed", "duplicates"]:
                global_stats[k] += stats[k]

            if final_content.strip() != content.strip():
                file_updates[file_path] = final_content
        except:
            continue

    # 4. GitOps - Solo si hay mejoras reales
    if file_updates:
        git_controller.apply_multi_file_changes(file_updates, global_stats)
        print(f"[+] Éxito. PR abierta con:")
        print(f"    - Enlaces reparados: {global_stats['fixed']}")
        print(f"    - Enlaces purgados: {global_stats['removed']}")
        print(f"    - Novedades añadidas: {global_stats['new']}")
    else:
        print("[~] Repositorio saludable. Sin cambios en este ciclo.")

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
