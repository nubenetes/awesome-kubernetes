import os
import re
import json
import asyncio
import httpx
import random
import difflib
from datetime import datetime
from typing import List, Dict, Set, Optional, Tuple
from src.config import GEMINI_API_KEYS, GH_TOKEN, TARGET_REPO, NUBENETES_CATEGORIES
from src.gitops_manager import RepositoryController
from src.gemini_utils import call_gemini_with_retry

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

async def _deep_fetch_content(url: str) -> str:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
    }
    try:
        # Stricter timeouts for Pay-as-you-go stability
        timeout = httpx.Timeout(10.0, connect=5.0)
        async with httpx.AsyncClient(timeout=timeout) as client:
            resp = await client.get(url, headers=headers, follow_redirects=True)
            if resp.status_code == 200:
                from bs4 import BeautifulSoup
                soup = BeautifulSoup(resp.text, 'html.parser')
                for s in soup(['script', 'style', 'nav', 'footer', 'aside']):
                    s.decompose()
                return soup.get_text(separator=' ', strip=True)[:4000]
    except: return ""
    return ""

from src.logger import log_event

async def _get_github_activity(url: str) -> Optional[datetime]:
    """Obtiene la fecha del último commit de un repo de GitHub usando la API (si hay token)."""
    if "github.com" not in url or not GH_TOKEN: return None
    try:
        # Extraer user/repo
        match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
        if match:
            owner, repo = match.groups()
            repo = repo.split('#')[0].split('?')[0].rstrip('.git')
            api_url = f"https://api.github.com/repos/{owner}/{repo}"
            headers = {"Authorization": f"token {GH_TOKEN}"}
            async with httpx.AsyncClient() as client:
                resp = await client.get(api_url, headers=headers, timeout=5)
                if resp.status_code == 200:
                    pushed_at = resp.json().get("pushed_at")
                    if pushed_at:
                        return datetime.fromisoformat(pushed_at.replace('Z', '+00:00'))
    except: pass
    return None

async def evaluate_extracted_assets(raw_assets: List[Dict]) -> Dict[str, Dict]:
    evaluations = {}
    if not GEMINI_API_KEYS:
        log_event("[!] CRITICAL ERROR: GEMINI_API_KEYS not found in environment.")
        return {a["url"]: {"status": "FILTERED", "reason": "Config: Missing API KEY"} for a in raw_assets}

    memory_file = "src/memory/health_learning.json"
    domain_blacklist = set()
    if os.path.exists(memory_file):
        try:
            with open(memory_file, 'r') as f:
                memory_data = json.load(f)
                domain_blacklist = set(memory_data.get("blacklisted_domains", []))
        except: pass

    for i, asset in enumerate(raw_assets):
        post_date = asset.get('timestamp', 'Unknown date')
        context = asset.get('context', asset.get('description', 'No additional context'))
        source = asset.get('source_type', 'Social')
        is_primary = "nubenetes" in source.lower()
        
        log_event(f"--- EVALUATING {i+1}/{len(raw_assets)} ---", section_break=False)
        log_event(f"  - URL: {asset['url']}")
        log_event(f"  - Source: {source} {'(Primary)' if is_primary else '(External)'}")

        domain = asset['url'].split("//")[-1].split("/")[0]
        if domain in domain_blacklist:
            log_event(f"  [-] REJECTED: Blacklisted domain ({domain})")
                            evaluations[asset["url"]] = {
                    "status": "INCLUDED", "title": data["title"], "description": data["desc"],
                    "year": year,
                    "category": primary_cat, "related_categories": list(set(related_cats))[:2],
                    "impact_score": score, "is_exceptional": score > 80,
                    "reasoning": reasoning
                }
                # Sync new link to unified inventory
                try:
                    self.inventory[asset["url"]] = {
                        "title": data["title"],
                        "description": data["desc"], 
                        "ai_summary": data["desc"],
                        "year": year,
                        "stars": min(max(score // 20, 0), 5),
                        "last_checked": datetime.now().timestamp()
                    }
                    self._save_inventory()
                except: pass
                log_event(f"  [+] ACCEPTED: \"{data['title']}\" (Score: {score})")
                log_event(f"      Primary: {primary_cat} | Related: {', '.join(related_cats)}")

        except Exception as e:
            log_event(f"  [!] ERROR EVALUATING {asset['url']}: {e}")
            evaluations[asset["url"]] = {"status": "FILTERED", "reason": f"Evaluation Failed"}
        
        # Re-optimized for Pay-as-you-go
        await asyncio.sleep(1.0)
            
    try:
        os.makedirs(os.path.dirname(memory_file), exist_ok=True)
        with open(memory_file, 'w') as f:
            json.dump({"blacklisted_domains": list(domain_blacklist)}, f, indent=2)
    except: pass
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
                with open(INVENTORY_PATH, "r") as f:
                    import yaml
                    return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def _save_inventory(self):
        os.makedirs(os.path.dirname(INVENTORY_PATH), exist_ok=True)
        with open(INVENTORY_PATH, "w") as f:
            import yaml
            yaml.dump(self.inventory, f, sort_keys=False, allow_unicode=True)
        self.inventory = self._load_inventory()

    async def _rebuild_toc(self, content: str) -> str:
        """
        Detecta y reconstruye el TOC interno de un archivo markdown.
        Busca el patrón de lista numerada al inicio del archivo.
        """
        lines = content.splitlines()
        new_lines = []
        headers = []
        toc_start_idx = -1
        toc_end_idx = -1
        
        # 1. Extraer todos los headers (## y ###) para el nuevo TOC
        for line in lines:
            if line.startswith("## ") or line.startswith("### "):
                title = line.strip("#").strip()
                # Generar ancla simplificada (slug)
                anchor = title.lower().replace(" ", "-").replace(".", "").replace("/", "").replace("(", "").replace(")", "").replace(",", "")
                level = 2 if line.startswith("## ") else 3
                headers.append({"title": title, "anchor": anchor, "level": level})

        if not headers: return content

        # 2. Localizar el TOC actual
        for i, line in enumerate(lines):
            if re.match(r'^\d+\.\s+\[', line.strip()):
                if toc_start_idx == -1: toc_start_idx = i
                toc_end_idx = i
            elif toc_start_idx != -1 and line.strip() == "" and i < len(lines)-1 and re.match(r'^\d+\.\s+\[', lines[i+1].strip()):
                continue # Espacios en blanco dentro del TOC
            elif toc_start_idx != -1 and not re.match(r'^\s*\d+\.\s+\[', line.strip()) and line.strip() != "":
                if toc_end_idx != -1: break

        if toc_start_idx == -1: return content # No hay TOC que actualizar

        # 3. Construir el nuevo TOC
        new_toc = []
        h2_count = 0
        h3_count = 0
        for h in headers:
            if h["level"] == 2:
                h2_count += 1
                h3_count = 0
                new_toc.append(f"{h2_count}. [{h['title']}](#{h['anchor']})")
            else:
                h3_count += 1
                new_toc.append(f"    {h3_count}. [{h['title']}](#{h['anchor']})")

        # 4. Reensamblar el archivo
        return "\n".join(lines[:toc_start_idx] + new_toc + lines[toc_end_idx + 1:])

    async def decide_smart_injection(self, markdown_content: str, asset: Dict) -> str:
        """
        Smartly injects a link and updates the TOC if necessary.
        """
        lines = markdown_content.splitlines()
        structure = "\n".join([l for l in lines if l.startswith("#")])
        
        stars = " 🌟" if asset['impact_score'] > 80 else ""
        year_prefix = f"**({asset.get('year')})** " if asset.get('year') and asset.get('year') != "N/A" else ""
        formatted_line = f"  - {year_prefix}[{asset['title']}]({asset['url']}){stars} - {asset['description']}"

        prompt = (
            "You act as a Content Architect for Nubenetes.com.\n"
            f"Your mission is to logically inject this new resource into the markdown file (LANGUAGE: ENGLISH):\n"
            f"RESOURCE: {formatted_line}\n"
            "CURRENT STRUCTURE:\n"
            f"{structure[:1500]}\n\n"
            "INSTRUCTIONS:\n"
            "1. Identify the most suitable header (##).\n"
            "2. If it doesn't exist, PROPOSE A NEW ONE (in English).\n"
            "Respond JSON: {\"target_header\": \"## ...\", \"is_new_header\": bool, \"insert_after_header\": \"## ...\"}"
        )

        try:
            data = await call_gemini_with_retry(prompt)
            target_header = data.get("target_header")
            is_new = data.get("is_new_header", False)
            ref_header = data.get("insert_after_header")
            
            if not target_header: return self._manual_fallback_injection(markdown_content, asset)

            new_content_raw = ""
            inserted = False
            new_lines = []
            
            if is_new:
                if not ref_header:
                    new_lines = lines + ["", target_header, formatted_line]
                    inserted = True
                else:
                    for line in lines:
                        new_lines.append(line)
                        if not inserted and ref_header.lower() in line.lower() and line.strip().startswith("#"):
                            new_lines.append("")
                            new_lines.append(target_header)
                            new_lines.append(formatted_line)
                            inserted = True
                new_content_raw = "\n".join(new_lines)
            else:
                for line in lines:
                    new_lines.append(line)
                    if not inserted and target_header.lower() in line.lower() and line.strip().startswith("#"):
                        new_lines.append(formatted_line)
                        inserted = True
                new_content_raw = "\n".join(new_lines)
            
            if inserted:
                # If a new header was added, rebuild the TOC
                if is_new:
                    log_event(f"  [🏠] AI decided: Section '{target_header}' (NEW)")
                    return await self._rebuild_toc(new_content_raw)
                log_event(f"  [🏠] AI decided: Section '{target_header}' (EXISTING)")
                return new_content_raw
                
        except: pass
        return self._manual_fallback_injection(markdown_content, asset)

    def _manual_fallback_injection(self, content: str, asset: Dict) -> str:
        stars = " 🌟" if asset['impact_score'] > 80 else ""
        year_prefix = f"**({asset.get('year')})** " if asset.get('year') and asset.get('year') != "N/A" else ""
        line = f"  - {year_prefix}[{asset['title']}]({asset['url']}){stars} - {asset['description']}"
        # If no sections, add a generic header
        if "##" not in content:
            return content + f"\n\n## Tools and Resources\n{line}"
        return content + f"\n{line}"

    async def suggest_reorganization(self):
        """
        Audits files and reorganizes them INTERNALLY, rebuilding the TOC.
        """
        log_event("[*] Starting Internal Reorganization Audit...", section_break=True)
        
        for file in os.listdir(self.docs_dir):
            if not file.endswith(".md") or file == "index.md": continue
            
            path = os.path.join(self.docs_dir, file)
            with open(path, 'r') as f: content = f.read()
            
            links = re.findall(r'^\s*-\s*\[', content, re.MULTILINE)
            headers = re.findall(r'^##\s+', content, re.MULTILINE)
            
            if len(links) > 25 and len(headers) < 3:
                log_event(f"  [!] REORGANIZING: {file}")
                
                prompt = (
                    f"Reorganize the file '{file}' into logical sections (##).\n"
                    "KEEP ALL LINKS. DO NOT include the TOC (I will generate it).\n"
                    "ALL HEADERS MUST BE IN ENGLISH.\n"
                    f"CURRENT CONTENT:\n{content[:5000]}"
                )
                
                try:
                    reorganized = await call_gemini_with_retry(prompt, response_format="text")
                    if len(reorganized) > len(content) * 0.7:
                        # Rebuild the TOC after massive reorganization
                        final_content = await self._rebuild_toc(reorganized)
                        with open(path, 'w') as f: f.write(final_content)
                        log_event(f"  [OK] Reorganization and TOC updated for {file}")
                except Exception as e:
                    log_event(f"  [!] Error reorganizing {file}: {e}")

    def validate_changes(self) -> bool:
        return True
