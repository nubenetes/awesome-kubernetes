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
            "PHASE 1: TECHNICAL PRESERVATION\n"
            "- Be INCLUSIVE. Do not discard useful technical content just because it's a few years old.\n"
            "- KEEP: Technically solid tools, guides, and documentation. Even if 'classic', they are part of the library.\n"
            "- DISCARD ONLY: Broken links, 404s, obvious spam, non-technical jokes, and personal anecdotes.\n"
            "- ALWAYS keep 'Awesome' repositories.\n\n"
            "PHASE 2: TEMPORAL ANALYSIS\n"
            "- For EACH kept resource, identify or estimate the PUBLICATION YEAR.\n"
            "- Use URL patterns (e.g., /2023/...), content clues, or tool era to decide the year.\n"
            "- If totally unknown, use 2024 as default for recently active looking sites, or 'N/A'.\n"
        )

    async def analyze_and_cluster(self):
        log_event("STARTING V2 HIGH-DENSITY CHRONOLOGICAL LIBRARY GENERATION", section_break=True)
        all_v1_links = await self._gather_all_v1_content()
        log_event(f"[*] Discovery: Found {len(all_v1_links)} resources in V1 archive.")

        log_event("[*] Phase 1: Library Evaluation & Year Extraction...")
        library_inventory = await self._evaluate_and_date_resources(all_v1_links)
        log_event(f"[*] Inventory Refined: {len(library_inventory)} high-quality resources kept.")

        log_event("[*] Phase 2: Dimensional Clustering & Chronological Sorting...")
        v2_data = await self._rebuild_structure(library_inventory)

        log_event("[*] Phase 3: Generating Premium Portal Pages...")
        os.makedirs(V2_DIR, exist_ok=True)
        await self._write_premium_files(v2_data)
        await self._sync_enterprise_navigation(v2_data)
        
        log_event("V2 LIBRARY GENERATION COMPLETED.", section_break=True)

    async def _gather_all_v1_content(self) -> List[Dict]:
        all_links = []
        for root, _, files in os.walk(V1_DIR):
            for file in files:
                if not file.endswith(".md") or file == "index.md": continue
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    content = f.read()
                matches = re.findall(r'^\s*-\s*\[([^\]]+)\]\(([^\)]+)\)(.*)', content, re.MULTILINE)
                for title, url, desc in matches:
                    all_links.append({"title": title, "url": url, "description": desc.strip(), "original_file": file})
        return all_links

    async def _evaluate_and_date_resources(self, links: List[Dict]) -> List[Dict]:
        refined = []
        BATCH_SIZE = 50 
        for i in range(0, len(links), BATCH_SIZE):
            batch = links[i:i+BATCH_SIZE]
            batch_num = i//BATCH_SIZE + 1
            log_event(f"  [>] Processing Batch {batch_num}...")
            
            prompt = (
                f"{self.library_criteria}\n"
                "Respond ONLY with a JSON object: {\"keep_indices\": [int, ...], \"years\": {\"index\": \"YYYY\"}}\n\n"
                "LINKS:\n" + "\n".join([f"{idx}. {l['title']} ({l['url']})" for idx, l in enumerate(batch)])
            )
            
            try:
                data = await call_gemini_with_retry(prompt)
                indices = data.get("keep_indices", [])
                years_map = data.get("years", {})
                
                for idx in indices:
                    try:
                        idx_int = int(idx)
                        if idx_int < len(batch):
                            item = batch[idx_int].copy()
                            year_val = years_map.get(str(idx), "2024")
                            item["year"] = str(year_val)
                            # Tag based on year
                            if item["year"].isdigit() and int(item["year"]) >= 2025: item["tag"] = "[CUTTING-EDGE]"
                            elif "awesome" in item["title"].lower(): item["tag"] = "[FOUNDATIONAL]"
                            else: item["tag"] = "[PRODUCTION-READY]"
                            refined.append(item)
                    except: continue
                log_event(f"    [Batch {batch_num}] Kept {len(indices)}/{len(batch)}")
            except:
                # Conservative fallback: keep and mark as 2024
                for l in batch:
                    item = l.copy()
                    item["year"] = "2024"
                    item["tag"] = "[FOUNDATIONAL]" if "awesome" in l["title"].lower() else "[PRODUCTION-READY]"
                    refined.append(item)
            await asyncio.sleep(0.5)
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

        # Sort within each category by year (descending)
        for dim in v2_structure.keys():
            if not v2_structure[dim]["categories"]: continue
            for cat in v2_structure[dim]["categories"]:
                v2_structure[dim]["categories"][cat].sort(key=lambda x: x.get("year", "0"), reverse=True)
            
            # Dimension summary
            prompt = f"Write a 1-sentence executive summary for section '{dim}'. Professional 2026 tone. Respond ONLY with the sentence."
            try:
                v2_structure[dim]["summary"] = await call_gemini_with_retry(prompt, response_format="text")
            except:
                v2_structure[dim]["summary"] = f"Curated high-density chronological resources for {dim}."
                
        return v2_structure

    async def _write_premium_files(self, data: Dict[str, Dict]):
        # Home
        mermaid_code = "graph TD\n"
        for dim in data.keys():
            if data[dim]["categories"]:
                mermaid_code += f"    V2[Nubenetes V2] --> {dim.replace(' ', '_').replace('&', 'and').replace('(', '').replace(')', '')}[{dim}]\n"

        index_md = (
            "# Nubenetes V2 | The High-Density Library (2026)\n\n"
            "![Banner](https://raw.githubusercontent.com/nubenetes/awesome-kubernetes/master/docs/images/logo.png)\n\n"
            "!!! quote \"Chronological Excellence\"\n"
            "    This portal is a time-indexed reference for Cloud Native engineering. Resources are sorted by publication year "
            "    to ensure you have both the latest innovations and foundational classics at your fingertips.\n\n"
            "## System Architecture View\n\n"
            "```mermaid\n" + mermaid_code + "```\n\n"
            "## Strategic Dimensions\n\n"
        )
        for dim, content in data.items():
            if not content["categories"]: continue
            slug = dim.lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "").replace(" ", "-")
            index_md += f"- **[{dim}](./{slug}.md)**: {content['summary']}\n"
        with open(os.path.join(V2_DIR, "index.md"), "w") as f: f.write(index_md)

        # Dimension pages
        for dim, content in data.items():
            if not content["categories"]: continue
            slug = dim.lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "").replace(" ", "-")
            md = f"# {dim}\n\n"
            md += f"!!! info \"Executive Overview\"\n    {content['summary']}\n\n"
            for cat, links in content["categories"].items():
                md += f"## {cat}\n"
                for l in links:
                    year = l.get("year", "N/A")
                    tag = l.get("tag", "[PRODUCTION-READY]")
                    color = "success" if "FOUNDATIONAL" in tag else "info" if "PRODUCTION" in tag else "warning"
                    md += f"  - **({year})** [{l['title']}]({l['url']}) {l['description']} <span class='md-tag md-tag--{color}'>{tag}</span>\n"
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
