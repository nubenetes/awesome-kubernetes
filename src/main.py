import asyncio
from datetime import datetime, timedelta
from src.config import TARGET_REPO, MAIN_DOC_FILE, MADRID_TZ, GH_TOKEN
from src.ingestion_twikit import SocialDataExtractor
from src.markdown_ast import MarkdownSanitizer
from src.agentic_curator import evaluate_extracted_assets
from src.autonomous_discovery import discover_trending_assets
from src.gitops_manager import RepositoryController

async def master_orchestrator():
    time_horizon = datetime(2024, 10, 5, 18, 36, tzinfo=MADRID_TZ)
    twitter_client = SocialDataExtractor()
    raw_social_links = await twitter_client.fetch_links_since(time_horizon)
    autonomous_links = await discover_trending_assets()
    curated_social_links = await evaluate_extracted_assets(raw_social_links)
    total_new_assets = curated_social_links + autonomous_links
    git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
    markdown_sanitizer = MarkdownSanitizer()
    repo_file_data = git_controller.repository.get_contents(MAIN_DOC_FILE)
    document_state = repo_file_data.decoded_content.decode("utf-8")
    purified_document_state = await markdown_sanitizer.sanitize_document(document_state)
    final_document_state = purified_document_state
    for asset in total_new_assets:
        final_document_state = markdown_sanitizer.inject_curated_link(final_document_state, asset["category"], asset["title"], asset["url"], asset["description"])
    if final_document_state != document_state:
        metrics = {"social_injections": len(curated_social_links), "autonomous_injections": len(autonomous_links)}
        git_controller.apply_state_changes(MAIN_DOC_FILE, final_document_state, metrics)
    else:
        print("Sin cambios detectados.")

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
