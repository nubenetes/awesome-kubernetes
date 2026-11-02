import yaml
import os
import re

INVENTORY_PATH = "data/inventory.yaml"
VIDEOS_DIR = "v2-docs/videos"

def to_embed_url(url):
    if not url:
        return ""
    # If playlist
    if "playlist?list=" in url:
        match = re.search(r"[?&]list=([^&#]+)", url)
        if match:
            return f"https://www.youtube.com/embed/videoseries?list={match.group(1)}"
        return url
    
    video_id = None
    if "youtu.be/" in url:
        match = re.search(r"youtu\.be/([^?&#]+)", url)
        if match:
            video_id = match.group(1)
    elif "embed/" in url:
        return url
    else:
        match = re.search(r"[?&]v=([^&#]+)", url)
        if match:
            video_id = match.group(1)
            
    if video_id:
        list_match = re.search(r"[?&]list=([^&#]+)", url)
        t_match = re.search(r"[?&]t=([^&#]+)", url)
        params = []
        if list_match:
            params.append(f"list={list_match.group(1)}")
        if t_match:
            t_val = t_match.group(1)
            seconds = 0
            time_matches = re.findall(r"(\d+)(h|m|s)?", t_val)
            if time_matches:
                for val, unit in time_matches:
                    val_int = int(val)
                    if unit == "h":
                        seconds += val_int * 3600
                    elif unit == "m":
                        seconds += val_int * 60
                    else:
                        seconds += val_int
                params.append(f"start={seconds}")
            elif t_val.isdigit():
                params.append(f"start={t_val}")
        
        query_string = f"?{f'&'.join(params)}" if params else ""
        return f"https://www.youtube.com/embed/{video_id}{query_string}"
        
    return url

def extract_youtube_id(url):
    if not url:
        return None
    if "playlist?list=" in url or "list=" in url:
        return None
    video_id = None
    if "embed/" in url:
        match = re.search(r"embed/([^?&#]+)", url)
        if match:
            video_id = match.group(1)
    elif "youtu.be/" in url:
        match = re.search(r"youtu\.be/([^?&#]+)", url)
        if match:
            video_id = match.group(1)
    else:
        match = re.search(r"[?&]v=([^&#]+)", url)
        if match:
            video_id = match.group(1)
    return video_id

def get_target_file(category, technology):
    cat_lower = category.lower()
    tech_lower = technology.lower()

    if "agent" in tech_lower or "mcp" in tech_lower or "ai and future operations" in cat_lower or "llm" in tech_lower or "chatgpt" in tech_lower:
        return "ai-agents.md", "AI Agents and MCP"
    elif "mlops" in tech_lower or "data science" in cat_lower or "machine learning" in tech_lower:
        return "ai-agents.md", "AI Agents and MCP"
    elif "security" in cat_lower or "devsecops" in tech_lower or "zero trust" in tech_lower or "vulnerability" in tech_lower:
        return "devops-iac.md", "DevOps, IaC, and SRE"
    elif "infrastructure as code" in cat_lower or "observability" in cat_lower or "monitoring" in cat_lower or "devops" in tech_lower or "iac" in tech_lower or "sre" in tech_lower:
        return "devops-iac.md", "DevOps, IaC, and SRE"
    elif "terraform" in tech_lower or "ansible" in tech_lower or "pulumi" in tech_lower or "crossplane" in tech_lower:
        return "devops-iac.md", "DevOps, IaC, and SRE"
    elif "gitops" in tech_lower or "argo" in tech_lower or "flux" in tech_lower or "tekton" in tech_lower or "jenkins" in tech_lower or "cicd" in tech_lower:
        return "devops-iac.md", "DevOps, IaC, and SRE"
    elif "prometheus" in tech_lower or "grafana" in tech_lower or "opentelemetry" in tech_lower or "otel" in tech_lower:
        return "devops-iac.md", "DevOps, IaC, and SRE"
    elif "finops" in tech_lower or "cost" in tech_lower or "kubecost" in tech_lower:
        return "devops-iac.md", "DevOps, IaC, and SRE"
    elif "fundamentals" in cat_lower or "certification" in tech_lower or "cka" in tech_lower or "training" in cat_lower:
        return "fundamentals.md", "Fundamentals"
    elif "aws" in tech_lower or "azure" in tech_lower or "gcp" in tech_lower or "google cloud" in tech_lower:
        return "cloud-native.md", "Cloud Native Core"
    elif "openshift" in tech_lower or "red hat" in tech_lower or "rancher" in tech_lower:
        return "cloud-native.md", "Cloud Native Core"
    elif "vmware" in tech_lower or "proxmox" in tech_lower or "virtualization" in tech_lower:
        return "cloud-native.md", "Cloud Native Core"
    elif "docker" in tech_lower or "container" in tech_lower or "podman" in tech_lower:
        return "cloud-native.md", "Cloud Native Core"
    elif "python" in tech_lower or "golang" in tech_lower or "java" in tech_lower or "javascript" in tech_lower:
        return "fundamentals.md", "Fundamentals"
    else:
        return "cloud-native.md", "Cloud Native Core"

def generate_v2_videos():
    from src.inventory_manager import load_inventory
    inventory = load_inventory()

    featured_videos = []
    for url, entry in inventory.items():
        if entry.get("is_featured_video"):
            featured_videos.append({
                "url": to_embed_url(url),
                "title": entry.get("title", "YouTube Video"),
                "category": entry.get("category", "General"),
                "technology": entry.get("technology", "Cloud Native"),
                "summary": entry.get("ai_summary", entry.get("description", "")),
                "video_order": entry.get("video_order", 999),
                "year": entry.get("year", "N/A")
            })

    if not featured_videos:
        print("No featured videos found in inventory.")
        return

    # Delete old videos.md if it exists
    old_videos_file = "v2-docs/videos.md"
    if os.path.exists(old_videos_file):
        os.remove(old_videos_file)
        print(f"Removed legacy {old_videos_file}")

    os.makedirs(VIDEOS_DIR, exist_ok=True)

    # Helper functions
    def clean_header(text):
        t = re.sub(r'^\d+\.\s*', '', text)
        t = t.replace("&", "and")
        t = re.sub(r'[^a-zA-Z0-9\s-]', ' ', t)
        t = re.sub(r'\s+', ' ', t)
        return t.strip()

    def get_slug(text):
        t = clean_header(text).lower()
        t = re.sub(r'[^a-z0-9\s-]', '', t)
        t = re.sub(r'[\s-]+', '-', t)
        return t.strip('-')

    def is_spanish(title, summary):
        if "[SPANISH CONTENT]" in summary or "[SPANISH CONTENT]" in title:
            return True
        if title.strip().startswith("¿"):
            return True
        return False

    # Group videos by target file
    themed_videos = {}
    for v in featured_videos:
        filename, title = get_target_file(v["category"], v["technology"])
        if filename not in themed_videos:
            themed_videos[filename] = {"title": title, "videos": []}
        themed_videos[filename]["videos"].append(v)

    # Generate each themed MD file
    for filename, theme_info in themed_videos.items():
        theme_title = theme_info["title"]
        videos = theme_info["videos"]
        videos.sort(key=lambda x: x.get("video_order", 999))

        content = [
            f"# 🎥 {theme_title}",
            "",
            "!!! tip \"Nubenetes V2 Elite Portal\"",
            "    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/).",
            "",
            f"Welcome to the **{theme_title}** section of the V2 Video Hub. Explore curated high-density videos with architectural summaries.",
            ""
        ]

        # In-page Markdown Table of Contents intentionally omitted: it duplicates
        # Material's native right-column "On this page" TOC (toc.follow). We still
        # build the ordered technology list below because it drives the rendering
        # order of the grouped video sections.
        techs = []
        for v in videos:
            tech = v.get("technology", "Cloud Native")
            if tech not in techs:
                techs.append(tech)

        # Render Grouped Videos
        grouped_by_tech = {}
        for v in videos:
            tech = v.get("technology", "Cloud Native")
            if tech not in grouped_by_tech:
                grouped_by_tech[tech] = []
            grouped_by_tech[tech].append(v)

        for tech in techs:
            clean_tech = clean_header(tech)
            content.append(f"## {clean_tech}")
            content.append("")

            for v in grouped_by_tech[tech]:
                summary = v.get("summary", "").strip()
                # Replace bullet points starting with '* ' with '- ' to avoid markdownlint MD037 errors
                lines_sum = []
                for line in summary.splitlines():
                    line = re.sub(r'^(\s*)\*\s+', r'\1- ', line)
                    lines_sum.append(line)
                summary = "\n".join(lines_sum)
                indented_summary = summary.replace("\n", "\n        ")
                is_sp = is_spanish(v['title'], summary)
                lang_suffix = " [SPANISH CONTENT]" if is_sp else ""

                content.append(f"??? note \"🎬 {v['title']}{lang_suffix}\"")
                content.append(f"    !!! info \"Architectural Summary\"")
                content.append(f"        {indented_summary}")
                content.append("")
                content.append('    <center markdown="1">')
                content.append('')
                video_id = extract_youtube_id(v["url"])
                if video_id:
                    content.append(f'    <div class="video-lazy-container" data-video-id="{video_id}" data-video-url="{v["url"]}" style="position: relative; width: 720px; max-width: 100%; aspect-ratio: 16/9; background: #000; border-radius: 8px; overflow: hidden; cursor: pointer; border: 1px solid var(--md-typeset-table-color);">')
                    content.append(f'      <img src="https://img.youtube.com/vi/{video_id}/hqdefault.jpg" alt="{v["title"]}" class="video-lazy-thumbnail" style="width: 100%; height: 100%; object-fit: cover; opacity: 0.8; transition: opacity 0.3s, transform 0.3s;">')
                    content.append('      <div class="video-lazy-play-btn" style="position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%); width: 68px; height: 48px; background: rgba(0, 0, 0, 0.7); border-radius: 12px; display: flex; align-items: center; justify-content: center; transition: all 0.3s ease;">')
                    content.append('        <svg viewBox="0 0 24 24" style="width: 30px; height: 30px; fill: #fff; transition: fill 0.3s;"><path d="M8 5v14l11-7z"/></svg>')
                    content.append('      </div>')
                    content.append('    </div>')
                else:
                    content.append(f'    <iframe width="720" height="405" src="{v["url"]}" title="{v["title"]}" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen loading="lazy" style="border: 1px solid var(--md-typeset-table-color); border-radius: 8px;"></iframe>')
                content.append('')
                content.append('    </center>')
                content.append("")

        filepath = os.path.join(VIDEOS_DIR, filename)
        with open(filepath, "w") as f:
            f.write("\n".join(content))
        print(f"Generated {filepath} with {len(videos)} videos.")

    # Generate Overview page
    overview_content = [
        "# Agentic Video Hub",
        "",
        "!!! tip \"Nubenetes V2 Elite Portal\"",
        "    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/).",
        "",
        "Welcome to the **Nubenetes Elite Video Hub**. Discover highly-curated architectural video resources organized into logical learning paths:",
        "",
        "## Learning Dimensions",
        "",
        '<div style="display: flex; justify-content: center; gap: 24px; margin: 24px 0; flex-wrap: wrap;">',
        '  <a href="./ai-agents/" style="text-decoration: none; color: inherit; display: block; flex: 1; min-width: 250px; max-width: 270px;">',
        '    <div class="hero-badge-card hero-badge-card--purple" style="min-height: 240px; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 24px 16px;">',
        '      <span style="font-size: 3.5rem; margin-bottom: 12px; display: block;">🤖</span>',
        '      <div class="hero-badge-title" style="font-size: 1.05rem; font-weight: bold;">AI Agents and MCP</div>',
        '      <div class="hero-badge-subtitle" style="font-size: 0.78rem; margin-top: 8px; line-height: 1.4; color: var(--md-primary-fg-color--dark);">Dive into agentic architectures, tool integration, and Model Context Protocol setups.</div>',
        '    </div>',
        '  </a>',
        '  <a href="./devops-iac/" style="text-decoration: none; color: inherit; display: block; flex: 1; min-width: 250px; max-width: 270px;">',
        '    <div class="hero-badge-card hero-badge-card--cyan" style="min-height: 240px; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 24px 16px;">',
        '      <span style="font-size: 3.5rem; margin-bottom: 12px; display: block;">🛠️</span>',
        '      <div class="hero-badge-title" style="font-size: 1.05rem; font-weight: bold;">DevOps, IaC, and SRE</div>',
        '      <div class="hero-badge-subtitle" style="font-size: 0.78rem; margin-top: 8px; line-height: 1.4; color: var(--md-primary-fg-color--dark);">Platform engineering, infrastructure automation with Terraform, SRE, and compliance workflows utilizing AI assistants.</div>',
        '    </div>',
        '  </a>',
        '  <a href="./cloud-native/" style="text-decoration: none; color: inherit; display: block; flex: 1; min-width: 250px; max-width: 270px;">',
        '    <div class="hero-badge-card hero-badge-card--teal" style="min-height: 240px; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 24px 16px;">',
        '      <span style="font-size: 3.5rem; margin-bottom: 12px; display: block;">☁️</span>',
        '      <div class="hero-badge-title" style="font-size: 1.05rem; font-weight: bold;">Cloud Native Core</div>',
        '      <div class="hero-badge-subtitle" style="font-size: 0.78rem; margin-top: 8px; line-height: 1.4; color: var(--md-primary-fg-color--dark);">Architectural strategies, Kubernetes operations, networking, and MLOps platforms.</div>',
        '    </div>',
        '  </a>',
        '  <a href="./fundamentals/" style="text-decoration: none; color: inherit; display: block; flex: 1; min-width: 250px; max-width: 270px;">',
        '    <div class="hero-badge-card hero-badge-card--pink" style="min-height: 240px; display: flex; flex-direction: column; align-items: center; justify-content: center; padding: 24px 16px;">',
        '      <span style="font-size: 3.5rem; margin-bottom: 12px; display: block;">🏁</span>',
        '      <div class="hero-badge-title" style="font-size: 1.05rem; font-weight: bold;">Fundamentals</div>',
        '      <div class="hero-badge-subtitle" style="font-size: 0.78rem; margin-top: 8px; line-height: 1.4; color: var(--md-primary-fg-color--dark);">Documentaries, foundational cloud native concepts, and core Strategy tutorials.</div>',
        '    </div>',
        '  </a>',
        '</div>',
        "",
        "## Official Nubenetes NotebookLM Video Playlists",
        "",
        "Explore our curated AI-synthesized architectural masterclasses and podcasts on the official [**@nubenetes YouTube Channel**](https://www.youtube.com/@nubenetes/playlists):",
        "",
        "| Dimension | Curated Playlist | Focus Area |",
        "| :--- | :--- | :--- |",
        "| **IaC and Terraform** | [Nubenetes Azure Verified Modules (AVM) Terraform Labs](https://www.youtube.com/playlist?list=PLNKD2Ya-t0zM) | End-to-end Terraform AVM labs and modular patterns |",
        "| **Cloud Architecture** | [Nubenetes Azure Landing Zones 2026 Blueprint](https://www.youtube.com/playlist?list=PLCgDGrDt3kNU) | Enterprise CAF, AVM rebuild, and zero-secret OIDC CI/CD |",
        "| **FinOps and Cloud Cost** | [Nubenetes Azure Hybrid IaaS FinOps Framework](https://www.youtube.com/playlist?list=PLaNxiRbEBYJ8) | Rightsizing, Premium SSD v2, SQL core masking, and governance |",
        "| **FinOps and Kubernetes** | [Nubenetes Kubernetes Rightsizing and FinOps](https://www.youtube.com/playlist?list=PLZ-bpd1sEISs) | Container resource optimization and cluster cost efficiency |",
        "| **eBPF and Observability** | [Nubenetes Kubernetes and Multi-Cloud Observability with OpenTelemetry eBPF (OBI)](https://www.youtube.com/playlist?list=PLRTV86SuuRbk) | Zero-code kernel telemetry, eBPF maps, and trace-log correlation |",
        "| **Service Mesh** | [Nubenetes Istio Ambient Mesh and Gateway API on OpenShift](https://www.youtube.com/playlist?list=PLWGYAgXdQh44) | Sidecarless service mesh architecture and Kubernetes Gateway API |",
        "| **GitOps and CI/CD** | [Nubenetes ArgoCD and GitOps Automation](https://www.youtube.com/playlist?list=PLYbmzkhLGOtI) | Declarative GitOps delivery and Jenkins/ArgoCD automation |",
        "| **OpenShift and IAM** | [Nubenetes OpenShift 4.20 Installation (Day 0 to Day 2)](https://www.youtube.com/playlist?list=PLDbL5Dh24a5g) | Enterprise OpenShift lifecycle, Keycloak IAM, and OAuth2/OIDC |",
        "| **Podcasts (EN / ES)** | [Cloud Native Podcasts (English)](https://www.youtube.com/playlist?list=PLBMAtCXWYfZA) · [Podcasts (Español)](https://www.youtube.com/playlist?list=PLB-3xSV3dAoU) | Bilingual NotebookLM audio/video deep-dives across all dimensions |",
    ]

    # Dynamically append any newly discovered @nubenetes playlists from inventory
    known_playlist_ids = {
        "PLNKD2Ya-t0zM", "PLCgDGrDt3kNU", "PLaNxiRbEBYJ8", "PLZ-bpd1sEISs",
        "PLRTV86SuuRbk", "PLWGYAgXdQh44", "PLYbmzkhLGOtI", "PLDbL5Dh24a5g",
        "PLBMAtCXWYfZA", "PLB-3xSV3dAoU",
    }
    for url, entry in inventory.items():
        if not isinstance(entry, dict):
            continue
        if "playlist?list=" in url and (entry.get("company") == "Nubenetes" or "nubenetes" in str(entry.get("source_provenance", "")).lower()):
            m_pl = re.search(r"[?&]list=([^&#]+)", url)
            pl_id = m_pl.group(1) if m_pl else ""
            if pl_id and pl_id not in known_playlist_ids:
                known_playlist_ids.add(pl_id)
                dim_label = clean_header(str(entry.get("technology") or entry.get("category") or "Cloud Native"))
                pl_title = str(entry.get("title") or "Nubenetes Playlist").replace("|", "-")
                pl_summary = str(entry.get("ai_summary") or entry.get("description") or "").splitlines()[0][:110].replace("|", "-")
                overview_content.append(f"| **{dim_label}** | [{pl_title}]({url}) | {pl_summary} |")

    overview_content.append("")
    with open(os.path.join(VIDEOS_DIR, "index.md"), "w") as f:
        f.write("\n".join(overview_content))
    print(f"Generated {VIDEOS_DIR}/index.md")

    # Update MkDocs Nav
    update_mkdocs_nav()

def update_mkdocs_nav():
    mkdocs_path = "v2-mkdocs.yml"
    if not os.path.exists(mkdocs_path):
        return
    with open(mkdocs_path, "r") as f:
        content = f.read()

    # Match exact entry and replace with nested list
    old_entry = '- "Agentic Video Hub": videos.md'
    new_entry = """- "Agentic Video Hub":
      - "Overview": videos/index.md
      - "AI Agents and MCP": videos/ai-agents.md
      - "DevOps, IaC, and SRE": videos/devops-iac.md
      - "Cloud Native Core": videos/cloud-native.md
      - "Fundamentals": videos/fundamentals.md"""

    if old_entry in content:
        content = content.replace(old_entry, new_entry)
        with open(mkdocs_path, "w") as f:
            f.write(content)
        print("Updated v2-mkdocs.yml navigation.")
    else:
        print("v2-mkdocs.yml navigation is already updated or entry not found.")

if __name__ == "__main__":
    generate_v2_videos()
