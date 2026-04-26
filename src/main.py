import asyncio
import sys
from datetime import datetime, timedelta
from src.config import TARGET_REPO, MADRID_TZ, GH_TOKEN, NUBENETES_CATEGORIES
from src.ingestion_twikit import SocialDataExtractor
from src.markdown_ast import MarkdownSanitizer
from src.agentic_curator import evaluate_extracted_assets
from src.autonomous_discovery import discover_trending_assets
from src.gitops_manager import RepositoryController

async def master_orchestrator(mode: str = "discovery"):
    git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
    markdown_sanitizer = MarkdownSanitizer()
    
    all_new_assets = []
    full_health_check = (mode == "health")

    if mode == "discovery":
        print("[*] MODO DESCUBRIMIENTO: Buscando nuevas joyas...")
        try:
            # Obtenemos los commits que han modificado la carpeta 'docs'
            # PyGithub por defecto consulta la rama principal (main/master)
            commits = git_controller.repository.get_commits(path="docs")
            
            if commits.totalCount > 0:
                # La fecha del último commit integrado (vía merge de PR o directo)
                last_commit_date = commits[0].commit.committer.date.replace(tzinfo=MADRID_TZ)
                time_horizon = last_commit_date + timedelta(seconds=1)
                print(f"[*] Última integración detectada el: {last_commit_date}")
            else:
                raise Exception("Sin historial en docs")
        except Exception:
            # Fallback: Octubre 2024 (Inicio de la automatización solicitado)
            time_horizon = datetime(2024, 10, 1, 0, 0, tzinfo=MADRID_TZ)
            print(f"[*] Iniciando desde el horizonte configurado: {time_horizon}")

        print(f"[*] Buscando novedades en X desde: {time_horizon}")

        # 1. Ingesta Multi-fuente
        twitter_client = SocialDataExtractor()
        raw_social = await twitter_client.fetch_links_since(time_horizon)
        
        print("[*] Buscando novedades en GitHub Trending...")
        trending = await discover_trending_assets()
        
        # 2. IA Evaluation
        curated = []
        if raw_social:
            print(f"[*] Evaluando {len(raw_social)} candidatos de X con Gemini...")
            curated = await evaluate_extracted_assets(raw_social)
        
        all_new_assets = curated + trending
    
    elif mode == "health":
        print("[*] MODO HEALTH CHECK: Revisión exhaustiva de enlaces...")

    # 3. Aplicación de Cambios (Misma lógica anterior...)
    file_updates = {}
    global_stats = {"fixed": 0, "removed": 0, "duplicates": 0, "new": 0}

    for category in NUBENETES_CATEGORIES:
        file_path = f"docs/{category}.md"
        try:
            repo_file = git_controller.repository.get_contents(file_path)
            content = repo_file.decoded_content.decode("utf-8")
            
            purified, stats = await markdown_sanitizer.sanitize_document(content, full_health_check=full_health_check)
            
            final_content = purified
            if mode == "discovery":
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
        except Exception:
            continue

    # 4. GitOps
    if file_updates:
        metrics = {
            "social_injections": len([a for a in all_new_assets if "context" in a]),
            "autonomous_injections": len([a for a in all_new_assets if "context" not in a]),
            "fixed": global_stats["fixed"],
            "removed": global_stats["removed"]
        }
        
        if mode == "health":
            print(f"[+] Health Check completado. Reparados: {metrics['fixed']}, Borrados: {metrics['removed']}")
        else:
            print(f"[+] Descubrimiento completado. Nuevos: {global_stats['new']}")
            
        git_controller.apply_multi_file_changes(file_updates, metrics)
    else:
        print("[~] Repositorio saludable. Sin cambios en este ciclo.")

if __name__ == "__main__":
    run_mode = "discovery"
    if len(sys.argv) > 1:
        if sys.argv[1] in ["discovery", "health"]:
            run_mode = sys.argv[1]
    
    asyncio.run(master_orchestrator(run_mode))
