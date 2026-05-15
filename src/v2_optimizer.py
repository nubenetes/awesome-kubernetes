import os
import re
import json
import asyncio
import yaml
from datetime import datetime
from typing import List, Dict, Set, Any
from src.config import GEMINI_API_KEYS, GH_TOKEN, TARGET_REPO, MADRID_TZ
from src.gemini_utils import call_gemini_with_retry
from src.logger import log_event

V1_DIR = "docs"
V2_DIR = "v2-docs"

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
            "- KEEP >90% of technical resources. Only discard 404s, obvious spam, or non-technical content.\n"
            "- 'Awesome' repositories, official documentation, and deep technical guides are mandatory.\n"
            "- YouTube videos are HIGH-VALUE resources; keep them as technical references.\n\n"
            "PHASE 2: TEMPORAL & QUALITY SYNTHESIS\n"
            "- Identify/estimate PUBLICATION YEAR.\n"
            "- Assign QUALITY level (1-3 stars):\n"
            "  * 3 stars (🌟🌟🌟): Masterpieces, foundational standards, definitive 'Awesome' lists.\n"
            "  * 2 stars (🌟🌟): Production-grade tools, deep tutorials, highly recommended videos.\n"
            "  * 1 star (🌟): Solid technical references.\n"
            "- Identify if a resource is a 'YouTube Video/Playlist' for special rendering.\n"
        )

    async def analyze_and_cluster(self):
        log_event("STARTING V2 HIGH-DENSITY CHRONOLOGICAL LIBRARY GENERATION", section_break=True)
        all_v1_links, mosaic_html, videos_html = await self._gather_all_v1_content()
        log_event(f"[*] Discovery: Found {len(all_v1_links)} resources in V1 archive.")

        log_event("[*] Phase 1: Library Evaluation, Year Extraction & Quality Scoring...")
        library_inventory = await self._evaluate_and_score_resources(all_v1_links)
        log_event(f"[*] Inventory Refined: {len(library_inventory)} resources kept.")

        log_event("[*] Phase 2: Dimensional Clustering & Chronological Sorting...")
        v2_data = await self._rebuild_structure(library_inventory)

        log_event("[*] Phase 3: Generating Premium Portal Pages...")
        os.makedirs(V2_DIR, exist_ok=True)
        await self._write_premium_files(v2_data, mosaic_html, videos_html)
        await self._sync_enterprise_navigation(v2_data)
        
        log_event("V2 LIBRARY GENERATION COMPLETED.", section_break=True)

    async def _gather_all_v1_content(self) -> (List[Dict], str, str):
        all_links = []
        mosaic_html = ""
        videos_html = ""
        
        # Read index.md specifically for mosaic and embedded videos
        if os.path.exists("docs/index.md"):
            with open("docs/index.md", "r") as f:
                idx_content = f.read()
                # Extract YouTuber Mosaic (the <center> block with images)
                mosaic_match = re.search(r'<center>\s*(\[!\[.*?)\s*</center>', idx_content, re.DOTALL)
                if mosaic_match: mosaic_html = mosaic_match.group(1)
                
                # Extract Top Videos (the ??? note block)
                videos_match = re.search(r'\?\?\? note "Top Videos & Clips.*?\n(.*?\n)\s*</center>', idx_content, re.DOTALL)
                if videos_match: videos_html = videos_match.group(1)

        for root, _, files in os.walk(V1_DIR):
            for file in files:
                if not file.endswith(".md") or file == "index.md": continue
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    content = f.read()
                
                # Regex for links + following blocks (indented or multiple lines)
                matches = re.finditer(r'^\s*-\s*\[([^\]]+)\]\(([^\)]+)\)(.*?(?:\n\s{2,}.*)*)', content, re.MULTILINE)
                for m in matches:
                    title, url, full_desc = m.groups()
                    all_links.append({
                        "title": title, 
                        "url": url, 
                        "description": full_desc.strip(), 
                        "original_file": file
                    })
        return all_links, mosaic_html, videos_html

    async def _evaluate_and_score_resources(self, links: List[Dict]) -> List[Dict]:
        refined = []
        BATCH_SIZE = 50 
        for i in range(0, len(links), BATCH_SIZE):
            batch = links[i:i+BATCH_SIZE]
            batch_num = i//BATCH_SIZE + 1
            log_event(f"  [>] Processing Batch {batch_num}...")
            
            prompt = (
                f"{self.library_criteria}\n"
                "Respond ONLY with a JSON object: {\"results\": [{\"idx\": int, \"year\": \"YYYY\", \"stars\": int, \"is_video\": bool}, ...]}\n\n"
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
                            item["year"] = str(res.get("year", "2024"))
                            item["stars"] = min(max(int(res.get("stars", 1)), 1), 3)
                            item["is_video"] = res.get("is_video", False)
                            
                            if item["year"].isdigit() and int(item["year"]) >= 2025: item["tag"] = "[CUTTING-EDGE]"
                            elif "awesome" in item["title"].lower(): item["tag"] = "[FOUNDATIONAL]"
                            else: item["tag"] = "[PRODUCTION-READY]"
                            
                            refined.append(item)
                    except: continue
            except:
                for l in batch:
                    item = l.copy()
                    item["year"], item["stars"], item["is_video"] = "2024", 1, "youtube" in l["url"]
                    item["tag"] = "[FOUNDATIONAL]" if "awesome" in l["title"].lower() else "[PRODUCTION-READY]"
                    refined.append(item)
            await asyncio.sleep(0.3)
        return refined

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
                # Chronological Ascending (Oldest -> Newest) as per user preference
                v2_structure[dim]["categories"][cat].sort(key=lambda x: (x.get("year", "0"), -x.get("stars", 0)))
            
            prompt = f"Write a professional 2026 executive summary for '{dim}'. Focus on high-density value. 1 sentence only."
            try:
                v2_structure[dim]["summary"] = await call_gemini_with_retry(prompt, response_format="text")
            except:
                v2_structure[dim]["summary"] = f"Comprehensive chronological reference library for {dim}."
                
        return v2_structure

    async def _write_premium_files(self, data: Dict[str, Dict], mosaic_html: str, videos_html: str):
        # High-Density Master Selection for index.md
        master_selection = []
        for dim in data.values():
            for cat_links in dim["categories"].values():
                master_selection.extend([l for l in cat_links if l.get("stars", 1) == 3])
        master_selection.sort(key=lambda x: (x.get("year", "0"), x["title"]))

        index_md = (
            "# Nubenetes V2 | The High-Density Library (2026)\n\n"
            "![Banner](https://raw.githubusercontent.com/nubenetes/awesome-kubernetes/master/docs/images/logo.png)\n\n"
            "!!! quote \"The Library of 2026\"\n"
            "    A meticulously curated reference of over 15,000 resources. This V2 portal preserves technical depth while providing "
            "    chronological clarity and expert quality synthesis.\n\n"
            f"<center>\n{mosaic_html}\n</center>\n\n"
            "## 🌟 Master Selection (Top-Tier Gems)\n"
            "A global selection of the most impactful resources across all dimensions.\n\n"
        )
        for l in master_selection[:100]: # Top 100 for the index
            index_md += f"- **({l['year']})** [{l['title']}]({l['url']}) 🌟🌟🌟\n"
        
        index_md += "\n??? note \"Elite Video Selection - Click to expand!\"\n"
        index_md += f"    <center>\n{videos_html}\n    </center>\n\n"
        
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
                    tag = l.get("tag", "[PRODUCTION-READY]")
                    color = "success" if "FOUNDATIONAL" in tag else "info" if "PRODUCTION" in tag else "warning"
                    title_display = f"**{l['title']}**" if l.get("stars", 1) >= 2 else l['title']
                    
                    icon = " 🎥" if l.get("is_video") else ""
                    md += f"  - **({year})** [{title_display}]({l['url']}){icon} {stars} <span class='md-tag md-tag--{color}'>{tag}</span>\n"
                    if l['description']:
                        desc = l['description']
                        # Preserve large summary blocks with proper indentation
                        if "\n" in desc:
                            md += "\n" + "\n".join(["      " + line for line in desc.split("\n")]) + "\n\n"
                        else:
                            md += f"      {desc}\n"
                md += "\n"
            with open(os.path.join(V2_DIR, f"{slug}.md"), "w") as f: f.write(md)



    async def _sync_enterprise_navigation(self, data: Dict[str, Dict]):
        try:
            with open("v2-mkdocs.yml", "r") as f: content = f.read()
            nav_items = ["nav:", "  - \"The 2026 Vision\": index.md"]
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
