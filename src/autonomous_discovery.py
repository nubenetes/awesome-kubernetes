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
        f"topic:k8s-operator+pushed:>{pushed_cutoff}+stars:>50",
        f"topic:vllm+pushed:>{pushed_cutoff}+stars:>30",
        f"topic:mlops+kubernetes+pushed:>{pushed_cutoff}+stars:>30",
        f"topic:azure-ai-foundry+pushed:>{pushed_cutoff}+stars:>10",
        f"topic:amazon-bedrock+pushed:>{pushed_cutoff}+stars:>20",
        f"topic:vertex-ai+pushed:>{pushed_cutoff}+stars:>20",
        f"topic:openshift-ai+OR+topic:opendatahub+pushed:>{pushed_cutoff}+stars:>10",
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
        f"topic:platform-engineering+pushed:>{pushed_cutoff}+stars:>100",
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
        "Prioritize Public Cloud & Enterprise AI Platforms (Azure AI Foundry, Amazon Bedrock & AgentCore, Google Cloud Vertex AI & ADK, Red Hat OpenShift AI / OpenDataHub, IBM watsonx, Databricks Mosaic AI), Cloud-Native AI infrastructure (GPU scheduling, DRA, vLLM/llm-d inference serving, KubeRay, KAITO), MCP servers for Kubernetes/SRE, Modern IaC & Terraform (Azure Verified Modules / AVM, OpenTofu, Terraform CI/CD pipelines, Landing Zones, official cloud samples), eBPF observability, and GitOps operators.\n"
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

        if any(k in desc_lower or k in name_lower or k in topics_set for k in ("mcp", "context-protocol", "mcp-server", "azure-ai-foundry", "bedrock", "vertex-ai", "adk", "agent-framework", "strands-agents")):
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
        elif "ebpf" in desc_lower or "cilium" in desc_lower or "ebpf" in topics_set:
            category = "kubernetes-networking"
        elif "security" in desc_lower or "cloud-security" in topics_set:
            category = "kubernetes-security"

        fallback_results.append({
            "title": r["name"],
            "url": r["url"],
            "description": r["desc"],
            "category": category,
        })
    return fallback_results
