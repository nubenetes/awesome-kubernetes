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

    print(f">>> Iniciando curaduría desde: {time_horizon}")

    # 1. Obtención de datos
    twitter_client = SocialDataExtractor()
    raw_social_links = await twitter_client.fetch_links_since(time_horizon)
    autonomous_links = await discover_trending_assets()
    
    # 2. Evaluación con IA
    curated_social_links = await evaluate_extracted_assets(raw_social_links)
    total_new_assets = curated_social_links + autonomous_links
    
    # 3. Preparar cambios
    markdown_sanitizer = MarkdownSanitizer()
    file_updates = {}
    
    # Identificar qué archivos necesitan ser procesados
    categories_to_update = set([a["category"] for asset in total_new_assets])
    
    # 4. Procesar inyecciones y saneamiento
    for category in NUBENETES_CATEGORIES:
        file_path = f"docs/{category}.md"
        try:
            repo_file = git_controller.repository.get_contents(file_path)
            content = repo_file.decoded_content.decode("utf-8")
            
            # Saneamiento (siempre lo hacemos para mantener la salud)
            new_content = await markdown_sanitizer.sanitize_document(content)
            
            # Inyección si hay activos para esta categoría
            for asset in total_new_assets:
                if asset["category"] == category:
                    new_content = markdown_sanitizer.inject_curated_link(
                        new_content, category, asset["title"], asset["url"], asset["description"]
                    )
            
            if new_content.strip() != content.strip():
                file_updates[file_path] = new_content
        except:
            continue

    # 5. Aplicar cambios vía GitOps
    if file_updates:
        metrics = {
            "social_injections": len(curated_social_links),
            "autonomous_injections": len(autonomous_links)
        }
        git_controller.apply_multi_file_changes(file_updates, metrics)
        print(f">>> Éxito: PR abierta con cambios en {len(file_updates)} archivos.")
    else:
        print(">>> Sin cambios necesarios.")

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
