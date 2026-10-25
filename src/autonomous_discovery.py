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
        f"topic:ebpf+kubernetes+pushed:>{pushed_cutoff}+stars:>50",
        f"awesome+kubernetes+pushed:>{pushed_cutoff}+stars:>200",
        f"topic:generative-ai+pushed:>{pushed_cutoff}+stars:>500",
        f"topic:devops+pushed:>{pushed_cutoff}+stars:>500",
        f"topic:observability+pushed:>{pushed_cutoff}+stars:>200",
        f"topic:cloud-security+pushed:>{pushed_cutoff}+stars:>200",
        f"topic:terraform+pushed:>{pushed_cutoff}+stars:>500",
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


async def discover_trending_assets() -> list[dict]:
    repos = await fetch_github_trending_cloud_native()
    if not repos:
        return []

    prompt = (
        "Analyze these active Cloud-Native and AI repositories (sorted by monthly star velocity) and select the 6 highest-impact tools for a 2026 Senior Kubernetes & AI Platform Architect.\n"
        "Prioritize Cloud-Native AI infrastructure (GPU scheduling, DRA, vLLM/inference serving, KubeRay), MCP servers for Kubernetes/SRE, eBPF observability, and GitOps operators.\n"
        f"Valid Categories: {', '.join(NUBENETES_CATEGORIES)}\n"
        f"Repos: {json.dumps(repos[:40])}\n\n"
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
    for r in repos[:6]:
        category = "kubernetes-tools"
        desc_lower = r["desc"].lower()
        name_lower = r["name"].lower()
        topics_set = {t.lower() for t in r.get("topics", [])}

        if "mcp" in desc_lower or "context-protocol" in desc_lower or "mcp" in name_lower or "mcp-server" in topics_set:
            category = "ai-agents-mcp"
        elif "awesome" in name_lower:
            category = "other-awesome-lists"
        elif any(k in desc_lower or k in topics_set for k in ("mlops", "gpu", "vllm", "kuberay", "inference", "kubeflow", "kueue", "volcano")):
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
