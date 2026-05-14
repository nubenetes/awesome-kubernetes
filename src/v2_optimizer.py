import os
import re
import json
import asyncio
import yaml
from datetime import datetime
from typing import List, Dict, Set
from src.config import GEMINI_API_KEYS, GH_TOKEN, TARGET_REPO, MADRID_TZ
from src.gemini_utils import call_gemini_with_retry
from src.logger import log_event

V1_DIR = "docs"
V2_DIR = "v2-docs"

class V2Optimizer:
    def __init__(self):
        self.elite_criteria = (
            "You are a Principal Platform Architect in May 2026.\n"
            "Your task is to select the ABSOLUTE BEST resources from a larger list.\n"
            "CRITERIA for V2 (Elite Edition):\n"
            "1. HIGH IMPACT: Only links with score > 90 or exceptional industry value.\n"
            "2. MODERNITY: Prefer 2024-2026 content. Avoid outdated patterns unless fundational.\n"
            "3. AWESOME LISTS: ALWAYS KEEP all links pointing to 'Awesome' repositories (GitHub/GitLab).\n"
            "4. NO REDUNDANCY: If multiple tools do the same, pick the 1-2 most innovative or widely adopted.\n"
            "5. AGENTIC FOCUS: Prioritize tools with AI/Agentic capabilities or eBPF/WASM innovation.\n"
        )

    async def optimize_file(self, filename: str):
        v1_path = os.path.join(V1_DIR, filename)
        v2_path = os.path.join(V2_DIR, filename)
        
        if not os.path.exists(v1_path): return

        with open(v1_path, "r") as f:
            content = f.read()

        # Extract all links and their descriptions
        links = re.findall(r'^\s*-\s*\[([^\]]+)\]\(([^\)]+)\)(.*)', content, re.MULTILINE)
        if not links:
            # If no links, just copy the structure/headers
            headers = [l for l in content.splitlines() if l.startswith("#")]
            with open(v2_path, "w") as f:
                f.write("\n".join(headers) + "\n\n*Content coming soon as part of the 2026 Agentic Elite curation.*")
            return

        formatted_links = []
        for title, url, desc in links:
            formatted_links.append(f"- [{title}]({url}) {desc.strip()}")

        log_event(f"[*] V2 Optimizer: Analyzing {len(formatted_links)} links in {filename}")

        prompt = (
            f"{self.elite_criteria}\n"
            f"FILE: {filename}\n"
            f"LINKS TO EVALUATE:\n" + "\n".join(formatted_links[:100]) + "\n\n"
            "Respond ONLY with a JSON list of indices to KEEP. "
            "Example: [0, 5, 22]. Remember to ALWAYS keep 'Awesome' repos."
        )

        try:
            indices = await call_gemini_with_retry(prompt)
            if not isinstance(indices, list): indices = []
            
            selected_links = [formatted_links[i] for i in indices if i < len(formatted_links)]
            
            # Reconstruct V2 file
            v2_content = f"# {filename.replace('.md', '').capitalize()} (Elite Selection)\n\n"
            v2_content += "!!! abstract \"2026 Agentic Vision\"\n"
            v2_content += "    This page contains a curated selection of top-tier resources, strictly filtered by our Agentic AI for high impact and modern relevance.\n\n"
            
            if selected_links:
                v2_content += "## Selected Resources\n"
                v2_content += "\n".join(selected_links)
            else:
                v2_content += "\n*No resources met the elite criteria for this specific category yet.*"

            with open(v2_path, "w") as f:
                f.write(v2_content)
                
            log_event(f"  [OK] V2 file generated: {v2_path} ({len(selected_links)} links kept)")

        except Exception as e:
            log_event(f"  [!] Error optimizing {filename} for V2: {e}")

    async def run_full_optimization(self):
        log_event("STARTING V2 AGENTIC OPTIMIZATION (THE ARCHITECT'S CUT)", section_break=True)
        
        if not os.path.exists(V1_DIR):
            log_event(f"[!] CRITICAL: Source directory {V1_DIR} not found.")
            return

        files = [f for f in os.listdir(V1_DIR) if f.endswith(".md") and f != "index.md"]
        log_event(f"[*] Found {len(files)} files to process in {V1_DIR}")
        
        if not files:
            log_event("[!] No markdown files found to optimize.")
            return

        # Ensure output directory exists
        os.makedirs(V2_DIR, exist_ok=True)
        log_event(f"[*] Output directory verified: {V2_DIR}")

        # Batch processing to avoid rate limits
        total_files = len(files)
        for i in range(0, total_files, 5):
            batch = files[i:i+5]
            log_event(f">>> Processing batch {i//5 + 1} ({len(batch)} files)...")
            await asyncio.gather(*[self.optimize_file(f) for f in batch])
            await asyncio.sleep(2)

        # Generate Landing Page
        log_event("[*] Generating V2 landing page...")
        await self._generate_v2_index()
        
        # Sync Navigation
        log_event("[*] Syncing V2 navigation from original mkdocs.yml...")
        await self._sync_navigation()

        log_event("V2 OPTIMIZATION FINISHED SUCCESSFULLY.", section_break=True)

    async def _sync_navigation(self):
        """
        Reads mkdocs.yml and generates a filtered nav for v2-mkdocs.yml
        """
        try:
            with open("mkdocs.yml", "r") as f:
                v1_config = yaml.safe_load(f)
            
            with open("v2-mkdocs.yml", "r") as f:
                v2_config = yaml.safe_load(f)

            v1_nav = v1_config.get("nav", [])
            
            def filter_nav(nav_item):
                if isinstance(nav_item, str):
                    return nav_item if os.path.exists(os.path.join(V2_DIR, nav_item)) else None
                if isinstance(nav_item, dict):
                    new_item = {}
                    for key, value in nav_item.items():
                        if isinstance(value, list):
                            filtered_list = [filter_nav(i) for i in value]
                            filtered_list = [i for i in filtered_list if i is not None]
                            if filtered_list: new_item[key] = filtered_list
                        else:
                            if os.path.exists(os.path.join(V2_DIR, value)):
                                new_item[key] = value
                    return new_item if new_item else None
                return None

            v2_nav = [filter_nav(item) for item in v1_nav]
            v2_nav = [item for item in v2_nav if item is not None]
            
            v2_config["nav"] = v2_nav
            
            with open("v2-mkdocs.yml", "w") as f:
                yaml.dump(v2_config, f, sort_keys=False)
            
            log_event("  [OK] v2-mkdocs.yml navigation updated.")
        except Exception as e:
            log_event(f"  [!] Error syncing navigation: {e}")

    async def _generate_v2_index(self):
        v2_index = (
            "# Welcome to Nubenetes V2\n\n"
            "## The Agentic Elite Edition (2026)\n\n"
            "This is a high-density, AI-curated view of the Cloud Native ecosystem. While our [Classic Archive](https://nubenetes.com) "
            "serves as a comprehensive encyclopedia of thousands of tools, **Nubenetes V2** is built for the time-constrained architect.\n\n"
            "### Core Principles of V2:\n"
            "- **Impact First**: Only resources with exceptional value are shown.\n"
            "- **2026 Ready**: Focus on eBPF, WASM, AI-Native Infrastructure, and Agentic Workflows.\n"
            "- **Always Awesome**: We maintain 100% of the community's fundational 'Awesome' lists.\n\n"
            "--- \n"
            "Generated by Nubenetes AI Agent using Gemini 2.0/2.5 Flash."
        )
        with open(os.path.join(V2_DIR, "index.md"), "w") as f:
            f.write(v2_index)

if __name__ == "__main__":
    optimizer = V2Optimizer()
    asyncio.run(optimizer.run_full_optimization())
