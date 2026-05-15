import os
import re
import subprocess
from datetime import datetime

def run_command(cmd):
    return subprocess.check_output(cmd, shell=True).decode('utf-8').strip()

def get_stats():
    # 1. Total Links
    total_links = run_command("grep -oP '\\[.*?\\]\\(http.*?\\)' docs/*.md | wc -l")
    
    # 2. MD Pages
    md_pages = run_command("ls docs/*.md | wc -l")
    
    # 3. Total Commits
    total_commits = run_command("git rev-list --count HEAD")
    
    # 4. Top Categories
    top_categories_raw = run_command("find docs/ -name '*.md' -exec bash -c \"echo -n '{}: ' && grep -oP '\\[.*?\\]\\(http.*?\\)' '{}' | wc -l\" \\; | sort -n -k 2 -r | head -n 10")
    top_categories = []
    for line in top_categories_raw.split('\n'):
        if line:
            path, count = line.split(': ')
            name = path.replace('docs/', '').replace('.md', '').replace('-', ' ').title()
            top_categories.append(f"| [{name}]({path}) | {count} |")

    # 5. Annual Growth
    annual_raw = run_command("git log --format='%ad' --date=format:'%Y' | sort | uniq -c")
    annual_rows = []
    milestones = {
        "2018": "**Munich Era (BMW IT-Zentrum)**",
        "2019": "Early Growth & Open Source Launch",
        "2020": "**The Great Expansion** (Global Lockdowns)",
        "2021": "Maturity & Industry Standardization",
        "2022": "Cloud Native Hardening & GitOps Era",
        "2023": "Maintenance & Refinement",
        "2024": "Curation Strategy Pivot",
        "2025": "Stability & Research Phase",
        "2026": "**Agentic AI Surge** (May 2026 Inception)"
    }
    for line in annual_raw.split('\n'):
        if line:
            count, year = line.strip().split(' ')
            est_refs = int(int(count) * 4.13)
            milestone = milestones.get(year, "Continuing Evolution")
            annual_rows.append(f"| {year} | {count} | {est_refs:,} | {milestone} |")

    # 6. Monthly Surge (2026)
    monthly_raw = run_command("git log --format='%ad' --date=format:'%Y-%m' | grep '2026' | sort | uniq -c")
    monthly_rows = []
    for line in monthly_raw.split('\n'):
        if line:
            count, month = line.strip().split(' ')
            est_refs = int(int(count) * 4.13)
            status = "**Agentic Inception (Gemini Era)**" if month == "2026-05" else "Active Curation"
            monthly_rows.append(f"| {month} | {count} | {est_refs:,} | {status} |")

    return {
        "total_links": total_links,
        "md_pages": md_pages,
        "total_commits": total_commits,
        "top_categories": "\n".join(top_categories),
        "annual_rows": "\n".join(annual_rows),
        "monthly_rows": "\n".join(monthly_rows),
        "last_update": datetime.now().strftime("%Y-%m-%d")
    }

def update_readme(stats):
    with open("README.md", "r") as f:
        content = f.read()

    # Update Heart Table
    content = re.sub(
        r"\| \*\*Total Technical Resources \(Links\)\*\* \| \*\*.*?\*\* \|",
        f"| **Total Technical Resources (Links)** | **{stats['total_links']}+** |",
        content
    )
    content = re.sub(
        r"\| \*\*Specialized MD Pages\*\* \| \*\*.*?\*\* \|",
        f"| **Specialized MD Pages** | **{stats['md_pages']}** |",
        content
    )
    content = re.sub(
        r"\| \*\*Total Commits\*\* \| \*\*.*?\*\* \|",
        f"| **Total Commits** | **{stats['total_commits']}+** |",
        content
    )
    content = re.sub(
        r"Stats as of .*?\)",
        f"Stats as of {stats['last_update']})",
        content
    )

    # Update Top Categories Table
    categories_header = "| Category (Markdown Page) | Total Links |\n| :--- | :---: |"
    content = re.sub(
        r"\| Category \(Markdown Page\) \| Total Links \|\n\| :--- \| :---: \|\n(?:\| .*? \| .*? \|\n?)*",
        f"{categories_header}\n{stats['top_categories']}\n",
        content
    )

    # Update Annual Growth Table
    annual_header = "| Year | Commits | Est. New Refs | Key Milestone |\n| :---: | :---: | :---: | :--- |"
    content = re.sub(
        r"\| Year \| Commits \| Est\. New Refs \| Key Milestone \|\n\| :---: \| :---: \| :---: \| :--- \|\n(?:\| .*? \| .*? \| .*? \| .*? \|\n?)*",
        f"{annual_header}\n{stats['annual_rows']}\n",
        content
    )

    # Update Monthly Surge Table
    monthly_header = "| Month | Commits | Est. New Refs | Status |\n| :--- | :---: | :---: | :--- |"
    content = re.sub(
        r"\| Month \| Commits \| Est\. New Refs \| Status \|\n\| :--- \| :---: \| :---: \| :--- \|\n(?:\| .*? \| .*? \| .*? \| .*? \|\n?)*",
        f"{monthly_header}\n{stats['monthly_rows']}\n",
        content
    )

    with open("README.md", "w") as f:
        f.write(content)

if __name__ == "__main__":
    stats = get_stats()
    update_readme(stats)
    print("README.md updated successfully with latest metrics.")
