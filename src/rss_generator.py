"""RSS 2.0 feed generator for the Nubenetes Intelligence Digest.

Reads data/news_digest.json and writes v2-docs/feed.xml with the top
items from the 3-month digest window across all tech categories.
"""

from __future__ import annotations

import json
import os
from datetime import datetime
from email.utils import format_datetime
from xml.sax.saxutils import escape

from src.logger import log_event

DIGEST_PATH = "data/news_digest.json"
OUTPUT_PATH = "v2-docs/feed.xml"
FEED_TITLE = "Nubenetes Intelligence Digest"
FEED_LINK = "https://nubenetes.com/"
FEED_DESCRIPTION = "AI-curated top picks from the Cloud Native & Kubernetes ecosystem"
FEED_LANGUAGE = "en"
ITEMS_PER_FEED = 20

TECH_CATS = [
    "Kubernetes & Orchestration", "AI & Agents", "Security & Compliance",
    "CI/CD & GitOps", "Observability, SRE & Testing", "Infrastructure as Code",
    "Containers & Runtime", "Networking & Service Mesh", "Cloud Providers & FinOps",
    "MLOps & Data Science", "Data, Messaging & Storage",
]


def _rfc822(dt: datetime) -> str:
    return format_datetime(dt)


def generate_rss() -> None:
    if not os.path.exists(DIGEST_PATH):
        log_event("[WARN] rss_generator: news_digest.json not found, skipping RSS generation")
        return

    try:
        with open(DIGEST_PATH, "r", encoding="utf-8") as f:
            digest = json.load(f)
    except Exception as e:
        log_event(f"[WARN] rss_generator: failed to load digest: {str(e)[:100]}")
        return

    period_data = digest.get("3_months", {})
    items: list[dict] = []

    for cat in TECH_CATS:
        for entry in period_data.get(cat, []):
            items.append({**entry, "_cat": cat})

    # Sort by impact then date
    impact_rank = {"critical": 3, "high": 2, "medium": 1}
    items.sort(
        key=lambda x: (impact_rank.get(x.get("impact", "medium"), 0), x.get("date", "")),
        reverse=True,
    )
    items = items[:ITEMS_PER_FEED]

    # Deterministic build date = the freshest item's content date, so the feed
    # is a pure function of its items and never churns on unchanged republishes
    # to master. Falls back to _meta.last_updated, then
    # a fixed constant, only when no item carries a parseable date.
    item_dates = []
    for _it in items:
        try:
            item_dates.append(datetime.strptime(_it.get("date", ""), "%Y-%m-%d"))
        except Exception:
            pass
    if item_dates:
        build_dt = max(item_dates)
    else:
        meta_updated = digest.get("_meta", {}).get("last_updated", "")
        try:
            build_dt = datetime.fromisoformat(meta_updated) if meta_updated else datetime(2026, 1, 1)
        except Exception:
            build_dt = datetime(2026, 1, 1)
    build_date = _rfc822(build_dt)

    lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">',
        "  <channel>",
        f"    <title>{escape(FEED_TITLE)}</title>",
        f"    <link>{FEED_LINK}</link>",
        f"    <description>{escape(FEED_DESCRIPTION)}</description>",
        f"    <language>{FEED_LANGUAGE}</language>",
        f"    <lastBuildDate>{build_date}</lastBuildDate>",
        f'    <atom:link href="{FEED_LINK}feed.xml" rel="self" type="application/rss+xml"/>',
    ]

    for item in items:
        title = escape(item.get("title", "Unknown"))
        url = item.get("url", "#")
        why = escape(item.get("why", ""))
        cat = escape(item.get("_cat", ""))
        impact = item.get("impact", "medium")
        date_str = item.get("date", "")
        try:
            pub_date = _rfc822(datetime.strptime(date_str, "%Y-%m-%d")) if date_str else build_date
        except Exception:
            pub_date = build_date

        lines += [
            "    <item>",
            f"      <title>{title}</title>",
            f"      <link>{url}</link>",
            f"      <guid isPermaLink=\"true\">{url}</guid>",
            f"      <pubDate>{pub_date}</pubDate>",
            f"      <category>{cat}</category>",
            f"      <description>[{impact.upper()}] {why}</description>",
            "    </item>",
        ]

    lines += ["  </channel>", "</rss>"]

    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")

    log_event(f"[INFO] rss_generator: wrote {len(items)} items to {OUTPUT_PATH}")


if __name__ == "__main__":
    generate_rss()
