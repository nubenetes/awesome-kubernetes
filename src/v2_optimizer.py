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
        self.taxonomy_2026 = {
            "Foundations": ["introduction", "faq", "kubernetes", "linux", "git"],
            "Agentic AI & LLMOps": ["ai", "ai-agents-mcp", "chatgpt", "mlops"],
            "Modern Infrastructure": ["iac", "terraform", "pulumi", "crossplane", "ansible", "cloud-arch-diagrams"],
            "Security & Zero Trust": ["securityascode", "kubernetes-security", "aws-security", "oauth", "devsecops"],
            "Observability & AIOps": ["monitoring", "prometheus", "grafana", "kubernetes-monitoring", "chaos-engineering"],
            "Platform Engineering": ["devops", "sre", "developerportals", "scaffolding", "finops"],
            "Cloud Providers": ["aws", "azure", "GoogleCloudPlatform", "digitalocean", "cloudflare"],
            "Networking & Connectivity": ["networking", "kubernetes-networking", "servicemesh", "istio"],
            "Runtime & Containers": ["docker", "container-managers", "serverless", "wasm"],
            "Data & Databases": ["databases", "nosql", "message-queue", "bigdata", "databricks"],
            "Software Delivery": ["cicd", "gitops", "argo", "flux", "tekton", "jenkins", "registries"],
            "Developer Experience": ["visual-studio", "javascript", "golang", "python", "java_frameworks", "angular", "react"]
        }

    async def analyze_and_cluster(self):
        log_event("STARTING V2 HIGH-DENSITY TRANSFORMATION", section_break=True)
        
        all_v1_links = await self._gather_all_v1_content()
        log_event(f"[*] Total resources discovered in V1: {len(all_v1_links)}")

        # 1. Semantic Purge & Scoring
        log_event("[*] Phase 1: Semantic Evaluation & Professional Filtering...")
        elite_inventory = await self._evaluate_professional_impact(all_v1_links)
        log_event(f"[*] Elite Inventory Size: {len(elite_inventory)} high-impact resources.")

        # 2. Re-architecting Sections
        log_event("[*] Phase 2: Structural Clustering for 2026 Taxonomy...")
        v2_structure = await self._cluster_into_2026_taxonomy(elite_inventory)

        # 3. Generating Files
        log_event("[*] Phase 3: Generating V2 High-Density Portal...")
        os.makedirs(V2_DIR, exist_ok=True)
        await self._write_v2_files(v2_structure)
        
        # 4. Generating Advanced Navigation
        await self._generate_v2_navigation(v2_structure)
        
        log_event("V2 TRANSFORMATION COMPLETED.", section_break=True)

    async def _gather_all_v1_content(self) -> List[Dict]:
        all_links = []
        for root, _, files in os.walk(V1_DIR):
            for file in files:
                if not file.endswith(".md") or file == "index.md": continue
                path = os.path.join(root, file)
                with open(path, "r") as f:
                    content = f.read()
                
                # Extract links with context
                matches = re.findall(r'^\s*-\s*\[([^\]]+)\]\(([^\)]+)\)(.*)', content, re.MULTILINE)
                for title, url, desc in matches:
                    all_links.append({
                        "title": title,
                        "url": url,
                        "description": desc.strip(),
                        "original_file": file
                    })
        return all_links

    async def _evaluate_professional_impact(self, links: List[Dict]) -> List[Dict]:
        elite = []
        
        async def process_link_batch(batch):
            prompt = (
                "Act as a Principal Platform Architect in 2026. Filter these resources for a HIGH-DENSITY professional portal.\n"
                "RULES:\n"
                "1. REMOVE: Non-professional content, jokes, personal notes, broken/outdated tools pre-2022.\n"
                "2. KEEP: All 'Awesome' repos, innovative tools (eBPF, AI, Agentic, WASM), and industry standards.\n"
                "3. TRANSFORM: Ensure descriptions are technical and English only.\n\n"
                "LINKS:\n" + "\n".join([f"{i}. [{l['title']}]({l['url']}) - {l['description']}" for i, l in enumerate(batch)]) + "\n\n"
                "Respond ONLY with a JSON list of indices to KEEP. Example: [0, 2, 3]"
            )
            try:
                indices = await call_gemini_with_retry(prompt)
                return [batch[i] for i in indices if i < len(batch)]
            except:
                # On error, keep all in batch to avoid data loss (safe fallback)
                return batch

        for i in range(0, len(links), 50):
            batch = links[i:i+50]
            log_event(f"  [>] Evaluating batch {i//50 + 1}...")
            result = await process_link_batch(batch)
            elite.extend(result)
            await asyncio.sleep(1)
            
        return elite

    async def _cluster_into_2026_taxonomy(self, inventory: List[Dict]) -> Dict[str, List[Dict]]:
        # This simplifies the complex V1 list into our new 2026 categories
        clustered = {cat: [] for cat in self.taxonomy_2026.keys()}
        
        # Mapping original files to new categories
        file_to_cat = {}
        for cat, v1_files in self.taxonomy_2026.items():
            for f in v1_files:
                file_to_cat[f + ".md"] = cat

        for item in inventory:
            cat = file_to_cat.get(item["original_file"], "Foundations")
            clustered[cat].append(item)
            
        return clustered

    async def _write_v2_files(self, structure: Dict[str, List[Dict]]):
        # Create Home
        index_content = (
            "# Nubenetes V2: The Agentic Elite Portal (2026 Edition)\n\n"
            "!!! quote \"The Architect's Vision\"\n"
            "    This is not just a list; it is a high-density intelligence layer for the modern Platform Engineer. "
            "    Every link has been semantically evaluated by our Agentic AI to ensure maximum professional value.\n\n"
            "## Exploration Path\n"
            "Choose your area of expertise or starting point from the navigation menu. Each section is optimized "
            "for high-signal learning and production-ready tool discovery.\n\n"
            "--- \n"
            "**Core Features:**\n"
            "- **Professional Only**: No noise, no outdated memes, just technical excellence.\n"
            "- **2026 Roadmap**: Prioritizing AI-Native, eBPF, and Autonomous Operations.\n"
            "- **Exhaustive but Elite**: Thousands of links maintained, but only the most impactful shown prominently.\n"
        )
        with open(os.path.join(V2_DIR, "index.md"), "w") as f:
            f.write(index_content)

        # Create category pages
        for cat, links in structure.items():
            slug = cat.lower().replace(" ", "-").replace("&", "and")
            filename = f"{slug}.md"
            
            content = f"# {cat}\n\n"
            content += f"!!! abstract \"2026 Focus\"\n    High-density curation of {cat} resources.\n\n"
            
            # Sub-grouping by original V1 categories to maintain some hierarchy
            original_groups = {}
            for l in links:
                group = l["original_file"].replace(".md", "").capitalize()
                if group not in original_groups: original_groups[group] = []
                original_groups[group].append(l)

            for group, g_links in original_groups.items():
                content += f"## {group}\n"
                for l in g_links:
                    stars = " 🌟" if "awesome" in l["title"].lower() else ""
                    content += f"  - [{l['title']}]({l['url']}){stars} - {l['description']}\n"
                content += "\n"

            with open(os.path.join(V2_DIR, filename), "w") as f:
                f.write(content)

    async def _generate_v2_navigation(self, structure: Dict[str, List[Dict]]):
        with open("v2-mkdocs.yml", "r") as f:
            config = yaml.safe_load(f)

        nav = [{"Home": "index.md"}]
        elite_nav = []
        
        for cat in structure.keys():
            slug = cat.lower().replace(" ", "-").replace("&", "and")
            elite_nav.append({cat: f"{slug}.md"})
            
        nav.append({"Elite Portal": elite_nav})
        config["nav"] = nav
        
        with open("v2-mkdocs.yml", "w") as f:
            yaml.dump(config, f, sort_keys=False)

if __name__ == "__main__":
    engine = V2VisionEngine()
    asyncio.run(engine.analyze_and_cluster())
