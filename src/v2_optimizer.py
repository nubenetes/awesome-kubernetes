import os
import re
import json
import asyncio
import yaml
import httpx
from datetime import datetime
from typing import List, Dict, Set, Any
from src.config import GEMINI_API_KEYS, GH_TOKEN, TARGET_REPO, MADRID_TZ
from src.gemini_utils import call_gemini_with_retry
from src.logger import log_event

V1_DIR = "docs"
V2_DIR = "v2-docs"
V2_CACHE_PATH = "data/v2_cache.json"

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
            "- Extract precise PUBLICATION YEAR: Look for dates in the URL (e.g., /2023/05/ post dates), Twitter/X post dates, or text context. Return 'N/A' if truly unknown, do NOT guess '2024'.\n"
            "- Assign QUALITY level (1-3 stars).\n"
            "- Assign a MATURITY TAG based on content type/status: '[ENTERPRISE-STABLE]', '[EMERGING / INNOVATION]', '[ARCHITECTURE-GUIDE]', '[TOOLING]', '[CASE-STUDY]', or '[CHEATSHEET]'.\n"
            "  * Note: We will override tags for GitHub repos using real API data (Stars/Commits), so focus on classifying blogs and articles correctly.\n"
        )
        self.cache = self._load_cache()

    def _load_cache(self) -> Dict:
        if os.path.exists(V2_CACHE_PATH):
            try:
                with open(V2_CACHE_PATH, "r") as f: return json.load(f)
            except: return {}
        return {}

    def _save_cache(self):
        os.makedirs(os.path.dirname(V2_CACHE_PATH), exist_ok=True)
        with open(V2_CACHE_PATH, "w") as f: json.dump(self.cache, f, indent=2)

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

        log_event("[*] Phase 4: Generating Premium Portal Pages...")
        os.makedirs(V2_DIR, exist_ok=True)
        await self._write_premium_files(v2_data, mosaic_html, videos_html)
        await self._sync_enterprise_navigation(v2_data)
        
        self._save_cache()
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
        
        # 1. Immediate Pass for Trusted / Logic-Enriched Domains
        if "github.com" in url or "awesome" in link["title"].lower():
            link["health_status"] = "trusted"
            return link

        # 2. Cached Health
        if url in self.cache and self.cache[url].get("status") == "online":
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
                    self.cache.setdefault(url, {})["status"] = "online"
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
            if not force_eval and url in self.cache and "stars" in self.cache[url]:
                item.update(self.cache[url])
            else:
                to_evaluate.append(item)
                continue # process later via API
            
            # Re-apply GitHub metadata and mature tagging for cached items
            if "github.com" in url:
                gh_meta = await self._fetch_github_metadata(url)
                item.update(gh_meta)
                if "gh_updated" in gh_meta and gh_meta["gh_updated"]:
                    item["year"] = gh_meta["gh_updated"].split("-")[0]
            
            item["tag"] = self._calculate_tag(item)
            refined.append(item)

        if not to_evaluate: return refined

        BATCH_SIZE = 50 
        for i in range(0, len(to_evaluate), BATCH_SIZE):
            batch = to_evaluate[i:i+BATCH_SIZE]
            batch_num = i//BATCH_SIZE + 1
            log_event(f"  [>] Processing Batch {batch_num} with AI...")
            
            prompt = (
                f"{self.library_criteria}\n"
                "Respond ONLY with a JSON object: {\"results\": [{\"idx\": int, \"year\": \"YYYY\", \"stars\": int, \"is_video\": bool, \"tag\": \"[TAG]\"}, ...]}\n\n"
                "LINKS:\n" + "\n".join([f"{idx}. {l['title']} ({l['url']})" for idx, l in enumerate(batch)])
            )
            
            try:
                data = await call_gemini_with_retry(prompt)
                results = data.get("results", [])
                
                for res in results:
                    try:
                        idx = int(res["idx"])
                        if idx < len(batch):
                            item = batch[idx].copy()
                            eval_data = {
                                "year": str(res.get("year", "N/A")),
                                "stars": min(max(int(res.get("stars", 1)), 1), 3),
                                "is_video": res.get("is_video", False),
                                "tag": res.get("tag", "[ENTERPRISE-STABLE]")
                            }
                            item.update(eval_data)
                            
                            # GitHub overrides
                            if "github.com" in item["url"]:
                                gh_meta = await self._fetch_github_metadata(item["url"])
                                item.update(gh_meta)
                                if "gh_updated" in gh_meta and gh_meta["gh_updated"]:
                                    item["year"] = gh_meta["gh_updated"].split("-")[0]
                                    eval_data["year"] = item["year"]

                            item["tag"] = self._calculate_tag(item)
                            eval_data["tag"] = item["tag"]

                            # Save to cache
                            self.cache[item["url"]] = eval_data
                            refined.append(item)
                    except: continue
            except:
                for l in batch:
                    item = l.copy()
                    item["year"], item["stars"], item["is_video"] = "N/A", 1, "youtube" in l["url"]
                    item["tag"] = self._calculate_tag(item)
                    refined.append(item)
            await asyncio.sleep(0.3)
        return refined

    def _calculate_tag(self, item: Dict) -> str:
        # Dynamic Tagging Strategy based on Maturity and Real Data
        if "github.com" in item["url"] and "gh_stars" in item:
            stars = item["gh_stars"]
            year = int(item.get("year")) if item.get("year", "").isdigit() else 2024
            if stars > 10000: return "[DE FACTO STANDARD]"
            if stars > 500 and year >= 2024: return "[ENTERPRISE-STABLE]"
            if year >= 2025: return "[EMERGING / INNOVATION]"
            if year <= 2022: return "[LEGACY / MAINTENANCE]"
            return "[TOOLING]"
        
        # Fallback to AI's tag or defaults for articles
        tag = item.get("tag", "").upper()
        valid_tags = ["[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]", "[EMERGING / INNOVATION]", "[LEGACY / MAINTENANCE]", "[ARCHITECTURE-GUIDE]", "[TOOLING]", "[CASE-STUDY]", "[CHEATSHEET]"]
        if tag in valid_tags:
            return tag
        
        # Basic inference for articles
        title = item.get("title", "").lower()
        if "awesome" in title: return "[FOUNDATIONAL]"
        if "guide" in title or "architecture" in title: return "[ARCHITECTURE-GUIDE]"
        if "how to" in title or "tutorial" in title: return "[CASE-STUDY]"
        return "[ENTERPRISE-STABLE]"

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
                        "gh_updated": data.get("updated_at", "").split("T")[0]
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
                v2_structure[dim]["categories"][cat].sort(key=lambda x: (x.get("year", "0"), -x.get("stars", 0)))
            
            prompt = f"Write a professional 2026 executive summary for '{dim}'. Focus on high-density value. 1 sentence only."
            try:
                v2_structure[dim]["summary"] = await call_gemini_with_retry(prompt, response_format="text")
            except:
                v2_structure[dim]["summary"] = f"Comprehensive chronological reference library for {dim}."
                
        return v2_structure

    async def _write_premium_files(self, data: Dict[str, Dict], mosaic_html: str, videos_html: str):
        # FIX: Ensure mosaic images point to V1 root via symlink
        mosaic_html = mosaic_html.replace('src="images/', 'src="images/').replace('](images/', '](images/')
        
        master_selection = []
        for dim in data.values():
            for cat_links in dim["categories"].values():
                master_selection.extend([l for l in cat_links if l.get("stars", 1) == 3])
        master_selection.sort(key=lambda x: (x.get("year", "0"), x["title"]), reverse=True)

        index_md = (
            "# Nubenetes V2 | The High-Density Library (2026)\n\n"
            "![Banner](images/kubernetes_logo.jpg)\n\n"
            "!!! quote \"The Library of 2026\"\n"
            "    A meticulously curated reference of over 15,000 resources. This V2 portal preserves technical depth while providing "
            "    chronological clarity and expert quality synthesis.\n\n"
            f"<center markdown=\"1\">\n{mosaic_html}\n</center>\n\n"
            
            "## 🛡️ V2 Taxonomy & Maturity Tags\n"
            "To maximize technical clarity, V2 resources are classified by maturity rather than subjective quality:\n\n"
            "- <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span>: Foundational industry tools with massive adoption (>10k GitHub stars).\n"
            "- <span class='md-tag md-tag--info'>[ENTERPRISE-STABLE]</span>: Production-ready tools actively maintained.\n"
            "- <span class='md-tag md-tag--warning'>[EMERGING / INNOVATION]</span>: High-growth technologies released or heavily updated recently (≥2025).\n"
            "- <span class='md-tag md-tag--critical'>[LEGACY / MAINTENANCE]</span>: Proven solutions with no major updates since 2022. Use with caution.\n"
            "- <span class='md-tag md-tag--primary'>[ARCHITECTURE-GUIDE]</span> / <span class='md-tag md-tag--primary'>[CASE-STUDY]</span>: High-value reading material and use cases.\n\n"
            
            "## 🌟 Master Selection (Top-Tier Gems)\n"
            "A global selection of the most impactful resources across all dimensions.\n\n"
        )
        for l in master_selection[:100]:
            gh_info = f" `[⭐ {l['gh_stars']}]`" if "gh_stars" in l else ""
            index_md += f"- **({l['year']})** [{l['title']}]({l['url']}){gh_info} 🌟🌟🌟\n"
        
        index_md += "\n??? note \"Elite Video Selection - Click to expand!\"\n"
        index_md += f"    <center markdown=\"1\">\n{videos_html}\n    </center>\n\n"
        
        index_md += "## Strategic Dimensions\n"
        for dim, content in data.items():
            if not content["categories"]: continue
            slug = dim.lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "").replace(" ", "-")
            index_md += f"- **[{dim}](./{slug}.md)**: {content['summary']}\n"
        
        with open(os.path.join(V2_DIR, "index.md"), "w") as f: f.write(index_md)

        for dim, content in data.items():
            if not content["categories"]: continue
            slug = dim.lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "").replace(" ", "-")
            md = f"# {dim}\n\n"
            md += f"!!! info \"Architectural Context\"\n    {content['summary']}\n\n"
            for cat, links in content["categories"].items():
                md += f"## {cat}\n"
                for l in links:
                    year, stars = l.get("year", "N/A"), "🌟" * l.get("stars", 1)
                    tag = l.get("tag", "[ENTERPRISE-STABLE]")
                    
                    # Determine color mapping for new tags
                    if "STANDARD" in tag or "FOUNDATIONAL" in tag: color = "success"
                    elif "EMERGING" in tag: color = "warning"
                    elif "LEGACY" in tag: color = "critical"
                    elif "STABLE" in tag: color = "info"
                    else: color = "primary"
                    
                    title_display = f"**{l['title']}**" if l.get("stars", 1) >= 2 else l['title']
                    
                    gh_info = f" <span class='md-tag md-tag--info'>⭐ {l['gh_stars']}</span>" if "gh_stars" in l else ""
                    icon = " 🎥" if l.get("is_video") else ""
                    md += f"  - **({year})** [{title_display}]({l['url']}){icon}{gh_info} {stars} <span class='md-tag md-tag--{color}'>{tag}</span>\n"
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
            new_nav = "\n".join(nav_items)
            updated_content = re.sub(r'nav:.*', new_nav, content, flags=re.DOTALL)
            with open("v2-mkdocs.yml", "w") as f: f.write(updated_content)
        except: pass

if __name__ == "__main__":
    engine = V2VisionEngine()
    asyncio.run(engine.analyze_and_cluster())
