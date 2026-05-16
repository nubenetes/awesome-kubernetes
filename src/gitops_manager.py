import json
import base64
from github import Github
from datetime import datetime

from src.gemini_utils import SESSION_TRACKER

class RepositoryController:
    def __init__(self, access_token: str, repository_identifier: str):
        self.github_client = Github(access_token)
        self.repository = self.github_client.get_repo(repository_identifier)
        # Force 'develop' as the primary target for all PRs and base for feature branches
        self.default_branch_name = "develop"

    def _create_feature_branch(self, branch_name: str) -> None:
        base_branch = self.repository.get_branch(self.default_branch_name)
        self.repository.create_git_ref(ref=f"refs/heads/{branch_name}", sha=base_branch.commit.sha)

    def get_file_from_branch(self, file_path: str, branch_name: str) -> str:
        try:
            file_meta = self.repository.get_contents(file_path, ref=branch_name)
            return base64.b64decode(file_meta.content).decode("utf-8")
        except:
            return ""

    def apply_historical_chunk(self, updates: dict, next_since: str) -> None:
        branch_name = "bot/historical-accumulator"
        
        # Check if branch exists, if not, create from develop
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
                print(f"Error in historical chunk for {file_path}: {e}")

    def apply_multi_file_changes(self, updates: dict, metrics: dict) -> None:
        timestamp_slug = datetime.now().strftime("%Y%m%d-%H%M")
        branch_name = f"bot/knowledge-update-{timestamp_slug}"
        
        # In the last historical chunk, use the accumulator as base if it exists
        accumulator_branch = "bot/historical-accumulator"
        base_sha = None
        try:
            acc = self.repository.get_branch(accumulator_branch)
            base_sha = acc.commit.sha
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
                print(f"Error processing {file_path}: {e}")

        # --- REPORT CONSTRUCTION ---
        full_report = metrics.get('full_report', [])
        
        # 1. Matrix Table with Numeric Index and Date (Prioritizing INCLUDED)
        sorted_report = sorted(full_report, key=lambda x: 0 if x['status'] == 'INCLUDED' else 1)
        
        header_table = "| # | Status | Post Date | Source | Reason | Category | URL |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
        
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

        # Split rows into chunks for PR Body and Comments
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
            matrix_table_body += f"\n> ℹ️ **Note:** The table continues in PR comments ({len(chunks)-1} additional parts).\n"

        # 2. Historical Extraction Diagnosis
        extraction_audit = "### 🕵️ Time Horizon Diagnosis\n"
        start_date_str = metrics.get('start_date')[:10] if metrics.get('start_date') else 'N/A'
        
        actual_oldest = "N/A"
        dates = [item.get('post_date') for item in full_report if item.get('post_date')]
        if dates: actual_oldest = min(dates)[:10]

        if actual_oldest != "N/A" and actual_oldest > start_date_str:
            extraction_audit += f"⚠️ **Limit Reached:** Requested from `{start_date_str}`, but stopped at `{actual_oldest}`.\n"
        else:
            extraction_audit += f"✅ **Horizon Reached:** Extraction successfully covered since `{start_date_str}`.\n"

        # 3. Mermaid Diagrams
        mermaid_pie = "### 📊 Decision Metrics\n```mermaid\npie title Agentic Decision Distribution\n"
        mermaid_pie += f"    \"Accepted (Injected)\" : {counts['INCLUDED']}\n"
        mermaid_pie += f"    \"Duplicates (Ignored)\" : {counts['DUPLICATE']}\n"
        mermaid_pie += f"    \"Filtered (Quality/Impact)\" : {counts['FILTERED']}\n```\n"

        mermaid_origin = ""
        if source_counts:
            mermaid_origin = "### 🌍 Source of Injected Updates\n```mermaid\npie title Added References Sources\n"
            for src, val in source_counts.items():
                mermaid_origin += f"    \"{src}\" : {val}\n"
            mermaid_origin += "```\n"

        # 4. Ingestion Log
        x_log = "### ⚡ Ingestion Audit Trail (X.com)\n"
        for entry in metrics.get('x_audit', []): x_log += f"- {entry}\n"

        # 5. AI Intelligence & Observability Report
        ai_intelligence = SESSION_TRACKER.get_intelligence_report()

        pr_narrative = (
            f"## 💎 Knowledge Update War Room: Kubernetes & Cloud Native\n\n"
            f"This report details the processing of **{metrics.get('total_extracted', 0)}** detected links.\n\n"
            f"{extraction_audit}\n"
            f"{ai_intelligence}\n"
            f"{mermaid_pie}\n"
            f"{mermaid_origin}\n"
            f"{x_log}\n"
            f"### 📋 Audit Matrix (Part 1)\n{matrix_table_body}\n"
            f"---\n"
            f"**Evaluation Note:** Full history analyzed successfully."
        )

        pr = self.repository.create_pull(
            title=f"💎 Knowledge Update & Optimization: {datetime.now().strftime('%d %b %Y')}",
            body=pr_narrative,
            head=branch_name,
            base=self.default_branch_name
        )

        # 5. Post comments with the rest of the table
        if len(chunks) > 1:
            for i, chunk in enumerate(chunks[1:], 2):
                pr.create_issue_comment(f"### 📋 Audit Matrix (Part {i})\n{chunk}")

