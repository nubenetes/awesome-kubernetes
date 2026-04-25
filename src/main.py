import asyncio
from datetime import datetime, timedelta
from src.config import TARGET_REPO, MAIN_DOC_FILE, MADRID_TZ, GH_TOKEN
from src.ingestion_twikit import SocialDataExtractor
from src.markdown_ast import MarkdownSanitizer
from src.agentic_curator import evaluate_extracted_assets
from src.autonomous_discovery import discover_trending_assets
from src.gitops_manager import RepositoryController

async def master_orchestrator():
    git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
    
    # DINÁMICO: Obtener la fecha del último commit en la carpeta docs/
    # Si no hay commits previos o hay error, usamos la fecha de seguridad 2024-10-05
    try:
        commits = git_controller.repository.get_commits(path="docs")
        last_commit_date = commits[0].commit.committer.date.replace(tzinfo=MADRID_TZ)
        time_horizon = last_commit_date + timedelta(seconds=1)
    except:
        time_horizon = datetime(2024, 10, 5, 18, 36, tzinfo=MADRID_TZ)

    print(f"Buscando actualizaciones desde: {time_horizon}")

    # 1. Extracción de X (Twitter)
    twitter_client = SocialDataExtractor()
    raw_social_links = await twitter_client.fetch_links_since(time_horizon)
    
    # 2. Descubrimiento proactivo en GitHub
    autonomous_links = await discover_trending_assets()
    
    # 3. Evaluación con IA (Gemini)
    curated_social_links = await evaluate_extracted_assets(raw_social_links)
    
    total_new_assets = curated_social_links + autonomous_links
    
    # 4. Procesamiento de Markdown
    markdown_sanitizer = MarkdownSanitizer()
    repo_file_data = git_controller.repository.get_contents(MAIN_DOC_FILE)
    document_state = repo_file_data.decoded_content.decode("utf-8")
    
    # 5. Limpieza de enlaces rotos y duplicados (Higiene)
    purified_document_state = await markdown_sanitizer.sanitize_document(document_state)
    
    # 6. Inyección de nuevos recursos
    final_document_state = purified_document_state
    for asset in total_new_assets:
        final_document_state = markdown_sanitizer.inject_curated_link(
            final_document_state, 
            asset["category"], 
            asset["title"], 
            asset["url"], 
            asset["description"]
        )
    
    # 7. Persistencia vía Pull Request si hay cambios
    if final_document_state.strip() != document_state.strip():
        metrics = {
            "social_injections": len(curated_social_links),
            "autonomous_injections": len(autonomous_links)
        }
        git_controller.apply_state_changes(MAIN_DOC_FILE, final_document_state, metrics)
        print(f"Cambios detectados. PR abierta con {len(total_new_assets)} nuevos recursos.")
    else:
        print("El repositorio ya está actualizado. Sin cambios pendientes.")

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
