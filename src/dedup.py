from __future__ import annotations

import re
import asyncio
from collections import defaultdict
from difflib import SequenceMatcher
from typing import Dict, List, Tuple
from urllib.parse import urlparse, parse_qs, urlencode, urlunparse

from src.inventory_manager import load_inventory, save_inventory
from src.logger import log_event

TRACKING_PARAMS = {"utm_source", "utm_medium", "utm_campaign", "utm_content", "utm_term",
                   "ref", "source", "fbclid", "gclid", "mc_cid", "mc_eid", "s", "share"}


def normalize_url_deep(url: str) -> str:
    parsed = urlparse(url.strip().lower())
    scheme = "https"
    netloc = parsed.netloc.removeprefix("www.")
    path = parsed.path.rstrip("/") or "/"
    params = parse_qs(parsed.query)
    clean_params = {k: v for k, v in params.items() if k not in TRACKING_PARAMS}
    query = urlencode(clean_params, doseq=True) if clean_params else ""
    return urlunparse((scheme, netloc, path, "", query, ""))


def normalize_title(title: str) -> str:
    if not title:
        return ""
    t = title.lower().strip()
    t = re.sub(r'^[\w.-]+\.\w{2,}:\s*', '', t)
    t = re.sub(r'[^\w\s]', ' ', t)
    t = re.sub(r'\s+', ' ', t).strip()
    return t


def find_url_duplicates(inventory: Dict) -> List[Tuple[str, str]]:
    norm_map = defaultdict(list)
    for url in inventory:
        if not isinstance(inventory[url], dict):
            continue
        deep = normalize_url_deep(url)
        norm_map[deep].append(url)

    duplicates = []
    for norm, urls in norm_map.items():
        if len(urls) > 1:
            for i in range(1, len(urls)):
                duplicates.append((urls[0], urls[i]))
    return duplicates


def find_hash_duplicates(inventory: Dict) -> List[List[str]]:
    hash_map = defaultdict(list)
    for url, entry in inventory.items():
        if not isinstance(entry, dict):
            continue
        ch = entry.get("content_hash")
        if ch and ch != "N/A":
            hash_map[ch].append(url)
    return [urls for urls in hash_map.values() if len(urls) > 1]


def find_title_duplicates(inventory: Dict, threshold: float = 0.85) -> List[Tuple[str, str, float]]:
    entries = []
    for url, entry in inventory.items():
        if not isinstance(entry, dict):
            continue
        title = entry.get("title", "")
        norm = normalize_title(title)
        if len(norm) < 10:
            continue
        entries.append((url, norm, entry.get("stars") or 0))

    log_event(f"[Dedup] Building title index for {len(entries)} entries...")

    prefix_groups = defaultdict(list)
    for url, norm, stars in entries:
        words = norm.split()
        prefix = " ".join(words[:3]) if len(words) >= 3 else norm
        prefix_groups[prefix].append((url, norm, stars))

    duplicates = []
    checked = 0
    for prefix, group in prefix_groups.items():
        if len(group) < 2:
            continue
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                url1, norm1, stars1 = group[i]
                url2, norm2, stars2 = group[j]
                if stars1 >= 4 and stars2 >= 4:
                    continue
                ratio = SequenceMatcher(None, norm1, norm2).ratio()
                if ratio >= threshold:
                    duplicates.append((url1, url2, ratio))
        checked += 1
        if checked % 500 == 0:
            log_event(f"[Dedup] Checked {checked}/{len(prefix_groups)} prefix groups...")

    log_event(f"[Dedup] Title scan complete: {len(duplicates)} potential duplicates found")
    return duplicates


def _entry_score(entry: Dict) -> Tuple:
    return (
        entry.get("stars") or 0,
        1 if entry.get("ai_summary") else 0,
        1 if entry.get("hierarchy") else 0,
        len(entry.get("tags", [])),
        -len(str(entry.get("url", "")))
    )


def resolve_duplicates(inventory: Dict, duplicate_pairs: List[Tuple[str, str, float]]) -> int:
    resolved = 0
    seen = set()

    for url1, url2, score in sorted(duplicate_pairs, key=lambda x: -x[2]):
        if url1 in seen or url2 in seen:
            continue

        entry1 = inventory.get(url1, {})
        entry2 = inventory.get(url2, {})

        if not isinstance(entry1, dict) or not isinstance(entry2, dict):
            continue

        score1 = _entry_score(entry1)
        score2 = _entry_score(entry2)

        if score1 >= score2:
            winner, loser = url1, url2
        else:
            winner, loser = url2, url1

        inventory[loser]["status"] = "duplicate"
        inventory[loser]["duplicate_of"] = winner
        seen.add(loser)
        resolved += 1

    return resolved


async def run_dedup(dry_run: bool = True) -> Dict:
    log_event("STARTING DEDUPLICATION SCAN", section_break=True)
    inventory = load_inventory()

    url_dups = find_url_duplicates(inventory)
    log_event(f"[Dedup] URL duplicates: {len(url_dups)}")

    hash_groups = find_hash_duplicates(inventory)
    hash_dups = []
    for group in hash_groups:
        for i in range(1, len(group)):
            hash_dups.append((group[0], group[i], 1.0))
    log_event(f"[Dedup] Content hash duplicates: {len(hash_dups)}")

    title_dups = find_title_duplicates(inventory)

    all_dups = [(u1, u2, 1.0) for u1, u2 in url_dups] + hash_dups + title_dups
    unique_pairs = {}
    for u1, u2, s in all_dups:
        key = tuple(sorted([u1, u2]))
        if key not in unique_pairs or s > unique_pairs[key]:
            unique_pairs[key] = s
    deduped_pairs = [(k[0], k[1], v) for k, v in unique_pairs.items()]

    stats = {
        "url_duplicates": len(url_dups),
        "hash_duplicates": len(hash_dups),
        "title_duplicates": len(title_dups),
        "total_unique_pairs": len(deduped_pairs),
    }

    if dry_run:
        log_event(f"[Dedup] DRY RUN — {len(deduped_pairs)} duplicates found, no changes made")
        for u1, u2, score in sorted(deduped_pairs, key=lambda x: -x[2])[:20]:
            t1 = str(inventory.get(u1, {}).get("title") or "?")[:60]
            t2 = str(inventory.get(u2, {}).get("title") or "?")[:60]
            log_event(f"  [{score:.0%}] {t1} <-> {t2}")
    else:
        resolved = resolve_duplicates(inventory, deduped_pairs)
        stats["resolved"] = resolved
        save_inventory(inventory)
        log_event(f"[Dedup] Resolved {resolved} duplicates")

    log_event(f"DEDUP COMPLETE: {stats}")
    return stats


if __name__ == "__main__":
    asyncio.run(run_dedup(dry_run=True))
