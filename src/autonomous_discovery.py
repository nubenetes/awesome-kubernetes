from datetime import datetime, timedelta
import json
import httpx
from src.config import GEMINI_API_KEY, NUBENETES_CATEGORIES, GH_TOKEN, MADRID_TZ
from src.gemini_utils import call_gemini_with_retry
from src.logger import log_event


def _calculate_repo_velocity(repo: dict, now: datetime) -> float:
    """Compute monthly star velocity (stars / age_in_months) to surface fast-rising tools."""
    stars = int(repo.get("stargazers_count") or 0)
    created_raw = repo.get("created_at") or ""
    try:
        created_dt = datetime.fromisoformat(created_raw.replace("Z", "+00:00"))
        age_months = max(1.0, (now - created_dt).days / 30.0)
    except Exception:
        age_months = 24.0
    return round(stars / age_months, 1)


async def fetch_github_trending_cloud_native() -> list[dict]:
    now = datetime.now(MADRID_TZ)
    pushed_cutoff = (now - timedelta(days=180)).strftime("%Y-%m-%d")

    queries = [
        f"topic:kubernetes+pushed:>{pushed_cutoff}+stars:>500",
        f"topic:kubernetes+topic:ai+pushed:>{pushed_cutoff}+stars:>30",
        f"topic:kubernetes+topic:llm+pushed:>{pushed_cutoff}+stars:>30",
        f"topic:kubernetes+topic:gpu+pushed:>{pushed_cutoff}+stars:>30",
        f"topic:mcp-server+kubernetes+pushed:>{pushed_cutoff}+stars:>10",
        f"topic:mcp-server+pushed:>{pushed_cutoff}+stars:>20",
        f"topic:model-context-protocol+pushed:>{pushed_cutoff}+stars:>20",
        f"topic:ai-agents+pushed:>{pushed_cutoff}+stars:>50",
        f"topic:rag+pushed:>{pushed_cutoff}+stars:>100",
        f"topic:graphrag+OR+topic:knowledge-graph+llm+pushed:>{pushed_cutoff}+stars:>50",
        f"open-knowledge-format+OR+llm-wiki+pushed:>{pushed_cutoff}+stars:>10",
        f"topic:agent-memory+OR+topic:vector-database+pushed:>{pushed_cutoff}+stars:>50",
        f"topic:k8s-operator+pushed:>{pushed_cutoff}+stars:>50",
        f"topic:vllm+pushed:>{pushed_cutoff}+stars:>30",
        f"topic:mlops+kubernetes+pushed:>{pushed_cutoff}+stars:>30",
        f"topic:azure-ai-foundry+pushed:>{pushed_cutoff}+stars:>10",
        f"topic:amazon-bedrock+pushed:>{pushed_cutoff}+stars:>20",
        f"topic:vertex-ai+pushed:>{pushed_cutoff}+stars:>20",
        f"topic:openshift-ai+OR+topic:opendatahub+pushed:>{pushed_cutoff}+stars:>10",
        f"topic:openshift+pushed:>{pushed_cutoff}+stars:>30",
        f"org:openshift+pushed:>{pushed_cutoff}+stars:>50",
        f"org:okd-project+OR+org:operator-framework+pushed:>{pushed_cutoff}+stars:>30",
        f"topic:kubevirt+OR+topic:hypershift+pushed:>{pushed_cutoff}+stars:>30",
        f"org:kaito-project+OR+org:llm-d+pushed:>{pushed_cutoff}",
        f"topic:ebpf+kubernetes+pushed:>{pushed_cutoff}+stars:>50",
        f"awesome+kubernetes+pushed:>{pushed_cutoff}+stars:>200",
        f"topic:generative-ai+pushed:>{pushed_cutoff}+stars:>500",
        f"topic:devops+pushed:>{pushed_cutoff}+stars:>500",
        f"topic:observability+pushed:>{pushed_cutoff}+stars:>200",
        f"topic:cloud-security+pushed:>{pushed_cutoff}+stars:>200",
        f"topic:terraform+pushed:>{pushed_cutoff}+stars:>300",
        f"topic:terraform-module+pushed:>{pushed_cutoff}+stars:>40",
        f"org:Azure+terraform-azurerm-avm+pushed:>{pushed_cutoff}",
        f"org:Azure-Samples+terraform+pushed:>{pushed_cutoff}+stars:>5",
        f"org:aws-ia+terraform+pushed:>{pushed_cutoff}+stars:>20",
        f"org:terraform-aws-modules+pushed:>{pushed_cutoff}+stars:>100",
        f"topic:opentofu+pushed:>{pushed_cutoff}+stars:>25",
        f"topic:terraform+topic:github-actions+pushed:>{pushed_cutoff}+stars:>20",
        f"topic:service-mesh+pushed:>{pushed_cutoff}+stars:>100",
        f"topic:gateway-api+OR+topic:cilium+pushed:>{pushed_cutoff}+stars:>50",
        f"topic:opentelemetry+pushed:>{pushed_cutoff}+stars:>100",
        f"topic:kyverno+OR+topic:falco+OR+topic:sigstore+pushed:>{pushed_cutoff}+stars:>50",
        f"topic:finops+OR+topic:karpenter+OR+topic:opencost+pushed:>{pushed_cutoff}+stars:>30",
        f"topic:platform-engineering+pushed:>{pushed_cutoff}+stars:>100",
        f"topic:sovereign-cloud+OR+topic:gaia-x+pushed:>{pushed_cutoff}+stars:>5",
        f"topic:proxmox+terraform+OR+topic:proxmox+kubernetes+pushed:>{pushed_cutoff}+stars:>20",
        f"topic:hetzner+kubernetes+OR+topic:scaleway+OR+topic:ovhcloud+pushed:>{pushed_cutoff}+stars:>20",
        f"topic:openstack+kubernetes+OR+topic:cloudstack+OR+topic:harvester+pushed:>{pushed_cutoff}+stars:>20",
        f"topic:cloudnativepg+OR+topic:velero+OR+topic:disaster-recovery+kubernetes+pushed:>{pushed_cutoff}+stars:>20",
    ]
    all_repos = []
    seen_urls = set()
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GH_TOKEN:
        headers["Authorization"] = f"token {GH_TOKEN}"
    async with httpx.AsyncClient(headers=headers, timeout=10.0) as client:
        for q in queries:
            url = f"https://api.github.com/search/repositories?q={q}&sort=stars&order=desc&per_page=10"
            try:
                resp = await client.get(url)
                if resp.status_code == 200:
                    data = resp.json()
                    for repo in data.get("items", [])[:8]:
                        html_url = repo.get("html_url")
                        if not html_url or html_url in seen_urls:
                            continue
                        seen_urls.add(html_url)
                        all_repos.append({
                            "name": repo["name"],
                            "url": html_url,
                            "desc": repo.get("description") or "No description provided.",
                            "stars": repo.get("stargazers_count", 0),
                            "stars_per_month": _calculate_repo_velocity(repo, now),
                            "topics": (repo.get("topics") or [])[:6],
                        })
            except Exception as e:
                log_event(f"[WARN] GitHub search query '{q}': {str(e)[:100]}")
                continue
    all_repos.sort(key=lambda r: (r.get("stars_per_month", 0), r.get("stars", 0)), reverse=True)
    return all_repos


async def fetch_watched_github_releases(since_date: datetime, repos: list[str]) -> list[dict]:
    """Fetch recent major/minor GitHub releases from watched repositories (e.g., Terraform, AVM, OpenTofu)."""
    if not repos:
        return []
    releases_found = []
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GH_TOKEN:
        headers["Authorization"] = f"token {GH_TOKEN}"
    async with httpx.AsyncClient(headers=headers, timeout=10.0) as client:
        for repo in repos:
            url = f"https://api.github.com/repos/{repo}/releases?per_page=3"
            try:
                resp = await client.get(url)
                if resp.status_code == 200:
                    for rel in resp.json():
                        if rel.get("draft") or rel.get("prerelease"):
                            continue
                        pub_raw = rel.get("published_at")
                        if not pub_raw:
                            continue
                        pub_dt = datetime.fromisoformat(pub_raw.replace("Z", "+00:00")).astimezone(MADRID_TZ)
                        if pub_dt >= since_date:
                            html_url = rel.get("html_url")
                            tag_name = rel.get("tag_name") or rel.get("name") or "Release"
                            body = (rel.get("body") or "")[:500]
                            releases_found.append({
                                "url": html_url,
                                "title": f"{repo} {tag_name} Release",
                                "text": body,
                                "context": f"Official GitHub Release {tag_name} for {repo}: {body[:250]}",
                                "timestamp": pub_dt.isoformat(),
                                "source_type": f"GitHub Release ({repo})",
                            })
            except Exception as e:
                log_event(f"[WARN] GitHub release watch '{repo}': {str(e)[:100]}")
                continue
    return releases_found


async def discover_trending_assets() -> list[dict]:
    repos = await fetch_github_trending_cloud_native()
    if not repos:
        return []

    prompt = (
        "Analyze these active Cloud-Native, AI, and Infrastructure as Code (IaC) repositories (sorted by monthly star velocity) and select the 8 highest-impact tools for a 2026 Senior Kubernetes, Cloud & AI Platform Architect.\n"
        "Prioritize Public Cloud & Enterprise AI Platforms (Azure AI Foundry, Amazon Bedrock & AgentCore, Google Cloud Vertex AI & ADK, Red Hat OpenShift AI / OpenDataHub, IBM watsonx, Databricks Mosaic AI), AI Knowledge & Retrieval architectures (RAG, Open Knowledge Format / OKF, LLM Wikis, GraphRAG, LightRAG, vectorless reasoning RAG / PageIndex, Cache-Augmented Generation / CAG, persistent agent memory like Mem0/Graphiti/Letta/Cognee, vector databases — categorize these under 'ai-rag-okf'), Red Hat OpenShift 5 / OCP 5 ecosystem (OpenShift Lightspeed, MCP servers, Hosted Control Planes / HyperShift, OLM v1, OpenShift Virtualization 5 / KubeVirt, OKD 5, MicroShift 5 — categorize these under 'ocp5'), European Sovereign Cloud & Private Data Center alternatives to US hyperscalers (Germany: STACKIT/IONOS/Hetzner/Open Telekom/PlusServer/noris/SysEleven/DE-CIX -> 'eu-cloud-germany'; France: OVHcloud/Scaleway/Outscale/Clever Cloud/Cloud Temple/Bleu/S3NS/Mistral/DATA4 -> 'eu-cloud-france'; Spain ENS Alto: Arsys/Gigas/Alhambra IT/Telefonica Tech/Stackscale/Merlin-Edged -> 'eu-cloud-spain'; Italy: Aruba/Seeweb/PSN/WIIT/ReeVo/CINECA -> 'eu-cloud-italy'; Benelux: Nebius/Leaseweb/Cyso/Leafcloud/LuxConnect/Gcore/AMS-IX -> 'eu-cloud-benelux'; Switzerland & Austria: Exoscale/Infomaniak/cloudscale.ch/VSHN/Anexia/Swisscom -> 'eu-cloud-switzerland-dach'; Nordics: UpCloud/Elastx/Cleura/GleSYS/Safespring/Evroc/Green Mountain/atNorth/Verne/LUMI -> 'eu-cloud-nordics'; UK: Civo/Pulsant/Brightbox/Redcentric/Nscale/LINX -> 'eu-cloud-uk'; Terraform/OpenTofu/Crossplane/CAPI providers -> 'eu-cloud-iac-maturity'; Proxmox/OpenStack/CloudStack/Harvester/EU GPU AI -> 'eu-cloud-workloads-stack'; RPO/RTO/DRaaS/Zerto/Veeam/PBS/CNPG/Velero -> 'eu-cloud-resilience-sla'; pan-EU frameworks -> 'eu-sovereign-cloud'), Global Neoclouds & GPU AI Clouds (North America CoreWeave/Lambda/Crusoe/TensorWave/Voltage Park/Together AI/Fireworks/RunPod/IREN/Applied Digital/QScale -> 'neoclouds-north-america'; European Neoclouds & EuroHPC AI Factories Nebius/Nscale/Taiga/Scaleway AI/Seeweb/Regolo/Isambard-AI/IT4LIA/JUPITER/MareNostrum 5 -> 'neoclouds-europe'; APAC Sakura/SoftBank/Yotta Shakti/Neysa/E2E/Firmus SMC/Singtel RE:AI/NEXTDC -> 'neoclouds-apac'; MENA Core42/Khazna/HUMAIN/center3/Ooredoo/MEEZA -> 'neoclouds-mena'; LatAm & Africa ODATA/Elea/KIO/Cirion/Cassava AI/Africa DCs/Raxio -> 'neoclouds-latam-africa'; NVLink/GB200 NVL72/InfiniBand/Spectrum-X/SUNK/KAI-Scheduler/WEKA/VAST/DDN -> 'neoclouds-architecture-stack'; SkyPilot/neocloud Terraform providers/DCGM goodput/LiteLLM/SGLang -> 'neoclouds-iac-finops-sla'; global benchmarks ClusterMAX/MLPerf/Neocloud vs Sovereign Cloud -> 'neoclouds'), Cloud-Native AI infrastructure (GPU scheduling, DRA, vLLM/llm-d inference serving, KubeRay, KAITO), MCP servers for Kubernetes/SRE, Modern IaC & Terraform (Azure Verified Modules / AVM, OpenTofu, Terraform CI/CD pipelines, Landing Zones, official cloud samples), eBPF observability, and GitOps operators.\n"
        f"Valid Categories: {', '.join(NUBENETES_CATEGORIES)}\n"
        f"Repos: {json.dumps(repos[:50])}\n\n"
        "Respond ONLY with a valid JSON list: [{\"title\": \"...\", \"url\": \"...\", \"description\": \"...\", \"category\": \"...\"}]"
    )

    try:
        results = await call_gemini_with_retry(prompt, prefer_flash=True)
        if isinstance(results, list):
            return [res for res in results if res.get("category") in NUBENETES_CATEGORIES]
    except Exception as e:
        log_event(f"[WARN] Gemini discovery classification fallback: {str(e)[:100]}")

    # --- HEURISTIC FALLBACK (sorted by velocity) ---
    fallback_results = []
    for r in repos[:8]:
        category = "kubernetes-tools"
        desc_lower = r["desc"].lower()
        name_lower = r["name"].lower()
        topics_set = {t.lower() for t in r.get("topics", [])}

        if any(k in desc_lower or k in name_lower or k in topics_set for k in ("azure-ai-foundry", "bedrock", "vertex-ai", "openshift-ai", "opendatahub", "llm-d", "kaito")):
            category = "enterprise-ai-platforms"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("open-knowledge-format", "okf", "graphrag", "lightrag", "ragflow", "pageindex", "ragas", "mem0", "graphiti", "letta", "cognee", "qdrant", "weaviate", "milvus", "pgvector", "chroma", "llama_index", "llamaindex", "haystack", "agent-memory", "vector-database", "cache-augmented", "contextual-retrieval")) or "rag" in topics_set:
            category = "ai-rag-okf"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("ocp5", "openshift-5", "openshift 5", "hypershift", "lightspeed", "microshift", "okd", "operator-controller", "openshift", "kubevirt")):
            category = "ocp5"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("arsys", "gigas", "alhambra", "stackscale", "telefonica", "ens-alto")):
            category = "eu-cloud-spain"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("terraform-provider-ovh", "terraform-provider-scaleway", "terraform-provider-ionos", "terraform-provider-stackit", "terraform-provider-hcloud", "terraform-provider-exoscale", "terraform-provider-upcloud", "terraform-provider-proxmox", "terraform-provider-openstack", "terraform-provider-vcd", "terraform-provider-cloudscale", "terraform-provider-leaseweb", "terraform-provider-anxcloud", "terraform-provider-brightbox", "cluster-api-provider-hetzner", "cluster-api-provider-proxmox", "crossplane-provider-ionos", "crossplane-provider-scaleway")):
            category = "eu-cloud-iac-maturity"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("cloudnativepg", "velero", "proxmox-backup", "zerto", "veeam", "disaster-recovery")):
            category = "eu-cloud-resilience-sla"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("proxmox", "cloudstack", "harvester", "sovereigncloudstack", "gardener", "talos")):
            category = "eu-cloud-workloads-stack"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("hetzner", "ionos", "stackit", "opentelekom", "open-telekom", "plusserver", "syseleven", "secunet", "noris", "gridscale", "delos", "bsi-c5", "de-cix")):
            category = "eu-cloud-germany"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("ovhcloud", "scaleway", "outscale", "clevercloud", "clever-cloud", "cloud-temple", "ikoula", "secnumcloud", "s3ns", "bleucloud", "mistral")):
            category = "eu-cloud-france"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("arubacloud", "seeweb", "wiit", "reevo", "polostrategico", "timenterprise", "acn-qc3")):
            category = "eu-cloud-italy"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("nebius", "leaseweb", "cyso", "leafcloud", "transip", "luxconnect", "gcore", "proximus", "ams-ix")):
            category = "eu-cloud-benelux"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("exoscale", "infomaniak", "cloudscale", "vshn", "appuio", "anexia", "swisscom", "finma")):
            category = "eu-cloud-switzerland-dach"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("upcloud", "elastx", "cleura", "glesys", "safespring", "evroc", "atnorth", "greenmountain", "verne", "lumi")):
            category = "eu-cloud-nordics"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("civo", "pulsant", "brightbox", "redcentric", "nscale", "telehouse", "ncsc")):
            category = "eu-cloud-uk"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("sovereign-cloud", "gaia-x", "eurostack", "cispe")):
            category = "eu-sovereign-cloud"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("skypilot", "terraform-provider-nebius", "terraform-provider-crusoe", "terraform-provider-vultr", "terraform-provider-runpod", "terraform-provider-nscale", "dcgm-exporter", "sglang", "litellm")):
            category = "neoclouds-iac-finops-sla"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("sunk-anywhere", "kai-scheduler", "nccl-tests", "nvl72", "infiniband", "spectrum-x", "rocm", "mi300x", "gpu-operator")):
            category = "neoclouds-architecture-stack"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("coreweave", "lambdalabs", "crusoe", "tensorwave", "voltagepark", "fluidstack", "together.ai", "fireworks.ai", "runpod", "hyperstack", "qscale")):
            category = "neoclouds-north-america"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("sakura-internet", "shakticloud", "neysa", "e2enetworks", "firmus", "singtel", "nextdc", "indiaai")):
            category = "neoclouds-apac"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("core42", "khazna", "humain", "center3", "ooredoo", "meeza", "sdaia")):
            category = "neoclouds-mena"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("odatadc", "eleadatacenters", "cassava", "africadatacentres", "raxiogroup")):
            category = "neoclouds-latam-africa"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("taigacloud", "eurohpc", "isambard", "it4lia", "marenostrum", "regolo.ai")):
            category = "neoclouds-europe"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("neocloud", "clustermax", "nvidia-cloud-partner")):
            category = "neoclouds"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("mcp", "context-protocol", "mcp-server", "adk", "agent-framework", "strands-agents")):
            category = "ai-agents-mcp"
        elif "awesome" in name_lower:
            category = "other-awesome-lists"
        elif any(k in desc_lower or k in name_lower or k in topics_set for k in ("terraform", "opentofu", "terragrunt", "terramate", "tflint", "avm-res", "avm-ptn", "azurerm")):
            category = "terraform"
        elif any(k in desc_lower or k in topics_set for k in ("iac", "infrastructure-as-code", "pulumi", "bicep")):
            category = "iac"
        elif any(k in desc_lower or k in topics_set for k in ("mlops", "gpu", "vllm", "llm-d", "kaito", "kuberay", "inference", "kubeflow", "kueue", "volcano", "sagemaker", "openshift-ai", "opendatahub")):
            category = "mlops"
        elif "ai" in desc_lower or "agent" in desc_lower or "llm" in desc_lower:
            category = "ai"
        elif "ebpf" in desc_lower or "cilium" in desc_lower or "gateway-api" in desc_lower or "ebpf" in topics_set:
            category = "kubernetes-networking"
        elif any(k in desc_lower or k in topics_set for k in ("opentelemetry", "prometheus", "observability", "victoriametrics", "grafana")):
            category = "kubernetes-monitoring"
        elif any(k in desc_lower or k in topics_set for k in ("finops", "opencost", "kubecost", "cloud-cost")):
            category = "finops"
        elif any(k in desc_lower or k in topics_set for k in ("karpenter", "keda", "autoscal")):
            category = "kubernetes-autoscaling"
        elif any(k in desc_lower or k in topics_set for k in ("backstage", "developer-portal", "platform-engineering")):
            category = "developerportals"
        elif "security" in desc_lower or "kyverno" in desc_lower or "falco" in desc_lower or "sigstore" in desc_lower or "cloud-security" in topics_set:
            category = "kubernetes-security"

        fallback_results.append({
            "title": r["name"],
            "url": r["url"],
            "description": r["desc"],
            "category": category,
        })
    return fallback_results
