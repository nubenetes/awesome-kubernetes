import os
import re
import json
import asyncio
import yaml
import httpx
from datetime import datetime
from typing import List, Dict, Set, Any, Tuple
from src.config import GEMINI_API_KEYS, GH_TOKEN, TARGET_REPO, MADRID_TZ, INVENTORY_PATH
from src.gemini_utils import call_gemini_with_retry, normalize_url, clean_toc_text
from src.logger import log_event

V1_DIR = "docs"
V2_DIR = "v2-docs"

class V2VisionEngine:
    def __init__(self):
        # Load Config & Policy
        self.special_assets_rules = self._load_special_assets()
        self.link_rules = self._load_link_rules()
        self.max_depth = self.link_rules.get("hierarchy_rules", {}).get("max_depth", 10)
        
        # 100% Comprehensive 2026 Taxonomy
        self.dimensions = {
            "AI and Artificial Intelligence": ["ai", "ai-agents-mcp", "chatgpt", "mlops"],
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
            "You are a Senior Technical Architect in 2026. Your mission is to organize a high-density technical reference portal "
            "structured like a professional technical book (O'Reilly style).\n"
            "PHASE 1: TECHNICAL PRESERVATION & CURATION\n"
            "- KEEP >90% of technical resources (except for 'introduction.md' where only high-impact links are kept).\n"
            "PHASE 2: SOPHISTICATED HIERARCHICAL CLASSIFICATION\n"
            "- Identify TECHNICAL_HIERARCHY: A list of strings (max 10) representing Area > Topic > Subtopics.\n"
            "- For 'introduction.md', set is_microservice: true if context matches.\n"
            "PHASE 3: KNOWLEDGE ASSIMILATION FLOW\n"
            "- Order hierarchy to facilitate a structured learning journey.\n"
            "PHASE 4: MANDATORY DESCRIPTIONS\n"
            "- If 'Current Desc' is empty, generate a professional summary. Style: O'Reilly technical.\n"
        )
        self.inventory = self._load_inventory()
        self.maturity_audit = []

    def _load_special_assets(self) -> Dict:
        path = "data/special_assets.yaml"
        if os.path.exists(path):
            try:
                with open(path, "r") as f: return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def _load_link_rules(self) -> Dict:
        path = "data/link_rules.yaml"
        if os.path.exists(path):
            try:
                with open(path, "r") as f: return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def _load_inventory(self) -> Dict:
        if os.path.exists(INVENTORY_PATH):
            try:
                with open(INVENTORY_PATH, "r") as f: return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def _save_inventory(self):
        os.makedirs(os.path.dirname(INVENTORY_PATH), exist_ok=True)
        with open(INVENTORY_PATH, "w") as f:
            yaml.dump(self.inventory, f, sort_keys=False, allow_unicode=True)

    async def analyze_and_cluster(self):
        log_event("STARTING V2 HIGH-DENSITY O'REILLY LIBRARY GENERATION", section_break=True)
        # 0. Mandate Sync
        try:
            from src.mandate_ingestor import MandateIngestor
            MandateIngestor().save_system_instructions()
        except: pass

        all_v1_links, mosaic_html, videos_html = await self._gather_all_v1_content()
        log_event(f"[*] Discovery: Found {len(all_v1_links)} resources in V1.")

        log_event("[*] Phase 1: Health Check...")
        health_inventory = await self._verify_link_health(all_v1_links)
        log_event(f"[*] Health Check Complete. {len(health_inventory)} online.")

        log_event("[*] Phase 2: Evaluation & Deep Indexing (Semantic Dedup)...")
        library_inventory = await self._evaluate_and_score_resources(health_inventory)
        log_event(f"[*] Inventory Refined: {len(library_inventory)} items kept after semantic consolidation.")

        log_event("[*] Phase 3: Recursive Hierarchy Construction...")
        v2_data = await self._rebuild_structure(library_inventory)
        
        log_event("[*] Phase 4: Generating Premium Portal Hubs (Comparison Tables)...")
        os.makedirs(V2_DIR, exist_ok=True)
        await self._write_premium_files(v2_data, mosaic_html, videos_html)
        await self._sync_enterprise_navigation(v2_data)
        self._save_inventory()
        log_event("V2 ELITE PORTAL GENERATED SUCCESSFULLY.")
        
        # --- FINAL SAFETY AUDIT ---
        try:
            from src.safety_guard import SafetyGuard
            guard = SafetyGuard()
            report = guard.generate_audit_report()
            with open("v2_safety_report.md", "w") as f: f.write(report)
        except Exception as e:
            log_event(f"  [!] V2 Safety Audit Error: {e}")

    async def _gather_all_v1_content(self):
        all_links, mosaic_html, videos_html = [], "", ""
        if os.path.exists("docs/index.md"):
            with open("docs/index.md", "r") as f:
                idx_content = f.read()
                mosaics = re.findall(r'<center markdown="1">\s*\n(.*?)\n\s*</center>', idx_content, re.DOTALL)
                if mosaics:
                    for m in mosaics:
                        if m.count("[![") > 5: mosaic_html = m; break
                videos_match = re.search(r'\?\?\? note "Top Videos & Clips.*?\n(.*?\n)\s*</center>', idx_content, re.DOTALL)
                if videos_match: videos_html = videos_match.group(1)

        for root, _, files in os.walk(V1_DIR):
            for file in files:
                if not file.endswith(".md") or file == "index.md": continue
                path = os.path.join(root, file)
                with open(path, "r") as f: content = f.read()
                matches = re.finditer(r'^\s*-\s*\[([^\]]+)\]\(([^\)]+)\)(.*?(?:\n\s{2,}.*)*)', content, re.MULTILINE)
                for m in matches:
                    title, url, full_desc = m.groups()
                    if not url.startswith(("http", "mailto", "#")):
                        url = f"https://nubenetes.com/{url.replace('.md', '/')}"
                    all_links.append({"title": title, "url": url, "description": full_desc.strip(), "original_file": file})
        return all_links, mosaic_html, videos_html

    async def _verify_link_health(self, links: List[Dict]):
        online_links = []
        async with httpx.AsyncClient(timeout=15.0, follow_redirects=True, verify=False) as client:
            for i in range(0, len(links), 50):
                batch = links[i:i+50]
                tasks = [self._check_single_link_resilient(client, l) for l in batch]
                results = await asyncio.gather(*tasks)
                online_links.extend([r for r in results if r is not None])
                await asyncio.sleep(0.1)
        return online_links

    async def _check_single_link_resilient(self, client, link: Dict):
        url = link["url"]
        norm_url = normalize_url(url)
        if norm_url in self.inventory and self.inventory[norm_url].get("status") == "online": return link
        try:
            resp = await client.get(url, timeout=10.0)
            if resp.status_code < 400:
                self.inventory.setdefault(norm_url, {})["status"] = "online"
                return link
        except: pass
        return None

    async def _evaluate_and_score_resources(self, links: List[Dict]):
        to_evaluate = []
        project_registry = {} # {project_id: best_item}
        force_eval = os.getenv("FORCE_EVAL", "false").lower() == "true"

        for l in links:
            item = l.copy()
            norm_url = normalize_url(l["url"])
            
            # Identify Project Signature (Semantic Dedup)
            project_id = norm_url
            if "github.com" in norm_url:
                match = re.search(r'github\.com/([^/]+/[^/]+)', norm_url)
                if match: project_id = match.group(1).lower()
            
            # --- MANDATE 27: SPECIAL ASSET PROTECTION ---
            is_special = orig_file in special_rules
            item["is_special"] = is_special

            # --- MANDATE 23: AUTHORITATIVE MERGE ---
            if not force_eval and norm_url in self.inventory and "stars" in self.inventory[norm_url]:
                cached = self.inventory[norm_url]
                item.update(cached)
                # Ensure is_special is preserved even if cache didn't have it
                if is_special: item["is_special"] = True
                
                if cached.get("hierarchy"):
                    if project_id not in project_registry:
                        project_registry[project_id] = item
                    else:
                        existing = project_registry[project_id]
                        # Inheritance: If any version was special, the consolidated one is special
                        if item.get("is_special"): existing["is_special"] = True
                        
                        is_current_root = "github.com" not in norm_url
                        if is_current_root or item.get("stars", 0) > existing.get("stars", 0):
                            item.setdefault("aliases", []).append(existing["url"])
                            # Preserve special status during overwrite
                            if existing.get("is_special"): item["is_special"] = True
                            project_registry[project_id] = item
                        else:
                            existing.setdefault("aliases", []).append(url)
                    continue
            to_evaluate.append(item)

        if to_evaluate:
            for i in range(0, len(to_evaluate), 50):
                batch = to_evaluate[i:i+50]
                prompt = (f"{self.library_criteria}\nRespond ONLY JSON: {{\"results\": [{{ \"idx\": int, \"year\": \"YYYY\", \"stars\": 0-5, \"hierarchy\": [\"Area\", \"Topic\", ...], \"summary\": \"...\", \"language\": \"...\", \"type\": \"...\", \"complexity\": \"...\", \"is_microservice\": bool }}, ...]}}\n\nLINKS:\n" + 
                          "\n".join([f"{idx}. {l['title']} ({l['url']})" for idx, l in enumerate(batch)]))
                try:
                    data = await call_gemini_with_retry(prompt, prefer_flash=True)
                    for res in data.get("results", []):
                        idx = int(res["idx"])
                        if idx < len(batch):
                            item = batch[idx].copy()
                            norm_url = normalize_url(item["url"])
                            p_id = norm_url
                            if "github.com" in norm_url:
                                m = re.search(r'github\.com/([^/]+/[^/]+)', norm_url)
                                if m: p_id = m.group(1).lower()

                            eval_data = {
                                "year": str(res.get("year", "N/A")), "stars": min(max(int(res.get("stars", 0)), 0), 5),
                                "ai_summary": res.get("summary", ""), "language": res.get("language", "English"),
                                "resource_type": res.get("type", "Reference"), "complexity": res.get("complexity", "Intermediate"),
                                "hierarchy": res.get("hierarchy", ["General"]), "is_microservice": bool(res.get("is_microservice", False)),
                                "status": "online", "tag": self._calculate_tag(item)
                            }
                            item.update(eval_data)
                            self.inventory[norm_url] = eval_data
                            self.inventory[norm_url]["title"] = item["title"]
                            if p_id not in project_registry or item["stars"] > project_registry[p_id].get("stars", 0):
                                project_registry[p_id] = item
                except: 
                    for l in batch:
                        # Fallback registry injection
                        u = normalize_url(l["url"])
                        if u not in project_registry: project_registry[u] = l
                await asyncio.sleep(0.3)
        return list(project_registry.values())

    def _calculate_tag(self, item: Dict) -> str:
        stars = item.get("gh_stars", 0)
        if stars > 15000: return "[DE FACTO STANDARD]"
        if stars > 3000: return "[ENTERPRISE-STABLE]"
        return "[COMMUNITY-TOOL]"

    async def _rebuild_structure(self, library_inventory: List[Dict]):
        special_rules = {sa["file"]: sa for sa in self.special_assets_rules.get("special_assets", [])}
        v2_structure = {dim: {"summary": "", "categories": {}} for dim in self.dimensions.keys()}
        file_to_dim = {f + ".md": dim for dim, files in self.dimensions.items() for f in files}

        for item in library_inventory:
            orig_file = item.get("original_file", "unknown.md")
            dim = file_to_dim.get(orig_file, "Architectural Foundations")
            cat_name = orig_file.replace(".md", "").replace("-", " ").title()
            if item.get("is_microservice"): cat_name = "Microservices"; dim = "Architectural Foundations" if orig_file == "introduction.md" else dim

            # --- MANDATE 27: SPECIAL ASSET PROTECTION ---
            is_special = item.get("is_special", False) or orig_file in special_rules

            if orig_file == "introduction.md" and item.get("stars", 0) < 4 and not item.get("is_microservice"): continue
            if not is_special and item.get("stars", 0) < 3 and not item.get("is_microservice"): continue

            if cat_name not in v2_structure[dim]["categories"]: v2_structure[dim]["categories"][cat_name] = {"__links__": []}
            hierarchy = item.get("hierarchy", [])
            if hierarchy and (hierarchy[0] == dim or hierarchy[0] == cat_name): hierarchy = hierarchy[1:]
            current = v2_structure[dim]["categories"][cat_name]
            for h_name in hierarchy[:self.max_depth]:
                if h_name not in current: current[h_name] = {"__links__": []}
                current = current[h_name]
            current["__links__"].append(item)

        def sort_rec(node):
            if "__links__" in node: node["__links__"].sort(key=lambda x: (-x.get("stars", 1), -(int(x["year"]) if str(x.get("year", "")).isdigit() else 0)))
            for k, v in node.items():
                if k != "__links__": sort_rec(v)
        for dim in v2_structure:
            for cat in list(v2_structure[dim]["categories"].keys()): sort_rec(v2_structure[dim]["categories"][cat])
            cache_key = f"INTRO:{dim}"
            v2_structure[dim]["summary"] = self.inventory.get(cache_key, {}).get("ai_summary", f"Strategic reference for {dim}.")
        return v2_structure

    async def _generate_comparison_table(self, links: List[Dict]) -> str:
        standard_tools = [l for l in links if l.get("stars", 0) >= 4]
        if len(standard_tools) < 6: return ""
        table = "\n??? abstract \"Architect's Technical Comparison Table\"\n"
        table += "    | Solution | Maturity | Primary Focus | Language | Stars |\n"
        table += "    | :--- | :--- | :--- | :--- | :--- |\n"
        for l in standard_tools[:12]:
            stars = "🌟" * l.get("stars", 0)
            focus = l.get("topic", l.get("hierarchy", ["General"])[-1])
            table += f"    | [{l['title'].replace('==','')}]({l['url']}) | {l.get('tag','').replace('[','').replace(']','')} | {focus} | {l.get('language','English')} | {stars} |\n"
        return table + "\n"

    async def _write_premium_files(self, data: Dict[str, Dict], mosaic_html: str, videos_html: str):
        mosaic_html = mosaic_html.replace('src="images/', 'src="images/').replace('](images/', '](images/')
        trending_pool = sorted([dict(meta, url=url) for url, meta in self.inventory.items() if meta.get("stars", 0) >= 3], key=lambda x: (x.get("pub_date", "0000"), -x.get("stars", 0)), reverse=True)
        pulse_md = "## ⚡ The Agentic Pulse\n" + "\n".join([f"- **({l.get('pub_date', 'N/A')[:10]})** [**=={l['title']}==**]({l['url']}) {'🌟'*l.get('stars',3)}" for l in trending_pool[:5]])
        
        index_md = f"# Nubenetes V2 | The High-Density Library (2026)\n\n![Banner](images/kubernetes_logo.jpg)\n\n!!! quote \"The Library of 2026\"\n    Structured like an advanced technical book.\n\n<center markdown=\"1\">\n{mosaic_html}\n</center>\n\n{pulse_md}\n\n## Strategic Dimensions\n"
        for dim, content in data.items():
            if not content["categories"]: continue
            slug = dim.lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "")
            index_md += f"- **[{dim}](./{slug}.md)**: {content['summary']}\n"
        with open(os.path.join(V2_DIR, "index.md"), "w") as f: f.write(index_md)
# Helper functions for recursive rendering
def gen_toc(node, depth, base_slug):
    toc = ""
    for name, subnode in sorted(node.items()):
        if name == "__links__": continue
        clean_name = clean_toc_text(name)
        slug = f"{base_slug}-{clean_name.lower().replace(' ', '-')}"
        toc += f"{' ' * (depth * 4)}- [{clean_name}](#{slug})\n" + gen_toc(subnode, depth + 1, slug)
    return toc

async def render_node(node, depth, base_slug, is_intro=False):
    md = ""
    for name, subnode in sorted(node.items()):
        if name == "__links__": continue
        clean_name = clean_toc_text(name)
        slug = f"{base_slug}-{clean_name.lower().replace(' ', '-')}"
        md += f"{'#' * min(6, depth + 2)} {clean_name}\n\n"
        if depth == 1 and "__links__" in subnode: md += await self._generate_comparison_table(subnode["__links__"])
        md += await render_node(subnode, depth + 1, slug, is_intro)
    if "__links__" in node:
                for l in node["__links__"]:
                    is_gold = is_intro and l.get("stars", 0) >= 4
                    title = l['title'].replace("==", "")
                    if is_gold:
                        img = f"    ![Preview]({l.get('social_preview_url')})\n" if l.get('social_preview_url') else ""
                        md += f"!!! note \"{title}\"\n{img}    **[Access Resource]({l['url']})** {'🌟'*l.get('stars',4)} | Level: {l.get('complexity', 'Beginner')}\n    \n    {l.get('ai_summary', l.get('description', ''))}\n\n"
                    else:
                        year_prefix = f"**({l.get('year', 'N/A')})** "
                        gh_info = f" <span class='md-tag md-tag--info'>⭐ {l.get('gh_stars',0)}</span>" if l.get('gh_stars') else ""
                        icon = " 🎥" if l.get("is_video") else ""
                        
                        lang = l.get("language", "English")
                        lang_tag = f" <span class='md-tag md-tag--warning'>[{lang.upper()} CONTENT]</span>" if lang.lower() != "english" else ""
                        
                        comp = l.get("complexity", "Intermediate")
                        comp_tag = f" <span class='md-tag md-tag--critical'>[{comp.upper()} LEVEL]</span>" if comp.lower() in ["architect", "advanced"] else ""
                        
                        res_type = l.get("resource_type", "Reference")
                        type_tag = f" <span class='md-tag md-tag--primary'>[{res_type.upper()}]</span>" if res_type.lower() in ["case study", "guide", "documentation"] else ""
                        
                        rich = "".join([
                            f" <small>by **{l['author']}**</small>" if l.get("author") else "",
                            f" <span class='md-tag md-tag--info'>⏱️ {l['duration']}</span>" if l.get("duration") else "",
                            f" <span class='md-tag md-tag--info'>📖 {l['reading_time']}</span>" if l.get("reading_time") else ""
                        ])
                        
                        tag = l.get("tag", "[COMMUNITY-TOOL]")
                        color = "success" if "STANDARD" in tag else "warning" if "EMERGING" in tag else "info"
                        
                        md += f"  - {year_prefix}[{title}]({l['url']}){icon}{gh_info}{lang_tag}{comp_tag}{type_tag}{rich} {'🌟'*l.get('stars',0)} <span class='md-tag md-tag--{color}'>{tag}</span>\n"
                        if l.get('ai_summary'): md += f"\n      {l['ai_summary']}\n\n"
            return md

        for dim, content in data.items():
            if not content["categories"]: continue
            slug = dim.lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "")
            v2_page = f"{slug}.md"
            
            # --- TRACK V2 LOCATIONS IN INVENTORY ---
            def track_v2(node, page_path):
                if "__links__" in node:
                    for l in node["__links__"]:
                        nu = normalize_url(l["url"])
                        if nu in self.inventory:
                            locs = self.inventory[nu].get("v2_locations", [])
                            if page_path not in locs:
                                self.inventory[nu].setdefault("v2_locations", []).append(page_path)
                for k, v in node.items():
                    if k != "__links__": track_v2(v, page_path)
            
            for cat_topics in content["categories"].values(): track_v2(cat_topics, v2_page)

            md = f"# {dim}\n\n!!! info \"Architectural Context\"\n    {content['summary']}\n\n## Table of Contents\n"
            for cat, topics in content["categories"].items():
                cat_slug = cat.lower().replace(" ", "-")
                md += f"- [{cat}](#{cat_slug})\n" + gen_toc(topics, 1, cat_slug)
            md += "\n---\n\n"
            for cat, topics in content["categories"].items():
                cat_slug = cat.lower().replace(" ", "-")
                md += f"## {cat}\n\n"
                if cat == "Introduction":
                    md += "!!! quote \"Vision 2026\"\n    The focus shifts to agentic autonomy and hardened security.\n\n### Ecosystem Map\n```mermaid\ngraph TD\n    A[Foundations] --> B[AI & Intelligence]\n    A --> C[Hardened Infra]\n    B --> D[Agentic Curation]\n    C --> E[Enterprise Stability]\n    D --> F[Nubenetes Portal]\n    E --> F\n```\n\n### Gateway Hub\n- 🚀 [Explore AI Dimensions](./ai-and-artificial-intelligence.md)\n- 📦 [Microservices Guide](./microservices.md)\n\n"
                md += await render_node(topics, 0, cat_slug, is_intro=(cat=="Introduction"))
            with open(os.path.join(V2_DIR, f"{slug}.md"), "w") as f: f.write(md)

    async def _sync_enterprise_navigation(self, data: Dict[str, Dict]):
        try:
            with open("v2-mkdocs.yml", "r") as f: content = f.read()
            nav = ["nav:", "  - \"The 2026 Vision\": index.md"]
            for dim in sorted(data.keys()):
                if data[dim]["categories"]:
                    slug = dim.lower().replace(" ", "-").replace("&", "and").replace("(", "").replace(")", "")
                    nav.append(f"  - \"{dim}\": {slug}.md")
            updated = re.sub(r'nav:.*', "\n".join(nav), content, flags=re.DOTALL)
            with open("v2-mkdocs.yml", "w") as f: f.write(updated)
        except: pass

if __name__ == "__main__":
    engine = V2VisionEngine()
    asyncio.run(engine.analyze_and_cluster())
