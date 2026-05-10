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
        timestamp_slug = datetime.now().strftime("%Y%m%d-%H%M")
        branch_name = f"bot/knowledge-update-{timestamp_slug}"
        self._create_feature_branch(branch_name)

        # Si no hay cambios en Markdowns, añadimos un cambio técnico para permitir abrir la PR con el reporte
        if not updates:
            updates["src/memory/last_audit_run.json"] = json.dumps({
                "timestamp": metrics.get("end_date"),
                "total_extracted": metrics.get("total_extracted"),
                "status": "Audit Only (No new links injected)"
            }, indent=2)

        for file_path, content in updates.items():
            try:
                commit_signature = f"chore: update {file_path} [{timestamp_slug}]"
                try:
                    file_meta = self.repository.get_contents(file_path, ref=self.default_branch_name)
                    self.repository.update_file(
                        path=file_path, message=commit_signature, content=content,
                        sha=file_meta.sha, branch=branch_name
                    )
                except Exception as e:
                    if "404" in str(e):
                        self.repository.create_file(
                            path=file_path, message=f"chore: create {file_path}",
                            content=content, branch=branch_name
                        )
            except Exception as e:
                print(f"Error procesando {file_path}: {e}")

        # --- CONSTRUCCIÓN DEL REPORTE ÉLITE ---
        full_report = metrics.get('full_report', [])
        
        # 1. Tabla Matricial de Auditoría
        # Limitamos la tabla si es muy larga para evitar errores de API de GitHub
        matrix_table = "### 📋 Matriz de Auditoría de Enlaces (Full Extraction)\n"
        matrix_table += "| Estado | Motivo | Categoría | URL |\n| :--- | :--- | :--- | :--- |\n"
        
        counts = {"INCLUDED": 0, "DUPLICATE": 0, "FILTERED": 0}
        for item in full_report[:200]: # Mostrar solo los primeros 200 para no romper el límite de caracteres del PR
            status_emoji = {"INCLUDED": "✅", "DUPLICATE": "👯", "FILTERED": "🛡️"}.get(item['status'], "❓")
            matrix_table += f"| {status_emoji} {item['status']} | {item['reason']} | `{item['category']}` | {item['url']} |\n"
            counts[item['status']] = counts.get(item['status'], 0) + 1

        if len(full_report) > 200:
            matrix_table += f"\n> 💡 *... y {len(full_report) - 200} enlaces más procesados.*"

        # 2. Diagrama Mermaid
        mermaid_pie = "### 📊 Métricas de Decisión\n```mermaid\npie title Distribución de Decisión Agéntica\n"
        mermaid_pie += f"    \"Aceptados (Inyectados)\" : {counts['INCLUDED']}\n"
        mermaid_pie += f"    \"Duplicados (Ignorados)\" : {counts['DUPLICATE']}\n"
        mermaid_pie += f"    \"Filtrados (Calidad/Impacto)\" : {counts['FILTERED']}\n```\n"

        # 3. Log de Ingesta
        x_log = "### ⚡ Audit Trail de Ingesta (X.com)\n"
        for entry in metrics.get('x_audit', []):
            x_log += f"- {entry}\n"

        pr_narrative = (
            f"## 💎 Knowledge Update War Room: Kubernetes & Cloud Native\n\n"
            f"Este reporte detalla el procesamiento de **{metrics.get('total_extracted', 0)}** enlaces detectados.\n\n"
            f"**Ventana Temporal:** `{metrics.get('start_date')}` ➔ `{metrics.get('end_date')}`\n\n"
            f"{mermaid_pie}\n"
            f"{x_log}\n"
            f"{matrix_table}\n"
            f"---\n"
            f"**Nota de Evaluación:** Este PR incluye {len(metrics.get('added_list', []))} novedades reales. "
            f"La ventana temporal se ha calculado automáticamente basándose en el último PR mergeado con éxito."
        )

        self.repository.create_pull(
            title=f"💎 Knowledge Update & Optimization: {datetime.now().strftime('%d %b %Y')}",
            body=pr_narrative,
            head=branch_name,
            base=self.default_branch_name
        )
