import os
import re
import subprocess
import yaml
from datetime import datetime

# Grouping definitions for Major Pillars
PILLARS = {
    "Kubernetes Ecosystem": ["kubernetes", "kubernetes-tools", "kubernetes-security", "kubernetes-networking", "kubernetes-monitoring", "kubernetes-storage", "kubernetes-operators-controllers", "kubernetes-autoscaling", "kubectl-commands"],
    "Developer Ecosystem": ["visual-studio", "javascript", "golang", "python", "java_frameworks", "react", "angular", "dotnet", "api", "linux-dev-env"],
    "Public/Private Cloud": ["aws", "azure", "GoogleCloudPlatform", "openshift", "rancher", "digitalocean", "managed-kubernetes-in-public-cloud"],
    "CI/CD and GitOps": ["cicd", "gitops", "argo", "flux", "tekton", "jenkins", "jenkins-alternatives"],
    "Infra as Code": ["iac", "terraform", "pulumi", "crossplane", "ansible"],
    "SRE and Observability": ["sre", "monitoring", "grafana", "prometheus", "chaos-engineering"],
    "Security and DevSecOps": ["securityascode", "devsecops", "oauth"]
}

def run_command(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
    except: return "0"

def get_stats():
    # 1. Total Links
    total_links = run_command("grep -oP '\\[.*?\\]\\(http.*?\\)' docs/*.md | wc -l")
    
    # 2. MD Pages
    md_pages = run_command("ls docs/*.md | wc -l")
    
    # 3. Total Commits
    total_commits = run_command("git rev-list --count HEAD")
    
    # 4. Density Map (All categories)
    category_counts = {}
    files = [f for f in os.listdir("docs") if f.endswith(".md") and f != "index.md"]
    for f in files:
        count = int(run_command(f"grep -oP '\\[.*?\\]\\(http.*?\\)' docs/{f} | wc -l"))
        name = f.replace(".md", "")
        category_counts[name] = count

    # Sort for Top 10 Table
    top_10 = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    top_categories_rows = []
    for name, count in top_10:
        display_name = name.replace('-', ' ').title()
        top_categories_rows.append(f"| [{display_name}](docs/{name}.md) | {count} |")

    # 5. Major Pillars Chart
    pillar_totals = {k: 0 for k in PILLARS.keys()}
    pillar_totals["Others (Specialized)"] = 0
    assigned_cats = []
    for p_name, cats in PILLARS.items():
        for c in cats:
            pillar_totals[p_name] += category_counts.get(c, 0)
            assigned_cats.append(c)
    
    for c, count in category_counts.items():
        if c not in assigned_cats:
            pillar_totals["Others (Specialized)"] += count

    pillar_chart = "pie title Nubenetes Major Ecosystem Pillars\n"
    for p, val in pillar_totals.items():
        if val > 0: pillar_chart += f"    \"{p}\" : {val}\n"

    # 6. Specialized Sub-ecosystems Chart
    sub_ecosystems = {
        "Databases (SQL/NoSQL)": ["databases", "nosql", "newsql", "crunchydata", "liquibase"],
        "AI and Agentic Systems": ["ai", "ai-agents-mcp", "chatgpt"],
        "Demos and Boilerplates": ["demos"],
        "Web Servers and Runtimes": ["web-servers", "caching", "java_app_servers"],
        "Message Queues and Data": ["message-queue", "bigdata"],
        "Career and Recruitment": ["recruitment", "hr", "freelancing", "remote-tech-jobs"],
        "Linux and OS Hardening": ["linux"]
    }
    sub_totals = {k: 0 for k in sub_ecosystems.keys()}
    sub_assigned = []
    for s_name, cats in sub_ecosystems.items():
        for c in cats:
            sub_totals[s_name] += category_counts.get(c, 0)
            sub_assigned.append(c)
    
    # Calculate "Others" for sub-chart (relative to assigned cats)
    sub_totals["Others (100+ Topics)"] = sum(category_counts.values()) - sum(sub_totals.values())

    sub_chart = "pie title Deep Dive: Specialized Sub-ecosystems\n"
    for s, val in sub_totals.items():
        if val > 0: sub_chart += f"    \"{s}\" : {val}\n"

    # 7. Annual Growth
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
            parts = line.strip().split(' ')
            if len(parts) >= 2:
                count, year = parts[0], parts[1]
                est_refs = int(int(count) * 4.13)
                milestone = milestones.get(year, "Continuing Evolution")
                annual_rows.append(f"| {year} | {count} | {est_refs:,} | {milestone} |")

    # 8. Monthly Surge (2026)
    monthly_raw = run_command("git log --format='%ad' --date=format:'%Y-%m' | grep '2026' | sort | uniq -c")
    monthly_rows = []
    for line in monthly_raw.split('\n'):
        if line:
            parts = line.strip().split(' ')
            if len(parts) >= 2:
                count, month = parts[0], parts[1]
                est_refs = int(int(count) * 4.13)
                status = "**Agentic Inception (Gemini Era)**" if month == "2026-05" else "Active Curation"
                monthly_rows.append(f"| {month} | {count} | {est_refs:,} | {status} |")

    return {
        "total_links": total_links,
        "md_pages": md_pages,
        "total_commits": total_commits,
        "top_categories": "\n".join(top_categories_rows),
        "pillar_chart": pillar_chart,
        "sub_chart": sub_chart,
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

    # Update Pillar Chart
    content = re.sub(
        r"```mermaid\npie title Nubenetes Major Ecosystem Pillars\n.*?```",
        f"```mermaid\n{stats['pillar_chart']}```",
        content,
        flags=re.DOTALL
    )

    # Update Sub Ecosystem Chart
    content = re.sub(
        r"```mermaid\npie title Deep Dive: Specialized Sub-ecosystems\n.*?```",
        f"```mermaid\n{stats['sub_chart']}```",
        content,
        flags=re.DOTALL
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
    print(f"README.md updated successfully with latest metrics (Links: {stats['total_links']}).")
