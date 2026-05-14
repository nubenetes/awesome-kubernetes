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
        self.elite_criteria = (
            "You are a Senior Principal Architect in May 2026.\n"
            "Your task is to curate an EXCELLENCE-DRIVEN portal for platform professionals.\n"
            "CRITERIA for V2 Selection:\n"
            "1. TECHNICAL DEPTH: Prioritize deep-dives, architectural masterclasses, and authoritative sources over shallow or introductory content.\n"
            "2. PRODUCTION VALUE: Keep tools and resources that are production-ready or represent the cutting edge of industry standards (2024-2026).\n"
            "3. AWESOME LISTS: ALWAYS KEEP all links pointing to 'Awesome' repositories, as they are foundational knowledge nodes.\n"
            "4. NO FLUFF: Remove personal anecdotes, outdated jokes, or introductory tutorials that don't add advanced value.\n"
            "5. MODERN ECOSYSTEM: Favor resources focusing on eBPF, WASM, Platform Engineering, Agentic AI, and Zero Trust security.\n"
        )

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
        
        async def process_link_batch(batch, batch_num):
            prompt = (
                f"{self.elite_criteria}\n"
                "Your mission is to evaluate the technical quality of these resources.\n"
                "Do not limit the quantity, but hold a VERY HIGH bar for quality.\n"
                "RULES:\n"
                "1. If a resource is technically exceptional and authoritative, KEEP IT.\n"
                "2. If it is a generic tutorial or an outdated news piece, DISCARD IT.\n"
                "3. Ensure the selection remains dense but purely high-quality.\n\n"
                "LINKS TO EVALUATE:\n" + "\n".join([f"{i}. [{l['title']}]({l['url']}) - {l['description']}" for i, l in enumerate(batch)]) + "\n\n"
                "Respond ONLY with a JSON object: {\"keep_indices\": [int, int, ...]}"
            )
            try:
                response = await call_gemini_with_retry(prompt)
                indices = []
                if isinstance(response, dict):
                    indices = response.get("keep_indices", [])
                elif isinstance(response, list):
                    indices = response
                
                kept = [batch[int(i)] for i in indices if int(i) < len(batch)]
                log_event(f"    [Batch {batch_num}] Quality Filter: Kept {len(kept)}/{len(batch)} high-quality links.")
                return kept
            except Exception as e:
                log_event(f"    [Batch {batch_num}] Evaluation failed: {e}. Falling back to original curation for safety.")
                return [l for l in batch if "awesome" in l['title'].lower() or "awesome" in l['url'].lower()]

        # Reduced batch size for higher AI attention
        BATCH_SIZE = 50
        for i in range(0, len(links), BATCH_SIZE):
            batch = links[i:i+BATCH_SIZE]
            batch_num = i//BATCH_SIZE + 1
            log_event(f"  [>] Evaluating batch {batch_num}...")
            result = await process_link_batch(batch, batch_num)
            elite.extend(result)
            # Short sleep to respect rate limits even in pay-per-use
            await asyncio.sleep(0.5)
            
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
        """
        Updates the v2-mkdocs.yml with the new structure.
        Uses a simpler approach to avoid breaking custom YAML tags.
        """
        try:
            with open("v2-mkdocs.yml", "r") as f:
                content = f.read()

            nav_lines = ["nav:", "  - Welcome: index.md"]
            elite_nav = ["  - Elite Portal:"]
            
            for cat in structure.keys():
                slug = cat.lower().replace(" ", "-").replace("&", "and")
                elite_nav.append(f"      - \"{cat}\": {slug}.md")
            
            nav_section = "\n".join(nav_lines + elite_nav)
            
            # Replace the old nav section using regex
            new_content = re.sub(r'nav:.*', nav_section, content, flags=re.DOTALL)
            
            with open("v2-mkdocs.yml", "w") as f:
                f.write(new_content)
            
            log_event("  [OK] v2-mkdocs.yml navigation updated using regex.")
        except Exception as e:
            log_event(f"  [!] Error updating navigation: {e}")

if __name__ == "__main__":
    engine = V2VisionEngine()
    asyncio.run(engine.analyze_and_cluster())
