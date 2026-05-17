import asyncio
import json
import os
import re
import httpx
import yaml
import hashlib
from datetime import datetime
from typing import List, Dict, Optional, Tuple
from src.config import GH_TOKEN, TARGET_REPO, GEMINI_API_KEY, NUBENETES_CATEGORIES, MADRID_TZ
from src.gitops_manager import RepositoryController
from src.gemini_utils import call_gemini_with_retry, normalize_url, clean_toc_text
from src.logger import log_event

def get_best_category_match(suggested: str) -> Optional[str]:
    if not suggested: return None
    suggested = suggested.lower().strip()
    for cat in NUBENETES_CATEGORIES:
        if suggested in cat or cat in suggested: return cat
    return None

async def _deep_fetch_content(url: str) -> Tuple[str, Dict]:
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.5",
    }
    try:
        timeout = httpx.Timeout(12.0, connect=5.0)
        async with httpx.AsyncClient(timeout=timeout, verify=False) as client:
            resp = await client.get(url, headers=headers, follow_redirects=True)
            if resp.status_code == 200:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(resp.text, "html.parser")
                rich_meta = await _enrich_rich_metadata(url, soup)
                for s in soup(["script", "style", "nav", "footer", "aside"]): s.decompose()
                return soup.get_text(separator=" ", strip=True)[:4000], rich_meta
    except: return "", {}
    return "", {}

async def _get_github_activity(url: str) -> Dict:
    match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
    if not match: return {}
    owner, repo = match.groups()
    repo = repo.split("#")[0].split("?")[0].rstrip(".git")
    headers = {"Authorization": f"token {GH_TOKEN}"} if GH_TOKEN else {}
    try:
        async with httpx.AsyncClient(timeout=10.0) as client:
            resp = await client.get(f"https://api.github.com/repos/{owner}/{repo}", headers=headers)
            if resp.status_code == 200:
                data = resp.json()
                return {"gh_stars": data.get("stargazers_count", 0), "gh_pushed": data.get("pushed_at", ""), "gh_created": data.get("created_at", "")}
    except: pass
    return {}

async def evaluate_extracted_assets(raw_assets: List[Dict]) -> Dict[str, Dict]:
    evaluations = {}
    curator = AgenticCurator()
    
    # Mandate 2: Load Blacklist
    memory_file = "src/memory/health_learning.json"
    domain_blacklist = set()
    if os.path.exists(memory_file):
        try:
            memory_data = json.load(open(memory_file, "r"))
            domain_blacklist = set(memory_data.get("blacklisted_domains", []))
        except: pass

    for i, asset in enumerate(raw_assets):
        url = asset["url"]
        log_event(f"--- EVALUATING {i+1}/{len(raw_assets)}: {url} ---")
        norm_url = normalize_url(url)
        
        # Mandate 2: Skip Blacklisted
        if any(domain in url.lower() for domain in domain_blacklist):
            log_event(f"  [-] SKIPPING: Blacklisted domain detected.")
            evaluations[url] = {"status": "FILTERED", "reason": "Blacklisted"}
            continue

        # --- DATABASE-FIRST: Reuse insights ---
        if norm_url in curator.inventory:
            cached = curator.inventory[norm_url]
            if cached.get("title") and cached.get("hierarchy"):
                log_event(f"  [⚡] REUSING CACHED INSIGHTS: {cached['title']}")
                from src.gemini_utils import SESSION_TRACKER
                SESSION_TRACKER.track_cache_hit(est_tokens=2200)
                evaluations[url] = {"status": "INCLUDED", **cached}
                continue

        # 1. Fetch & Fingerprint
        web_content, rich_meta = await _deep_fetch_content(url)
        content_hash = hashlib.sha256(web_content.encode()).hexdigest() if web_content else "N/A"
        
        # Mandate 3: MVQ Check (GitHub Activity)
        mvq_penalty = False
        gh_meta = {}
        if "github.com" in url:
            gh_meta = await _get_github_activity(url)
            pushed = gh_meta.get("gh_pushed", "")
            if pushed:
                last_date = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
                if (datetime.now(last_date.tzinfo) - last_date).days > (365 * 4):
                    mvq_penalty = True
                    log_event(f"  [!] MVQ ALERT: Stale repository (>4 years). Penalty applied.")

        # 2. AI Logic (O'Reilly + Linguistic Diversity)
        is_primary = "nubenetes" in asset.get("source_type", "Social").lower()
        strictness = "BE EXTREMELY SELECTIVE.\n" if not is_primary else ""
        prompt = (
            "You act as a Senior Technical Librarian in 2026.\n" + strictness +
            f"{'IMPORTANT: This repo is old (>4 years inactive). Assign impact_score < 30.' if mvq_penalty else ''}\n"
            "PHASE 1: LINGUISTIC DIVERSITY (Mandate 10)\n"
            "- DESC (V1 Archive): Professional summary in native language.\n"
            "- EN_SUMMARY (V2 Portal): English synthesis.\n"
            "Respond ONLY with JSON: {\"impact_score\": int, \"pub_date\": \"YYYY-MM-DD\", \"primary_category\": \"cat\", \"title\": \"...\", \"desc\": \"...\", \"en_summary\": \"...\", \"language\": \"...\", \"resource_type\": \"...\", \"complexity\": \"...\", \"technical_hierarchy\": [\"Area\", ...], \"is_microservice\": bool}\n"
            f"CONTENT: {web_content[:2000]}"
        )
        
        try:
            data = await call_gemini_with_retry(prompt)
            score = data.get("impact_score", 50)
            primary_cat = get_best_category_match(data.get("primary_category"))
            
            if score >= (5 if is_primary else 80) and primary_cat:
                eval_data = {
                    "title": data["title"], "description": data["desc"], "ai_summary": data.get("en_summary", data["desc"]),
                    "language": data.get("language", "English"), "resource_type": data.get("resource_type", "Reference"),
                    "complexity": data.get("complexity", "Intermediate"), "hierarchy": data.get("technical_hierarchy", ["General"]),
                    "is_microservice": data.get("is_microservice", False), "year": data.get("pub_date", "N/A")[:4],
                    "stars": min(max(score // 20, 0), 5), "content_hash": content_hash,
                    "source_provenance": asset.get("source_type", "Social"), "social_preview_url": rich_meta.get("og_image", ""),
                    "mentions_count": curator.inventory.get(norm_url, {}).get("mentions_count", 0) + 1,
                    "category": primary_cat, "status": "online", "last_checked": datetime.now().timestamp(),
                    **gh_meta
                }
                curator.inventory[norm_url] = eval_data
                evaluations[url] = {"status": "INCLUDED", **eval_data}
                curator._save_inventory()
                log_event(f"  [+] ACCEPTED: {data['title']}")
            else:
                evaluations[url] = {"status": "FILTERED"}
        except Exception as e: log_event(f"  [!] AI Error: {e}")
    return evaluations

INVENTORY_PATH = "data/inventory.yaml"

class AgenticCurator:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.docs_dir = "docs"
        self.inventory = self._load_inventory()

    def _load_inventory(self) -> dict:
        if os.path.exists(INVENTORY_PATH):
            try:
                with open(INVENTORY_PATH, "r") as f: return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def _save_inventory(self):
        os.makedirs(os.path.dirname(INVENTORY_PATH), exist_ok=True)
        with open(INVENTORY_PATH, "w") as f: yaml.dump(self.inventory, f, sort_keys=False, allow_unicode=True)

    async def _rebuild_toc(self, content: str) -> str:
        lines = content.splitlines()
        headers = []
        for line in lines:
            if line.startswith("## ") or line.startswith("### "):
                raw_title = line.strip("#").strip()
                title = clean_toc_text(raw_title)
                anchor = title.lower().replace(" ", "-").replace(".", "").replace("/", "").replace("(", "").replace(")", "").replace(",", "")
                headers.append({"title": title, "anchor": anchor, "level": 2 if line.startswith("## ") else 3})
        if not headers: return content
        toc_start_idx = -1
        toc_end_idx = -1
        for i, line in enumerate(lines):
            if re.match(r"^\d+\.\s+\[", line.strip()):
                if toc_start_idx == -1: toc_start_idx = i
                toc_end_idx = i
            elif toc_start_idx != -1 and not re.match(r"^\s*\d+\.\s+\[", line.strip()) and line.strip() != "":
                if toc_end_idx != -1: break
        if toc_start_idx == -1: return content
        new_toc = []
        h2_count, h3_count = 0, 0
        for h in headers:
            if h["level"] == 2:
                h2_count += 1; h3_count = 0
                new_toc.append(f"{h2_count}. [{h['title']}](#{h['anchor']})")
            else:
                h3_count += 1
                new_toc.append(f"    {h3_count}. [{h['title']}](#{h['anchor']})")
        return "\n".join(lines[:toc_start_idx] + new_toc + lines[toc_end_idx + 1:])

    async def decide_smart_injection(self, markdown_content: str, asset: Dict) -> str:
        lines = markdown_content.splitlines(); structure = "\n".join([l for l in lines if l.startswith("#")])
        stars = " 🌟" if asset.get("stars", 0) >= 4 else ""
        line = f"  - **({asset.get('year', 'N/A')})** [{asset['title']}]({asset['url']}){stars} - {asset['description']}"
        prompt = f"Inject resource: {line} into structure: {structure[:1000]}. JSON: {{\"target_header\": \"## ...\", \"is_new_header\": bool}}"
        try:
            data = await call_gemini_with_retry(prompt)
            target = data.get("target_header")
            if not target: return self._manual_fallback_injection(markdown_content, asset)
            new_lines = []; inserted = False
            for l in lines:
                new_lines.append(l)
                if not inserted and target.lower() in l.lower() and l.startswith("#"):
                    if data.get("is_new_header"): new_lines.append("")
                    new_lines.append(line); inserted = True
            res = "\n".join(new_lines)
            return await self._rebuild_toc(res) if data.get("is_new_header") else res
        except: pass
        return self._manual_fallback_injection(markdown_content, asset)

    def _manual_fallback_injection(self, content: str, asset: Dict) -> str:
        stars = " 🌟" if asset.get("stars", 0) >= 4 else ""
        line = f"  - **({asset.get('year', 'N/A')})** [{asset['title']}]({asset['url']}){stars} - {asset['description']}"
        return content + f"\n{line}" if "##" in content else content + f"\n\n## Tools and Resources\n{line}"

    async def suggest_reorganization(self):
        log_event("[*] Starting Internal Reorganization & TOC Audit...", section_break=True)
        # Load Special Assets & Link Rules for exceptions
        special_rules = {}
        exempt_files = []
        if os.path.exists("data/special_assets.yaml"):
            try: special_rules = {sa["file"]: sa for sa in yaml.safe_load(open("data/special_assets.yaml"))["special_assets"]}
            except: pass
        if os.path.exists("data/link_rules.yaml"):
            try: exempt_files = yaml.safe_load(open("data/link_rules.yaml"))["hierarchy_rules"].get("toc_exempt_files", [])
            except: pass

        for file in os.listdir(self.docs_dir):
            if not file.endswith(".md") or file == "index.md" or file in exempt_files: continue
            path = os.path.join(self.docs_dir, file)
            with open(path, "r") as f: content = f.read()
            
            is_special = file in special_rules
            link_count = len(re.findall(r"^\s*-\s*\[", content, re.MULTILINE))
            headers = re.findall(r"^##+ ", content, re.MULTILINE)
            
            # --- FEATURE: Automatic TOC Injection for V1 ---
            # Check for existing TOC (explicit header or numbered list)
            has_toc = "Table of Contents" in content or len(re.findall(r'^\d+\.\s+\[.*?\]\(#.*?\)', content, re.MULTILINE)) >= 3
            
            if len(headers) >= 3 and not has_toc:
                log_event(f"  [+] INJECTING TOC: {file}")
                content = await self._rebuild_toc(content)
                with open(path, "w") as f: f.write(content)
            
            # Reorganize if special OR if flat and large
            if is_special or (link_count > 25 and len(headers) < 2):
                log_event(f"  [!] REORGANIZING: {file} ({'Special' if is_special else 'Standard'})")
                instruction = (
                    "SOPHISTICATED O'REILLY HIERARCHY: Create nested sections (##) and subsections (###). "
                    "Group links by technical AREAS, TOPICS, and SUBTOPICS. Preserve all links."
                    if is_special else "Group into logical sections (##)."
                )
                prompt = f"You act as a Technical Content Architect. Reorganize '{file}' based on: {instruction}\nCONTENT:\n{content[:5000]}"
                try:
                    reorg = await call_gemini_with_retry(prompt, response_format="text", prefer_flash=True)
                    if len(reorg) > len(content) * 0.7:
                        final = await self._rebuild_toc(reorg)
                        with open(path, "w") as f: f.write(final)
                        log_event(f"  [OK] Reorganized: {file}")
                except Exception as e: log_event(f"  [!] Error: {e}")

    async def apply_semantic_interlinking(self, evaluations: Dict[str, Dict]):
        log_event("[*] Phase 5: Executing Semantic Interlinking (Mandate 5)...", section_break=True)
        for url, eval_data in evaluations.items():
            if eval_data.get("status") != "INCLUDED": continue
            for rel_cat in eval_data.get("related_categories", []):
                rel_path = os.path.join(self.docs_dir, f"{rel_cat}.md")
                if os.path.exists(rel_path):
                    content = open(rel_path, "r").read()
                    if url not in content:
                        log_event(f"  [+] Interlinking: {eval_data['title']} -> {rel_cat}.md")
                        see_also = f"\n  - *See also: [{eval_data['title']}]({url}) in [{eval_data['category'].replace('-', ' ').title()}]*"
                        match = re.search(r'^## ', content, re.MULTILINE)
                        if match:
                            next_h2 = re.search(r'^## ', content[match.end():], re.MULTILINE)
                            pos = match.end() + next_h2.start() if next_h2 else len(content)
                            content = content[:pos] + see_also + "\n" + content[pos:]
                        else: content += f"\n\n## Related Resources\n{see_also}"
                        with open(rel_path, "w") as f: f.write(content)

async def _enrich_rich_metadata(url: str, soup) -> Dict:
    meta = {}; url_l = url.lower()
    og = soup.find("meta", property="og:image") or soup.find("meta", {"name": "twitter:image"})
    if og: meta["og_image"] = og.get("content")
    if "youtube.com" in url_l or "youtu.be" in url_l:
        a = soup.find("link", itemprop="name"); d = soup.find("meta", itemprop="duration")
        if a: meta["author"] = a.get("content")
        if d:
            m = re.search(r'PT(\d+H)?(\d+M)?(\d+S)?', d.get("content", ""))
            if m: h, mi, s = m.groups(); meta["duration"] = f"{h.replace('H','h ') if h else ''}{mi.replace('M','m') if mi else '0m'}".strip()
    elif any(d in url_l for d in ["medium.com", "dev.to", "blog"]):
        rt = soup.find("meta", property="twitter:data1"); a = soup.find("meta", {"name": "author"}) or soup.find("meta", property="article:author")
        if rt and "min" in rt.get("content", "").lower(): meta["reading_time"] = rt.get("content")
        if a: meta["author"] = a.get("content")
    return meta
