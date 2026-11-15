"""Audits critical ([DE FACTO STANDARD] / [ENTERPRISE-STABLE]) inventory links."""

import argparse
import asyncio
from collections import defaultdict
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlsplit
import httpx

from src.config import MADRID_TZ
from src.inventory_manager import load_inventory, save_inventory

CRITICAL_TAGS = {"[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]"}
DEAD_CODES = {404, 410}
RETRY_WITH_GET_CODES = {403, 404, 405, 410, 501}
TRANSIENT_CODES = {429, 502, 503, 504}
HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36"
    ),
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
}


async def _request_with_backoff(
    client: httpx.AsyncClient,
    method: str,
    url: str,
    max_retries: int = 2,
) -> httpx.Response:
    """Issues an HTTP request with polite backoff on transient 429/5xx responses."""
    for attempt in range(max_retries + 1):
        resp = await client.request(method, url)
        if resp.status_code not in TRANSIENT_CODES or attempt == max_retries:
            return resp
        retry_after = resp.headers.get("Retry-After")
        delay = float(retry_after) if retry_after and retry_after.isdigit() else (1.5 * (attempt + 1))
        await asyncio.sleep(min(delay, 10.0))
    return resp


async def _probe_url(
    client: httpx.AsyncClient,
    global_sem: asyncio.Semaphore,
    host_sems: Dict[str, asyncio.Semaphore],
    url: str,
) -> Tuple[str, Optional[int]]:
    """Checks URL liveliness with per-host throttling and GET confirmation for 404/410."""
    host = urlsplit(url).netloc.lower()
    async with global_sem, host_sems[host]:
        try:
            resp = await _request_with_backoff(client, "HEAD", url)
            status = resp.status_code
            if status in RETRY_WITH_GET_CODES:
                resp = await _request_with_backoff(client, "GET", url)
                status = resp.status_code
            return url, status
        except httpx.HTTPError:
            return url, None


def _select_critical_urls(inv: Dict) -> List[Tuple[str, str]]:
    """Returns (url, current_status) for critical tagged entries."""
    selected: List[Tuple[str, str]] = []
    for url, data in inv.items():
        if not isinstance(data, dict) or not str(url).startswith("http"):
            continue
        tags = data.get("tags") or []
        if any(t in CRITICAL_TAGS for t in tags):
            selected.append((url, str(data.get("status") or "online")))
    return selected


def _build_markdown_report(
    total_audited: int,
    newly_offline: List[Tuple[str, int]],
    recovered: List[Tuple[str, int]],
    already_offline: List[str],
) -> str:
    """Formats a concise Markdown report summarizing critical asset health changes."""
    lines = [
        "### 🚨 Critical Asset Health Audit",
        "",
        f"- **Critical assets audited**: {total_audited}",
        f"- **Newly offline (HTTP 404/410 confirmed)**: {len(newly_offline)}",
        f"- **Recovered back online**: {len(recovered)}",
        f"- **Previously offline (unchanged)**: {len(already_offline)}",
        "",
    ]
    if newly_offline:
        lines.append("#### ❌ Newly Offline Assets")
        lines.append("")
        lines.append("| HTTP Status | URL |")
        lines.append("| :---: | :--- |")
        for url, code in newly_offline:
            lines.append(f"| `{code}` | {url} |")
        lines.append("")

    if recovered:
        lines.append("#### ✅ Recovered Assets")
        lines.append("")
        lines.append("| HTTP Status | URL |")
        lines.append("| :---: | :--- |")
        for url, code in recovered:
            lines.append(f"| `{code}` | {url} |")
        lines.append("")

    return "\n".join(lines).strip() + "\n"


async def run_audit(
    dry_run: bool = False,
    concurrency: int = 20,
    per_host: int = 2,
    report_file: Optional[str] = None,
) -> int:
    """Audits all critical URLs, updates inventory SQL+YAML on changes, and emits a report."""
    inv = load_inventory()
    targets = _select_critical_urls(inv)
    print(f"[*] Auditing {len(targets)} critical assets (concurrency={concurrency}, per_host={per_host})...")

    global_sem = asyncio.Semaphore(concurrency)
    host_sems: Dict[str, asyncio.Semaphore] = defaultdict(lambda: asyncio.Semaphore(per_host))
    limits = httpx.Limits(max_connections=concurrency + 10, max_keepalive_connections=concurrency)
    timeout = httpx.Timeout(12.0, connect=6.0)

    async with httpx.AsyncClient(
        headers=HEADERS,
        timeout=timeout,
        follow_redirects=True,
        limits=limits,
    ) as client:
        results = await asyncio.gather(
            *(_probe_url(client, global_sem, host_sems, url) for url, _ in targets)
        )

    status_map = dict(results)
    now_iso = datetime.now(MADRID_TZ).isoformat()

    newly_offline: List[Tuple[str, int]] = []
    recovered: List[Tuple[str, int]] = []
    already_offline: List[str] = []

    for url, prev_status in targets:
        code = status_map.get(url)
        if code in DEAD_CODES:
            if prev_status in ("offline", "review_required"):
                already_offline.append(url)
            else:
                newly_offline.append((url, code))
                inv[url]["status"] = "offline"
                inv[url]["last_offline"] = now_iso
                inv[url]["health_score"] = 0.0
        elif code is not None and 200 <= code < 400 and prev_status in ("offline", "dead"):
            recovered.append((url, code))
            inv[url]["status"] = "online"
            inv[url]["health_score"] = 100.0
        elif prev_status == "offline":
            already_offline.append(url)

    for url, code in newly_offline:
        print(f"  [!] NEWLY OFFLINE ({code}): {url}")
    for url, code in recovered:
        print(f"  [+] RECOVERED ({code}): {url}")

    report = _build_markdown_report(len(targets), newly_offline, recovered, already_offline)
    if report_file:
        with open(report_file, "w", encoding="utf-8") as f:
            f.write(report)

    changed = bool(newly_offline or recovered)
    if changed and not dry_run:
        save_inventory(inv)
        print(
            f"[OK] Saved data/inventory.sql and data/inventory.yaml "
            f"({len(newly_offline)} newly offline, {len(recovered)} recovered)."
        )
    elif changed:
        print(
            f"[DRY-RUN] Detected {len(newly_offline)} newly offline and "
            f"{len(recovered)} recovered (inventory not written)."
        )
    else:
        print("[OK] No critical asset status changes detected.")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit critical inventory assets.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write inventory files.")
    parser.add_argument("--concurrency", type=int, default=20, help="Concurrent HTTP probes.")
    parser.add_argument("--report-file", type=str, default=None, help="Optional Markdown report path.")
    args = parser.parse_args()
    return asyncio.run(
        run_audit(
            dry_run=args.dry_run,
            concurrency=args.concurrency,
            report_file=args.report_file,
        )
    )


if __name__ == "__main__":
    raise SystemExit(main())
