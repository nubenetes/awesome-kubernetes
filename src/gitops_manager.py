import json
import base64
from github import Github
from datetime import datetime
from typing import List, Dict

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

    def apply_multi_file_changes(self, updates: dict, metrics: dict, safety_report: str = "") -> str:
        timestamp_slug = datetime.now().strftime("%Y%m%d-%H%M")
        branch_name = f"bot/knowledge-update-{timestamp_slug}"
        
        try:
            self._create_feature_branch(branch_name)
        except:
            branch_name = f"bot/knowledge-update-{timestamp_slug}-{id(updates)}"
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
        sorted_report = sorted(full_report, key=lambda x: 0 if x['status'] == 'INCLUDED' else (1 if x['status'] == 'DUPLICATE' else 2))
        
        counts = {"INCLUDED": 0, "DUPLICATE": 0, "FILTERED": 0}
        source_counts = {}
        all_rows = []
        
        header_table = "| # | Status | Score | Lang | Type | Date | Source | Reason | URL |\n| :--- | :--- | :---: | :---: | :--- | :---: | :--- | :--- | :--- |\n"
        
        for idx, item in enumerate(sorted_report, 1):
            status_emoji = {"INCLUDED": "✅", "DUPLICATE": "👯", "FILTERED": "🛡️"}.get(item['status'], "❓")
            date_str = str(item.get('post_date', 'N/A'))[:10] if item.get('post_date') else 'N/A'
            score = item.get('impact_score', 'N/A')
            lang = item.get('language', 'N/A')[:2].upper() if item.get('language') else 'EN'
            res_type = item.get('type', 'Ref')
            
            row = f"| {idx} | {status_emoji} {item['status']} | {score} | {lang} | {res_type} | {date_str} | {item.get('source', 'N/A')} | {item['reason']} | {item['url']} |\n"
            all_rows.append(row)
            
            counts[item['status']] = counts.get(item['status'], 0) + 1
            src = item.get('source', 'Unknown')
            source_counts[src] = source_counts.get(src, 0) + 1

        # AI Intel and Mermaid
        ai_intel = SESSION_TRACKER.get_intelligence_report()
        source_md = "#### 📊 Source Distribution\n| Source | Count |\n| :--- | :---: |\n"
        for src, count in sorted(source_counts.items(), key=lambda x: x[1], reverse=True):
            source_md += f"| {src} | {count} |\n"

        mermaid = f"### 📊 Decision Metrics\n```mermaid\npie title Agentic Decision Distribution\n    \"Accepted\" : {counts['INCLUDED']}\n    \"Duplicates\" : {counts['DUPLICATE']}\n    \"Filtered\" : {counts['FILTERED']}\n```\n"
        
        # Build PR Body (With Safety Guard Splitting)
        pr_body = f"## 💎 Knowledge Update: {datetime.now().strftime('%d %b %Y')}\n\nProcessed **{metrics.get('total_extracted', 0)}** links.\n\n"
        
        # If safety_report is huge, move it to its own comment
        safety_in_body = True
        if len(safety_report) > 30000:
            pr_body += "⚠️ **Detailed Safety Audit moved to comments due to scale.**\n\n"
            safety_in_body = False
        else:
            pr_body += f"{safety_report}\n\n"
            
        pr_body += f"{ai_intel}\n\n{mermaid}\n{source_md}\n---\n**Audit Matrix and Logs follow in successive comments.**\n"

        pr = self.repository.create_pull(
            title=f"💎 Knowledge Update & Optimization: {datetime.now().strftime('%d %b %Y')}",
            body=pr_body[:65000],
            head=branch_name,
            base=self.default_branch_name
        )

        # 1. Safety Report (if huge)
        if not safety_in_body:
            log_header = "## 🛡️ Safety & Mandate Audit (Detailed)\n"
            current_chunk = log_header
            for line in safety_report.splitlines():
                if len(current_chunk) + len(line) > 60000:
                    pr.create_issue_comment(current_chunk)
                    current_chunk = log_header + line + "\n"
                else:
                    current_chunk += line + "\n"
            pr.create_issue_comment(current_chunk)

        # 2. X.com Extraction Audit Trail
        x_audit = metrics.get('x_audit', [])
        if x_audit:
            log_header = "### 📜 Extraction Audit Trail\n*Detailed logs of social and RSS discovery attempts.*\n\n"
            current_log = log_header
            for entry in x_audit:
                if len(current_log) + len(entry) > 60000:
                    pr.create_issue_comment(current_log)
                    current_log = log_header + entry + "\n"
                else:
                    current_log += entry + "\n"
            pr.create_issue_comment(current_log)

        # 3. Split Audit Matrix into Comments
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
