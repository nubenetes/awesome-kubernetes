import os
import re
import subprocess
import yaml
from datetime import datetime
from src.config import INVENTORY_PATH

# Unified Path Config
V1_DIR = "docs"
V2_DIR = "v2-docs"

def run_command(cmd):
    try:
        return subprocess.check_output(cmd, shell=True).decode('utf-8').strip()
    except: return "0"

def clean_text(text: str) -> str:
    """Strips emojis and ampersands for README compatibility."""
    if not text: return ""
    text = text.replace("&", "and")
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text) # Strip emojis
    return text.strip()

def get_stats():
    # 1. Load Inventory (The Source of Truth)
    inventory = {}
    if os.path.exists(INVENTORY_PATH):
        try:
            with open(INVENTORY_PATH, "r") as f:
                inventory = yaml.safe_load(f) or {}
        except: pass

    # 2. Basic Metrics
    total_links = len([u for u in inventory.keys() if not u.startswith("INTRO:")])
    md_pages = len([f for f in os.listdir(V1_DIR) if f.endswith(".md")])
    total_commits = run_command("git rev-list --count HEAD")
    
    # 3. Density Map (Links per category)
    category_counts = {}
    for url, meta in inventory.items():
        if url.startswith("INTRO:"): continue
        cat = meta.get("category", "uncategorized")
        category_counts[cat] = category_counts.get(cat, 0) + 1

    # Top 10 Table
    top_10 = sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:10]
    top_categories_rows = []
    for name, count in top_10:
        display_name = clean_text(name.replace('-', ' ').title())
        top_categories_rows.append(f"| [{display_name}](docs/{name}.md) | {count} |")

    # 4. Strategic Dimension Mapping (Sync with V2 Optimizer)
    DIMENSIONS = {
        "AI and Artificial Intelligence": ["ai", "ai-agents-mcp", "chatgpt", "mlops"],
        "Architectural Foundations": ["introduction", "faq", "kubernetes", "linux", "git", "cloud-arch-diagrams", "matrix-table", "other-awesome-lists", "about"],
        "Platform & Site Reliability": ["sre", "devops", "developerportals", "scaffolding", "finops", "chaos-engineering", "performance-testing-with-jenkins-and-jmeter", "project-management-methodology", "project-management-tools", "qa", "test-automation-frameworks", "testops"],
        "Hardened Infrastructure": ["iac", "terraform", "pulumi", "crossplane", "ansible", "securityascode", "kubernetes-security", "aws-security", "oauth", "devsecops", "kustomize", "liquibase", "chef"],
        "Cloud Providers": ["aws", "azure", "GoogleCloudPlatform", "ibm_cloud", "oraclecloud", "digitalocean", "cloudflare", "scaleway", "managed-kubernetes-in-public-cloud", "public-cloud-solutions", "private-cloud-solutions", "edge-computing"],
        "Container Stack": ["docker", "container-managers", "serverless", "kubernetes-autoscaling", "kubernetes-operators-controllers", "kubernetes-storage", "kubernetes-monitoring", "kubernetes-troubleshooting", "kubernetes-backup-migrations", "kubernetes-on-premise", "kubernetes-bigdata", "kubernetes-client-libraries", "kubernetes-releases", "kubernetes-based-devel", "kubernetes-alternatives", "kubectl-commands", "rancher", "openshift", "ocp3", "ocp4", "noops"],
        "Data & Analytics": ["databases", "nosql", "newsql", "message-queue", "crunchydata", "yaml", "bigdata"],
        "Engineering Pipeline": ["cicd", "gitops", "argo", "flux", "tekton", "jenkins", "jenkins-alternatives", "openshift-pipelines", "sonarqube", "registries", "keptn", "stackstorm", "cicd-kubernetes-plugins"]
    }

    pillar_totals = {k: 0 for k in DIMENSIONS.keys()}
    pillar_totals["Specialized Topics"] = 0
    assigned_cats = [c for sublist in DIMENSIONS.values() for c in sublist]
    
    for c, count in category_counts.items():
        found = False
        for p_name, cats in DIMENSIONS.items():
            if c in cats:
                pillar_totals[p_name] += count
                found = True; break
        if not found:
            pillar_totals["Specialized Topics"] += count

    pillar_chart = "pie title Nubenetes Major Ecosystem Pillars\n"
    for p, val in sorted(pillar_totals.items(), key=lambda x: x[1], reverse=True):
        if val > 0: pillar_chart += f"    \"{p}\" : {val}\n"

    # 5. Language Diversity (Mandate 10)
    lang_counts = {}
    for url, meta in inventory.items():
        if url.startswith("INTRO:"): continue
        lang = meta.get("language", "English")
        lang_counts[lang] = lang_counts.get(lang, 0) + 1
    
    lang_chart = "pie title Linguistic Diversity (Global Access)\n"
    for lang, val in sorted(lang_counts.items(), key=lambda x: x[1], reverse=True)[:6]:
        lang_chart += f"    \"{lang}\" : {val}\n"

    # 6. Annual Growth
    annual_raw = run_command("git log --format='%ad' --date=format:'%Y' | sort | uniq -c")
    annual_rows = []
    milestones = {
        "2018": "**Munich Era (BMW IT-Zentrum)**",
        "2019": "Early Growth & Open Source Launch",
        "2020": "**The Great Expansion**",
        "2021": "Maturity & Standardization",
        "2022": "Cloud Native Hardening",
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

    # 7. Monthly Surge (2026)
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
        "lang_chart": lang_chart,
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

    # Replace specialized sub-chart with Language Chart (More useful for 2026)
    content = re.sub(
        r"#### 2. Deep Dive: Specialized Sub-ecosystems\nTo better.*?\n\n```mermaid\npie title Deep Dive: Specialized Sub-ecosystems\n.*?```",
        f"#### 2. Global Linguistic Diversity\nReflecting Nubenetes' mission of global access while maintaining technical English as the primary interface.\n\n```mermaid\n{stats['lang_chart']}```",
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
    print(f"README.md updated successfully with database-driven metrics.")
