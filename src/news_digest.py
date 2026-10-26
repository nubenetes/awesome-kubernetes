from __future__ import annotations

import os
import json
import hashlib
import asyncio
from datetime import datetime, timedelta
from typing import Dict, List, Any, Tuple

from src.inventory_manager import load_inventory
from src.gemini_utils import call_gemini_with_retry
from src.config import MADRID_TZ
from src.logger import log_event

DIGEST_OUTPUT_PATH = "data/news_digest.json"

# Refresh a cell even when hash matches if last_analyzed is older than this.
# Ensures Gemini rankings stay fresh even for stable categories.
MAX_STALENESS_DAYS = 30


class NewsDigestEngine:
    """Generates a curated news digest by filtering inventory entries by
    recency and using Gemini AI to rank the most relevant ones per category.

    Three time windows (3 / 6 / 12 months) are produced in a single run.
    Each window contains up to 10 AI-ranked items per digest category.
    """

    # ------------------------------------------------------------------ #
    # 26 Digest Categories – mapped from V2 category slugs               #
    # ------------------------------------------------------------------ #
    DIGEST_CATEGORIES: Dict[str, List[str]] = {
        # --- TECH CORE (9) ---
        "Kubernetes & Orchestration": [
            "kubernetes", "kubernetes-tools", "kubernetes-tutorials",
            "kubectl-commands", "kubernetes-releases", "kubernetes-autoscaling",
            "kubernetes-operators-controllers", "kubernetes-based-devel",
            "kubernetes-alternatives", "kubernetes-client-libraries",
            "kubernetes-bigdata", "managed-kubernetes-in-public-cloud", "helm",
        ],
        "Containers & Runtime": [
            "docker", "container-managers", "serverless", "noops", "registries",
        ],
        "Networking & Service Mesh": [
            "networking", "kubernetes-networking", "servicemesh", "istio",
            "caching", "web-servers", "cloudflare",
        ],
        "Architecture & Microservices": [
            "introduction", "faq", "cloud-arch-diagrams", "matrix-table",
            "other-awesome-lists", "about",
        ],
        "Data, Messaging & Storage": [
            "databases", "nosql", "newsql", "message-queue", "crunchydata",
            "yaml", "kubernetes-storage", "kubernetes-backup-migrations",
        ],
        "AI & Agents": [
            "ai", "ai-agents-mcp", "chatgpt",
        ],
        "MLOps & Data Science": [
            "mlops",
        ],
        "Python, Java & Developer Ecosystem": [
            "python", "golang", "java_frameworks", "java_app_servers",
            "java-and-java-performance-optimization", "javascript", "dotnet",
            "angular", "react", "web3", "api",
            "swagger-code-generator-for-rest-apis", "postman",
            "lowcode-nocode", "devel-sites", "dom", "linux-dev-env",
            "ChromeDevTools", "xamarin", "jvm-parameters-matrix-table",
            "maven-gradle", "embedded-servlet-containers", "visual-studio",
        ],
        "Linux & System Foundations": [
            "linux", "git",
        ],
        # --- PLATFORM & OPS (8) ---
        "Security & Compliance": [
            "securityascode", "kubernetes-security", "aws-security", "oauth",
            "devsecops",
        ],
        "Infrastructure as Code": [
            "iac", "terraform", "pulumi", "crossplane", "ansible",
            "kustomize", "chef", "liquibase",
        ],
        "CI/CD & GitOps": [
            "cicd", "gitops", "argo", "flux", "tekton", "jenkins",
            "jenkins-alternatives", "sonarqube", "cicd-kubernetes-plugins",
            "openshift-pipelines", "stackstorm", "keptn",
        ],
        "Observability, SRE & Testing": [
            "sre", "monitoring", "prometheus", "grafana",
            "kubernetes-monitoring", "chaos-engineering", "qa",
            "test-automation-frameworks", "testops",
            "performance-testing-with-jenkins-and-jmeter",
            "kubernetes-troubleshooting",
        ],
        "DevOps & Culture": [
            "devops", "devops-tools", "project-management-methodology",
            "project-management-tools",
        ],
        "Platform Engineering & DevEx": [
            "developerportals", "scaffolding", "mkdocs",
        ],
        "FinOps & Cloud Cost": [
            "finops", "aws-pricing",
        ],
        "Certification & Training": [
            "elearning", "interview-questions", "aws-training", "cheatsheets",
            "demos",
        ],
        # --- CLOUD & ENTERPRISE (5) ---
        "AWS": [
            "aws", "aws-architecture", "aws-security", "aws-networking",
            "aws-databases", "aws-storage", "aws-monitoring", "aws-iac",
            "aws-tools-scripts", "aws-messaging", "aws-data", "aws-devops",
            "aws-serverless", "aws-containers", "aws-backup",
            "aws-newfeatures", "aws-miscellaneous", "aws-spain",
        ],
        "Azure": [
            "azure",
        ],
        "GCP, OCI & Others": [
            "GoogleCloudPlatform", "ibm_cloud", "oraclecloud",
            "digitalocean", "scaleway", "edge-computing",
            "public-cloud-solutions",
        ],
        "OpenShift / Red Hat": [
            "openshift", "ocp3", "ocp4", "openshift-pipelines", "rancher",
        ],
        "Virtualization & Private Cloud": [
            "kubernetes-on-premise", "kubernetes-alternatives",
            "private-cloud-solutions",
        ],
        # --- INDUSTRY / GEO (4) – resolved via geo_region, not slugs ---
        "Americas": [],
        "Europe": [],
        "Spain": [],
        "Asia-Pacific": [],
    }

    GEO_CATEGORIES: Dict[str, str] = {
        "Americas": "americas",
        "Europe": "europe",
        "Spain": "spain",
        "Asia-Pacific": "asia_pacific",
    }

    PERIODS: Dict[str, int] = {
        "3_months": 90,
        "6_months": 180,
        "12_months": 365,
    }

    ITEMS_PER_PERIOD: Dict[str, int] = {
        "3_months": 10,
        "6_months": 15,
        "12_months": 20,
    }

    # ------------------------------------------------------------------ #

    def __init__(self) -> None:
        self.inventory: Dict[str, Any] = load_inventory()

        # Reverse map: v2_category_slug -> digest_category_name
        self.category_map: Dict[str, str] = {}
        for digest_cat, slugs in self.DIGEST_CATEGORIES.items():
            for slug in slugs:
                self.category_map[slug] = digest_cat

    # ------------------------------------------------------------------ #
    # Classification helpers                                              #
    # ------------------------------------------------------------------ #

    def _get_entry_category(self, entry: dict) -> str | None:
        """Determine which digest category an entry belongs to.

        Checks ``v2_locations`` paths first (more specific), then falls
        back to the ``category`` field.
        """
        for loc in (entry.get("v2_locations") or []):
            if not loc or not isinstance(loc, str):
                continue
            slug = loc.replace(".md", "")
            if slug in self.category_map:
                return self.category_map[slug]
        cat = entry.get("category") or ""
        if cat in self.category_map:
            return self.category_map[cat]
        return None

    def _get_entry_geo(self, entry: dict, url: str = "") -> str | None:
        """Return the geo digest category using geo_region field, falling back to URL TLD inference."""
        region = entry.get("geo_region") or ""
        for geo_name, geo_val in self.GEO_CATEGORIES.items():
            if region == geo_val:
                return geo_name
        # Fallback: infer from URL TLD (entry.get("url") populated only after url injection)
        return self._infer_geo_from_url(str(entry.get("url") or url or ""))

    @staticmethod
    def _infer_geo_from_url(url: str) -> str | None:
        """Infer geo category from URL TLD. Returns GEO_CATEGORIES key or None."""
        try:
            from urllib.parse import urlparse
            host = urlparse(url).hostname or ""
            # Ordered longest-first to avoid .uk matching before .co.uk
            tld_to_region = [
                (".com.au", "Asia-Pacific"), (".co.uk", "Europe"), (".co.jp", "Asia-Pacific"),
                (".co.kr", "Asia-Pacific"), (".com.br", "Americas"), (".com.mx", "Americas"),
                (".es", "Spain"), (".de", "Europe"), (".fr", "Europe"), (".it", "Europe"),
                (".pt", "Europe"), (".nl", "Europe"), (".be", "Europe"), (".se", "Europe"),
                (".dk", "Europe"), (".fi", "Europe"), (".no", "Europe"), (".ch", "Europe"),
                (".at", "Europe"), (".pl", "Europe"), (".cz", "Europe"), (".uk", "Europe"),
                (".ie", "Europe"), (".eu", "Europe"), (".cn", "Asia-Pacific"),
                (".jp", "Asia-Pacific"), (".kr", "Asia-Pacific"), (".sg", "Asia-Pacific"),
                (".in", "Asia-Pacific"), (".au", "Asia-Pacific"), (".nz", "Asia-Pacific"),
                (".ca", "Americas"), (".mx", "Americas"), (".br", "Americas"),
            ]
            for tld, region in tld_to_region:
                if host.endswith(tld):
                    return region
        except Exception:
            pass
        return None

    @staticmethod
    def _is_within_period(entry: dict, cutoff_iso: str) -> bool:
        """Check if entry falls within the time period using discovered_at,
        with year field as fallback for backfilled entries."""
        discovered = entry.get("discovered_at") or ""
        if discovered:
            try:
                if str(discovered) >= cutoff_iso:
                    return True
            except Exception:
                pass
        year = entry.get("year")
        if year is not None:
            year_str = str(year).strip()
            if year_str.isdigit():
                cutoff_year = cutoff_iso[:4] if len(cutoff_iso) >= 4 else "2020"
                return year_str >= cutoff_year
        return False

    # ------------------------------------------------------------------ #
    # Prompt builder                                                      #
    # ------------------------------------------------------------------ #

    @staticmethod
    def _build_ranking_prompt(
        category: str, entries: List[dict], period: str
    ) -> str:
        """Assemble the Gemini prompt that asks for a ranked TOP-10."""
        period_label = period.replace("_", " ")
        lines: List[str] = []
        for i, e in enumerate(entries[:50]):
            summary_fragment = str(e.get("ai_summary") or "")[:200]
            lines.append(
                f'{i}. "{e.get("title") or "Unknown"}" '
                f'({e.get("url") or ""}) | '
                f'Stars: {e.get("stars") or 0} | '
                f'Year: {e.get("year") or "N/A"} | '
                f'Summary: {summary_fragment}'
            )
        entries_text = "\n".join(lines)

        return (
            "You are a Senior Technical Curator for a Cloud Native "
            "knowledge portal.\n"
            f'Given these resources discovered in the last {period_label} '
            f'for "{category}", select the TOP 10 most relevant.\n\n'
            "SCORING CRITERIA:\n"
            "- Industry Impact (30%): Does this change how teams "
            "build/operate?\n"
            "- Technical Novelty (25%): New capability, paradigm shift, "
            "major release?\n"
            "- Enterprise Adoption (20%): GA releases, production-ready?\n"
            "- Community Signal (15%): CNCF graduations, major blog posts?\n"
            "- Nubenetes Relevance (10%): Directly related to cloud native?\n\n"
            'Respond ONLY JSON: {"items": [{"idx": int, '
            '"impact": "critical|high|medium", '
            '"why": "1 sentence explaining why this matters"}]}\n\n'
            f"RESOURCES:\n{entries_text}"
        )

    @staticmethod
    def _extract_entry_date(e: dict) -> str:
        """Extract a 10-char date string (YYYY-MM-DD or YYYY) safely from an entry."""
        discovered = e.get("discovered_at")
        if discovered and isinstance(discovered, str):
            return discovered[:10]
        gh_pushed = e.get("gh_pushed")
        if gh_pushed and isinstance(gh_pushed, str):
            return gh_pushed[:10]
        year = e.get("year")
        if year is not None:
            year_str = str(year).strip()
            if year_str.isdigit() and len(year_str) == 4:
                return year_str
        return ""

    # ------------------------------------------------------------------ #
    # Star-based fallback (used when Gemini is unavailable / < 3 entries) #
    # ------------------------------------------------------------------ #

    @classmethod
    def _fallback_items(
        cls, entries: List[dict], cat_name: str, limit: int = 10
    ) -> List[dict]:
        """Return up to *limit* items using a deterministic star-based
        ranking (no AI call required)."""
        return [
            {
                "url": e.get("url") or "",
                "title": e.get("title") or "Unknown",
                "date": cls._extract_entry_date(e),
                "stars": e.get("stars") or 0,
                "impact": "high" if (e.get("stars") or 0) >= 4 else "medium",
                "why": str(e.get("ai_summary") or "")[:200],
                "category": cat_name,
            }
            for e in entries[:limit]
        ]

    # ------------------------------------------------------------------ #
    # Incremental cache helpers                                           #
    # ------------------------------------------------------------------ #

    @staticmethod
    def _compute_pool_hash(entries: List[dict]) -> str:
        """Stable fingerprint of a category entry pool.

        Uses sorted URLs so the hash only changes when the actual set of
        entries changes — not when their order or metadata is updated.
        Returns first 16 hex chars (64-bit fingerprint, collision-safe).
        """
        sorted_urls = sorted(e["url"] for e in entries if e.get("url"))
        return hashlib.sha256("|".join(sorted_urls).encode()).hexdigest()[:16]

    def _load_existing_digest(self) -> Tuple[dict, dict]:
        """Load existing digest + meta block from disk.

        Returns ``(periods_dict, meta_dict)``. Both are empty dicts if the
        file does not exist or cannot be parsed.  The ``_meta`` key is
        stripped from *periods_dict* so callers only see period data.
        """
        if not os.path.exists(DIGEST_OUTPUT_PATH):
            return {}, {}
        try:
            with open(DIGEST_OUTPUT_PATH, encoding="utf-8") as f:
                raw = json.load(f)
            meta = raw.pop("_meta", {})
            return raw, meta
        except Exception as e:
            log_event(
                f"[Digest WARN] Could not load existing digest: {str(e)[:100]}"
            )
            return {}, {}

    def _is_cache_valid(
        self, period: str, cat: str, pool_hash: str, meta: dict
    ) -> bool:
        """Return True when the stored result can be reused without Gemini.

        Conditions (both must hold):
        1. Entry-pool hash matches (same URLs, same period).
        2. Result was analysed no more than MAX_STALENESS_DAYS ago.
        """
        if not isinstance(meta, dict):
            return False
        period_meta = meta.get(period)
        if not isinstance(period_meta, dict):
            return False
        cell = period_meta.get(cat)
        if not isinstance(cell, dict):
            return False
        if cell.get("entry_hash") != pool_hash:
            return False
        last = cell.get("last_analyzed") or ""
        if not last:
            return False
        try:
            age = (
                datetime.now(MADRID_TZ) - datetime.fromisoformat(str(last))
            ).days
            return age <= MAX_STALENESS_DAYS
        except Exception:
            return False

    # ------------------------------------------------------------------ #
    # Core generation loop                                                #
    # ------------------------------------------------------------------ #

    async def generate_digest(self) -> dict:
        """Incrementally generate the digest for all categories / periods.

        For each (category, period) cell the engine checks whether the
        inventory pool hash has changed since the last run.  If the hash
        is identical *and* the result is not stale, the existing ranked
        list is reused with zero Gemini API calls.  Gemini is only invoked
        for cells whose entry pool has actually changed or exceeded
        MAX_STALENESS_DAYS.

        Returns a nested dict::

            {
                "3_months": { "Kubernetes & Orchestration": [...], ... },
                "6_months": { ... },
                "12_months": { ... },
                "_meta": { ... }   ← persistence metadata, internal use
            }
        """
        existing, old_meta = self._load_existing_digest()
        new_meta: Dict[str, Dict[str, dict]] = {}
        digest: Dict[str, Dict[str, List[dict]]] = {}

        n_cached = n_refreshed = n_fallback = 0

        for period_name, days in self.PERIODS.items():
            cutoff = (
                datetime.now(MADRID_TZ) - timedelta(days=days)
            ).isoformat()
            digest[period_name] = {}
            new_meta[period_name] = {}

            # Build per-category entry pools for this period
            category_pools: Dict[str, List[dict]] = {}
            for url, entry in self.inventory.items():
                if not isinstance(entry, dict):
                    continue
                if not self._is_within_period(entry, cutoff):
                    continue
                cat = self._get_entry_category(entry)
                if cat:
                    category_pools.setdefault(cat, []).append(
                        dict(entry, url=url)
                    )
                geo = self._get_entry_geo(entry, url=url)
                if geo:
                    category_pools.setdefault(geo, []).append(
                        dict(entry, url=url)
                    )

            for cat_name, entries in category_pools.items():
                entries.sort(
                    key=lambda x: (
                        x.get("stars") or 0,
                        str(x.get("discovered_at") or ""),
                    ),
                    reverse=True,
                )
                max_items = self.ITEMS_PER_PERIOD.get(period_name, 10)
                pool_hash = self._compute_pool_hash(entries)

                # ── Cache hit: reuse without calling Gemini ──
                if self._is_cache_valid(period_name, cat_name, pool_hash, old_meta):
                    cached_items = existing.get(period_name, {}).get(cat_name, [])
                    if cached_items:
                        digest[period_name][cat_name] = cached_items
                        new_meta[period_name][cat_name] = (
                            old_meta[period_name][cat_name]
                        )
                        n_cached += 1
                        continue

                # ── Fewer than 3 entries: star-based fallback (no AI) ──
                if len(entries) < 3:
                    digest[period_name][cat_name] = self._fallback_items(
                        entries, cat_name, limit=max_items
                    )
                    new_meta[period_name][cat_name] = {
                        "last_analyzed": datetime.now(MADRID_TZ).isoformat(),
                        "entry_hash": pool_hash,
                        "entry_count": len(entries),
                        "method": "fallback_small",
                    }
                    n_fallback += 1
                    continue

                # ── Gemini ranking ──
                try:
                    prompt = self._build_ranking_prompt(
                        cat_name, entries, period_name
                    )
                    result = await call_gemini_with_retry(
                        prompt, prefer_flash=True, role="Digest-Analyst"
                    )
                    ranked: List[dict] = []
                    for item in result.get("items", []):
                        if not isinstance(item, dict):
                            continue
                        try:
                            idx = int(item.get("idx", -1))
                        except (ValueError, TypeError):
                            continue
                        if 0 <= idx < len(entries):
                            e = entries[idx]
                            ranked.append(
                                {
                                    "url": e.get("url") or "",
                                    "title": e.get("title") or "Unknown",
                                    "date": self._extract_entry_date(e),
                                    "stars": e.get("stars") or 0,
                                    "impact": item.get("impact") or "medium",
                                    "why": str(item.get("why") or "")[:200],
                                    "category": cat_name,
                                }
                            )
                    digest[period_name][cat_name] = ranked[:max_items]
                    new_meta[period_name][cat_name] = {
                        "last_analyzed": datetime.now(MADRID_TZ).isoformat(),
                        "entry_hash": pool_hash,
                        "entry_count": len(entries),
                        "method": "gemini",
                    }
                    n_refreshed += 1
                    log_event(
                        f"  [Digest] {period_name}/{cat_name}: "
                        f"{len(ranked)} items ranked (Gemini)"
                    )
                except Exception as exc:
                    log_event(
                        f"  [Digest WARN] {period_name}/{cat_name}: "
                        f"Gemini failed ({str(exc)[:80]}), using fallback"
                    )
                    digest[period_name][cat_name] = self._fallback_items(
                        entries, cat_name, limit=max_items
                    )
                    new_meta[period_name][cat_name] = {
                        "last_analyzed": datetime.now(MADRID_TZ).isoformat(),
                        "entry_hash": pool_hash,
                        "entry_count": len(entries),
                        "method": "fallback_error",
                    }
                    n_fallback += 1

                await asyncio.sleep(1.0)

        log_event(
            f"[Digest] {n_cached} cells reused (0 API calls), "
            f"{n_refreshed} refreshed via Gemini, "
            f"{n_fallback} fallback"
        )
        new_meta["last_updated"] = datetime.now(MADRID_TZ).isoformat()
        digest["_meta"] = new_meta
        return digest

    # ------------------------------------------------------------------ #
    # Persistence                                                         #
    # ------------------------------------------------------------------ #

    @staticmethod
    def save_digest(digest: dict) -> None:
        """Serialise digest (including ``_meta``) to ``data/news_digest.json``."""
        os.makedirs(os.path.dirname(DIGEST_OUTPUT_PATH), exist_ok=True)
        with open(DIGEST_OUTPUT_PATH, "w", encoding="utf-8") as fh:
            json.dump(digest, fh, indent=2, ensure_ascii=False)
        # Count only period keys for the total-items stat
        total_items = sum(
            len(items)
            for key, period in digest.items()
            if key != "_meta" and isinstance(period, dict)
            for items in period.values()
            if isinstance(items, list)
        )
        gemini_cells = sum(
            1
            for period_meta in digest.get("_meta", {}).values()
            if isinstance(period_meta, dict)
            for cell in period_meta.values()
            if isinstance(cell, dict) and cell.get("method") == "gemini"
        )
        log_event(
            f"[Digest] Saved to {DIGEST_OUTPUT_PATH} — "
            f"{total_items} items, {gemini_cells} Gemini calls this run"
        )


# ====================================================================== #
# CLI / CI entry point                                                    #
# ====================================================================== #


async def run_news_digest() -> None:
    """Entry point for the CI pipeline."""
    log_event("STARTING NEWS DIGEST GENERATION", section_break=True)
    engine = NewsDigestEngine()
    digest = await engine.generate_digest()
    engine.save_digest(digest)

    total_items = sum(
        len(items)
        for key, period in digest.items()
        if key != "_meta" and isinstance(period, dict)
        for items in period.values()
        if isinstance(items, list)
    )
    log_event(
        f"NEWS DIGEST COMPLETE: {total_items} total items across all periods"
    )


if __name__ == "__main__":
    asyncio.run(run_news_digest())
