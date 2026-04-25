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

    def apply_state_changes(self, target_file_path: str, new_document_state: str, metrics: dict) -> None:
        timestamp_slug = datetime.now().strftime("%Y%m%d-%H%M")
        branch_name = f"bot/agentic-curation-{timestamp_slug}"
        self._create_feature_branch(branch_name)
        file_meta = self.repository.get_contents(target_file_path, ref=self.default_branch_name)
        commit_signature = f"chore(docs): automatización agéntica de curaduría [{timestamp_slug}]"
        self.repository.update_file(path=target_file_path, message=commit_signature, content=new_document_state, sha=file_meta.sha, branch=branch_name)
        pr_narrative = (
            "## 🤖 Ejecución del Agente Curador de Nubenetes\n\n"
            "Este Pull Request ha sido ensamblado de manera autónoma.\n\n"
            "### Resumen:\n"
            f"- Nuevos Enlaces (Redes): {metrics.get('social_injections', 0)}\n"
            f"- Nuevos Enlaces (Descubrimiento): {metrics.get('autonomous_injections', 0)}\n"
            "- Purga de enlaces caídos y duplicados completada."
        )
        self.repository.create_pull(title=f"Curation: {datetime.now().strftime('%d %b %Y')}", body=pr_narrative, head=branch_name, base=self.default_branch_name)
