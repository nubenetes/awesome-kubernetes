import yaml
import os
import re
import json
import time
import asyncio
import httpx
import feedparser
from datetime import datetime
from src.logger import log_event
from src.config import MADRID_TZ
from src.gemini_utils import call_gemini_with_retry, fetch_youtube_metadata
from src.inventory_manager import load_inventory, save_inventory

INVENTORY_PATH = "data/inventory.yaml"
NUBENETES_CHANNEL_ID = "UCnrc0CFnNJSG2Kt4Ohdr3UA"
NUBENETES_FEED_URL = f"https://www.youtube.com/feeds/videos.xml?channel_id={NUBENETES_CHANNEL_ID}"


async def discover_nubenetes_channel_assets(inventory: dict) -> int:
    """
    Automatically discovers new playlists and videos published on https://www.youtube.com/@nubenetes
    (via both the YouTube Atom feed and the /playlists & /videos tabs) and registers them
    in the inventory as featured videos so they are enriched and added to the V2 Video Hub.
    """
    log_event("[*] Syncing official @nubenetes YouTube channel (playlists & new videos)...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.9",
    }
    cookies = {
        "CONSENT": "YES+cb.20210328-17-p0.en+FX+410",
        "SOCS": "CAISHAgBEhJnd3NfMjAyMzA4MTAtMF9SQzIaAmVuIAEaBgiAo_CmBg",
    }
    discovered = []

    async with httpx.AsyncClient(headers=headers, cookies=cookies, follow_redirects=True, timeout=15.0) as client:
        # 1. Atom Feed (fastest & most reliable for newest video uploads)
        try:
            resp = await client.get(NUBENETES_FEED_URL)
            if resp.status_code == 200:
                feed = await asyncio.to_thread(feedparser.parse, resp.content)
                for entry in feed.entries:
                    link = entry.get("link", "").strip()
                    title = entry.get("title", "").strip()
                    summary = entry.get("summary", "").strip()
                    if link:
                        discovered.append({"url": link, "title": title, "raw_desc": summary, "is_playlist": False})
        except Exception as e:
            log_event(f"    [WARN] @nubenetes Atom feed check failed: {str(e)[:80]}")

        # 2. Channel /playlists tab (discovers new categorized NotebookLM playlists)
        try:
            resp_pl = await client.get("https://www.youtube.com/@nubenetes/playlists")
            if resp_pl.status_code == 200:
                m = re.search(r"var ytInitialData = (\{.*?\});</script>", resp_pl.text)
                if m:
                    data = json.loads(m.group(1))
                    def _walk_pl(obj):
                        if isinstance(obj, dict):
                            if "lockupViewModel" in obj:
                                lvm = obj["lockupViewModel"]
                                cid = lvm.get("contentId", "")
                                title = (
                                    lvm.get("metadata", {})
                                    .get("lockupMetadataViewModel", {})
                                    .get("title", {})
                                    .get("content", "")
                                )
                                if cid.startswith("PL") and title:
                                    clean_title = title.lstrip("⭐ ").strip()
                                    discovered.append({
                                        "url": f"https://www.youtube.com/playlist?list={cid}",
                                        "cid": cid,
                                        "title": f"{clean_title} (Playlist)" if not clean_title.endswith("(Playlist)") else clean_title,
                                        "raw_desc": f"Official @nubenetes NotebookLM curated playlist: {clean_title}",
                                        "is_playlist": True,
                                    })
                            for v in obj.values():
                                _walk_pl(v)
                        elif isinstance(obj, list):
                            for item in obj:
                                _walk_pl(item)
                    _walk_pl(data)
        except Exception as e:
            log_event(f"    [WARN] @nubenetes playlists check failed: {str(e)[:80]}")

        # For any newly discovered playlist not yet in inventory, fetch its full playlistMetadataRenderer description
        for item in discovered:
            if item.get("is_playlist") and item["url"] not in inventory:
                cid = item.get("cid", "")
                if cid:
                    try:
                        rp = await client.get(f"https://www.youtube.com/playlist?list={cid}", headers=headers)
                        if rp.status_code == 200:
                            mp = re.search(r"var ytInitialData = (\{.*?\});</script>", rp.text)
                            if mp:
                                dp = json.loads(mp.group(1))
                                desc_box = [""]
                                def _walk_pdesc(o):
                                    if isinstance(o, dict):
                                        if "playlistMetadataRenderer" in o:
                                            desc_box[0] = o["playlistMetadataRenderer"].get("description", "")
                                        for v in o.values():
                                            _walk_pdesc(v)
                                    elif isinstance(o, list):
                                        for i in o:
                                            _walk_pdesc(i)
                                _walk_pdesc(dp)
                                if desc_box[0]:
                                    clean_d = desc_box[0].split("[id:nubenetes-playlist-manager]")[0].split("🤖 Curated automatically")[0].strip()
                                    if clean_d:
                                        item["raw_desc"] = clean_d
                    except Exception:
                        pass

    now_iso = datetime.now(MADRID_TZ).isoformat()
    now_ts = int(time.time())
    added_count = 0

    for item in discovered:
        url = item["url"]
        vid_id_match = re.search(r"[?&]v=([^&#]+)", url)
        embed_alt = f"https://www.youtube.com/embed/{vid_id_match.group(1)}" if vid_id_match else None

        if url in inventory or (embed_alt and embed_alt in inventory):
            target_key = url if url in inventory else embed_alt
            if not inventory[target_key].get("is_featured_video"):
                inventory[target_key]["is_featured_video"] = True
                inventory[target_key]["company"] = "Nubenetes"
                inventory[target_key]["source_provenance"] = "Official @nubenetes YouTube Channel"
                added_count += 1
            continue

        inventory[url] = {
            "title": item["title"],
            "description": item["raw_desc"],
            "year": str(datetime.now(MADRID_TZ).year),
            "stars": 5,
            "ai_summary": item["raw_desc"],
            "language": "Spanish" if any(w in item["title"].lower() for w in ("español", "ahorra", "economía", "almacenamiento", "finops en azure", "arquitectura de")) else "English",
            "resource_type": "Video",
            "complexity": "Intermediate",
            "is_microservice": False,
            "is_featured_video": True,
            "is_enriched": False,
            "video_order": 25,
            "technology": "Cloud Native",
            "category": "Architecture and Cloud Strategy",
            "status": "online",
            "addition_method": "automatic",
            "health_score": 100.0,
            "last_checked": now_ts,
            "needs_ai_refresh": False,
            "discovered_at": now_iso,
            "last_ai_eval": now_iso,
            "company": "Nubenetes",
            "geo_region": "spain",
            "hierarchy": ["Cloud Native", "Video Masterclasses"],
            "tags": ["[GUIDE]"],
            "v1_locations": ["docs/index.md"],
            "v2_locations": ["index.md"],
            "youtube_mosaic": {},
            "source_provenance": "Official @nubenetes YouTube Channel",
        }
        added_count += 1

    if added_count > 0:
        log_event(f"    [+] Discovered {added_count} new @nubenetes videos/playlists for the Video Hub.")
        save_inventory(inventory)
    else:
        log_event("    [OK] @nubenetes channel is up to date with inventory.")
    return added_count

async def enrich_video_entry(url: str, entry: dict):
    log_event(f"[*] Enriching video: {url}")
    meta = await fetch_youtube_metadata(url)
    
    # Strategy A: Use metadata from direct fetch
    # Strategy B: Fallback to AI Grounding if fetch was blocked or generic
    use_grounding = False
    is_generic = False
    if meta:
        title = meta.get('raw_title', '').lower()
        if title in ['youtube', 'before you continue', 'n/a', '']:
            is_generic = True

    if not meta or is_generic:
        existing_title = str(entry.get("title") or "").strip()
        existing_desc = str(entry.get("description") or entry.get("ai_summary") or "").strip()
        bad_markers = ("youtube", "before you continue", "n/a", "", "unverified", "unindexed", "truncated", "unavailable")
        if existing_title and not any(b in existing_title.lower() for b in bad_markers):
            context = f"Local Context (from channel feed/playlist metadata):\nTitle: {existing_title}\nDescription: {existing_desc}"
            use_grounding = False
        else:
            log_event(f"    [!] Missing or generic metadata for {url}. Forcing AI Grounding (Pro Model)...")
            use_grounding = True
            context = f"YouTube URL: {url}\nNote: The local scraper was blocked and returned generic platform metadata. YOU MUST SEARCH FOR THE REAL TITLE."
    else:
        context = f"Local Context (from YouTube extraction):\nTitle: {meta['raw_title']}\nDescription: {meta['raw_description']}"

    prompt = f"""
    You are a Senior Cloud Architect. Your goal is to provide a high-fidelity summary of a technical YouTube video.
    
    INPUT CONTEXT:
    {context}

    CRITICAL INSTRUCTIONS:
    1. If the 'Local Context' above is missing, generic, or mentions 'YouTube' without a specific title, you MUST use your internal GOOGLE SEARCH GROUNDING to find the actual title and technical description of this video URL: {url}.
    2. Identify the ACTUAL technical content based on the verified video metadata.
    3. Generate a high-density architectural summary (2-3 sentences) explaining its specific value for a 2026 Cloud Native context.
    4. DO NOT describe generic YouTube platform infrastructure unless the video is specifically about it.
    5. Crossover AI Agents Detection: Pay special attention to AI Agents & MCP, and how they integrate with Cloud Native (e.g. SRE with AI Agents, Kubernetes with AI Agents, IaC with Terraform and AI, DevOps with AI, MLOps with AI). If the video covers these topics, reflect it in the technology field.
    6. Select the primary technology (e.g., Kubernetes + AI Agents, IaC + Terraform + AI Agents, DevOps + AI Agents, SRE + AI Agents, MLOps + AI Agents, or standard core tech like Kubernetes, Istio) and a category from: [Fundamentals and Documentaries, Architecture and Cloud Strategy, Networking and Service Mesh, Infrastructure as Code, Observability and Monitoring, AI and Future Operations, Security and Compliance].

    Return ONLY a JSON object:
    {{
      "title": "Actual Verified Title",
      "summary": "Specific and faithful architectural summary...",
      "technology": "...",
      "category": "..."
    }}
    """
    
    try:
        # Use grounding only if direct fetch failed
        data = await call_gemini_with_retry(prompt, prefer_flash=True, use_grounding=use_grounding)
        
        ai_title = str(data.get("title") or "").strip()
        ai_summary = str(data.get("summary") or "").strip()
        hallucinated_markers = ("unverified", "unindexed", "truncated", "unavailable", "cannot be resolved", "invalid")
        if any(m in (ai_title + " " + ai_summary).lower() for m in hallucinated_markers):
            fallback_title = (meta.get("raw_title") if meta else "") or entry.get("title", "YouTube Video")
            fallback_desc = (meta.get("raw_description") if meta else "") or entry.get("description", "")
            entry["title"] = fallback_title.lstrip("⭐ ").strip()
            if fallback_desc:
                entry["ai_summary"] = fallback_desc.split("[id:nubenetes-playlist-manager]")[0].split("🤖 Curated automatically")[0].strip()
        else:
            entry["title"] = ai_title or (meta['raw_title'] if meta else "YouTube Video")
            entry["ai_summary"] = ai_summary
        entry["technology"] = data.get("technology") or entry.get("technology", "Cloud Native")
        entry["category"] = data.get("category") or entry.get("category", "Architecture and Cloud Strategy")
        entry["is_enriched"] = True
        log_event(f"    [OK] {url} enriched successfully.")
    except (Exception, SystemExit) as e:
        log_event(f"    [WARN] AI enrichment failed for {url} ({e}). Falling back to YouTube metadata.")
        fallback_title = (meta.get("raw_title") if meta else "") or entry.get("title", "YouTube Video")
        fallback_desc = (meta.get("raw_description") if meta else "") or entry.get("description", "")
        entry["title"] = fallback_title.lstrip("⭐ ").strip()
        if fallback_desc:
            entry["ai_summary"] = fallback_desc.split("[id:nubenetes-playlist-manager]")[0].split("🤖 Curated automatically")[0].strip()
        entry["is_enriched"] = True
    
    return entry

async def main():
    if not os.path.exists(INVENTORY_PATH):
        return

    force_enrich = os.getenv("FORCE_ENRICH", "false").lower() == "true"

    inventory = load_inventory()

    # Auto-discover any new videos or playlists uploaded to https://www.youtube.com/@nubenetes
    await discover_nubenetes_channel_assets(inventory)

    video_urls = [u for u, e in inventory.items() if isinstance(e, dict) and e.get("is_featured_video")]
    
    tasks = []
    skipped = 0
    for url in video_urls:
        if inventory[url].get("is_enriched") and not force_enrich:
            skipped += 1
            continue
        tasks.append(enrich_video_entry(url, inventory[url]))

    if skipped > 0:
        log_event(f"[*] Skipped {skipped} already enriched videos. Use FORCE_ENRICH=true to re-process.")

    if not tasks:
        log_event("[*] No videos need enrichment.")
        return

    # Process in small batches to respect rate limits
    batch_size = 5
    for i in range(0, len(tasks), batch_size):
        batch = tasks[i:i+batch_size]
        await asyncio.gather(*batch)
        
        # Incremental Persistence: Save after each batch
        save_inventory(inventory)
        log_event(f"    [💾] Saved progress: {min(i + batch_size, len(tasks))}/{len(tasks)} videos.")
        
        if i + batch_size < len(tasks):
            await asyncio.sleep(2) # Safety delay
    
    log_event("✅ Video Hub Enrichment Complete.")

if __name__ == "__main__":
    asyncio.run(main())
