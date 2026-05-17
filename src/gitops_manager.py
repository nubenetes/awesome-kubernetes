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

    def apply_multi_file_changes(self, updates: dict, metrics: dict, safety_report: str = "") -> str:
        timestamp_slug = datetime.now().strftime("%Y%m%d-%H%M")
        branch_name = f"bot/knowledge-update-{timestamp_slug}"
        
        # In the last historical chunk, use the accumulator as base if it exists
        accumulator_branch = "bot/historical-accumulator"
        try:
            acc = self.repository.get_branch(accumulator_branch)
            self.repository.create_git_ref(ref=f"refs/heads/{branch_name}", sha=acc.commit.sha)
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
                    file_meta = self.repository.get_contents(file_path, ref=branch_name)
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
        sorted_report = sorted(full_report, key=lambda x: 0 if x['status'] == 'INCLUDED' else 1)
        
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

        # 1. Mermaid Diagrams & Stats
        ai_intel = SESSION_TRACKER.get_intelligence_report()
        mermaid = f"### 📊 Decision Metrics\n```mermaid\npie title Agentic Decision Distribution\n    \"Accepted\" : {counts['INCLUDED']}\n    \"Duplicates\" : {counts['DUPLICATE']}\n    \"Filtered\" : {counts['FILTERED']}\n```\n"
        
        pr_body = (
            f"## 💎 Knowledge Update: {datetime.now().strftime('%d %b %Y')}\n\n"
            f"Processed **{metrics.get('total_extracted', 0)}** links.\n\n"
            f"{safety_report}\n\n"
            f"{ai_intel}\n\n"
            f"{mermaid}\n"
            f"---\n"
            f"**Audit Matrix follows in comments due to scale.**\n"
        )

        pr = self.repository.create_pull(
            title=f"💎 Knowledge Update & Optimization: {datetime.now().strftime('%d %b %Y')}",
            body=pr_body[:65000],
            head=branch_name,
            base=self.default_branch_name
        )

        # 2. Split Audit Matrix into Comments
        header_table = "| # | Status | Date | Source | Reason | Category | URL |\n| :--- | :--- | :--- | :--- | :--- | :--- | :--- |\n"
        current_comment = header_table
        part = 1
        for row in all_rows:
            if len(current_comment) + len(row) > 60000:
                pr.create_issue_comment(f"### 📋 Audit Matrix (Part {part})\n{current_comment}")
                current_comment = header_table + row
                part += 1
            else:
                current_comment += row
        pr.create_issue_comment(f"### 📋 Audit Matrix (Part {part})\n{current_comment}")

        return pr.html_url
