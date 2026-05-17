import os
import re
import json
import asyncio
import httpx
import random
import difflib
from datetime import datetime
from typing import List, Dict, Set, Optional, Tuple
import yaml
from src.config import GEMINI_API_KEYS, GH_TOKEN, TARGET_REPO, NUBENETES_CATEGORIES
from src.gitops_manager import RepositoryController
from src.gemini_utils import call_gemini_with_retry
from src.logger import log_event

def normalize_url(url: str) -> str:
    url = url.split("#")[0].split("?")[0].rstrip("/")
    if url.startswith("http://"): url = "https://" + url[7:]
    return url.lower()

# Silenciar advertencias de XML/HTML
import warnings
from bs4 import XMLParsedAsHTMLWarning
warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def get_best_category_match(suggested: str) -> Optional[str]:
    """Usa similitud de texto para mapear sugerencias de la IA a categorías existentes."""
    if not suggested: return None
    suggested = suggested.lower().strip()
    if suggested in NUBENETES_CATEGORIES: return suggested
    
    matches = difflib.get_close_matches(suggested, NUBENETES_CATEGORIES, n=1, cutoff=0.6)
    return matches[0] if matches else None

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
                
                # Extract Rich Metadata
                rich_meta = await _enrich_rich_metadata(url, soup)
                
                for s in soup(["script", "style", "nav", "footer", "aside"]): s.decompose()
                return soup.get_text(separator=" ", strip=True)[:4000], rich_meta
    except: return "", {}
    return "", {}

async def _get_github_activity(url: str) -> Dict:
    """Obtiene metadatos de GitHub (estrellas, creación, actividad)."""
    if "github.com" not in url or not GH_TOKEN: return {}
    try:
        match = re.search(r"github\.com/([^/]+)/([^/]+)", url)
        if match:
            owner, repo = match.groups()
            repo = repo.split("#")[0].split("?")[0].rstrip(".git")
            api_url = f"https://api.github.com/repos/{owner}/{repo}"
            headers = {"Authorization": f"token {GH_TOKEN}"}
            async with httpx.AsyncClient() as client:
                resp = await client.get(api_url, headers=headers, timeout=5)
                if resp.status_code == 200:
                    data = resp.json()
                    return {
                        "gh_pushed": data.get("pushed_at", "").split("T")[0],
                        "gh_created": data.get("created_at", "").split("T")[0],
                        "gh_stars": data.get("stargazers_count", 0)
                    }
    except: pass
    return {}

async def evaluate_extracted_assets(raw_assets: List[Dict]) -> Dict[str, Dict]:
    evaluations = {}
    memory_file = "src/memory/health_learning.json"
    domain_blacklist = set()
    if os.path.exists(memory_file):
        try:
            with open(memory_file, "r") as f:
                memory_data = json.load(f)
                domain_blacklist = set(memory_data.get("blacklisted_domains", []))
        except: pass

    curator = AgenticCurator()

    for i, asset in enumerate(raw_assets):
        context = asset.get("text", "No additional context")
        source = asset.get("source_type", "Social")
        is_primary = "nubenetes" in source.lower()
        
        log_event(f"--- EVALUATING {i+1}/{len(raw_assets)} ---", section_break=False)
        log_event(f"  - URL: {asset['url']}")

        norm_url = normalize_url(asset["url"])
        if norm_url.split("//")[-1].split("/")[0] in domain_blacklist:
            log_event(f"  [-] REJECTED: Blacklisted domain")
            evaluations[asset["url"]] = {"status": "FILTERED", "reason": "Blacklisted domain"}
            continue

        # --- DATABASE-FIRST: Check if already analyzed ---
        if norm_url in curator.inventory:
            cached = curator.inventory[norm_url]
            # If it has the core fields, reuse them
            if cached.get("title") and cached.get("description") and cached.get("year"):
                log_event(f"  [⚡] REUSING CACHED INSIGHTS: {cached['title']}")
                
                from src.gemini_utils import SESSION_TRACKER
                SESSION_TRACKER.track_cache_hit(est_tokens=2200) # Full curation token estimate

                evaluations[asset["url"]] = {
                    "status": "INCLUDED", "title": cached["title"], "description": cached["description"],
                    "year": cached["year"], "category": cached.get("category", "kubernetes-tools"),
                    "related_categories": cached.get("related_categories", []),
                    "impact_score": cached.get("stars", 1) * 20, 
                    "is_exceptional": cached.get("stars", 0) >= 4,
                    "language": cached.get("language", "English"),
                    "en_summary": cached.get("ai_summary", cached["description"]),
                    "resource_type": cached.get("resource_type", "Reference"),
                    "complexity": cached.get("complexity", "Intermediate")
                }
                continue

        gh_meta = {}
        mvq_penalty = False
        if "github.com" in asset["url"]:
            gh_meta = await _get_github_activity(asset["url"])
            if gh_meta.get("gh_pushed"):
                try:
                    last_date = datetime.fromisoformat(gh_meta["gh_pushed"])
                    if (datetime.now() - last_date).days > (365 * 4):
                        mvq_penalty = True
                except: pass

        web_content, rich_meta = await _deep_fetch_content(asset["url"])
        strictness_directive = "BE EXTREMELY SELECTIVE.\n" if not is_primary else ""

        prompt = (
            "You act as a Senior Technical Librarian for 'nubenetes/awesome-kubernetes' in 2026.\n"
            f"{strictness_directive}"
            "PHASE 1: SOPHISTICATED SYNTHESIS & DATING\n"
            "- Extract precise PUBLICATION DATE (YYYY-MM-DD or YYYY).\n"
            "- Identify ONE primary_category and up to TWO related_categories.\n"
            "- DETECT source content LANGUAGE.\n"
            "PHASE 2: ARCHITECTURAL CLASSIFICATION (O'REILLY STYLE)\n"
            "- Identify TECHNICAL_HIERARCHY: A list of strings representing Area > Topic > Subtopics (up to 10 levels deep).\n"
            "- For 'introduction.md', set is_microservice: true if context matches.\n"
            "PHASE 3: LINGUISTIC DIVERSITY & GLOBAL ACCESS\n"
            "- TITLE: Use the technical title.\n"
            "- DESC (V1 Archive): Professional summary in the RESOURCE'S NATIVE LANGUAGE.\n"
            "- EN_SUMMARY (V2 Portal): Professional summary in high-quality ENGLISH.\n"
            "PHASE 4: QUALITY, TYPE & COMPLEXITY\n"
            "- Identify RESOURCE_TYPE and complexity LEVEL.\n"
            "- Evaluate TECHNICAL IMPACT (1-100).\n"
            f"{'IMPORTANT: This repo is old (>4 years inactive). Apply penalty.' if mvq_penalty else ''}\n\n"
            "Respond ONLY with a JSON: {\"impact_score\": int, \"pub_date\": \"YYYY-MM-DD\", \"primary_category\": \"cat\", \"related_categories\": [\"cat1\", \"cat2\"], \"title\": \"...\", \"desc\": \"...\", \"en_summary\": \"...\", \"language\": \"...\", \"resource_type\": \"...\", \"complexity\": \"...\", \"technical_hierarchy\": [\"Area\", \"Topic\", \"Subtopic1\", ...], \"is_microservice\": bool, \"reasoning\": \"...\"}"
        )

        try:
            data = await call_gemini_with_retry(prompt)
            # ... metadata extraction ...
            else:
                evaluations[asset["url"]] = {
                    "status": "INCLUDED", "title": data["title"], "description": data["desc"],
                    "year": year, "category": primary_cat, "related_categories": related_cats[:2],
                    "impact_score": score, "is_exceptional": score > 80,
                    "language": data.get("language", "English"),
                    "en_summary": data.get("en_summary", data["desc"]),
                    "resource_type": data.get("resource_type", "Reference"),
                    "complexity": data.get("complexity", "Intermediate"),
                    "hierarchy": data.get("technical_hierarchy", ["General"]),
                    "is_microservice": data.get("is_microservice", False)
                }
                curator.inventory[norm_url] = {
                    "title": data["title"], "description": data["desc"], 
                    "ai_summary": data.get("en_summary", data["desc"]),
                    "language": data.get("language", "English"),
                    "resource_type": data.get("resource_type", "Reference"),
                    "complexity": data.get("complexity", "Intermediate"),
                    "hierarchy": data.get("technical_hierarchy", ["General"]),
                    "is_microservice": data.get("is_microservice", False),
                    "year": year, "pub_date": data.get("pub_date", "N/A"), "post_date": asset.get("timestamp", "N/A"),
                    "stars": min(max(score // 20, 0), 5), "last_checked": datetime.now().timestamp(),
                    "category": primary_cat, "related_categories": related_cats[:2]
                }
                curator._save_inventory()
                log_event(f"  [+] ACCEPTED: {data['title']} ({data.get('language', 'English')})")
        except: pass
        await asyncio.sleep(1.0)
    return evaluations

INVENTORY_PATH = "data/inventory.yaml"

class AgenticCurator:
    def __init__(self):
        self.git_controller = RepositoryController(GH_TOKEN, TARGET_REPO)
        self.docs_dir = "docs"
        self.mkdocs_path = "mkdocs.yml"
        self.index_path = "docs/index.md"
        self.stats = {"orphans_linked": 0}
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
                title = line.strip("#").strip()
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
                h2_count += 1
                h3_count = 0
                new_toc.append(f"{h2_count}. [{h['title']}](#{h['anchor']})")
            else:
                h3_count += 1
                new_toc.append(f"    {h3_count}. [{h['title']}](#{h['anchor']})")
        return "\n".join(lines[:toc_start_idx] + new_toc + lines[toc_end_idx + 1:])

    async def decide_smart_injection(self, markdown_content: str, asset: Dict) -> str:
        lines = markdown_content.splitlines()
        structure = "\n".join([l for l in lines if l.startswith("#")])
        stars = " 🌟" if asset["impact_score"] > 80 else ""
        year_prefix = f"**({asset.get('year')})** " if asset.get("year") and asset.get("year") != "N/A" else ""
        formatted_line = f"  - {year_prefix}[{asset['title']}]({asset['url']}){stars} - {asset['description']}"
        prompt = f"Inject resource: {formatted_line} into structure: {structure[:1000]}. JSON: {{\"target_header\": \"## ...\", \"is_new_header\": bool}}"
        try:
            data = await call_gemini_with_retry(prompt)
            target = data.get("target_header")
            is_new = data.get("is_new_header", False)
            if not target: return self._manual_fallback_injection(markdown_content, asset)
            new_lines = []
            inserted = False
            for line in lines:
                new_lines.append(line)
                if not inserted and target.lower() in line.lower() and line.startswith("#"):
                    if is_new: new_lines.append("")
                    new_lines.append(formatted_line)
                    inserted = True
            res = "\n".join(new_lines)
            return await self._rebuild_toc(res) if is_new else res
        except: pass
        return self._manual_fallback_injection(markdown_content, asset)

    def _manual_fallback_injection(self, content: str, asset: Dict) -> str:
        stars = " 🌟" if asset["impact_score"] > 80 else ""
        year_prefix = f"**({asset.get('year')})** " if asset.get("year") and asset.get("year") != "N/A" else ""
        line = f"  - {year_prefix}[{asset['title']}]({asset['url']}){stars} - {asset['description']}"
        return content + f"\n{line}" if "##" in content else content + f"\n\n## Tools and Resources\n{line}"

    async def suggest_reorganization(self):
        log_event("[*] Starting Internal Reorganization Audit...", section_break=True)
        # Load Special Assets config
        special_rules = {}
        if os.path.exists("data/special_assets.yaml"):
            try:
                with open("data/special_assets.yaml", "r") as f:
                    special_rules = yaml.safe_load(f).get("special_assets", [])
            except: pass
        special_files = {sa["file"]: sa for sa in special_rules}

        for file in os.listdir(self.docs_dir):
            if not file.endswith(".md") or file == "index.md": continue
            path = os.path.join(self.docs_dir, file)
            with open(path, "r") as f: content = f.read()
            
            is_special = file in special_files
            link_count = len(re.findall(r"^\s*-\s*\[", content, re.MULTILINE))
            
            # Reorganize if special OR if flat and large
            if is_special or (link_count > 25 and len(re.findall(r"^## ", content, re.M)) < 2):
                log_event(f"  [!] REORGANIZING: {file} ({'Special' if is_special else 'Standard'})")
                
                depth_instruction = (
                    "SOPHISTICATED O'REILLY HIERARCHY: Create nested sections (##) and subsections (###). "
                    "Group links by technical AREAS, TOPICS, and SUBTOPICS (e.g. 'Foundations' -> 'Container Orchestration'). "
                    "The structure must facilitate knowledge assimilation like a professional technical book. "
                    "Ensure every valid link is preserved. Maintain professional titles."
                    if is_special else "Group into logical sections (##)."
                )
                
                prompt = (
                    f"You act as a Technical Content Architect. Reorganize the file '{file}' based on this rule: {depth_instruction}\n"
                    f"IMPORTANT: DO NOT DELETE any valid link. English headers only. Content:\n{content[:5000]}"
                )
                try:
                    reorganized = await call_gemini_with_retry(prompt, response_format="text", prefer_flash=True)
                    if len(reorganized) > len(content) * 0.7:
                        final = await self._rebuild_toc(reorganized)
                        with open(path, "w") as f: f.write(final)
                        log_event(f"  [OK] Reorganized: {file}")
                except Exception as e: log_event(f"  [!] Error: {e}")

    async def apply_semantic_interlinking(self, evaluations: Dict[str, Dict]):
        """
        Implements Automated Semantic Interlinking (Mandate 5).
        Adds 'See also' references to related categories to improve site navigation.
        """
        log_event("[*] Phase 5: Executing Semantic Interlinking (Mandate 5)...", section_break=True)
        
        for url, eval_data in evaluations.items():
            if eval_data.get("status") != "INCLUDED": continue
            
            primary_cat = eval_data.get("category")
            related_cats = eval_data.get("related_categories", [])
            
            for rel_cat in related_cats:
                if not rel_cat or rel_cat == primary_cat: continue
                
                rel_path = os.path.join(self.docs_dir, f"{rel_cat}.md")
                if not os.path.exists(rel_path): continue
                
                with open(rel_path, "r") as f: content = f.read()
                
                # Check if already interlinked
                if url in content: continue
                
                log_event(f"  [+] Interlinking: {eval_data['title']} -> {rel_cat}.md")
                
                see_also = f"\n  - *See also: [{eval_data['title']}]({url}) in [{primary_cat.replace('-', ' ').title()}]*"
                
                # Inject at the end of the first H2 or at the end of the file
                match = re.search(r'^## ', content, re.MULTILINE)
                if match:
                    # Find the next H2 or end of section
                    next_h2 = re.search(r'^## ', content[match.end():], re.MULTILINE)
                    if next_h2:
                        pos = match.end() + next_h2.start()
                        content = content[:pos] + see_also + "\n" + content[pos:]
                    else:
                        content += see_also
                else:
                    content += f"\n\n## Related Resources\n{see_also}"
                
                with open(rel_path, "w") as f: f.write(content)

    def validate_changes(self) -> bool: return True

async def _enrich_rich_metadata(url: str, soup) -> Dict:
    """Extrae metadatos específicos para YouTube y Blogs."""
    meta = {}
    url_lower = url.lower()
    
    # 1. YouTube Enrichment
    if "youtube.com" in url_lower or "youtu.be" in url_lower:
        try:
            author_tag = soup.find("link", itemprop="name")
            if author_tag: meta["author"] = author_tag.get("content")
            
            # YouTube duration is often in schema meta
            duration_tag = soup.find("meta", itemprop="duration")
            if duration_tag:
                duration_str = duration_tag.get("content") # PT15M30S
                match = re.search(r'PT(\d+H)?(\d+M)?(\d+S)?', duration_str)
                if match:
                    h, m, s = match.groups()
                    h = h.replace('H', 'h ') if h else ""
                    m = m.replace('M', 'm') if m else "0m"
                    meta["duration"] = f"{h}{m}".strip()
        except: pass

    # 2. Blog Enrichment (Medium, Dev.to, etc.)
    elif any(d in url_lower for d in ["medium.com", "dev.to", "blog", "hashnode"]):
        try:
            # Reading time
            rt_tag = soup.find("meta", property="twitter:data1") # Common for Medium
            if rt_tag and "min" in rt_tag.get("content", "").lower():
                meta["reading_time"] = rt_tag.get("content")
            
            # Author
            author_tag = soup.find("meta", {"name": "author"}) or soup.find("meta", property="article:author")
            if author_tag: meta["author"] = author_tag.get("content")
        except: pass
        
    return meta
