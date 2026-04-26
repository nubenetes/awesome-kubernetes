from github import Github
from datetime import datetime

class RepositoryController:
    def __init__(self, access_token: str, repository_identifier: str):
        self.github_client = Github(access_token)
        self.repository = self.github_client.get_repo(repository_identifier)
        self.default_branch_name = self.repository.default_branch

    def _create_feature_branch(self, branch_name: str) -> None:
        base_branch = self.repository.get_branch(self.default_branch_name)
        self.repository.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base_branch.commit.sha)

    def apply_multi_file_changes(self, updates: dict, metrics: dict) -> None:
        if not updates:
            return

        timestamp_slug = datetime.now().strftime("%Y%m%d-%H%M")
        branch_name = f"bot/knowledge-update-{timestamp_slug}"
        self._create_feature_branch(branch_name)

        for file_path, content in updates.items():
            try:
                file_meta = self.repository.get_contents(file_path, ref=self.default_branch_name)
                commit_signature = f"chore(docs): optimizar y curar {file_path} [{timestamp_slug}]"
                self.repository.update_file(
                    path=file_path,
                    message=commit_signature,
                    content=content,
                    sha=file_meta.sha,
                    branch=branch_name
                )
            except Exception as e:
                print(f"Error actualizando {file_path}: {e}")

        # Informe Visual en el PR
        categories_str = ", ".join([f"`{c}`" for c in metrics.get('categories', [])])
        
        pr_narrative = (
            f"## 💎 Actualización de Conocimiento: Kubernetes & Cloud Native\n\n"
            f"Este PR añade **{metrics.get('total_new', 0)}** nuevos recursos y optimiza los existentes.\n\n"
            f"### ✅ Mejoras realizadas:\n"
            f"- **Inyección de Novedades**: Nuevos recursos filtrados desde X y Trending.\n"
            f"- **Optimización de Duplicados**: Se han detectado URLs repetidas y el bot ha elegido mantener la versión con **más estrellas (🌟)** y **mejor descripción**, eliminando las versiones redundantes más pobres.\n\n"
            f"### 📊 Resumen de Ingesta:\n"
            f"```mermaid\n"
            f"pie title Origen de los Nuevos Recursos\n"
            f"    \"X (@nubenetes)\" : {metrics.get('social_injections', 0)}\n"
            f"    \"GitHub Trending\" : {metrics.get('trending_injections', 0)}\n"
            f"```\n\n"
            f"### 📂 Categorías Impactadas:\n"
            f"{categories_str}\n\n"
            f"---\n"
            f"**Nota del Bot:** El bot ya no borra enlaces por falta de respuesta del servidor (salud), solo optimiza el contenido duplicado basándose en la calidad del texto y las menciones destacadas."
        )

        self.repository.create_pull(
            title=f"💎 Knowledge Update & Optimization: {datetime.now().strftime('%d %b %Y')}",
            body=pr_narrative,
            head=branch_name,
            base=self.default_branch_name
        )
