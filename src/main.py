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
    
    print("[*] INICIANDO CURADURÍA AGÉNTICA (SOLO INYECCIÓN DE NOVEDADES)")
    
    # 1. Determinar horizonte temporal
    try:
        commits = git_controller.repository.get_commits(path="docs")
        if commits.totalCount > 0:
            last_commit_date = commits[0].commit.committer.date.replace(tzinfo=MADRID_TZ)
            time_horizon = last_commit_date + timedelta(seconds=1)
        else:
            raise Exception()
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
    print(f"[*] Total candidatos a inyectar: {len(all_new_assets)}")

    # 4. Inyección en Markdowns
    file_updates = {}
    stats = {"new_links": 0, "categories_updated": set()}

    for category in NUBENETES_CATEGORIES:
        file_path = f"docs/{category}.md"
        try:
            repo_file = git_controller.repository.get_contents(file_path)
            content = repo_file.decoded_content.decode("utf-8")
            
            # Limpiamos solo duplicados existentes para mantener higiene
            final_content, _ = await markdown_sanitizer.sanitize_document(content)
            
            # Inyectar novedades
            original_content = final_content
            for asset in all_new_assets:
                if asset["category"] == category:
                    final_content = markdown_sanitizer.inject_curated_link(
                        final_content, category, asset["title"], asset["url"], asset["description"]
                    )
            
            if final_content.strip() != original_content.strip():
                file_updates[file_path] = final_content
                stats["new_links"] += (final_content.count("  - [") - original_content.count("  - ["))
                stats["categories_updated"].add(category)
        except Exception:
            continue

    # 5. GitOps - Generar Informe Mermaid en el PR
    if file_updates:
        metrics = {
            "social_injections": len(curated),
            "trending_injections": len(trending),
            "total_new": stats["new_links"],
            "categories": list(stats["categories_updated"])
        }
        
        print(f"[+] Éxito. Preparando PR con {stats['new_links']} nuevos recursos.")
        git_controller.apply_multi_file_changes(file_updates, metrics)
    else:
        print("[~] No se han encontrado novedades relevantes en este ciclo.")

if __name__ == "__main__":
    asyncio.run(master_orchestrator())
