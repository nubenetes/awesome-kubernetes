import json
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

        if not updates:
            updates["src/memory/last_audit_run.json"] = json.dumps({
                "timestamp": metrics.get("end_date"),
                "total_extracted": metrics.get("total_extracted"),
                "status": "Audit Only"
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

        # --- CONSTRUCCIÓN DEL REPORTE ---
        full_report = metrics.get('full_report', [])
        
        # 1. Tabla Matricial con Índice Numérico y Fecha (Priorizando INCLUDED)
        # Ordenamos para que los INCLUDED salgan primero en el reporte del PR
        sorted_report = sorted(full_report, key=lambda x: 0 if x['status'] == 'INCLUDED' else 1)
        
        matrix_table = "### 📋 Matriz de Auditoría de Enlaces (Full Extraction)\n"
        matrix_table += "| # | Estado | Fecha Post | Origen | Motivo | Categoría | URL |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
        
        counts = {"INCLUDED": 0, "DUPLICATE": 0, "FILTERED": 0}
        source_counts = {}
        
        # Construcción segura para no exceder el límite de GH (65k chars)
        current_table_rows = ""
        is_truncated = False
        
        for idx, item in enumerate(sorted_report, 1):
            status_emoji = {"INCLUDED": "✅", "DUPLICATE": "👯", "FILTERED": "🛡️"}.get(item['status'], "❓")
            date_str = item.get('post_date', 'N/A')[:10] if item.get('post_date') else 'N/A'
            
            row = f"| {idx} | {status_emoji} {item['status']} | {date_str} | {item.get('source', 'N/A')} | {item['reason']} | `{item['category']}` | {item['url']} |\n"
            
            # Si la tabla ya es muy grande (~45k chars), truncamos para dejar espacio al resto del PR
            if len(current_table_rows) < 45000:
                current_table_rows += row
            else:
                is_truncated = True
                
            counts[item['status']] = counts.get(item['status'], 0) + 1
            if item['status'] == "INCLUDED":
                src = item.get('source', 'Unknown')
                source_counts[src] = source_counts.get(src, 0) + 1

        matrix_table += current_table_rows
        if is_truncated:
            matrix_table += f"\n> ⚠️ **Nota:** El reporte se ha truncado debido al límite de caracteres de GitHub. Se muestran los primeros {idx-1} de {len(full_report)} elementos procesados.\n"

        # 2. Diagnóstico de Extracción Histórica
        extraction_audit = "### 🕵️ Diagnóstico de Horizonte Temporal\n"
        start_date_str = metrics.get('start_date')[:10] if metrics.get('start_date') else 'N/A'
        
        # Encontrar la fecha más antigua realmente extraída
        actual_oldest = "N/A"
        dates = [item.get('post_date') for item in full_report if item.get('post_date')]
        if dates:
            actual_oldest = min(dates)[:10]

        if actual_oldest != "N/A" and actual_oldest > start_date_str:
            extraction_audit += f"⚠️ **Límite Alcanzado:** Se solicitó desde `{start_date_str}`, pero la extracción se detuvo en `{actual_oldest}`.\n"
            extraction_audit += "- **Motivo:** X.com limita el scroll infinito o se alcanzó el límite de 1000 enlaces.\n"
            extraction_audit += "- **Acción Recomendada:** Para llegar a Oct 2024 exacto, el bot usa búsqueda avanzada. Si no lo logra, puede ser por densidad de posts.\n"
        else:
            extraction_audit += f"✅ **Horizonte Alcanzado:** La extracción cubrió exitosamente desde `{start_date_str}`.\n"

        # 3. Diagramas Mermaid
        mermaid_pie = "### 📊 Métricas de Decisión\n```mermaid\npie title Distribución de Decisión Agéntica\n"
        mermaid_pie += f"    \"Aceptados (Inyectados)\" : {counts['INCLUDED']}\n"
        mermaid_pie += f"    \"Duplicados (Ignorados)\" : {counts['DUPLICATE']}\n"
        mermaid_pie += f"    \"Filtrados (Calidad/Impacto)\" : {counts['FILTERED']}\n```\n"

        mermaid_origin = ""
        if source_counts:
            mermaid_origin = "### 🌍 Origen de las Novedades Inyectadas\n```mermaid\npie title Fuentes de Referencias Añadidas\n"
            for src, val in source_counts.items():
                mermaid_origin += f"    \"{src}\" : {val}\n"
            mermaid_origin += "```\n"

        # 4. Log de Ingesta
        x_log = "### ⚡ Audit Trail de Ingesta (X.com)\n"
        for entry in metrics.get('x_audit', []):
            x_log += f"- {entry}\n"

        pr_narrative = (
            f"## 💎 Knowledge Update War Room: Kubernetes & Cloud Native\n\n"
            f"Este reporte detalla el procesamiento de **{metrics.get('total_extracted', 0)}** enlaces detectados.\n\n"
            f"{extraction_audit}\n"
            f"{mermaid_pie}\n"
            f"{mermaid_origin}\n"
            f"{x_log}\n"
            f"{matrix_table}\n"
            f"---\n"
            f"**Nota de Evaluación:** Se ha analizado exitosamente el histórico. "
            f"Se han procesado un total de {len(full_report)} elementos."
        )

        self.repository.create_pull(
            title=f"💎 Knowledge Update & Optimization: {datetime.now().strftime('%d %b %Y')}",
            body=pr_narrative,
            head=branch_name,
            base=self.default_branch_name
        )
