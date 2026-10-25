from __future__ import annotations

import asyncio
import math
import re
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple

import httpx
import yaml
try:
    from yaml import CSafeLoader as Loader
except ImportError:
    from yaml import SafeLoader as Loader

from src.config import GH_TOKEN, MADRID_TZ
from src.logger import log_event

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CNCF_LANDSCAPE_YAML_URL = "https://raw.githubusercontent.com/cncf/landscape/master/landscape.yml"
LFAI_LANDSCAPE_YAML_URL = "https://raw.githubusercontent.com/lfai/landscape/master/landscape.yml"
GITHUB_API_BASE = "https://api.github.com"
GITHUB_RATE_DELAY = 0.5   # seconds between GitHub API calls (5000/hr limit = ~1.4/s safe)
MAX_REPOS_DEFAULT = 200   # cap per run — 200 × 0.5s = ~100s, well within CI timeout
ACTIVITY_STALENESS_DAYS = 30

# Community health thresholds
HEALTH_ACTIVE = 50
HEALTH_HEALTHY = 10


# ---------------------------------------------------------------------------
# Helpers & Composite Momentum Algorithm
# ---------------------------------------------------------------------------

def _github_headers() -> Dict[str, str]:
    """Build GitHub API request headers with optional auth."""
    headers = {"Accept": "application/vnd.github.v3+json"}
    if GH_TOKEN:
        headers["Authorization"] = f"token {GH_TOKEN}"
    return headers


def _parse_github_repo(url: str) -> Optional[str]:
    """Extract 'owner/repo' from a GitHub URL. Returns None if not a GitHub URL."""
    match = re.search(r"github\.com/([^/]+/[^/]+)", url)
    if not match:
        return None
    repo = match.group(1).split("#")[0].split("?")[0].rstrip("/")
    if repo.endswith(".git"):
        repo = repo[:-4]
    return repo


def _normalize_repo_url(url: str) -> str:
    """Normalize a GitHub repo URL for comparison (lowercase, no trailing slash)."""
    url = url.lower().rstrip("/")
    if url.endswith(".git"):
        url = url[:-4]
    url = re.sub(r"^https?://", "", url)
    return url


def _is_activity_stale(entry: Dict) -> bool:
    """Check whether an entry's activity data is older than ACTIVITY_STALENESS_DAYS."""
    checked = entry.get("gh_activity_checked")
    if not checked:
        return True
    try:
        checked_dt = datetime.fromisoformat(checked)
        return datetime.now(MADRID_TZ) - checked_dt > timedelta(days=ACTIVITY_STALENESS_DAYS)
    except (ValueError, TypeError):
        return True


def compute_momentum_score(entry: Dict, now: Optional[datetime] = None) -> float:
    """Compute a 0–100 Composite Momentum Score combining log-stars, star velocity,
    and commit freshness to counter incumbent bias and surface fast-rising AI/K8s tools.

    Formula:
        base_stars = 12.5 * log10(max(1, gh_stars))            # up to ~62.5 pts at 100k stars
        velocity   = 14.0 * log10(1 + stars_per_month)         # up to ~35 pts at 300 stars/mo
        freshness  = +8 pts if pushed < 90d, -25 pts if > 4y   # Mandate 3 MVQ alignment
        cncf_bonus = +6 pts (graduated), +4 pts (incubating), +2 pts (sandbox)
    """
    if now is None:
        now = datetime.now(MADRID_TZ)

    raw_gh = entry.get("gh_stars")
    gh_stars = int(raw_gh) if raw_gh is not None and str(raw_gh).isdigit() else 0
    curator_stars = int(entry.get("stars") or 0)

    if gh_stars <= 0:
        # Non-GitHub or un-enriched resource: map curator 0-5 stars + recency year
        year_raw = str(entry.get("year") or "")
        recency_bonus = 0.0
        if year_raw.isdigit():
            age_yrs = max(0, now.year - int(year_raw))
            recency_bonus = max(-10.0, 8.0 - age_yrs * 2.0)
        return round(min(100.0, max(0.0, curator_stars * 18.0 + recency_bonus)), 1)

    # 1. Log-scaled total stars
    base_stars = 12.5 * math.log10(max(1, gh_stars))

    # 2. Monthly star velocity
    stars_per_month = entry.get("gh_stars_per_month")
    if stars_per_month is None:
        year_raw = str(entry.get("year") or "")
        if year_raw.isdigit() and 2008 <= int(year_raw) <= now.year:
            age_months = max(3.0, (now.year - int(year_raw)) * 12.0 + 6.0)
        else:
            age_months = 36.0
        stars_per_month = gh_stars / age_months
    try:
        spm_val = max(0.0, float(stars_per_month))
    except (ValueError, TypeError):
        spm_val = 0.0
    velocity_pts = 14.0 * math.log10(1.0 + spm_val)

    # 3. Commit freshness / staleness penalty (Mandate 3: 4-year MVQ cutoff)
    freshness_pts = 0.0
    pushed_raw = str(entry.get("gh_pushed") or entry.get("gh_last_commit") or "")
    if pushed_raw and len(pushed_raw) >= 10:
        try:
            pushed_dt = datetime.fromisoformat(pushed_raw[:10])
            days_since_push = (now.date() - pushed_dt.date()).days
            if days_since_push <= 90:
                freshness_pts = 8.0
            elif days_since_push <= 365:
                freshness_pts = 4.0
            elif days_since_push > 4 * 365:
                freshness_pts = -25.0
            elif days_since_push > 2 * 365:
                freshness_pts = -10.0
        except Exception:
            pass

    # 4. CNCF / LFAI Foundation maturity bonus
    cncf_status = str(entry.get("cncf_status") or "").lower()
    cncf_bonus = {"graduated": 6.0, "incubating": 4.0, "sandbox": 2.0, "archived": -20.0}.get(cncf_status, 0.0)

    total = base_stars + velocity_pts + freshness_pts + cncf_bonus
    return round(min(100.0, max(0.0, total)), 1)


# ---------------------------------------------------------------------------
# Module 1: CNCF & LF AI Landscape Status
# ---------------------------------------------------------------------------

def _extract_landscape_yaml_projects(yaml_text: str) -> Dict[str, str]:
    """Parse canonical CNCF / LFAI landscape.yml text into normalized_repo_url -> maturity."""
    projects: Dict[str, str] = {}
    data = yaml.load(yaml_text, Loader=Loader) or {}
    for cat in data.get("landscape") or []:
        if not isinstance(cat, dict):
            continue
        for sub in cat.get("subcategories") or []:
            if not isinstance(sub, dict):
                continue
            for item in sub.get("items") or []:
                if not isinstance(item, dict):
                    continue
                maturity = str(item.get("project") or "").lower().strip()
                repo_url = str(item.get("repo_url") or "").strip()
                if maturity in ("graduated", "incubating", "sandbox", "archived") and repo_url:
                    projects[_normalize_repo_url(repo_url)] = maturity
    return projects


async def fetch_cncf_landscape() -> Dict[str, str]:
    """Fetch canonical CNCF and LF AI & Data project graduation statuses.

    Primary source: Canonical YAML files from `cncf/landscape` and `lfai/landscape`
    repositories (320+ official projects across Graduated, Incubating, Sandbox, Archived).
    Fallback: GitHub topic search (`topic:cncf-graduated`, etc.) if raw GitHub is unreachable.

    Returns dict mapping repo_url (normalized) -> maturity.
    """
    result: Dict[str, str] = {}

    async with httpx.AsyncClient(timeout=30.0, follow_redirects=True) as client:
        for label, landscape_url in (("CNCF", CNCF_LANDSCAPE_YAML_URL), ("LFAI", LFAI_LANDSCAPE_YAML_URL)):
            try:
                resp = await client.get(landscape_url)
                if resp.status_code == 200 and resp.text:
                    parsed = _extract_landscape_yaml_projects(resp.text)
                    result.update(parsed)
                    log_event(f"  [{label}] Loaded {len(parsed)} projects from canonical landscape.yml")
            except Exception as e:
                log_event(f"[WARN] {label} landscape.yml fetch failed: {str(e)[:100]}")

        # Fallback to GitHub topic search only if canonical YAML returned nothing
        if not result:
            headers = _github_headers()
            maturity_queries = {
                "graduated": "topic:cncf-graduated",
                "incubating": "topic:cncf-incubating",
                "sandbox": "topic:cncf-sandbox",
            }
            for maturity, query in maturity_queries.items():
                try:
                    url = f"{GITHUB_API_BASE}/search/repositories?q={query}&per_page=100"
                    resp = await client.get(url, headers=headers)
                    resp.raise_for_status()
                    data = resp.json()
                    for repo in data.get("items", []):
                        repo_url = repo.get("html_url", "")
                        if repo_url:
                            result[_normalize_repo_url(repo_url)] = maturity
                    log_event(f"  [CNCF-Fallback] {maturity}: {len(data.get('items', []))} repos found")
                except Exception as e:
                    log_event(f"[WARN] CNCF {maturity} search failed: {str(e)[:100]}")
                await asyncio.sleep(GITHUB_RATE_DELAY)

    log_event(f"[CNCF] Fetched {len(result)} total projects from CNCF & LFAI landscapes")
    return result


async def enrich_cncf_status(inventory: Dict) -> int:
    """Update inventory entries with cncf_status field and aligned maturity tags.

    - ``graduated`` -> ensures ``[DE FACTO STANDARD]``
    - ``incubating`` -> ensures ``[ENTERPRISE-STABLE]`` (unless already De Facto Standard)
    - ``sandbox`` -> ensures ``[EMERGING]`` (unless already higher tier)
    - ``archived`` -> ensures ``[LEGACY]``

    Returns count of entries updated.
    """
    landscape = await fetch_cncf_landscape()
    if not landscape:
        return 0

    updated = 0
    for url, entry in inventory.items():
        if url.startswith("INTRO:") or not isinstance(entry, dict):
            continue
        normalized = _normalize_repo_url(url)
        maturity = landscape.get(normalized)
        if not maturity:
            continue

        old_status = entry.get("cncf_status")
        entry["cncf_status"] = maturity
        if old_status != maturity:
            updated += 1

        tags = entry.get("tags")
        if not isinstance(tags, list):
            tags = []

        if maturity == "graduated" and "[DE FACTO STANDARD]" not in tags:
            tags.append("[DE FACTO STANDARD]")
            if "[COMMUNITY-TOOL]" in tags:
                tags.remove("[COMMUNITY-TOOL]")
        elif maturity == "incubating" and "[ENTERPRISE-STABLE]" not in tags and "[DE FACTO STANDARD]" not in tags:
            tags.append("[ENTERPRISE-STABLE]")
            if "[COMMUNITY-TOOL]" in tags:
                tags.remove("[COMMUNITY-TOOL]")
        elif maturity == "sandbox" and not any(t in tags for t in ("[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]", "[EMERGING]")):
            tags.append("[EMERGING]")
        elif maturity == "archived" and "[LEGACY]" not in tags:
            tags.append("[LEGACY]")

        entry["tags"] = tags

    log_event(f"[CNCF] Enriched {updated} inventory entries with CNCF/LFAI status")
    return updated


# ---------------------------------------------------------------------------
# Module 2: Social Signal & Velocity Enrichment (GitHub Activity)
# ---------------------------------------------------------------------------

async def _fetch_repo_activity(
    client: httpx.AsyncClient,
    owner_repo: str,
) -> Tuple[int, int, Optional[Dict]]:
    """Fetch open issue/PR count and velocity metadata for a single repo in one API call."""
    headers = _github_headers()
    open_issues = 0
    repo_meta: Optional[Dict] = None

    try:
        resp = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner_repo}",
            headers=headers,
            timeout=15.0,
        )
        if resp.status_code == 200:
            data = resp.json()
            open_issues = data.get("open_issues_count", 0)
            stars = int(data.get("stargazers_count") or 0)
            created_raw = data.get("created_at") or ""
            pushed_raw = data.get("pushed_at") or ""
            now = datetime.now(MADRID_TZ)
            try:
                created_dt = datetime.fromisoformat(created_raw.replace("Z", "+00:00"))
                age_months = max(1.0, (now - created_dt).days / 30.0)
            except Exception:
                age_months = 24.0
            repo_meta = {
                "gh_stars": stars,
                "gh_stars_per_month": round(stars / age_months, 2),
                "gh_pushed": pushed_raw[:10] if pushed_raw else None,
                "gh_archived": bool(data.get("archived", False)),
            }
        elif resp.status_code == 429:
            await asyncio.sleep(5.0)
    except Exception as e:
        log_event(f"[WARN] GitHub repo fetch failed for {owner_repo}: {str(e)[:120]}")

    await asyncio.sleep(GITHUB_RATE_DELAY)

    return open_issues, 0, repo_meta


def _classify_health(total_activity: int) -> str:
    """Classify community health based on combined issue + PR activity."""
    if total_activity > HEALTH_ACTIVE:
        return "active"
    if total_activity >= HEALTH_HEALTHY:
        return "healthy"
    if total_activity > 0:
        return "low"
    return "dormant"


async def enrich_github_activity(inventory: Dict, max_repos: int = MAX_REPOS_DEFAULT) -> int:
    """Fetch recent issue/PR velocity and star momentum for GitHub repos in the inventory.

    Adds fields:
    - ``gh_open_issues_30d``
    - ``gh_open_prs_30d``
    - ``gh_community_health`` ("active" | "healthy" | "low" | "dormant")
    - ``gh_stars_per_month`` (monthly star velocity)
    - ``momentum_score`` (0–100 composite momentum score)
    - ``gh_activity_checked`` (ISO timestamp)
    """
    candidates: List[Tuple[str, str]] = []

    for url, entry in inventory.items():
        if url.startswith("INTRO:") or not isinstance(entry, dict):
            continue
        repo = _parse_github_repo(url)
        if not repo:
            continue
        if not _is_activity_stale(entry):
            continue
        candidates.append((url, repo))
        if len(candidates) >= max_repos:
            break

    if not candidates:
        log_event("[Activity] No GitHub repos require activity enrichment")
        return 0

    log_event(f"[Activity] Enriching {len(candidates)} GitHub repos (max {max_repos})")

    enriched = 0
    now = datetime.now(MADRID_TZ)
    async with httpx.AsyncClient() as client:
        for url, owner_repo in candidates:
            try:
                open_issues, open_prs, repo_meta = await _fetch_repo_activity(client, owner_repo)
                total = open_issues + open_prs
                health = _classify_health(total)

                entry = inventory[url]
                entry["gh_open_issues_30d"] = open_issues
                entry["gh_open_prs_30d"] = open_prs
                entry["gh_community_health"] = health
                if repo_meta:
                    entry["gh_stars"] = repo_meta["gh_stars"]
                    entry["gh_stars_per_month"] = repo_meta["gh_stars_per_month"]
                    if repo_meta.get("gh_pushed"):
                        entry["gh_pushed"] = repo_meta["gh_pushed"]
                    if repo_meta.get("gh_archived"):
                        tags = entry.get("tags")
                        if isinstance(tags, list) and "[LEGACY]" not in tags:
                            tags.append("[LEGACY]")
                            entry["tags"] = tags
                entry["momentum_score"] = compute_momentum_score(entry, now)
                entry["gh_activity_checked"] = now.isoformat()
                enriched += 1
            except Exception as e:
                log_event(f"[WARN] Activity enrichment failed for {owner_repo}: {str(e)[:150]}")

    log_event(f"[Activity] Enriched {enriched}/{len(candidates)} repos with community health & velocity data")
    return enriched


# ---------------------------------------------------------------------------
# Module 3: License Change Detection
# ---------------------------------------------------------------------------

async def _fetch_current_license(
    client: httpx.AsyncClient,
    owner_repo: str,
) -> Optional[str]:
    """Fetch the current SPDX license identifier for a GitHub repo."""
    headers = _github_headers()
    try:
        resp = await client.get(
            f"{GITHUB_API_BASE}/repos/{owner_repo}",
            headers=headers,
            timeout=15.0,
        )
        if resp.status_code == 200:
            data = resp.json()
            lic = data.get("license")
            if isinstance(lic, dict):
                return lic.get("spdx_id", "N/A")
            return "N/A"
        elif resp.status_code == 404:
            return None
    except Exception as e:
        log_event(f"[WARN] License fetch failed for {owner_repo}: {str(e)[:120]}")
    return None


async def detect_license_changes(inventory: Dict) -> List[Dict]:
    """Compare current gh_license with stored license, flag changes."""
    candidates: List[Tuple[str, str, Dict]] = []

    for url, entry in inventory.items():
        if url.startswith("INTRO:") or not isinstance(entry, dict):
            continue
        if not entry.get("gh_license") or entry["gh_license"] == "N/A":
            continue
        repo = _parse_github_repo(url)
        if not repo:
            continue
        candidates.append((url, repo, entry))

    if not candidates:
        log_event("[License] No repos with stored licenses to check")
        return []

    candidates = candidates[:MAX_REPOS_DEFAULT]
    log_event(f"[License] Checking {len(candidates)} repos for license changes")

    changes: List[Dict] = []
    async with httpx.AsyncClient() as client:
        for url, owner_repo, entry in candidates:
            try:
                current = await _fetch_current_license(client, owner_repo)
                if current is None:
                    continue

                stored = entry.get("gh_license", "N/A")
                if current != stored:
                    change_record = {
                        "url": url,
                        "old_license": stored,
                        "new_license": current,
                        "title": entry.get("title", url),
                    }
                    changes.append(change_record)
                    entry["gh_license_previous"] = stored
                    entry["gh_license"] = current
                    log_event(
                        f"[License] Change detected: {owner_repo} "
                        f"{stored} -> {current}"
                    )
            except Exception as e:
                log_event(f"[WARN] License check failed for {owner_repo}: {str(e)[:150]}")

            await asyncio.sleep(GITHUB_RATE_DELAY)

    log_event(f"[License] Detected {len(changes)} license change(s)")
    return changes


# ---------------------------------------------------------------------------
# Full Enrichment Pipeline
# ---------------------------------------------------------------------------

async def run_enrichment():
    """Full enrichment pipeline: CNCF/LFAI + GitHub velocity/activity + license detection."""
    from src.inventory_manager import load_inventory, save_inventory

    log_event("ENRICHMENT PIPELINE STARTING", section_break=True)
    inventory = load_inventory()
    log_event(f"[*] Loaded {len(inventory)} inventory entries")

    cncf_count = await enrich_cncf_status(inventory)
    activity_count = await enrich_github_activity(inventory)
    license_changes = await detect_license_changes(inventory)

    save_inventory(inventory)
    log_event(
        f"Enrichment complete: {cncf_count} CNCF/LFAI, "
        f"{activity_count} activity/velocity, "
        f"{len(license_changes)} license changes",
        section_break=True,
    )

    return license_changes


if __name__ == "__main__":
    asyncio.run(run_enrichment())
