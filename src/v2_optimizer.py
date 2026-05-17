import os
import re
import json
import asyncio
import yaml
import httpx
from datetime import datetime
from typing import List, Dict, Set, Any
from src.config import GEMINI_API_KEYS, GH_TOKEN, TARGET_REPO, MADRID_TZ, INVENTORY_PATH, STRUCTURE_MAP_PATH
from src.gemini_utils import call_gemini_with_retry, normalize_url
from src.logger import log_event

V1_DIR = "docs"
V2_DIR = "v2-docs"
INVENTORY_PATH = "data/inventory.yaml"
STRUCTURE_MAP_PATH = "data/structure_map.yaml"

class V2VisionEngine:
    def __init__(self):
        # 100% Comprehensive 2026 Taxonomy
        self.dimensions = {
            "Intelligent Control Plane": ["ai", "ai-agents-mcp", "chatgpt", "mlops"],
            "Architectural Foundations": ["introduction", "faq", "kubernetes", "linux", "git", "cloud-arch-diagrams", "matrix-table", "other-awesome-lists", "about"],
            "Platform & Site Reliability": ["sre", "devops", "developerportals", "scaffolding", "finops", "chaos-engineering", "performance-testing-with-jenkins-and-jmeter", "project-management-methodology", "project-management-tools", "qa", "test-automation-frameworks", "testops"],
            "Hardened Infrastructure": ["iac", "terraform", "pulumi", "crossplane", "ansible", "securityascode", "kubernetes-security", "aws-security", "oauth", "devsecops", "kustomize", "liquibase", "chef"],
            "Cloud Providers (Hyperscalers)": ["aws", "azure", "GoogleCloudPlatform", "ibm_cloud", "oraclecloud", "digitalocean", "cloudflare", "scaleway", "managed-kubernetes-in-public-cloud", "public-cloud-solutions", "private-cloud-solutions", "edge-computing", "aws-architecture", "aws-security", "aws-networking", "aws-databases", "aws-storage", "aws-monitoring", "aws-iac", "aws-tools-scripts", "aws-messaging", "aws-data", "aws-devops", "aws-serverless", "aws-containers", "aws-backup", "aws-training", "aws-newfeatures", "aws-miscellaneous", "aws-pricing", "aws-spain"],
            "Networking & Service Mesh": ["networking", "kubernetes-networking", "servicemesh", "istio", "caching", "web-servers", "cloudflare"],
            "The Container Stack": ["docker", "container-managers", "serverless", "kubernetes-autoscaling", "kubernetes-operators-controllers", "kubernetes-storage", "kubernetes-monitoring", "kubernetes-troubleshooting", "kubernetes-backup-migrations", "kubernetes-on-premise", "kubernetes-bigdata", "kubernetes-client-libraries", "kubernetes-releases", "kubernetes-based-devel", "kubernetes-alternatives", "kubectl-commands", "rancher", "openshift", "ocp3", "ocp4", "noops"],
            "Data & Advanced Analytics": ["databases", "nosql", "newsql", "message-queue", "crunchydata", "yaml", "bigdata"],
            "Engineering Pipeline": ["cicd", "gitops", "argo", "flux", "tekton", "jenkins", "jenkins-alternatives", "openshift-pipelines", "sonarqube", "registries", "keptn", "stackstorm", "cicd-kubernetes-plugins"],
            "Developer Ecosystem": ["visual-studio", "javascript", "golang", "python", "java_frameworks", "java_app_servers", "java-and-java-performance-optimization", "dotnet", "angular", "react", "web3", "api", "swagger-code-generator-for-rest-apis", "postman", "lowcode-nocode", "devel-sites", "dom", "linux-dev-env", "ChromeDevTools", "xamarin", "jvm-parameters-matrix-table", "maven-gradle", "embedded-servlet-containers"],
            "Career & Industry": ["recruitment", "hr", "freelancing", "remote-tech-jobs", "workfromhome", "interview-questions", "elearning", "digital-money", "appointment-scheduling", "newsfeeds"]
        }
        
        self.library_criteria = (
            "You are a Technical Librarian in 2026. Your mission is to build a high-density, professional reference library.\n"
            "PHASE 1: TECHNICAL PRESERVATION (HIGH INCLUSIVITY)\n"
            "- KEEP >90% of technical resources.\n"
            "PHASE 2: SOPHISTICATED SYNTHESIS & DATING\n"
            "- Extract precise PUBLICATION DATE (YYYY-MM-DD or YYYY): Look for dates in the URL, Twitter/X post dates, or text context. Return 'N/A' if truly unknown.\n"
            "- Detect source content LANGUAGE (e.g., 'English', 'Spanish', 'French').\n"
            "- Identify RESOURCE_TYPE: (Blog, Repository, Video, Tool, Documentation, Guide, Case Study).\n"
            "- Assign COMPLEXITY: (Beginner, Intermediate, Advanced, Architect).\n"
            "- Assign QUALITY level (0-5 stars):\n"
            "  * 0 stars: Good technical resource (Baseline).\n"
            "  * 1 star (🌟): High-quality technical guide or tool.\n"
            "  * 2 stars (🌟🌟): Exceptional, enterprise-grade resource.\n"
            "  * 3 stars (🌟🌟🌟): Elite Gem. Recommended for all architects.\n"
            "  * 4 stars (🌟🌟🌟🌟): Masterclass content or Essential Industry Tool.\n"
            "  * 5 stars (🌟🌟🌟🌟🌟): Legendary Resource (e.g., K8s Official Docs, Foundations like Prometheus/Envoy).\n"
            "- Assign a MATURITY TAG based on content type/status.\n"
            "PHASE 3: MANDATORY DESCRIPTIONS (V1 PRIORITY)\n"
            "- If 'Current Desc' is already provided and descriptive, DO NOT CHANGE IT.\n"
            "- If 'Current Desc' is empty, too short, or non-descriptive, generate a professional 1-2 sentence summary.\n"
            "- Style: Technical, neutral, and informative. Language: English only.\n"
        )
        self.inventory = self._load_inventory()
        self.structure_map = self._load_structure_map()
        self.maturity_audit = []

    def _load_inventory(self) -> Dict:
        if os.path.exists(INVENTORY_PATH):
            try:
                with open(INVENTORY_PATH, "r") as f:
                    return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def _save_inventory(self):
        os.makedirs(os.path.dirname(INVENTORY_PATH), exist_ok=True)
        with open(INVENTORY_PATH, "w") as f:
            yaml.dump(self.inventory, f, sort_keys=False, allow_unicode=True)

    def _load_structure_map(self) -> dict:
        if os.path.exists(STRUCTURE_MAP_PATH):
            try:
                with open(STRUCTURE_MAP_PATH, "r") as f:
                    import yaml
                    return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def _save_structure_map(self):
        os.makedirs(os.path.dirname(STRUCTURE_MAP_PATH), exist_ok=True)
        with open(STRUCTURE_MAP_PATH, "w") as f:
            import yaml
            yaml.dump(self.structure_map, f, sort_keys=False, allow_unicode=True)

    async def analyze_and_cluster(self):
        log_event("STARTING V2 HIGH-DENSITY CHRONOLOGICAL LIBRARY GENERATION", section_break=True)
        all_v1_links, mosaic_html, videos_html = await self._gather_all_v1_content()
        log_event(f"[*] Discovery: Found {len(all_v1_links)} resources in V1 archive.")

        log_event("[*] Phase 1: Health Check & Metadata Enrichment...")
        # Rapid Async Health Check
        health_inventory = await self._verify_link_health(all_v1_links)
        log_event(f"[*] Health Check Complete. {len(health_inventory)}/{len(all_v1_links)} links are online.")

        log_event("[*] Phase 2: Library Evaluation, Year Extraction & Quality Scoring...")
        library_inventory = await self._evaluate_and_score_resources(health_inventory)
        log_event(f"[*] Inventory Refined: {len(library_inventory)} resources kept.")

        log_event("[*] Phase 3: Dimensional Clustering & Chronological Sorting...")
        v2_data = await self._rebuild_structure(library_inventory)
        
        log_event("[*] Phase 3.5: Generating Executive State-of-the-Art Introductions...")
        for dim in v2_data.keys():
            cache_key = f"INTRO:{dim}"
            if cache_key in self.inventory and not os.getenv("FORCE_EVAL", "false").lower() == "true":
                v2_data[dim]["summary"] = self.inventory[cache_key].get("ai_summary")
            else:
                prompt = (
                    f"You act as a CTO and Cloud Architect in 2026. Write a professional, high-density paragraph (3-4 sentences) "
                    f"explaining the current 'State of the Art' and strategic importance of '{dim}' in the Kubernetes ecosystem. "
                    "Focus on executive value, innovation, and long-term technical direction. Language: English only."
                )
                try:
                    summary = await call_gemini_with_retry(prompt, response_format="text", prefer_flash=False) # Use Pro for better intros
                    v2_data[dim]["summary"] = summary
                    self.inventory[cache_key] = {"ai_summary": summary, "last_updated": datetime.now().isoformat()}
                except:
                    v2_data[dim]["summary"] = f"Executive reference library for {dim} architectures."

        log_event("[*] Phase 4: Generating Premium Portal Pages...")
        os.makedirs(V2_DIR, exist_ok=True)
        await self._write_premium_files(v2_data, mosaic_html, videos_html)
        await self._sync_enterprise_navigation(v2_data)
        
        self._save_inventory(); self._save_structure_map()
        log_event("V2 LIBRARY GENERATION COMPLETED.", section_break=True)

    async def _gather_all_v1_content(self) -> (List[Dict], str, str):
        all_links = []
        mosaic_html = ""
        videos_html = ""
        
        if os.path.exists("docs/index.md"):
            with open("docs/index.md", "r") as f:
                idx_content = f.read()
                # Find the BIG mosaic (the one with many images)
                # Support both old <center> and new <div style="text-align: center;" markdown="1">
                mosaics = re.findall(r'<(?:div style="text-align: center;" markdown="1"|center markdown="1"|center)>\s*(.*?)\s*</(?:div|center)>', idx_content, re.DOTALL)
                if mosaics:
                    # Filter for the one containing many image links
                    for m in mosaics:
                        if m.count("[![") > 5:
                            mosaic_html = m
                            break

                videos_match = re.search(r'\?\?\? note "Top Videos & Clips.*?\n(.*?\n)\s*</center>', idx_content, re.DOTALL)
                if videos_match: videos_html = videos_match.group(1)

        for root, _, files in os.walk(V1_DIR):
            for file in files:
                if not file.endswith(".md") or file == "index.md": continue
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    content = f.read()
                matches = re.finditer(r'^\s*-\s*\[([^\]]+)\]\(([^\)]+)\)(.*?(?:\n\s{2,}.*)*)', content, re.MULTILINE)
                for m in matches:
                    title, url, full_desc = m.groups()
                    
                    # FIX: Convert relative .md links to absolute V1 links for cross-edition stability
                    if not url.startswith(("http://", "https://", "mailto:", "#")):
                        if url.endswith(".md"):
                            url = f"https://nubenetes.com/{url.replace('.md', '/')}"
                        elif url.startswith("images/"):
                            # Use relative path from V2 to V1 images (handled via symlink)
                            url = f"{url}"

                    all_links.append({
                        "title": title, 
                        "url": url, 
                        "description": full_desc.strip(), 
                        "original_file": file
                    })
        return all_links, mosaic_html, videos_html

    async def _verify_link_health(self, links: List[Dict]) -> List[Dict]:
        online_links = []
        BATCH_SIZE = 50  # Smaller batches for stability
        
        # User-Agent rotation to mimic real browsers
        user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:125.0) Gecko/20100101 Firefox/125.0"
        ]

        async with httpx.AsyncClient(timeout=15.0, follow_redirects=True, verify=False) as client:
            for i in range(0, len(links), BATCH_SIZE):
                batch = links[i:i+BATCH_SIZE]
                tasks = []
                for l in batch:
                    ua = user_agents[i % len(user_agents)]
                    tasks.append(self._check_single_link_resilient(client, l, ua))
                
                results = await asyncio.gather(*tasks)
                online_links.extend([r for r in results if r is not None])
                
                if i % 500 == 0:
                    log_event(f"    [Resilient Health] Verified {i}/{len(links)} links...")
                
                # Brief pause to avoid triggering Rate Limits
                await asyncio.sleep(0.1)
                
        return online_links

    async def _check_single_link_resilient(self, client, link: Dict, ua: str, attempts: int = 3) -> Dict:
        url = link["url"]
        
        # NOTE: All domains must be checked for validity.

        # 2. Cached Health
        if url in self.inventory and self.inventory[normalize_url(url)].get("status") == "online":
            link["health_status"] = "cached"
            return link

        # 3. Multi-Attempt Verification with Identity Rotation
        headers = {
            "User-Agent": ua,
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.google.com/"
        }

        for attempt in range(attempts):
            try:
                # Use GET instead of HEAD as many sites block HEAD or return 405
                resp = await client.get(url, headers=headers, timeout=10.0)
                if resp.status_code < 400:
                    self.inventory.setdefault(url, {})["status"] = "online"
                    link["health_status"] = "online"
                    return link
                
                # If 404, it's a definitive fail
                if resp.status_code == 404:
                    log_event(f"    [Health] Definitive 404: {url}")
                    return None
                    
            except Exception as e:
                if attempt == attempts - 1:
                    # Final attempt failed - Soft Flagging instead of removal
                    # If it's not a 404, we keep it but with a warning
                    link["health_status"] = "uncertain"
                    link["warning"] = "offline"
                    return link
            
            # Backoff before retry
            await asyncio.sleep(0.5 * (attempt + 1))
            
        return link

    async def _evaluate_and_score_resources(self, links: List[Dict]) -> List[Dict]:
        refined = []
        to_evaluate = []
        force_eval = os.getenv("FORCE_EVAL", "false").lower() == "true"
        
        # We want to re-evaluate the tags and years, so we will bypass cache for tagging logic,
        # but use cache for AI stars if available to save cost.
        for l in links:
            url = l["url"]
            # To allow the new logic to apply to cached items, we re-process GitHub links 
            # and re-apply the tag logic even if it's in the cache.
            item = l.copy()
            if not force_eval and url in self.inventory and "stars" in self.inventory[normalize_url(url)]:
                item.update(self.inventory[normalize_url(url)])
                # If cache has a generated description and item is missing one, use it
                if "ai_summary" in self.inventory[normalize_url(url)] and not item["description"]:
                    item["description"] = self.inventory[normalize_url(url)]["ai_summary"]
            
            # --- TRACK MATURITY CHANGES ---
            old_tag = self.inventory.get(normalize_url(url), {}).get("tag")

            # Re-evaluate if description is still missing even after cache check
            if not item.get("description"):
                to_evaluate.append(item)
                continue
            
            # Re-apply GitHub metadata and mature tagging for cached items
            if "github.com" in url:
                gh_meta = await self._fetch_github_metadata(url)
                item.update(gh_meta)
                if "gh_updated" in gh_meta and gh_meta["gh_updated"]:
                    item["year"] = gh_meta["gh_updated"].split("-")[0]
            
            item["tag"] = self._calculate_tag(item)
            
            # Audit Check
            if old_tag and old_tag != item["tag"]:
                self.maturity_audit.append({
                    "url": url, "title": item["title"], "type": "Promotion" if "STANDARD" in item["tag"] or "STABLE" in item["tag"] else "Reclassification",
                    "old": old_tag, "new": item["tag"]
                })

            refined.append(item)

        if not to_evaluate: return refined

        BATCH_SIZE = 50 
        for i in range(0, len(to_evaluate), BATCH_SIZE):
            batch = to_evaluate[i:i+BATCH_SIZE]
            batch_num = i//BATCH_SIZE + 1
            log_event(f"  [>] Processing Batch {batch_num} with AI (Mandatory Descriptions)...")
            
            prompt = (
                f"{self.library_criteria}\n"
                "UNIVERSAL ENGLISH CURATION: ALL output 'summary' fields MUST be in ENGLISH. If source is non-English (e.g. Spanish), TRANSLATE to professional English.\n"
                "Respond ONLY with a JSON object: {\"results\": [{\"idx\": int, \"year\": \"YYYY\", \"stars\": 0-5, \"is_video\": bool, \"tag\": \"[TAG]\", \"summary\": \"1-2 sentences description\", \"language\": \"...\", \"type\": \"...\", \"level\": \"...\"}, ...]}\n\n"
                "LINKS:\n" + "\n".join([f"{idx}. {l['title']} ({l['url']}) - Current Desc: {l['description'][:50]}" for idx, l in enumerate(batch)])
            )
            
            try:
                data = await call_gemini_with_retry(prompt, prefer_flash=True)
                results = data.get("results", [])
                
                for res in results:
                    try:
                        idx = int(res["idx"])
                        if idx < len(batch):
                            item = batch[idx].copy()
                            norm_url = normalize_url(item["url"])
                            old_tag = self.inventory.get(norm_url, {}).get("tag")

                            eval_data = {
                                "year": str(res.get("year", "N/A")),
                                "stars": min(max(int(res.get("stars", 0)), 0), 5),
                                "is_video": res.get("is_video", False) or "video" in str(res.get("type", "")).lower(),
                                "tag": res.get("tag", "[ENTERPRISE-STABLE]"),
                                "ai_summary": res.get("summary", ""),
                                "language": res.get("language", "English"),
                                "resource_type": res.get("type", "Reference"),
                                "complexity": res.get("level", "Intermediate")
                            }
                            item.update(eval_data)
                            if not item["description"] and item["ai_summary"]:
                                item["description"] = item["ai_summary"]
                            
                            # GitHub overrides
                            if "github.com" in item["url"]:
                                gh_meta = await self._fetch_github_metadata(item["url"])
                                item.update(gh_meta)
                                if "gh_updated" in gh_meta and gh_meta["gh_updated"]:
                                    item["year"] = gh_meta["gh_updated"].split("-")[0]

                            item["tag"] = self._calculate_tag(item)
                            
                            # Audit Check for AI re-evaluation
                            if old_tag and old_tag != item["tag"]:
                                self.maturity_audit.append({
                                    "url": item["url"], "title": item["title"], "type": "AI Reclassification",
                                    "old": old_tag, "new": item["tag"]
                                })

                            refined.append(item)
                            
                            # Update inventory correctly
                            self.inventory[norm_url] = {
                                "title": item["title"], "year": item["year"], "stars": item["stars"],
                                "is_video": item["is_video"], "ai_summary": item["ai_summary"],
                                "language": item["language"], "resource_type": item["resource_type"],
                                "complexity": item["complexity"], "tag": item["tag"], "status": "online"
                            }
                            if "gh_stars" in item: self.inventory[norm_url]["gh_stars"] = item["gh_stars"]
                            if "gh_updated" in item: self.inventory[norm_url]["gh_updated"] = item["gh_updated"]
                    except: continue
            except:
                for l in batch:
                    item = l.copy()
                    item["year"], item["stars"], item["is_video"] = "N/A", 0, "youtube" in l["url"]
                    item["tag"] = self._calculate_tag(item)
                    refined.append(item)
            await asyncio.sleep(0.3)
        return refined

    def _calculate_tag(self, item: Dict) -> str:
        # Dynamic Evolutionary Tagging (Automatic Project Growth Detection)
        url = item.get("url", "").lower()
        stars = item.get("gh_stars", 0)
        year_str = str(item.get("year", "2024"))
        year = int(year_str) if year_str.isdigit() else 2024

        if "github.com" in url or "gitlab.com" in url:
            if stars > 15000: return "[DE FACTO STANDARD]"
            if stars > 3000: return "[ENTERPRISE-STABLE]"
            if stars > 500 and year >= 2025: return "[HIGH-GROWTH / EMERGING]"
            if year <= 2021 and stars < 100: return "[LEGACY / MAINTENANCE]"
            return "[COMMUNITY-TOOL]"
        
        # Article/Guide Logic
        title = item.get("title", "").lower()
        if "awesome" in title: return "[FOUNDATIONAL]"
        if "guide" in title or "architecture" in title: return "[ARCHITECTURE-GUIDE]"
        if "deep dive" in title or "internals" in title: return "[TECHNICAL-DEEP-DIVE]"
        if "how to" in title or "tutorial" in title: return "[CASE-STUDY]"
        
        # Fallback to AI's tag or defaults
        tag = item.get("tag", "").upper()
        valid_tags = ["[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]", "[EMERGING / INNOVATION]", "[LEGACY / MAINTENANCE]", "[ARCHITECTURE-GUIDE]", "[TOOLING]", "[CASE-STUDY]", "[CHEATSHEET]"]
        if tag in valid_tags:
            return tag
            
        return "[EXPERT-ARTICLE]"

    async def _fetch_github_metadata(self, url: str) -> Dict:
        match = re.search(r'github\.com/([^/]+)/([^/]+)', url)
        if not match: return {}
        owner, repo = match.groups()
        repo = repo.split("#")[0].split("?")[0] # Clean up
        
        headers = {"Authorization": f"token {GH_TOKEN}"} if GH_TOKEN else {}
        api_url = f"https://api.github.com/repos/{owner}/{repo}"
        
        try:
            async with httpx.AsyncClient(timeout=5.0) as client:
                resp = await client.get(api_url, headers=headers)
                if resp.status_code == 200:
                    data = resp.json()
                    return {
                        "gh_stars": data.get("stargazers_count", 0),
                        "gh_pushed": data.get("pushed_at", "").split("T")[0], "gh_created": data.get("created_at", "").split("T")[0]
                    }
        except: pass
        return {}

    async def _rebuild_structure(self, inventory: List[Dict]) -> Dict[str, Dict]:
        v2_structure = {dim: {"summary": "", "categories": {}} for dim in self.dimensions.keys()}
        file_to_dim = {}
        for dim, files in self.dimensions.items():
            for f in files: file_to_dim[f + ".md"] = dim

        for item in inventory:
            dim = file_to_dim.get(item["original_file"], "Architectural Foundations")
            cat_name = item["original_file"].replace(".md", "").capitalize()
            if cat_name not in v2_structure[dim]["categories"]:
                v2_structure[dim]["categories"][cat_name] = []
            v2_structure[dim]["categories"][cat_name].append(item)

        for dim in v2_structure.keys():
            if not v2_structure[dim]["categories"]: continue
            for cat in v2_structure[dim]["categories"]:
                # Sort by: 1. Stars (DESC), 2. Year (DESC, N/A at the end)
                v2_structure[dim]["categories"][cat].sort(
                    key=lambda x: (
                        -x.get("stars", 1),
                        -(int(x["year"]) if x.get("year", "").isdigit() else 0)
                    )
                )
            
            prompt = f"Write a professional 2026 executive summary for '{dim}'. Focus on high-density value. 1 sentence only."
            try:
                v2_structure[dim]["summary"] = await call_gemini_with_retry(prompt, response_format="text", prefer_flash=True)
            except:
                v2_structure[dim]["summary"] = f"Impact-driven reference library for {dim}."
                
        return v2_structure

    async def _write_premium_files(self, data: Dict[str, Dict], mosaic_html: str, videos_html: str):
        # FIX: Ensure mosaic images point to V1 root via symlink
        mosaic_html = mosaic_html.replace('src="images/', 'src="images/').replace('](images/', '](images/')
        
        master_selection = []
        for dim in data.values():
            for cat_links in dim["categories"].values():
                master_selection.extend([l for l in cat_links if l.get("stars", 0) >= 3])
        
        # Sort master selection by Stars (DESC), then Year (DESC), then Title (ASC)
        master_selection.sort(
            key=lambda x: (
                -x.get("stars", 0),
                -(int(x["year"]) if x.get("year", "").isdigit() else 0),
                x["title"]
            )
        )

        # --- THE AGENTIC PULSE (Trending) ---
        trending_pool = []
        for url, meta in self.inventory.items():
            if meta.get("stars", 0) >= 3:
                trending_pool.append(meta.copy())
                trending_pool[-1]["url"] = url

        # Sort by: 1. Pub/Post Date (DESC), 2. Stars (DESC)
        trending_pool.sort(key=lambda x: (
            x.get("pub_date", "0000") if x.get("pub_date") != "N/A" else x.get("post_date", "0000"),
            -x.get("stars", 0)
        ), reverse=True)

        pulse_md = "## ⚡ The Agentic Pulse: Trending Excellence\n"
        pulse_md += "Directly from the latest 2026 curation surges. High-impact technical depth recently added.\n\n"
        for l in trending_pool[:5]:
            stars = "🌟" * l.get("stars", 3)
            date = l.get("pub_date") if l.get("pub_date") != "N/A" else l.get("post_date")
            date_prefix = f"**({date[:10]})** " if date and date != "N/A" else ""
            pulse_md += f"- {date_prefix}[**=={l['title']}==**]({l['url']}) {stars}\n"

        index_md = (
            "# Nubenetes V2 | The High-Density Library (2026)\n\n"
            "![Banner](images/kubernetes_logo.jpg)\n\n"
            "!!! quote \"The Library of 2026\"\n"
            "    A meticulously curated reference of over 15,000 resources. This V2 portal preserves technical depth while providing "
            "    impact-driven synthesis and expert quality classification.\n\n"
            f"<center markdown=\"1\">\n{mosaic_html}\n</center>\n\n"
            f"{pulse_md}\n"
            "## 🛡️ V2 Taxonomy and Multi-Dimensional Tags\n"
            "To maximize technical clarity, V2 resources are categorized across four critical dimensions:\n\n"
            
            "### 1. Maturity Tiers (Strategic Status)\n"
            "- <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span>: Foundational industry tools with massive adoption (>10k GitHub stars).\n"
            "- <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>: Production-ready tools actively maintained.\n"
            "- <span class='md-tag md-tag--warning'>[EMERGING / INNOVATION]</span>: High-growth technologies released or heavily updated recently (≥2025).\n"
            "- <span class='md-tag md-tag--critical'>[LEGACY / MAINTENANCE]</span>: Proven solutions with no major updates since 2022. Use with caution.\n\n"

            "### 2. Audience Complexity (Target Level)\n"
            "- <span class='md-tag md-tag--critical'>[ARCHITECT LEVEL]</span>: High-level reasoning, system design, and long-term trade-offs.\n"
            "- <span class='md-tag md-tag--critical'>[ADVANCED LEVEL]</span>: Deep technical internals and complex implementations.\n"
            "- `(Default)`: Intermediate/General technical content for practitioners.\n\n"

            "### 3. Linguistic Diversity (Global Access)\n"
            "- <span class='md-tag md-tag--warning'>[SPANISH CONTENT]</span>: High-value resources in Spanish (Blogs, Videos, Guides).\n"
            "- `(Default)`: Professional technical English.\n\n"

            "### 4. Specialized Resource Types\n"
            "- <span class='md-tag md-tag--primary'>[CASE STUDY]</span>: Real-world implementation stories and post-mortems.\n"
            "- <span class='md-tag md-tag--primary'>[GUIDE]</span> / <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span>: Official or high-authority technical instructions.\n\n"
            
            "## 🌟 Master Selection (Top-Tier Gems)\n"
            "A global selection of the most impactful resources across all dimensions.\n\n"
        )
        for l in master_selection[:100]:
            gh_info = f" `[⭐ {l['gh_stars']}]`" if "gh_stars" in l else ""
            year_prefix = f"**({l['year']})** " if l.get("year") and l["year"] != "N/A" else ""
            title_clean = l['title'].replace("==", "")
            # Master selection links are 3-5 stars, so we highlight
            title_display = f"**=={title_clean}==**"
            stars_val = l.get("stars", 3)
            stars_str = "🌟" * stars_val
            index_md += f"- {year_prefix}[{title_display}]({l['url']}){gh_info} {stars_str}\n"
        
        index_md += "\n??? note \"Elite Video Selection - Click to expand!\"\n"
        index_md += f"    <center markdown=\"1\">\n{videos_html}\n    </center>\n\n"
        
        index_md += "## Strategic Dimensions\n"
        for dim, content in data.items():
            if not content["categories"]: continue
            slug = dim.lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "").replace(" ", "-")
            index_md += f"- **[{dim}](./{slug}.md)**: {content['summary']}\n"
        
        # Add Maturity Audit Log entry if changes exist
        if self.maturity_audit:
            index_md += f"\n---\n### 📈 [Latest Maturity Promotions and Reclassifications](./audit-log.md)\n"
            audit_md = "# Maturity Audit Log\n\nTransparency on AI curation decisions and project evolution.\n\n"
            audit_md += "| Project | Event | Previous Status | New Status |\n| :--- | :--- | :--- | :--- |\n"
            for change in self.maturity_audit[:50]: # Show last 50
                audit_md += f"| [{change['title']}]({change['url']}) | **{change['type']}** | `{change['old']}` | `{change['new']}` |\n"
            with open(os.path.join(V2_DIR, "audit-log.md"), "w") as f: f.write(audit_md)

        with open(os.path.join(V2_DIR, "index.md"), "w") as f: f.write(index_md)

        for dim, content in data.items():
            if not content["categories"]: continue
            slug = dim.lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "").replace(" ", "-")
            md = f"# {dim}\n\n"
            md += f"!!! info \"Architectural Context\"\n    {content['summary']}\n\n"
            for cat, links in content["categories"].items():
                md += f"## {cat}\n"
                for l in links:
                    year, stars_val = l.get("year", "N/A"), l.get("stars", 0)
                    stars = ("🌟" * stars_val) if stars_val > 0 else ""
                    tag = l.get("tag", "[ENTERPRISE-STABLE]")
                    
                    # Determine color mapping for new tags
                    if "STANDARD" in tag or "FOUNDATIONAL" in tag: color = "success"
                    elif "EMERGING" in tag: color = "warning"
                    elif "LEGACY" in tag: color = "critical"
                    elif "STABLE" in tag: color = "info"
                    else: color = "primary"
                    
                    title_clean = l['title'].replace("==", "")
                    if stars_val >= 3 or "STANDARD" in tag:
                        title_display = f"**=={title_clean}==**"
                    elif stars_val == 2:
                        title_display = f"**{title_clean}**"
                    else:
                        title_display = title_clean
                    
                    year_prefix = f"**({year})** " if year and year != "N/A" else ""
                    
                    gh_info = f" <span class='md-tag md-tag--info'>⭐ {l['gh_stars']}</span>" if "gh_stars" in l else ""
                    icon = " 🎥" if l.get("is_video") else ""
                    
                    # Language Tagging
                    lang = l.get("language", "English")
                    lang_tag = ""
                    if lang.lower() != "english":
                        lang_tag = f" <span class='md-tag md-tag--warning'>[{lang.upper()} CONTENT]</span>"
                    
                    # Complexity Tagging
                    level = l.get("complexity", "Intermediate")
                    level_tag = ""
                    if level.lower() in ["architect", "advanced"]:
                        level_tag = f" <span class='md-tag md-tag--critical'>[{level.upper()} LEVEL]</span>"
                    
                    # Resource Type Tagging
                    res_type = l.get("resource_type", "Reference")
                    type_tag = ""
                    if res_type.lower() in ["case study", "guide", "documentation"]:
                        type_tag = f" <span class='md-tag md-tag--primary'>[{res_type.upper()}]</span>"

                    # Rich Metadata Tags (Author, Duration, RT)
                    rich_tags = ""
                    if l.get("author"): rich_tags += f" <small>by **{l['author']}**</small>"
                    if l.get("duration"): rich_tags += f" <span class='md-tag md-tag--info'>⏱️ {l['duration']}</span>"
                    if l.get("reading_time"): rich_tags += f" <span class='md-tag md-tag--info'>📖 {l['reading_time']}</span>"

                    md += f"  - {year_prefix}[{title_display}]({l['url']}){icon}{gh_info}{lang_tag}{level_tag}{type_tag}{rich_tags} {stars} <span class='md-tag md-tag--{color}'>{tag}</span>\n"
                    if l['description']:
                        desc = l['description']
                        if "\n" in desc:
                            md += "\n" + "\n".join(["      " + line for line in desc.split("\n")]) + "\n\n"
                        else:
                            md += f"      {desc}\n"
                md += "\n"
            with open(os.path.join(V2_DIR, f"{slug}.md"), "w") as f: f.write(md)

    async def _sync_enterprise_navigation(self, data: Dict[str, Dict]):
        try:
            with open("v2-mkdocs.yml", "r") as f: content = f.read()
            nav_items = [
                "nav:", 
                "  - \"🔙 Back to V1 (Exhaustive)\": https://nubenetes.com/",
                "  - \"The 2026 Vision\": index.md"
            ]
            for dim in data.keys():
                if not data[dim]["categories"]: continue
                slug = dim.lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "").replace(" ", "-")
                nav_items.append(f"  - \"{dim}\": {slug}.md")
            
            if self.maturity_audit:
                nav_items.append("  - \"📈 Maturity Audit Log\": audit-log.md")
                
            new_nav = "\n".join(nav_items)
            updated_content = re.sub(r'nav:.*', new_nav, content, flags=re.DOTALL)
            with open("v2-mkdocs.yml", "w") as f: f.write(updated_content)
        except: pass

if __name__ == "__main__":
    engine = V2VisionEngine()
    asyncio.run(engine.analyze_and_cluster())
