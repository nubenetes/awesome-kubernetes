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
        """
        updates: dict { "path/to/file": "new_content" }
        """
        if not updates:
            return

        timestamp_slug = datetime.now().strftime("%Y%m%d-%H%M")
        branch_name = f"bot/agentic-curation-{timestamp_slug}"
        self._create_feature_branch(branch_name)

        for file_path, content in updates.items():
            try:
                file_meta = self.repository.get_contents(file_path, ref=self.default_branch_name)
                commit_signature = f"chore(docs): curaduría agéntica en {file_path} [{timestamp_slug}]"
                self.repository.update_file(
                    path=file_path,
                    message=commit_signature,
                    content=content,
                    sha=file_meta.sha,
                    branch=branch_name
                )
            except Exception as e:
                print(f"Error actualizando {file_path}: {e}")

        pr_narrative = (
            "## 🤖 Ejecución del Agente Curador de Nubenetes\n\n"
            "Este Pull Request ha sido ensamblado de manera autónoma con **Gemini**.\n\n"
            "### Resumen de Inyecciones:\n"
            f"- **Vía Redes Sociales (@nubenetes):** {metrics.get('social_injections', 0)}\n"
            f"- **Vía Descubrimiento Autónomo (Trending):** {metrics.get('autonomous_injections', 0)}\n\n"
            "### Labores de Mantenimiento:\n"
            "- Purga global de hipervínculos caídos (404/500).\n"
            "- Eliminación de duplicados y optimización de Markdown en múltiples archivos."
        )

        self.repository.create_pull(
            title=f"Automated Knowledge Curation: {datetime.now().strftime('%d %b %Y')}",
            body=pr_narrative,
            head=branch_name,
            base=self.default_branch_name
        )
