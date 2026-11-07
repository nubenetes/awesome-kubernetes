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
        match = re.search(r"youtu\.be/([^?&#/]+)", url)
        if match:
            video_id = match.group(1)
    elif "/shorts/" in url:
        match = re.search(r"/shorts/([^?&#/]+)", url)
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
        match = re.search(r"embed/([^?&#/]+)", url)
        if match:
            video_id = match.group(1)
    elif "/shorts/" in url:
        match = re.search(r"/shorts/([^?&#/]+)", url)
        if match:
            video_id = match.group(1)
    elif "youtu.be/" in url:
        match = re.search(r"youtu\.be/([^?&#/]+)", url)
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
        grouped_by_tech = {}
        for v in videos:
            raw_tech = v.get("technology", "Cloud Native")
            clean_tech = clean_header(raw_tech) or "Cloud Native"
            if clean_tech not in techs:
                techs.append(clean_tech)
                grouped_by_tech[clean_tech] = []
            grouped_by_tech[clean_tech].append(v)

        for clean_tech in techs:
            content.append(f"## {clean_tech}")
            content.append("")

            for v in grouped_by_tech[clean_tech]:
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
        "| **Enterprise AI Platforms** | [Nubenetes Enterprise AI Platforms: Cloud AI Control Planes vs Kubernetes](https://www.youtube.com/playlist?list=PLBZl7QsgYjrw) | Architectural reference comparison matrix and production engineering deep-dive on Enterprise AI Platforms: Managed Cloud AI Control Planes (Azure AI Foundry, Bedrock AgentCore, Vertex AI) vs Turnkey Kubernetes (Red Hat OpenShift AI, watsonx, llm-d, vLLM, Kueue, KAITO), zero-trust Agent IAM (Entra Agent ID), and the 2026 Hybrid Reference Architecture. |",
        "| **IaC and Terraform** | [Nubenetes Azure Verified Modules (AVM) Terraform Labs](https://www.youtube.com/playlist?list=PLNKD2Ya-t0zM) | Hands-on Terraform AVM implementation labs: VS Code/Azure CLI toolchain, Log Analytics sinks, Key Vault secrets, Storage CMK encryption, Private Endpoints, Azure Bastion zero-public-IP access, and Managed Identity RBAC. |",
        "| **Cloud Architecture** | [Nubenetes Azure Landing Zones 2026: Enterprise CAF and Architecture Blueprint](https://www.youtube.com/playlist?list=PLCgDGrDt3kNU) | Enterprise CAF reference architecture: retiring the legacy CAF monolith in favor of AVM and ALZ Library (2026.10.0), Management Groups, Hub-Spoke vs. Virtual WAN, Private Endpoints, and zero-secret OIDC CI/CD. |",
        "| **FinOps and Cloud Cost** | [Nubenetes Azure Hybrid IaaS FinOps Framework](https://www.youtube.com/playlist?list=PLaNxiRbEBYJ8) | Mathematical break-even decision models and continuous automation for Azure IaaS: Azure Hybrid Benefit (AHUB), Constrained vCPUs, Premium SSD v2 decoupling, and AMA/DCR edge log filtering. |",
        "| **FinOps and Kubernetes** | [Nubenetes Kubernetes Rightsizing and FinOps](https://www.youtube.com/playlist?list=PLZ-bpd1sEISs) | Pod failure analysis, container CPU/memory resource optimization, VPA/Goldilocks strategies, and AI-driven workload rightsizing for Kubernetes clusters. |",
        "| **Storage Compliance and IaC** | [Nubenetes Azure Storage WORM and ERP Compliance (Spain Central)](https://www.youtube.com/playlist?list=PLc2WtEw1pojo) | Immutable WORM storage architecture on Azure Blob Storage (Terraform, Bicep, Ansible) in Spain Central for Commercial Code Art. 30, Anti-Fraud Law 11/2021, and VeriFactu compliance with 75%+ FinOps lifecycle savings. [SPANISH CONTENT] |",
        "| **Zero-Trust IAM and OIDC** | [Nubenetes OAuth2, OIDC and Entra ID Identity on Azure](https://www.youtube.com/playlist?list=PLcCUAwooFb6s) | OAuth 2.0, OpenID Connect (OIDC), Microsoft Entra ID App Registrations, On-Behalf-Of (OBO) token exchange, Workload Identity Federation, and secretless zero-trust governance with Terraform. |",
        "| **Keycloak and Enterprise IAM** | [Nubenetes Keycloak and RHBK Enterprise IAM on OpenShift](https://www.youtube.com/playlist?list=PLUt4PJvFTysY) | Enterprise identity architecture, Red Hat Build of Keycloak (RHBK), OAuth 2.1, OIDC federation, and multi-region high-availability replication on OpenShift. |",
        "| **Red Hat OpenShift** | [Nubenetes OpenShift 4.20 Installation (Day 0 to Day 2)](https://www.youtube.com/playlist?list=PLDbL5Dh24a5g) | End-to-end OpenShift 4.20 lifecycle across bare metal, VMware, Nutanix, and Hyper-V: ABI/IPI/UPI installers, SNO, HyperShift (HCP), ZTP, air-gapped mirroring, Day 1 hardening, etcd recovery, and OADP. |",
        "| **OpenShift Modernization** | [Nubenetes OpenShift Legacy Java and Air-Gapped Migration](https://www.youtube.com/playlist?list=PLOb7y_S6Kcd8) | Air-gapped OpenShift architectures, legacy J2EE lift-and-shift container modernization, and zero-trust database routing in disconnected environments. |",
        "| **Service Mesh and Gateway API** | [Nubenetes Istio Ambient Mesh and Gateway API on OpenShift](https://www.youtube.com/playlist?list=PLWGYAgXdQh44) | Red Hat OpenShift Service Mesh 3.0 (OSSM 3), Istio Ambient Mesh sidecarless zero-trust networking with Rust ztunnel (HBONE mTLS), L7 Waypoint proxies, and Kubernetes Gateway API across 12 enterprise scenarios. |",
        "| **eBPF and Service Mesh** | [Nubenetes Service Mesh vs. Kernel eBPF (OBI)](https://www.youtube.com/playlist?list=PLI0K_-6LrXgM) | Architectural comparison and production synergies between Service Meshes (Istio Ambient, Envoy, Cilium Mesh) and Kernel-level eBPF Instrumentation (OpenTelemetry OBI) for zero-code trace-log correlation. |",
        "| **eBPF and Observability** | [Nubenetes Kubernetes and Multi-Cloud Observability with OpenTelemetry eBPF (OBI)](https://www.youtube.com/playlist?list=PLRTV86SuuRbk) | Multi-cloud Kubernetes observability blueprints with OpenTelemetry eBPF (OBI), multi-backend Collector routing, tail-based sampling (80%-95% cost reduction), and Grafana LGTM stack integration. |",
        "| **eBPF Kernel Telemetry** | [Nubenetes eBPF Metrics and Telemetry: Kernel Maps, OBI and Prometheus](https://www.youtube.com/playlist?list=PLZhOsH66dFmw) | Zero-code RED metrics (Golden Signals), Linux kernel socket probes (`sockops`/`tcp_recvmsg`), eBPF map capacity monitoring, and Prometheus/Mimir Exemplars using OpenTelemetry eBPF (OBI). |",
        "| **eBPF Trace-Log Correlation** | [Nubenetes OpenTelemetry eBPF (OBI) Zero-Code Trace-Log Correlation](https://www.youtube.com/playlist?list=PLYmAuttxFYjA) | Linux kernel internals and incident triage workflows for zero-code trace-log correlation with OpenTelemetry eBPF (OBI), `write`/`writev` syscall tracing, and Fluent Bit/Vector/Collector pipelines. |",
        "| **Full-Stack eBPF** | [Nubenetes Browser to Kernel: Full-Stack eBPF Observability (OBI)](https://www.youtube.com/playlist?list=PLIDgJtbMXQ6s) | End-to-end zero-code observability from React/Angular SPAs and Next.js/Node.js SSR down to Linux kernel eBPF log enrichment via W3C Trace Context (`traceparent`) propagation. |",
        "| **SRE and SLO Governance** | [Nubenetes SLAs and SLOs Observability](https://www.youtube.com/playlist?list=PLBUzSeBwfM7M) | Engineering guide to SLAs, SLOs, SLIs, Error Budgets, and P99 tail latency: Linux CFS CPU quota throttling, PromQL percentile math, canary SLO gates, and tail-based distributed tracing. |",
        "| **Observability Platforms** | [Nubenetes Enterprise Observability and Monitoring Platforms](https://www.youtube.com/playlist?list=PLcUy0RRCT9fg) | Comparative architecture, high-load stress testing, TCO modeling, and air-gapped monitoring strategies across 12 enterprise observability platforms. |",
        "| **Datadog on OpenShift** | [Nubenetes Datadog on OpenShift](https://www.youtube.com/playlist?list=PLR6nHneHUvqU) | Deploying, tuning, and scaling the Datadog Agent and Operator on Red Hat OpenShift with Security Context Constraints (SCCs), edge log filtering, and FinOps ingestion cost control. |",
        "| **GitOps and ArgoCD** | [Nubenetes ArgoCD and GitOps Automation](https://www.youtube.com/playlist?list=PLYbmzkhLGOtI) | Declarative GitOps deployments, ArgoCD ApplicationSets, sync waves, multi-cluster architectures, and progressive delivery on Kubernetes and OpenShift. |",
        "| **Jenkins Pure GitOps** | [Nubenetes Jenkins Pure GitOps (Without Git Parameter)](https://www.youtube.com/playlist?list=PLMiMCcgzkPpw) | Declarative pull-based GitOps architectures, multi-cluster delivery with ArgoCD, and automated canary rollouts eliminating manual Jenkins UI Git Parameter dropdowns. |",
        "| **Jenkins CI/CD Automation** | [Nubenetes Jenkins Git Parameter Automation](https://www.youtube.com/playlist?list=PLaqfcvWjZHso) | Enterprise immutable promotion, SCM tagging, release validation, and CI/CD pipelines using the Jenkins Git Parameter plugin and GitOps delivery patterns. |",
        "| **Multi-Distro Kubernetes** | [Nubenetes Multi-Distro Kubernetes and Portable Ingress](https://www.youtube.com/playlist?list=PLcgcGU_pGpv8) | Portable Helm architecture across OpenShift, RKE2, K3s, kubeadm, and Tanzu with air-gapped ingress, MetalLB/Cilium networking, and HashiCorp Vault External Secrets. |",
        "| **Google Cloud and GKE** | [Nubenetes Google Cloud (GCP) and GKE Architecture](https://www.youtube.com/playlist?list=PLNtKxnT9mK7g) | Enterprise Google Cloud Platform (GCP) and Google Kubernetes Engine (GKE) architecture, Golden Path blueprints, Workload Identity Federation, and automated deployments. |",
        "| **Enterprise Modernization** | [Nubenetes TIBCO BWCE Modernization and GitOps](https://www.youtube.com/playlist?list=PLRz_DgUi73hc) | Enterprise containerization, canary rollouts, Linux CFS CPU throttling tuning, and GitOps delivery pipelines for TIBCO BusinessWorks Container Edition (BWCE) on Kubernetes. |",
        "| **SRE Decision Architecture** | [Nubenetes JevOps and System 1 Decision Models](https://www.youtube.com/playlist?list=PLWwVdOapXzDc) | Reflexive System 1 decision models for cloud-native infrastructure, submillisecond log filtering, and production deployment patterns on Kubernetes and OpenShift. |",
        "| **AI Agents and Radar** | [Nubenetes Awesome Kubernetes and Cloud Native Guide](https://www.youtube.com/playlist?list=PLH1sVn4CEfPY) | Curated cloud-native architectural guides, 2026 technology radars, Model Context Protocol (MCP) AI agents, and production Kubernetes blueprints. |",
        "| **Cloud Native Tutorials** | [Nubenetes Cloud Native Architecture and Tutorials](https://www.youtube.com/playlist?list=PLQAXmE_Qq4bU) | Foundational cloud-native architectures, platform engineering blueprints, and step-by-step enterprise Kubernetes tutorials. |",
        "| **Global Engineering Teams** | [Nubenetes Employer of Record (EOR) and Native Teams](https://www.youtube.com/playlist?list=PLY9afYE9hx70) | Global remote employment, Employer of Record (EOR) architectures, Native Teams guides, payroll compliance, and international engineering hiring without freelance bureaucracy. |",
        "| **Podcasts (EN / ES)** | [Cloud Native Podcasts (English)](https://www.youtube.com/playlist?list=PLBMAtCXWYfZA) · [Podcasts (Español)](https://www.youtube.com/playlist?list=PLB-3xSV3dAoU) | Bilingual NotebookLM audio/video deep-dives covering Kubernetes, OpenShift 4.20, P99 latency, eBPF (OBI), Gateway API, GKE, Backstage IDP, and Azure Terraform automation. |",
    ]

    # Dynamically append any newly discovered @nubenetes playlists from inventory
    known_playlist_ids = {
        "PLBZl7QsgYjrw", "PLNKD2Ya-t0zM", "PLCgDGrDt3kNU", "PLaNxiRbEBYJ8", "PLZ-bpd1sEISs",
        "PLc2WtEw1pojo", "PLcCUAwooFb6s", "PLUt4PJvFTysY", "PLDbL5Dh24a5g",
        "PLOb7y_S6Kcd8", "PLWGYAgXdQh44", "PLI0K_-6LrXgM", "PLRTV86SuuRbk",
        "PLZhOsH66dFmw", "PLYmAuttxFYjA", "PLIDgJtbMXQ6s", "PLBUzSeBwfM7M",
        "PLcUy0RRCT9fg", "PLR6nHneHUvqU", "PLYbmzkhLGOtI", "PLMiMCcgzkPpw",
        "PLaqfcvWjZHso", "PLcgcGU_pGpv8", "PLNtKxnT9mK7g", "PLRz_DgUi73hc",
        "PLWwVdOapXzDc", "PLH1sVn4CEfPY", "PLQAXmE_Qq4bU", "PLY9afYE9hx70",
        "PLBMAtCXWYfZA", "PLB-3xSV3dAoU",
    }
    for url, entry in inventory.items():
        if not isinstance(entry, dict):
            continue
        if "playlist?list=" in url and (entry.get("company") == "Nubenetes" or entry.get("source_provenance") == "Official @nubenetes YouTube Channel"):
            m_pl = re.search(r"[?&]list=([^&#]+)", url)
            pl_id = m_pl.group(1) if m_pl else ""
            if pl_id and pl_id not in known_playlist_ids:
                known_playlist_ids.add(pl_id)
                dim_label = clean_header(str(entry.get("technology") or entry.get("category") or "Cloud Native"))
                pl_title = str(entry.get("title") or "Nubenetes Playlist").replace("(Playlist)", "").replace("|", "-").strip()
                pl_summary = str(entry.get("ai_summary") or entry.get("description") or "").splitlines()[0].replace("|", "-").strip()
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
