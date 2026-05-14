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
        # Comprehensive 2026 Taxonomy mapping EVERY relevant area from V1
        self.dimensions = {
            "Intelligent Control Plane": [
                "ai", "ai-agents-mcp", "chatgpt", "mlops"
            ],
            "Architectural Foundations": [
                "introduction", "faq", "kubernetes", "linux", "git", "cloud-arch-diagrams", 
                "introduction", "matrix-table", "other-awesome-lists"
            ],
            "Platform & Site Reliability": [
                "sre", "devops", "developerportals", "scaffolding", "finops", "chaos-engineering",
                "performance-testing-with-jenkins-and-jmeter", "project-management-methodology",
                "project-management-tools", "qa", "test-automation-frameworks", "testops"
            ],
            "Hardened Infrastructure": [
                "iac", "terraform", "pulumi", "crossplane", "ansible", "securityascode", 
                "kubernetes-security", "aws-security", "oauth", "devsecops", "kustomize", "liquibase"
            ],
            "Cloud Providers (Hyperscalers)": [
                "aws", "azure", "GoogleCloudPlatform", "ibm_cloud", "oraclecloud", "digitalocean", 
                "cloudflare", "scaleway", "managed-kubernetes-in-public-cloud", "public-cloud-solutions",
                "private-cloud-solutions", "edge-computing", "aws-architecture", "aws-security",
                "aws-networking", "aws-databases", "aws-storage", "aws-monitoring", "aws-iac",
                "aws-tools-scripts", "aws-messaging", "aws-data", "aws-devops", "aws-serverless",
                "aws-containers", "aws-backup", "aws-training", "aws-newfeatures"
            ],
            "Networking & Service Mesh": [
                "networking", "kubernetes-networking", "servicemesh", "istio", "caching", "web-servers"
            ],
            "The Container Stack": [
                "docker", "container-managers", "serverless", "kubernetes-autoscaling", 
                "kubernetes-operators-controllers", "kubernetes-storage", "kubernetes-monitoring",
                "kubernetes-troubleshooting", "kubernetes-backup-migrations", "kubernetes-on-premise",
                "kubernetes-bigdata", "kubernetes-client-libraries", "kubernetes-releases",
                "kubernetes-based-devel", "kubernetes-alternatives", "kubectl-commands", "rancher",
                "openshift", "ocp3", "ocp4"
            ],
            "Data & Advanced Analytics": [
                "databases", "nosql", "newsql", "message-queue", "crunchydata", "yaml"
            ],
            "Engineering Pipeline": [
                "cicd", "gitops", "argo", "flux", "tekton", "jenkins", "jenkins-alternatives",
                "openshift-pipelines", "sonarqube", "registries", "keptn", "stackstorm", 
                "cicd-kubernetes-plugins"
            ],
            "Developer Ecosystem": [
                "visual-studio", "javascript", "golang", "python", "java_frameworks", "java_app_servers",
                "java-and-java-performance-optimization", "dotnet", "angular", "react", "web3", 
                "api", "swagger-code-generator-for-rest-apis", "postman", "lowcode-nocode",
                "devel-sites", "dom", "linux-dev-env", "ChromeDevTools"
            ],
            "Career & Industry": [
                "recruitment", "hr", "freelancing", "remote-tech-jobs", "workfromhome", "interview-questions", "elearning", "about"
            ]
        }
        
        self.elite_criteria = (
            "You are a Senior Principal Architect in May 2026. "
            "Your task is to transform a raw technical list into an ENTERPRISE-GRADE technical portal.\n\n"
            "PHASE 1: TECHNICAL EVALUATION\n"
            "- Hold a VERY HIGH bar for quality and production relevance.\n"
            "- KEEP: Foundational Awesome lists, masterclasses, production-ready tools, and 2024-2026 innovations.\n"
            "- DISCARD: Introductory noise, redundant tools, personal anecdotes, and pre-2022 outdated content.\n\n"
            "PHASE 2: SEMANTIC SYNTHESIS\n"
            "- For the selected links, categorize them into: [FOUNDATIONAL], [PRODUCTION-READY], or [CUTTING-EDGE].\n"
            "- Write a 1-sentence technical executive summary for the whole section.\n"
        )

    async def analyze_and_cluster(self):
        log_event("STARTING V2 ARCHITECT'S CUT TRANSFORMATION (FULL COVERAGE)", section_break=True)
        
        all_v1_links = await self._gather_all_v1_content()
        log_event(f"[*] Discovery: Found {len(all_v1_links)} nodes in V1.")

        # 1. Excellence Filtering
        log_event("[*] Phase 1: Excellence Filtering & Quality Pass...")
        elite_inventory = await self._evaluate_quality(all_v1_links)
        log_event(f"[*] Inventory Refined: {len(elite_inventory)} high-signal resources selected.")

        # 2. Structural Reconstruction
        log_event("[*] Phase 2: Dimensional Clustering & Semantic Enrichment...")
        v2_data = await self._rebuild_structure(elite_inventory)

        # 3. File Generation
        log_event("[*] Phase 3: Generating Premium Portal Content...")
        os.makedirs(V2_DIR, exist_ok=True)
        await self._write_premium_files(v2_data)
        
        # 4. Navigation Sync
        await self._sync_enterprise_navigation(v2_data)
        
        log_event("V2 TRANSFORMATION COMPLETED SUCCESSFULLY.", section_break=True)

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
                    all_links.append({
                        "title": title, "url": url, "description": desc.strip(), "original_file": file
                    })
        return all_links

    async def _evaluate_quality(self, links: List[Dict]) -> List[Dict]:
        refined = []
        # Increase batch size slightly but keep it manageable
        BATCH_SIZE = 60
        for i in range(0, len(links), BATCH_SIZE):
            batch = links[i:i+BATCH_SIZE]
            batch_num = i//BATCH_SIZE + 1
            log_event(f"  [>] Processing Excellence Batch {batch_num}...")
            
            prompt = (
                f"{self.elite_criteria}\n"
                "Mission: Identify technically superior nodes.\n"
                "Respond ONLY with a JSON object: {\"keep_indices\": [int, ...], \"tags\": {\"index\": \"TAG\"}}\n"
                "TAGS available: [FOUNDATIONAL], [PRODUCTION-READY], [CUTTING-EDGE].\n\n"
                "LINKS:\n" + "\n".join([f"{idx}. {l['title']} ({l['url']})" for idx, l in enumerate(batch)])
            )
            
            try:
                data = await call_gemini_with_retry(prompt)
                indices = data.get("keep_indices", [])
                tags_map = data.get("tags", {})
                
                for idx in indices:
                    try:
                        idx_int = int(idx)
                        if idx_int < len(batch):
                            item = batch[idx_int].copy()
                            item["tag"] = tags_map.get(str(idx), "[PRODUCTION-READY]")
                            refined.append(item)
                    except: continue
                
                log_event(f"    [Batch {batch_num}] Quality: Kept {len(indices)}/{len(batch)}")
            except:
                # Conservative fallback for critical nodes
                refined.extend([l for l in batch if "awesome" in l['title'].lower()])
            
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

        # Generate summaries for each dimension
        for dim in v2_structure.keys():
            if not v2_structure[dim]["categories"]: continue
            log_event(f"  [*] Synthesizing executive summary for {dim}...")
            prompt = f"Write a 1-sentence professional executive summary for a technical portal section titled '{dim}'. Use sophisticated 2026 architectural tone. Respond ONLY with the sentence."
            try:
                v2_structure[dim]["summary"] = await call_gemini_with_retry(prompt, response_format="text")
            except:
                v2_structure[dim]["summary"] = f"Curated selection of high-impact resources for {dim}."
                
        return v2_structure

    async def _write_premium_files(self, data: Dict[str, Dict]):
        # Home
        index_md = (
            "# Nubenetes V2 | The Architect's Cut (2026)\n\n"
            "![Nubenetes Banner](https://raw.githubusercontent.com/nubenetes/awesome-kubernetes/master/docs/images/logo.png)\n\n"
            "!!! quote \"Engineering the Future\"\n"
            "    This portal represents the state-of-the-art in Cloud Native engineering. It is a derived intelligence layer "
            "    filtered through the lens of production stability and technical innovation.\n\n"
            "## Exploration Dimensions\n"
            "Our repository is organized into professional dimensions for the modern engineer:\n\n"
        )
        for dim, content in data.items():
            if not content["categories"]: continue
            slug = dim.lower().replace(" ", "-").replace("&", "and")
            index_md += f"- **[{dim}](./{slug}.md)**: {content['summary']}\n"
        
        with open(os.path.join(V2_DIR, "index.md"), "w") as f: f.write(index_md)

        # Dimension pages
        for dim, content in data.items():
            if not content["categories"]: continue
            slug = dim.lower().replace(" ", "-").replace("&", "and")
            
            md = f"# {dim}\n\n"
            md += f"!!! summary \"Executive Overview\"\n    {content['summary']}\n\n"
            
            for cat, links in content["categories"].items():
                md += f"## {cat}\n"
                for l in links:
                    tag_color = "success" if "FOUNDATIONAL" in l["tag"] else "info" if "PRODUCTION" in l["tag"] else "warning"
                    md += f"  - [{l['title']}]({l['url']}) {l['description']} <span class='md-tag md-tag--{tag_color}'>{l['tag']}</span>\n"
                md += "\n"
                
            with open(os.path.join(V2_DIR, f"{slug}.md"), "w") as f: f.write(md)

    async def _sync_enterprise_navigation(self, data: Dict[str, Dict]):
        try:
            with open("v2-mkdocs.yml", "r") as f: content = f.read()
            
            nav_items = ["nav:", "  - \"The 2026 Vision\": index.md"]
            for dim in data.keys():
                if not data[dim]["categories"]: continue
                slug = dim.lower().replace(" ", "-").replace("&", "and")
                nav_items.append(f"  - \"{dim}\": {slug}.md")
                
            new_nav = "\n".join(nav_items)
            updated_content = re.sub(r'nav:.*', new_nav, content, flags=re.DOTALL)
            
            with open("v2-mkdocs.yml", "w") as f: f.write(updated_content)
            log_event("  [OK] v2-mkdocs.yml navigation updated for Full Enterprise View.")
        except Exception as e:
            log_event(f"  [!] Error syncing navigation: {e}")

if __name__ == "__main__":
    engine = V2VisionEngine()
    asyncio.run(engine.analyze_and_cluster())
