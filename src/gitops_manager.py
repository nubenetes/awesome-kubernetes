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

    def apply_historical_chunk(self, updates: dict, next_since: str) -> None:
        branch_name = "bot/historical-accumulator"
        
        # Verificar si la rama existe, si no, crearla desde master
        try:
            self.repository.get_branch(branch_name)
        except:
            self._create_feature_branch(branch_name)

        for file_path, content in updates.items():
            try:
                try:
                    file_meta = self.repository.get_contents(file_path, ref=branch_name)
                    self.repository.update_file(
                        path=file_path, message=f"chore(historical): chunk sync since {next_since}",
                        content=content, sha=file_meta.sha, branch=branch_name
                    )
                except Exception as e:
                    if "404" in str(e):
                        self.repository.create_file(
                            path=file_path, message=f"chore(historical): init {file_path}",
                            content=content, branch=branch_name
                        )
            except Exception as e:
                print(f"Error en tramo histórico para {file_path}: {e}")

    def apply_multi_file_changes(self, updates: dict, metrics: dict) -> None:
        timestamp_slug = datetime.now().strftime("%Y%m%d-%H%M")
        is_historical = "historical" in metrics.get("start_date", "").lower() or metrics.get("total_extracted", 0) > 500
        
        branch_name = f"bot/knowledge-update-{timestamp_slug}"
        
        # En el último tramo histórico, usamos el accumulator como base si existe
        accumulator_branch = "bot/historical-accumulator"
        base_sha = None
        try:
            acc = self.repository.get_branch(accumulator_branch)
            base_sha = acc.commit.sha
            # Si venimos de histórico, la rama destino debe ser creada desde el accumulator
            self.repository.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base_sha)
        except:
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
        sorted_report = sorted(full_report, key=lambda x: 0 if x['status'] == 'INCLUDED' else 1)
        
        header_table = "| # | Estado | Fecha Post | Origen | Motivo | Categoría | URL |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
        
        counts = {"INCLUDED": 0, "DUPLICATE": 0, "FILTERED": 0}
        source_counts = {}
        
        all_rows = []
        for idx, item in enumerate(sorted_report, 1):
            status_emoji = {"INCLUDED": "✅", "DUPLICATE": "👯", "FILTERED": "🛡️"}.get(item['status'], "❓")
            date_str = item.get('post_date', 'N/A')[:10] if item.get('post_date') else 'N/A'
            all_rows.append(f"| {idx} | {status_emoji} {item['status']} | {date_str} | {item.get('source', 'N/A')} | {item['reason']} | `{item['category']}` | {item['url']} |\n")
            
            counts[item['status']] = counts.get(item['status'], 0) + 1
            if item['status'] == "INCLUDED":
                src = item.get('source', 'Unknown')
                source_counts[src] = source_counts.get(src, 0) + 1

        # Dividir filas en fragmentos para PR Body y Comentarios
        # Límite GH: 65,536. Usamos fragmentos de ~50k chars para seguridad.
        chunks = []
        current_chunk = header_table
        for row in all_rows:
            if len(current_chunk) + len(row) > 50000:
                chunks.append(current_chunk)
                current_chunk = header_table + row
            else:
                current_chunk += row
        chunks.append(current_chunk)

        matrix_table_body = chunks[0]
        if len(chunks) > 1:
            matrix_table_body += f"\n> ℹ️ **Nota:** La tabla continúa en los comentarios del PR ({len(chunks)-1} partes adicionales).\n"

        # 2. Diagnóstico de Extracción Histórica
        extraction_audit = "### 🕵️ Diagnóstico de Horizonte Temporal\n"
        start_date_str = metrics.get('start_date')[:10] if metrics.get('start_date') else 'N/A'
        
        actual_oldest = "N/A"
        dates = [item.get('post_date') for item in full_report if item.get('post_date')]
        if dates: actual_oldest = min(dates)[:10]

        if actual_oldest != "N/A" and actual_oldest > start_date_str:
            extraction_audit += f"⚠️ **Límite Alcanzado:** Se solicitó desde `{start_date_str}`, pero se detuvo en `{actual_oldest}`.\n"
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
        for entry in metrics.get('x_audit', []): x_log += f"- {entry}\n"

        pr_narrative = (
            f"## 💎 Knowledge Update War Room: Kubernetes & Cloud Native\n\n"
            f"Este reporte detalla el procesamiento de **{metrics.get('total_extracted', 0)}** enlaces detectados.\n\n"
            f"{extraction_audit}\n"
            f"{mermaid_pie}\n"
            f"{mermaid_origin}\n"
            f"{x_log}\n"
            f"### 📋 Matriz de Auditoría (Parte 1)\n{matrix_table_body}\n"
            f"---\n"
            f"**Nota de Evaluación:** Se ha analizado exitosamente el histórico completo."
        )

        pr = self.repository.create_pull(
            title=f"💎 Knowledge Update & Optimization: {datetime.now().strftime('%d %b %Y')}",
            body=pr_narrative,
            head=branch_name,
            base=self.default_branch_name
        )

        # 5. Publicar comentarios con el resto de la tabla
        if len(chunks) > 1:
            for i, chunk in enumerate(chunks[1:], 2):
                pr.create_issue_comment(f"### 📋 Matriz de Auditoría (Parte {i})\n{chunk}")

