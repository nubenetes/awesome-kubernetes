import os
import re
import json
import math
import hashlib
import asyncio
import yaml
try:
    from yaml import CSafeLoader as Loader
except ImportError:
    from yaml import SafeLoader as Loader
import httpx
from datetime import datetime
from typing import List, Dict, Set, Any, Tuple
from src.config import GEMINI_API_KEYS, GH_TOKEN, TARGET_REPO, MADRID_TZ, INVENTORY_PATH
from src.gemini_utils import call_gemini_with_retry, normalize_url, clean_toc_text, get_github_activity, fetch_youtube_metadata
from src.logger import log_event
from src.inventory_manager import update_inventory_entry
from src.awesome_page import build_awesome_lists_header


def nuclear_strip(text: str) -> str:
    """Mandate 30: MD039 - Removes all leading/trailing whitespace including hidden unicode characters."""
    if not text: return ""
    # Purge all known whitespace characters (standard, non-breaking, thin, etc.)
    text = re.sub(r'^[\s\u00a0\u200b\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+', '', text)
    text = re.sub(r'[\s\u00a0\u200b\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+$', '', text)
    return text.replace("==", "")


def clean_hierarchy_section_name(name: str) -> str:
    """Normalizes hierarchy names to standard canonical versions to avoid redundant sections."""
    if not name: return ""
    name_stripped = name.strip()
    
    # 1. Normalize CI/CD patterns (CI-CD, CICD, CI/CD, and combinations with DevOps)
    ci_cd_pattern = re.compile(r'\b(ci[-/]cd|cicd)\b', re.IGNORECASE)
    if ci_cd_pattern.search(name_stripped):
        if re.search(r'\bdevops\b', name_stripped, re.IGNORECASE):
            return "CI/CD and DevOps"
        return "CI/CD"
        
    # 2. Case-insensitive exact mappings for common synonyms/variants
    name_lower = name_stripped.lower()
    mappings = {
        "k8s": "Kubernetes",
        "kubernetes": "Kubernetes",
        "aws": "AWS",
        "gcp": "GCP",
        "api": "API",
        "apis": "APIs",
        "cli": "CLI",
        "sre": "SRE",
        "iac": "IaC",
        "vm": "VMs",
        "vms": "VMs",
        "database": "Databases",
        "databases": "Databases",
        "microservice": "Microservices",
        "microservices": "Microservices",
        "container": "Containers",
        "containers": "Containers",
        "plugin": "Plugins",
        "plugins": "Plugins",
        "tutorial": "Tutorials",
        "tutorials": "Tutorials",
        "guide": "Guides",
        "guides": "Guides",
        "tool": "Tools",
        "tools": "Tools"
    }
    if name_lower in mappings:
        return mappings[name_lower]
        
    # 3. Capitalize standard acronyms in arbitrary strings
    words = name_stripped.split()
    for i, w in enumerate(words):
        w_clean = re.sub(r'[^\w]', '', w).lower()
        acronyms_map = {
            "aws": "AWS", "gcp": "GCP", "api": "API", "sre": "SRE", "iac": "IaC",
            "cli": "CLI", "vm": "VM", "vms": "VMs", "k8s": "Kubernetes", "cicd": "CI/CD",
            "sql": "SQL", "nosql": "NoSQL", "xml": "XML", "yaml": "YAML", "json": "JSON",
            "devops": "DevOps"
        }
        if w_clean in acronyms_map:
            words[i] = w.lower().replace(w_clean, acronyms_map[w_clean])
        else:
            if not words[i].isupper():
                words[i] = words[i].capitalize()
                
    return " ".join(words)

V1_DIR = "docs"
V2_DIR = "v2-docs"

class V2VisionEngine:
    def __init__(self, render_only: bool = False):
        self.render_only = render_only
        # Load Config & Policy
        self.special_assets_rules = self._load_special_assets()
        self.link_rules = self._load_link_rules()
        self.max_depth = self.link_rules.get("hierarchy_rules", {}).get("max_depth", 10)
        
        # 100% Comprehensive 2026 Taxonomy
        self.dimensions = {
            "AI": ["ai", "ai-agents-mcp", "chatgpt", "mlops"],
            "Architectural Foundations": ["introduction", "faq", "kubernetes", "linux", "git", "cloud-arch-diagrams", "matrix-table", "other-awesome-lists", "about"],
            "Platform & Site Reliability": ["sre", "devops", "developerportals", "scaffolding", "finops", "chaos-engineering", "performance-testing-with-jenkins-and-jmeter", "project-management-methodology", "project-management-tools", "qa", "test-automation-frameworks", "testops"],
            "Hardened Infrastructure": ["iac", "terraform", "pulumi", "crossplane", "ansible", "securityascode", "kubernetes-security", "aws-security", "devsecops", "kustomize", "liquibase"],
            "Cloud Providers (Hyperscalers)": ["aws", "azure", "GoogleCloudPlatform", "ibm_cloud", "oraclecloud", "digitalocean", "cloudflare", "managed-kubernetes-in-public-cloud", "public-cloud-solutions", "edge-computing", "aws-security", "aws-networking", "aws-storage", "aws-iac", "aws-serverless", "aws-backup", "aws-newfeatures"],
            "Networking & Service Mesh": ["networking", "kubernetes-networking", "servicemesh", "istio", "caching", "web-servers", "cloudflare"],
            "The Container Stack": ["docker", "container-managers", "serverless", "kubernetes-autoscaling", "kubernetes-operators-controllers", "kubernetes-storage", "kubernetes-monitoring", "kubernetes-troubleshooting", "kubernetes-backup-migrations", "kubernetes-on-premise", "kubernetes-bigdata", "kubernetes-client-libraries", "kubernetes-releases", "kubernetes-based-devel", "kubernetes-alternatives", "kubectl-commands", "rancher", "openshift", "ocp3", "ocp4", "noops"],
            "Data & Advanced Analytics": ["databases", "nosql", "message-queue", "crunchydata", "yaml", "bigdata"],
            "Engineering Pipeline": ["cicd", "gitops", "argo", "flux", "tekton", "jenkins", "jenkins-alternatives", "openshift-pipelines", "sonarqube", "registries", "keptn", "cicd-kubernetes-plugins"],
            "Developer Ecosystem": ["visual-studio", "javascript", "golang", "python", "java_frameworks", "java_app_servers", "java-and-java-performance-optimization", "dotnet", "angular", "web3", "api", "swagger-code-generator-for-rest-apis", "postman", "lowcode-nocode", "devel-sites", "linux-dev-env", "ChromeDevTools", "maven-gradle", "embedded-servlet-containers"],
            "Career & Industry": ["recruitment", "hr", "finops", "freelancing", "remote-tech-jobs", "workfromhome", "interview-questions", "elearning", "appointment-scheduling", "newsfeeds"]
        }

        # Stub page merge map: content from source pages renders on target pages
        self.merge_map = {
            "jvm-parameters-matrix-table": "java-and-java-performance-optimization",
            "private-cloud-solutions": "kubernetes-on-premise",
            "stackstorm": "cicd",
            "chef": "ansible",
            "newsql": "databases",
            "scaleway": "digitalocean",
            "xamarin": "dotnet",
            "dom": "javascript",
            "react": "javascript",
            "oauth": "securityascode",
            "digital-money": "finops",
            "aws-spain": "aws",
            # AWS de-fragmentation: the near-empty / junk-drawer AWS sub-pages
            # (<=7 links, plus "miscellaneous") merge into the main aws page so
            # it stops being a 3-link stub. The substantial AWS topics
            # (serverless, storage, networking, security, iac, backup,
            # newfeatures) stay as their own pages and are surfaced via the
            # provider hub block (self.subpage_hubs) on aws.md.
            "aws-miscellaneous": "aws",
            "aws-databases": "aws",
            "aws-devops": "aws",
            "aws-containers": "aws",
            "aws-monitoring": "aws",
            "aws-architecture": "aws",
            "aws-tools-scripts": "aws",
            "aws-messaging": "aws",
            "aws-data": "aws",
            "aws-training": "aws",
            "aws-pricing": "aws",
        }

        # Provider hub: pages that should render a "deep-dive topic pages" index
        # linking to the substantial sub-pages that remain after consolidation.
        # (slug, display label) — labels kept short and human-readable.
        self.subpage_hubs = {
            "aws": [
                ("aws-serverless", "Serverless"),
                ("aws-storage", "Storage"),
                ("aws-networking", "Networking"),
                ("aws-security", "Security"),
                ("aws-iac", "IaC"),
                ("aws-backup", "Backup"),
                ("aws-newfeatures", "New Features"),
            ],
            # Kubernetes is well-classified (rich parent + substantial distinct
            # children), so nothing is merged here — the hub is purely an index
            # so the flagship landing surfaces its deep-dive topic pages.
            "kubernetes": [
                ("kubernetes-tools", "Tools"),
                ("kubernetes-networking", "Networking"),
                ("kubernetes-security", "Security"),
                ("kubernetes-monitoring", "Monitoring"),
                ("kubernetes-storage", "Storage"),
                ("kubernetes-autoscaling", "Autoscaling"),
                ("kubernetes-operators-controllers", "Operators"),
                ("kubernetes-alternatives", "Alternatives"),
                ("kubernetes-bigdata", "Big Data"),
                ("kubernetes-tutorials", "Tutorials"),
                ("kubernetes-backup-migrations", "Backup & Migrations"),
                ("kubernetes-client-libraries", "Client Libraries"),
                ("kubernetes-based-devel", "Local Dev"),
                ("kubernetes-on-premise", "On-Premise"),
            ],
        }
        
        self.library_criteria = (
            "You are a Senior Technical Architect in 2026. Your mission is to organize a high-density technical reference portal "
            "structured like a professional technical book (O'Reilly style).\n"
            "PHASE 1: TECHNICAL PRESERVATION & CURATION\n"
            "- KEEP >90% of technical resources (except for 'introduction.md' where only high-impact links are kept).\n"
            "PHASE 2: SOPHISTICATED HIERARCHICAL CLASSIFICATION\n"
            "- Identify TECHNICAL_HIERARCHY: A list of strings (max 10) representing Area > Topic > Subtopics.\n"
            "- For 'introduction.md', identify links related to MICROSERVICES for extraction.\n"
            "PHASE 3: KNOWLEDGE ASSIMILATION FLOW\n"
            "- Order hierarchy to facilitate a structured learning journey.\n"
            "PHASE 4: HIGH-DENSITY TECHNICAL SUMMARIES (Double-Evidence Synthesis)\n"
            "- Generate professional, neutral, and advanced technical summaries. Style: O'Reilly technical.\n"
            "- PROTOCOL: Contrast 'Curator Insight' (from source) with 'Live Grounding' (from search).\n"
            "- If discrepancies are found (e.g. project is archived but source says it's new), PRIORITIZE live engineering truth.\n"
            "- Summaries MUST be high-density: Include architectural value, key features, and technical significance.\n"
            "- Format: Use paragraphs and bullet points for complex tools. Aim for 2-5 sentences of depth.\n"
            "PHASE 5: ADVANCED MATURITY TAGGING\n"
            "- Assign tags. You MUST include:\n"
            "  1. 1 to 2 maturity tags from: [DE FACTO STANDARD], [ENTERPRISE-STABLE], [EMERGING], [GUIDE], [CASE STUDY], [COMMUNITY-TOOL], [LEGACY].\n"
            "  2. Fine-grained technical/architectural tags from the content (e.g., [EBPF], [WASM], [GITOPS], [IAC], [SERVICE-MESH], [SERVERLESS], [MLOPS], [DB]). Keep them uppercase and wrapped in brackets.\n"
        )
        self.inventory = self._load_inventory()
        self.maturity_audit = []

    def _load_special_assets(self) -> Dict:
        path = "data/special_assets.yaml"
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return yaml.load(f, Loader=Loader) or {}
            except Exception as e:
                log_event(f"[WARN] load special_assets.yaml: {str(e)[:100]}")
                return {}
        return {}

    def _load_link_rules(self) -> Dict:
        path = "data/link_rules.yaml"
        if os.path.exists(path):
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return yaml.load(f, Loader=Loader) or {}
            except Exception as e:
                log_event(f"[WARN] load link_rules.yaml: {str(e)[:100]}")
                return {}
        return {}

    def _load_inventory(self) -> Dict:
        from src.inventory_manager import load_inventory
        return load_inventory()

    def _save_inventory(self):
        from src.inventory_manager import save_inventory
        save_inventory(self.inventory)

    async def analyze_and_cluster(self):
        log_event("STARTING V2 HIGH-DENSITY O'REILLY LIBRARY GENERATION", section_break=True)
        
        # Mandate 30: MD039 - Global Data Sanitization (Purge all whitespace/hidden chars from titles)
        for url in list(self.inventory.keys()):
            if isinstance(self.inventory[url], dict) and self.inventory[url].get("title") is not None:
                t = self.inventory[url]["title"]
                if isinstance(t, str):
                    # Purge all known whitespace characters (standard, non-breaking, thin, etc.)
                    t = re.sub(r'^[\s\u00a0\u200b\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+', '', t)
                    t = re.sub(r'[\s\u00a0\u200b\u1680\u180e\u2000-\u200a\u2028\u2029\u202f\u205f\u3000]+$', '', t)
                    self.inventory[url]["title"] = t
        
        # 0. Mandate Sync
        try:
            from src.mandate_ingestor import MandateIngestor
            MandateIngestor().save_system_instructions()
        except Exception as e:
            log_event(f"[WARN] mandate sync: {str(e)[:100]}")

        all_v1_links, mosaic_html, videos_html = await self._gather_all_v1_content()
        
        log_event(f"[*] Discovery: Found {len(all_v1_links)} resources to process.")

        log_event("[*] Phase 1: Health Check...")
        if self.render_only:
            # Mandate 19/22: In render-only mode (Fast-Track), we are conservative to avoid pruning valid sections.
            # We keep links that are explicitly 'online', 'review_required' OR have no status yet.
            health_inventory = []
            for l in all_v1_links:
                entry = self.inventory.get(normalize_url(l["url"]), {})
                status = entry.get("status", "online") # Assume online if unknown for rendering
                if status in ["online", "review_required"]:
                    health_inventory.append(l)
        else:
            health_inventory = await self._verify_link_health(all_v1_links)
        
        log_event("[*] Phase 2: Evaluation & Deep Indexing (Semantic Dedup)...")
        library_inventory = await self._evaluate_and_score_resources(health_inventory)

        log_event("[*] Phase 3: Recursive Hierarchy Construction...")
        v2_data = await self._rebuild_structure(library_inventory)
        
        log_event("[*] Phase 4: Generating Premium Portal Hubs...")
        os.makedirs(V2_DIR, exist_ok=True)
        
        # --- SURGICAL GARBAGE COLLECTION ---
        # Track every file we generate
        generated_files = {"index.md", "audit-log.md", "videos.md", "tags.md", "tech-digest.md", "industry-digest.md", "topic-map.md", "methodology.md"}
        for f_name in v2_data.keys():
            generated_files.add(f_name)


        await self._write_premium_files(v2_data, mosaic_html, videos_html)
        self._generate_digest_pages()
        await self._generate_global_tag_index(v2_data)

        # Phase 5: Structural changes — ONLY in full (non-render-only) mode
        # In render-only mode we never delete pages or rewrite the nav, because
        # the inventory pass is conservative and some pages may not be regenerated
        # in a given run even though they should still exist (e.g. low-hit pages).
        # Deleting them would break MkDocs nav references and corrupt the site.
        if self.render_only:
            log_event("[*] Phase 5: Skipped (render-only mode — nav and pages preserved)")
        else:
            log_event("[*] Phase 5: Syncing navigation and pruning orphaned pages...")
            nav_ok = await self._sync_enterprise_navigation(v2_data)
            if nav_ok:
                # Only prune if nav was successfully updated, and never delete
                # pages that are defined in self.dimensions (expected to exist).
                dimension_pages = {f"{slug}.md" for pages in self.dimensions.values() for slug in pages}
                for f in os.listdir(V2_DIR):
                    if f.endswith(".md") and f not in generated_files and f not in dimension_pages:
                        log_event(f"  [DEL] Pruning truly orphaned V2 page: {f}")
                        os.remove(os.path.join(V2_DIR, f))
            else:
                log_event("[WARN] Phase 5: Nav sync failed — skipping page deletion to avoid corruption")

        self._save_inventory()
        
        # --- FINAL SAFETY AUDIT ---
        try:
            from src.safety_guard import SafetyGuard
            guard = SafetyGuard()
            report = guard.generate_audit_report()
            with open("v2_safety_report.md", "w") as f: f.write(report)
        except Exception as e:
            log_event(f"  [!] V2 Safety Audit Error: {e}")
        
        log_event("V2 ELITE PORTAL GENERATED SUCCESSFULLY.")

    async def _gather_all_v1_content(self):
        all_links, mosaic_html, videos_html = [], "", ""
        if os.path.exists("docs/index.md"):
            with open("docs/index.md", "r") as f:
                idx_content = f.read()
                videos_match = re.search(r'\?\?\? note "Top Videos & Clips.*?\n\s+(<center.*?</center>)', idx_content, re.DOTALL)
                if videos_match:
                    videos_html = videos_match.group(1)
        
        # Dynamically generate V2 categorized mosaic from youtube_channels_mosaic.yaml
        try:
            from src.reorganize_mosaic import build_v2_mosaic_markdown
            v2_mosaic_full = build_v2_mosaic_markdown("data/youtube_channels_mosaic.yaml")
            mosaic_html = v2_mosaic_full.replace('<center markdown="1">', '').replace('</center>', '').strip()
        except Exception as e:
            log_event(f"  [!] Error generating V2 mosaic dynamically: {e}")
            mosaic_html = ""

        for root, _, files in os.walk(V1_DIR):
            for file in files:
                if not file.endswith(".md") or file == "index.md": continue
                path = os.path.join(root, file)
                with open(path, "r") as f: content = f.read()
                matches = re.finditer(r'^\s*-\s*(?:\*\*\(\d{4}\)\*\*\s+)?\[([^\]]+)\]\(([^\)]+)\)(.*?(?:\n\s{2,}.*)*)', content, re.MULTILINE)
                for m in matches:
                    title, url, full_desc = m.groups()
                    if not url.startswith(("http", "mailto", "#")):
                        url = f"https://nubenetes.com/{url.replace('.md', '/')}"
                    # Mandate 30: MD039 - Strip all whitespace (including non-breaking space) from link text
                    orig_file = file
                    slug = file.replace(".md", "")
                    if slug in self.merge_map:
                        orig_file = self.merge_map[slug] + ".md"
                    all_links.append({"title": nuclear_strip(title), "url": url.strip(), "description": full_desc.strip(), "original_file": orig_file})
        return all_links, mosaic_html, videos_html

    async def _verify_link_health(self, links: List[Dict]):
        force_full = os.getenv("FORCE_FULL_CHECK", "false").lower() == "true"
        fast_online = []
        needs_check = []
        
        for l in links:
            nu = normalize_url(l["url"])
            entry = self.inventory.get(nu, {})
            # Mandate 32: skip links under review
            if entry.get("status") == "review_required": continue
            
            if not force_full and entry.get("status") == "online":
                last_checked = entry.get("last_checked", 0)
                if isinstance(last_checked, (int, float)) and (datetime.now().timestamp() - last_checked) > 30 * 86400:
                    needs_check.append(l)
                else:
                    fast_online.append(l)
            else:
                needs_check.append(l)
                
        if not needs_check: return fast_online

        log_event(f"    [>] Fast-Track Health: {len(fast_online)} | Network-Check: {len(needs_check)}")
        
        online_links = list(fast_online)
        total_needs = len(needs_check)
        async with httpx.AsyncClient(timeout=15.0, follow_redirects=True, verify=False) as client:
            # Mandate 16/22: Resilient asynchronous health checks with increased concurrency
            CHUNK_SIZE = 100 
            for i in range(0, total_needs, CHUNK_SIZE):
                batch = needs_check[i:i+CHUNK_SIZE]
                tasks = [self._check_single_link_resilient(client, l) for l in batch]
                results = await asyncio.gather(*tasks)
                online_links.extend([r for r in results if r is not None])
                if i % 100 == 0:
                    log_event(f"    [>] Progress: [{i}/{total_needs}] links validated over network...")
                await asyncio.sleep(0.05) # Minimal delay
        return online_links

    async def _check_single_link_resilient(self, client, link: Dict):
        url = link["url"]
        norm_url = normalize_url(url)
        entry = self.inventory.get(norm_url, {})
        
        # Mandate 31: Skip links under review for V2 Elite
        if entry.get("status") == "review_required":
            log_event(f"  [-] SKIPPING V2: {url} is under Review.")
            return None
            
        if entry.get("status") == "online" and os.getenv("FORCE_FULL_CHECK", "false").lower() != "true": return link
        try:
            resp = await client.get(url, timeout=10.0)
            if resp.status_code < 400:
                final_url = str(resp.url)
                from src.gemini_utils import sanitize_trailing_slashes
                final_url = sanitize_trailing_slashes(final_url)
                
                # Update URL if it was redirected/normalized
                if final_url != url:
                    link["url"] = final_url
                
                self.inventory.setdefault(normalize_url(final_url), {})["status"] = "online"
                # Mandate 22: Update last_checked for the inventory entry
                self.inventory[normalize_url(final_url)]["last_checked"] = datetime.now().timestamp()
                return link
        except Exception as e:
            log_event(f"[WARN] resilient link check for {url}: {str(e)[:100]}")
        return None

    async def _evaluate_and_score_resources(self, links: List[Dict]):
        to_evaluate = []
        project_registry = {} 
        force_eval = os.getenv("FORCE_EVAL", "false").lower() == "true"
        force_full_check = os.getenv("FORCE_FULL_CHECK", "false").lower() == "true"
        # Bypassing GitHub UI limitation: If force_eval or force_full_check is ON, we must enrich metadata
        enrich_metadata = os.getenv("ENRICH_METADATA", "false").lower() == "true" or force_eval or force_full_check
        special_files = [sa["file"] for sa in self.special_assets_rules.get("special_assets", [])]
        
        # Mandate 47: Zero-Redundancy & Smart Grounding
        from src.mandate_ingestor import get_system_mandates
        dynamic_mandates = get_system_mandates()

        # Mandate 15: Proactive Enrichment for V2 (GitHub metadata is critical for tags)
        # Optimized: Parallel fetching with Semaphore to avoid sequential bottleneck
        processed_gh_metadata = set()
        gh_fetch_count = 0
        gh_tasks = []
        gh_sem = asyncio.Semaphore(30) # Increased for final sprint strategy

        async def _fetch_gh_with_sem(url: str):
            async with gh_sem:
                return url, await get_github_activity(url)

        for l in links:
            norm_url = normalize_url(l["url"])
            if "github.com" not in norm_url or self.render_only: continue

            cached = self.inventory.get(norm_url, {})
            # Mandate 43: Always ensure GH metadata for GitHub links in V2 to power [DE FACTO STANDARD] logic
            if (enrich_metadata or cached.get("gh_stars") is None) and norm_url not in processed_gh_metadata:
                processed_gh_metadata.add(norm_url)
                gh_tasks.append(_fetch_gh_with_sem(norm_url))

        if gh_tasks:
            log_event(f"  [METADATA] V2 Pulse: Batch fetching {len(gh_tasks)} GitHub profiles in parallel...", section_break=True)
            gh_results = await asyncio.gather(*gh_tasks)
            for norm_url, gh_data in gh_results:
                if gh_data:
                    if norm_url not in self.inventory: self.inventory[norm_url] = {}
                    self.inventory[norm_url].update(gh_data)
                    gh_fetch_count += 1

            # Periodic Save: Save once after the massive batch
            from src.inventory_manager import save_inventory
            save_inventory(self.inventory)
            log_event(f"    [💾] Inventory Persisted: {gh_fetch_count} metadata entries updated.")

        for l in links:
            item = l.copy()
            norm_url = normalize_url(l["url"])
            orig_file = l.get("original_file", "unknown.md")
            is_special = orig_file in special_files
            item["is_special"] = is_special
            project_id = norm_url
            if "github.com" in norm_url:
                match = re.search(r'github\.com/([^/]+/[^/]+)', norm_url)
                if match: project_id = match.group(1).lower()

            # Reuse enriched metadata from inventory
            if "github.com" in norm_url:
                item.update(self.inventory.get(norm_url, {}))

            if not force_eval and norm_url in self.inventory:
                cached = self.inventory[norm_url]
                item.update(cached)
                if is_special: item["is_special"] = True
                # Mandate 30: Hierarchy and AI Summaries are mandatory for ELITE AI curation.
                # Optimized Skip Logic: Only skip if we already have BOTH hierarchy and a summary.
                last_eval = cached.get("last_ai_eval", "")
                eval_stale = False
                if last_eval and isinstance(last_eval, str) and len(last_eval) >= 10:
                    try:
                        eval_age = (datetime.now(MADRID_TZ) - datetime.fromisoformat(last_eval)).days
                        eval_stale = eval_age > 180
                    except Exception:
                        pass
                if ((cached.get("hierarchy") and cached.get("ai_summary") and not eval_stale) or self.render_only) and not force_eval:
                    if project_id not in project_registry or (item.get("stars") or 0) > (project_registry[project_id].get("stars") or 0):
                        if project_id in project_registry and project_registry[project_id].get("is_special"): item["is_special"] = True
                        project_registry[project_id] = item
                    continue
            to_evaluate.append(item)

        if to_evaluate and (not self.render_only or force_eval):
            # Mandate 47: Zero-Redundancy & Smart Grounding
            # Fast-Track (Metadata/Desc present) vs Grounded-Track (Needs deep search)
            fast_track = []
            grounded_track = []
            
            for l in to_evaluate:
                nu = normalize_url(l["url"])
                is_github = "github.com" in nu
                
                # Fast-Track Eligibility:
                # 1. Has AI summary (previous run)
                # 2. Is GitHub and has stars (metadata present)
                # 3. Has decent manual description (> 40 chars)
                # 4. Is already in inventory (we have title/category context)
                has_ai_summary = l.get("ai_summary") is not None and len(l.get("ai_summary")) > 50
                has_stars = l.get("gh_stars") is not None
                has_desc = len(l.get("description", "")) > 40
                is_known = nu in self.inventory

                if has_ai_summary or has_stars or has_desc or is_known:
                    fast_track.append(l)
                else:
                    # Grounded-Track is ONLY for "Unknown" resources with zero context
                    grounded_track.append(l)

            log_event(f"[*] Agent Phase 1: Analyst Evaluation ({len(to_evaluate)} resources)...")
            log_event(f"    [>] Fast-Track: {len(fast_track)} | Grounded-Track: {len(grounded_track)}")

            analyst_results = []

            # 1.1 Fast-Track: Large Batches, NO GROUNDING (Fast)
            # Optimized: Parallel batch processing to leverage high-tier API quotas
            BATCH_SIZE_FAST = 50 
            total_fast = len(fast_track)
            fast_tasks = []

            async def _process_fast_batch(batch_links, batch_idx, total_b):
                log_event(f"    [>] Fast-Track: Queuing Batch {batch_idx}/{total_b}...")
                prompt = (
                    f"You are the Nubenetes Technical Analyst (2026).\n"
                    f"{dynamic_mandates}\n"
                    f"{self.library_criteria}\n"
                    "PHASE 5: TECHNICAL SYNTHESIS (FAST-TRACK)\n"
                    "- Use provided metadata, AI summaries, and descriptions to classify maturity.\n"
                    "Respond ONLY JSON: {{\"results\": [{{ \"idx\": int, \"year\": \"YYYY\", \"stars\": 0-5, \"hierarchy\": [\"Area\", \"Topic\", ...], \"tags\": [\"...\"], \"summary\": \"Synthesis...\", \"language\": \"...\", \"type\": \"...\", \"complexity\": \"...\", \"is_microservice\": bool }}, ...]}}\n\n"
                    "LINKS:\n" + "\n".join([f"{idx}. {l['title']} ({l['url']}) | Stars: {l.get('gh_stars', l.get('stars'))} | Existing Summary: {l.get('ai_summary', l.get('description'))}" for idx, l in enumerate(batch_links)])
                )
                try:
                    data = await call_gemini_with_retry(prompt, prefer_flash=True, use_grounding=False, role="Analyst-Fast")
                    batch_results = []
                    for res in data.get("results", []):
                        idx = int(res["idx"])
                        if idx < len(batch_links):
                            item = batch_links[idx].copy()
                            eval_data = {
                                "year": str(res.get("year", "N/A")), "stars": min(max(int(res.get("stars") or 0), 0), 5),
                                "ai_summary": res.get("summary", item.get("ai_summary", "")),
                                "language": res.get("language", "English"),
                                "resource_type": res.get("type", "Reference"), "complexity": res.get("complexity", "Intermediate"),
                                "hierarchy": res.get("hierarchy", ["General"]), "tags": res.get("tags", []),
                                "is_microservice": bool(res.get("is_microservice", False)),
                                "status": "online", "is_special": item.get("is_special", False),
                                "last_ai_eval": datetime.now(MADRID_TZ).isoformat()
                            }
                            existing_entry = self.inventory.get(normalize_url(item["url"]), {})
                            if existing_entry.get("discovered_at"):
                                eval_data["discovered_at"] = existing_entry["discovered_at"]
                            item.update(eval_data)
                            batch_results.append(item)

                            # Incremental Persistence
                            norm_url = normalize_url(item["url"])
                            from src.inventory_manager import update_inventory_entry
                            new_data = {k:v for k,v in item.items() if k not in ["url", "title", "original_file", "aliases"]}
                            new_data["title"] = item["title"]
                            update_inventory_entry(self.inventory, norm_url, new_data)
                    return batch_results
                except Exception as e:
                    log_event(f"    [!] Error in Fast-Batch {batch_idx}: {e}")
                    return batch_links # Fallback to original links (standard layer)

            total_batches_fast = (total_fast + BATCH_SIZE_FAST - 1) // BATCH_SIZE_FAST
            for i in range(0, total_fast, BATCH_SIZE_FAST):
                batch = fast_track[i:i+BATCH_SIZE_FAST]
                batch_num = (i // BATCH_SIZE_FAST) + 1
                fast_tasks.append(_process_fast_batch(batch, batch_num, total_batches_fast))

            if fast_tasks:
                log_event(f"[*] Agent Phase 1.1: Dispatching {len(fast_tasks)} parallel batches...")
                
                # Use as_completed to persist results incrementally during parallel execution
                processed_count = 0
                for task in asyncio.as_completed(fast_tasks):
                    r_list = await task
                    analyst_results.extend(r_list)
                    processed_count += 1
                    
                    # Mandate 22: Save every 10 batches to disk to avoid data loss during 6h timeouts
                    if processed_count % 10 == 0:
                        log_event(f"    [💾] Periodic Save: Persisting inventory after {processed_count} batches...")
                        from src.inventory_manager import save_inventory
                        save_inventory(self.inventory)

                # Final Save
                from src.inventory_manager import save_inventory
                save_inventory(self.inventory)
                log_event(f"    [💾] Inventory Persisted after {len(analyst_results)} AI evaluations.")

                await asyncio.sleep(2.0) # Safety delay to respect TPM limits

            # 1.2 Grounded-Track: Small Batches, WITH GROUNDING (Slower but precise)
            BATCH_SIZE_GROUNDED = 15 # Increased from 5
            total_grounded = len(grounded_track)
            for i in range(0, total_grounded, BATCH_SIZE_GROUNDED):
                batch = grounded_track[i:i+BATCH_SIZE_GROUNDED]
                batch_num = (i // BATCH_SIZE_GROUNDED) + 1
                total_batches = (total_grounded + BATCH_SIZE_GROUNDED - 1) // BATCH_SIZE_GROUNDED
                log_event(f"    [🌟] Grounded-Track: Processing Batch {batch_num}/{total_batches} (Grounding active)...")

                # MANDATE 25: Pre-enrich YouTube links with real metadata
                enriched_batch = []
                for item in batch:
                    url = item["url"]
                    if "youtube.com" in url or "youtu.be" in url:
                        log_event(f"      [YT] Pre-fetching metadata for: {url}")
                        meta = await fetch_youtube_metadata(url)
                        if meta:
                            item["description"] = f"TITLE: {meta['raw_title']}\nDESCRIPTION: {meta['raw_description']}"
                    enriched_batch.append(item)

                prompt = (
                    f"You are the Nubenetes Technical Analyst (2026).\n"
                    f"{dynamic_mandates}\n"
                    f"{self.library_criteria}\n"
                    "PHASE 5: DOUBLE-EVIDENCE SYNTHESIS & RICH SUMMARY (GROUNDED)\n"
                    "- Cross-reference provided title/desc with search grounding.\n"
                    "Respond ONLY JSON: {{\"results\": [{{ \"idx\": int, \"year\": \"YYYY\", \"stars\": 0-5, \"hierarchy\": [\"Area\", \"Topic\", ...], \"tags\": [\"...\"], \"summary\": \"Synthesis...\", \"language\": \"...\", \"type\": \"...\", \"complexity\": \"...\", \"is_microservice\": bool }}, ...]}}\n\n"
                    "LINKS:\n" + "\n".join([f"{idx}. {l['title']} ({l['url']}) | Input Context: {l.get('description', 'N/A')}" for idx, l in enumerate(enriched_batch)])
                )
                try:
                    data = await call_gemini_with_retry(prompt, prefer_flash=True, use_grounding=True, role="Analyst-Grounded")
                    for res in data.get("results", []):
                        idx = int(res["idx"])
                        if idx < len(batch):
                            item = batch[idx].copy()
                            eval_data = {
                                "year": str(res.get("year", "N/A")), "stars": min(max(int(res.get("stars") or 0), 0), 5),
                                "ai_summary": res.get("summary", ""), "language": res.get("language", "English"),
                                "resource_type": res.get("type", "Reference"), "complexity": res.get("complexity", "Intermediate"),
                                "hierarchy": res.get("hierarchy", ["General"]), "tags": res.get("tags", []),
                                "is_microservice": bool(res.get("is_microservice", False)),
                                "status": "online", "is_special": item.get("is_special", False),
                                "last_ai_eval": datetime.now(MADRID_TZ).isoformat()
                            }
                            existing_entry = self.inventory.get(normalize_url(item["url"]), {})
                            if existing_entry.get("discovered_at"):
                                eval_data["discovered_at"] = existing_entry["discovered_at"]
                            item.update(eval_data)
                            analyst_results.append(item)
                except Exception:
                    for l in batch: analyst_results.append(l)
                await asyncio.sleep(0.01 if os.environ.get("MOCK_DEBATE") == "true" else 4.0)
            # --- AGENT PHASE 2: MULTI-AGENT CONSENSUS & DEBATE PROTOCOL ---
            # Identify candidates for debate:
            # 1. High-impact candidates (marked as [DE FACTO STANDARD] or [ENTERPRISE-STABLE])
            # 2. Borderline candidates (stars == 3 or stars == 4)
            debate_candidates = [
                l for l in analyst_results 
                if "[DE FACTO STANDARD]" in l.get("tags", []) 
                or "[ENTERPRISE-STABLE]" in l.get("tags", [])
                or l.get("stars") or 0 in [3, 4]
            ]
            
            if debate_candidates:
                log_event(f"[*] Agent Phase 2: Multi-Agent Consensus & Debate Protocol ({len(debate_candidates)} candidates)...")
                from src.v2_debate import run_debate_protocol
                for item in debate_candidates:
                    try:
                        # Map current stars (0-5) to initial score (0-100)
                        item["impact_score"] = item.get("impact_score", item.get("stars", 3) * 20)
                        final_score, final_tags, refined_summary, debate_data = await run_debate_protocol(item)
                        
                        # Update item with consensus results
                        item["stars"] = min(max(final_score // 20, 0), 5)
                        item["impact_score"] = final_score
                        item["tags"] = final_tags
                        item["ai_summary"] = refined_summary
                        item["debate_log"] = debate_data
                    except Exception as e:
                        log_event(f"    [!] Debate failed for '{item.get('title')}': {e}")
                    await asyncio.sleep(0.01 if os.environ.get("MOCK_DEBATE") == "true" else 0.5)

            # Finalize Registry
            for item in analyst_results:
                norm_url = normalize_url(item["url"])
                p_id = norm_url
                if "github.com" in norm_url:
                    m = re.search(r'github\.com/([^/]+/[^/]+)', norm_url)
                    if m: p_id = m.group(1).lower()
                
                # Persist to inventory
                new_data = {k:v for k,v in item.items() if k not in ["url", "title", "original_file", "aliases"]}
                new_data["title"] = item["title"]
                if "addition_method" not in self.inventory.get(norm_url, {}):
                    new_data["addition_method"] = "manual"
                update_inventory_entry(self.inventory, norm_url, new_data)
                
                if p_id not in project_registry or item.get("stars") or 0 > project_registry[p_id].get("stars") or 0:
                    if p_id in project_registry and project_registry[p_id].get("is_special"): item["is_special"] = True
                    project_registry[p_id] = item

        return list(project_registry.values())

    def _calculate_tags(self, item: Dict) -> List[str]:
        """
        Mandate 40: Multi-Dimensional Tagging (1:N).
        Merges AI-assigned tags with rule-based maturity signals to ensure high-fidelity classification.
        Utilizes MCP-style grounding data (GitHub stars, resource types) to override generic defaults.
        """
        # 0. Collect all possible tag sources
        ai_tags = item.get("tags", [])
        if isinstance(ai_tags, str): ai_tags = [ai_tags] # Resiliency
        
        valid_set = {"[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]", "[EMERGING]", "[GUIDE]", "[CASE STUDY]", "[COMMUNITY-TOOL]", "[LEGACY]"}
        
        # Start with filtered AI tags and custom tech stack tags
        tags = set()
        for t in ai_tags:
            if not isinstance(t, str): continue
            t_stripped = t.strip()
            if t_stripped in valid_set:
                tags.add(t_stripped)
            elif t_stripped.startswith("[") and t_stripped.endswith("]"):
                inner = t_stripped[1:-1].strip()
                if inner.isupper() and all(c.isalnum() or c in "_-" for c in inner):
                    tags.add(t_stripped)
        
        # 1. GitHub Objective Reality (Mandate 43)
        raw_gh = item.get("gh_stars", 0)
        gh_stars = int(raw_gh) if str(raw_gh).isdigit() else 0
        curator_stars = int(item.get("stars") or 0)

        if gh_stars > 15000 or curator_stars >= 5: 
            tags.add("[DE FACTO STANDARD]")
            if "[COMMUNITY-TOOL]" in tags: tags.remove("[COMMUNITY-TOOL]")
        elif gh_stars > 3000 or curator_stars >= 4: 
            tags.add("[ENTERPRISE-STABLE]")
            if "[COMMUNITY-TOOL]" in tags: tags.remove("[COMMUNITY-TOOL]")
        
        # 2. Type Mapping (AI based labels)
        res_type = (item.get("resource_type") or "Reference").lower()
        if any(x in res_type for x in ["guide", "tutorial", "hands-on", "learning", "course"]): 
            tags.add("[GUIDE]")
        if any(x in res_type for x in ["case study", "report", "whitepaper", "success story", "usage"]): 
            tags.add("[CASE STUDY]")
        
        # 3. Emerging / Legacy logic
        ai_summary = (item.get("ai_summary") or "").lower()
        complexity = item.get("complexity", "Intermediate")
        if complexity == "Cutting Edge" or "emerging" in ai_summary or "experimental" in ai_summary or "alpha" in ai_summary:
            tags.add("[EMERGING]")
        if "legacy" in ai_summary or "deprecated" in ai_summary or "archived" in ai_summary or "v1-only" in ai_summary:
            tags.add("[LEGACY]")

        # 4. Fallback: Only use [COMMUNITY-TOOL] if no other maturity tag is present
        maturity_tags = {"[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]", "[EMERGING]", "[LEGACY]"}
        if not (tags & maturity_tags):
            tags.add("[COMMUNITY-TOOL]")
        
        # Clean up: If we have high maturity, remove community-tool
        if (tags & {"[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]"}) and "[COMMUNITY-TOOL]" in tags:
            tags.remove("[COMMUNITY-TOOL]")

        return sorted(list(tags))

    async def _rebuild_structure(self, library_inventory: List[Dict]):
        special_rules = {sa["file"]: sa for sa in self.special_assets_rules.get("special_assets", [])}
        v2_structure = {} 
        
        file_to_dim = {f + ".md": dim for dim, files in self.dimensions.items() for f in files}

        for item in library_inventory:
            # Calculate multi-tags
            item["tags"] = self._calculate_tags(item)
            
            # Mandate: Persist tags back to inventory for reporting & caching
            norm_url = normalize_url(item["url"])
            
            # Mandate 19: Use v1_locations to preserve file context and prevent page deletions
            v1_locations = item.get("v1_locations", [])
            if not v1_locations:
                # Fallback to original_file if v1_locations is missing
                v1_locations = [f"docs/{item.get('original_file', 'unknown.md')}"]
            
            for loc in v1_locations:
                orig_file = os.path.basename(loc)
                if not orig_file.endswith(".md") or orig_file == "index.md": continue
                
                if norm_url in self.inventory:
                    self.inventory[norm_url]["tags"] = item["tags"]
                    # Track V2 locations for reporting (Mandate 22)
                    v2_locs = self.inventory[norm_url].get("v2_locations", [])
                    if orig_file not in v2_locs:
                        v2_locs.append(orig_file)
                        self.inventory[norm_url]["v2_locations"] = v2_locs
                
                dim = file_to_dim.get(orig_file, "Architectural Foundations")
                
                # Mandate 29: Special Assets must include 100% of ALIVE links, bypassing impact filters.
                is_special = item.get("is_special", False) or orig_file in special_rules
                if not is_special and orig_file == "introduction.md" and (item.get("stars") or 0) < 3 and not item.get("is_microservice"):
                    continue
                
                if orig_file not in v2_structure:
                    short_title = orig_file.replace(".md", "").replace("-", " ").title()
                    # Custom mapping for known acronyms (Mandate 32)
                    acronyms = {
                        "Ai": "AI", "Mcp": "MCP", "Iac": "IaC", "Aws": "AWS", "Gcp": "GCP", 
                        "Api": "API", "Sre": "SRE", "Cicd": "CI/CD", "Ocp3": "OCP 3", 
                        "Ocp4": "OCP 4", "Jvm": "JVM", "Sql": "SQL", "Nosql": "NoSQL",
                        "Chatgpt": "ChatGPT", "Mlops": "MLOps", "Devops": "DevOps",
                        "Hr": "HR", "Qa": "QA"
                    }
                    for k, v in acronyms.items():
                        short_title = short_title.replace(k, v)
                    
                    long_title = short_title
                    v1_path = os.path.join("docs", orig_file)
                    if os.path.exists(v1_path):
                        with open(v1_path, "r", encoding="utf-8") as f:
                            for line in f:
                                if line.startswith("# "):
                                    long_title = line.strip().replace("# ", "").strip()
                                    break

                    v2_structure[orig_file] = {
                        "dim": dim,
                        "title": short_title,
                        "long_title": long_title,
                        "content": {"__links__": []}
                    }
                
                # Populate Maturity Audit for GitOps Reporting (Deduplicated)
                audit_entry = {
                    "url": item["url"],
                    "tag": ", ".join(item["tags"]),
                    "stars": item.get("stars") or 0,
                    "dimension": dim,
                    "v2_locations": True 
                }
                if audit_entry not in self.maturity_audit:
                    self.maturity_audit.append(audit_entry)
                
                hierarchy = item.get("hierarchy", [])
                # Skip redundant top-level labels
                if hierarchy and (hierarchy[0] == dim or hierarchy[0] == v2_structure[orig_file]["title"]): hierarchy = hierarchy[1:]
                
                current = v2_structure[orig_file]["content"]
                cleaned_hierarchy = []
                for h_raw in hierarchy:
                    h_name = clean_hierarchy_section_name(h_raw)
                    if h_name and (not cleaned_hierarchy or h_name != cleaned_hierarchy[-1]):
                        cleaned_hierarchy.append(h_name)
                
                for h_name in cleaned_hierarchy[:self.max_depth]:
                    if h_name not in current: current[h_name] = {"__links__": []}
                    current = current[h_name]
                current["__links__"].append(item)

        def sort_rec(node):
            if "__links__" in node: node["__links__"].sort(key=lambda x: (-(x.get("stars") or 1), -(int(x["year"]) if str(x.get("year", "")).isdigit() else 0)))
            for k, v in node.items():
                if k != "__links__" and isinstance(v, dict): sort_rec(v)
                
        for f_name in v2_structure:
            sort_rec(v2_structure[f_name]["content"])
            
        return v2_structure

    def _collect_tags_from_tree(self, node: Dict) -> List[Set]:
        """Recursively collect maturity/tech tags from a content tree for cross-referencing."""
        results = []
        if "__links__" in node:
            for link in node["__links__"]:
                tags = set(link.get("tags", []))
                if tags:
                    results.append(tags)
        for key, val in node.items():
            if key != "__links__" and isinstance(val, dict):
                results.extend(self._collect_tags_from_tree(val))
        return results

    async def _generate_comparison_table(self, links: List[Dict]) -> str:
        standard_tools = [l for l in links if l.get("stars") or 0 >= 3]
        if len(standard_tools) < 8: return ""
        table = "\n??? abstract \"Architect's Technical Comparison Table\"\n"
        table += "    | Solution | Maturity | Primary Focus | Language | Stars |\n"
        table += "    | :--- | :--- | :--- | :--- | :--- |\n"
        for l in standard_tools[:10]:
            stars = "🌟" * l.get("stars") or 0
            focus = l.get("topic", l.get("hierarchy", ["General"])[-1])
            # Mandate 30: MD039 - Strip all whitespace (including non-breaking space) from link text
            clean_title = nuclear_strip(l['title'])
            table += f"    | [{clean_title}]({l['url'].strip()}) | {l.get('tag','').replace('[','').replace(']','')} | {focus} | {l.get('language','English')} | {stars} |\n"
        return table + "\n"

    def generate_sparkline_svg(self, url: str, stars_count: int) -> str:
        # Deterministic points based on hash of url
        h = hashlib.sha256(url.encode()).digest()
        # Map hash bytes to 6 y-coordinates between 2 and 13 (within 15px height)
        points = []
        for i in range(6):
            byte_val = h[i % len(h)]
            # Add wave variance based on stars_count
            wave = (stars_count % (i + 1)) * 2
            y = 13 - ((byte_val + wave) % 12)
            points.append(y)
        
        # Trend generally goes upwards for higher-star repos
        if stars_count > 1000:
            points[-1] = min(points[-1], 5) # high y means low index in SVG coordinates (0 is top)
        
        path_d = f"M 0 {points[0]} L 10 {points[1]} L 20 {points[2]} L 30 {points[3]} L 40 {points[4]} L 50 {points[5]}"
        
        # Unique ID for gradient to avoid clashes
        url_hash = hashlib.md5(url.encode()).hexdigest()[:8]
        
        svg = (
            f'<svg class="v2-sparkline" width="50" height="15" viewBox="0 0 50 15" style="vertical-align: middle; display: inline-block; margin-left: 6px;" title="Activity Trend">'
            f'<defs>'
            f'<linearGradient id="spark-grad-{url_hash}" x1="0" y1="0" x2="1" y2="0">'
            f'<stop offset="0%" stop-color="rgba(34, 211, 238, 0.2)" />'
            f'<stop offset="100%" stop-color="var(--md-accent-fg-color)" />'
            f'</linearGradient>'
            f'</defs>'
            f'<path class="v2-sparkline-path" d="{path_d}" fill="none" stroke="url(#spark-grad-{url_hash})" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" />'
            f'<circle cx="50" cy="{points[5]}" r="2" fill="var(--md-accent-fg-color)" />'
            f'</svg>'
        )
        return svg

    async def _render_single_link(self, l: Dict, is_intro: bool) -> str:
        md = ""
        is_gold = is_intro and (l.get("stars") or 0) >= 4
        title = nuclear_strip(l['title']) 
        if is_gold:
            img = f"    ![Preview]({l.get('social_preview_url')})\n" if l.get('social_preview_url') else ""
            md += f"??? note \"{title}\"\n{img}    **[Access Resource]({l['url'].strip()})** {'🌟'*l.get('stars',4)} | Level: {l.get('complexity', 'Beginner')}\n    \n    {l.get('ai_summary', l.get('description', ''))}\n\n"
        else:
            year = l.get('year', 'N/A')
            year_prefix = f"**({year})** " if year != 'N/A' else ""
            gh_info = f" <span class='md-tag md-tag--info'>⭐ {l.get('gh_stars',0)}</span>" if l.get('gh_stars') else ""
            sparkline = ""
            if l.get('gh_stars'):
                sparkline = " " + self.generate_sparkline_svg(l['url'], l.get('gh_stars', 0))
            
            icon = " 🎥" if l.get("is_video") else ""
            lang = l.get("language") or "English"
            lang_tag = f" <span class='md-tag md-tag--warning'>[{lang.upper()} CONTENT]</span>" if lang.lower() != "english" else ""
            comp = l.get("complexity") or "Intermediate"
            level_tag = f" <span class='md-tag md-tag--critical'>[{comp.upper()} LEVEL]</span>" if comp.lower() in ["architect", "advanced"] else ""
            res_type = l.get("resource_type") or "Reference"
            type_tag = ""
            if res_type.lower() in ["case study", "guide", "documentation"]:
                if f"[{res_type.upper()}]" not in l.get("tags", []):
                    type_tag = f" <span class='md-tag md-tag--primary'>[{res_type.upper()}]</span>"
            rich = "".join([f" <small>by **{l['author']}**</small>" if l.get("author") else "", f" <span class='md-tag md-tag--info'>⏱️ {l['duration']}</span>" if l.get("duration") else "", f" <span class='md-tag md-tag--info'>📖 {l['reading_time']}</span>" if l.get("reading_time") else ""])
            tag_html = ""
            for tag in l.get("tags", ["[COMMUNITY-TOOL]"]):
                if tag in ["[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]"]:
                    color = "success"
                elif tag == "[EMERGING]":
                    color = "warning"
                elif tag == "[LEGACY]":
                    color = "critical"
                elif tag in ["[GUIDE]", "[CASE STUDY]"]:
                    color = "secondary"
                elif tag == "[COMMUNITY-TOOL]":
                    color = "info"
                else:
                    color = "primary"
                tag_html += f" <span class='md-tag md-tag--{color}'>{tag}</span>"
            
            # Apply Visual Highlighting based on stars
            raw_stars = l.get('stars') or 0
            link_content = title
            if raw_stars >= 5:
                link_content = f"=={link_content}=="
            elif raw_stars >= 4:
                link_content = f"**{link_content}**"
            
            md += f"  - {year_prefix}[{link_content}]({l['url'].strip()}){icon}{gh_info}{sparkline}{lang_tag}{level_tag}{type_tag}{rich} {'🌟'*raw_stars}{tag_html}"

            # Layer 2: High-Density Technical Summary (Always Visible Inline)
            summary = l.get('ai_summary', l.get('description', ''))
            if summary:
                # Use a separator and append summary directly to the same line
                md += f" — {summary.strip()}\n"
            else:
                md += "\n"
        return md


    def _render_compact_tag_link(self, l: Dict) -> str:
        orig_file = l.get("original_file", "")
        cat_link = ""
        if orig_file:
            cat_link = f" — *Go to [Section](./{orig_file})*"

        year = l.get("year", "")
        year_prefix = f"**({year})** " if year and str(year).lower() != "n/a" else ""

        raw_stars = l.get("stars") or 0
        stars_str = f" {'🌟' * raw_stars}" if raw_stars > 0 else ""

        # Title formatting based on impact
        title = nuclear_strip(l.get("title", "Unknown Resource"))
        link_content = title
        if raw_stars >= 5:
            link_content = f"=={link_content}=="
        elif raw_stars >= 4:
            link_content = f"**{link_content}**"

        # Build other tags compactly
        tag_html = ""
        for tag in l.get("tags", []):
            if tag in ["[DE FACTO STANDARD]", "[ENTERPRISE-STABLE]"]:
                color = "success"
            elif tag == "[EMERGING]":
                color = "warning"
            elif tag == "[LEGACY]":
                color = "critical"
            elif tag in ["[GUIDE]", "[CASE STUDY]"]:
                color = "secondary"
            elif tag == "[COMMUNITY-TOOL]":
                color = "info"
            else:
                color = "primary"
            tag_html += f" <span class='md-tag md-tag--{color}'>{tag}</span>"

        lang = l.get("language", "English")
        lang_tag = ""
        if lang.lower() not in ["english", "n/a", "none"]:
            lang_tag = f" <span class='md-tag md-tag--warning'>[{lang.upper()} CONTENT]</span>"

        return f"  - {year_prefix}[{link_content}]({l['url'].strip()}){stars_str}{tag_html}{lang_tag}{cat_link}\n"



    def _generate_digest_pages(self):
        """Generate tech-digest.md and industry-digest.md from news_digest.json."""
        digest_path = "data/news_digest.json"
        if not os.path.exists(digest_path):
            log_event("[Digest] No digest data found, skipping page generation")
            return
        with open(digest_path, "r", encoding="utf-8") as f:
            digest_data = json.load(f)

        tech_cats = [
            "Kubernetes & Orchestration", "Containers & Runtime", "Networking & Service Mesh",
            "Architecture & Microservices", "Data, Messaging & Storage", "AI & Agents",
            "MLOps & Data Science", "Python, Java & Developer Ecosystem", "Linux & System Foundations",
            "Security & Compliance", "Infrastructure as Code", "CI/CD & GitOps",
            "Observability, SRE & Testing", "DevOps & Culture", "Platform Engineering & DevEx",
            "FinOps & Cloud Cost", "Certification & Training",
            "AWS", "Azure", "GCP, OCI & Others", "OpenShift / Red Hat", "Virtualization & Private Cloud"
        ]
        geo_cats = ["Americas", "Europe", "Spain", "Asia-Pacific"]
        period_labels = {"3_months": "Last 3 Months", "6_months": "Last 6 Months", "12_months": "Last 12 Months"}

        def render_digest_page(title, categories, digest_data, search_boost=1):
            md = f"---\nsearch:\n  boost: {search_boost}\n---\n\n"
            md += f"# {title}\n\n"
            md += "!!! tip \"Nubenetes Intelligence Digest\"\n"
            md += "    AI-curated ranking of the most impactful resources, updated monthly.\n\n"
            # Category-first layout: each category is a real H2 heading (at column 0)
            # so it appears exactly once in the MkDocs Material right-hand "On this page"
            # TOC, with the three time-windows as content tabs *inside* the category.
            # (The previous period-first layout nested categories as bold text inside
            # tabs, which produced no TOC entries and tripped MD023 on indented headings.)
            for cat in categories:
                # Skip categories with no ranked items in any time window.
                if not any(digest_data.get(pk, {}).get(cat) for pk in period_labels):
                    continue
                md += f"## {cat}\n\n"
                for period_key, period_label in period_labels.items():
                    items = digest_data.get(period_key, {}).get(cat, [])
                    if not items:
                        continue
                    md += f'=== "{period_label}"\n\n'
                    md += "    | Date | Resource | Impact | Why It Matters |\n"
                    md += "    | :--- | :--- | :---: | :--- |\n"
                    for item in items:
                        impact_badge = {"critical": "🔴", "high": "🟡", "medium": "🔵"}.get(item.get("impact", "medium"), "🔵")
                        t = nuclear_strip(item.get("title", "Unknown")).replace("|", r"\|")
                        why = (item.get("why", "") or "").replace("|", "-").replace("\n", " ")
                        md += f'    | {item.get("date", "")} | [{t}]({item.get("url", "#")}) | {impact_badge} {item.get("impact", "medium")} | {why} |\n'
                    md += "\n"
                md += "\n"
            return md

        tech_md = render_digest_page("📊 Nubenetes Tech & Cloud Intelligence Digest", tech_cats, digest_data, search_boost=2)
        with open(os.path.join(V2_DIR, "tech-digest.md"), "w", encoding="utf-8") as f:
            f.write(tech_md)

        industry_md = render_digest_page("🌍 Nubenetes Industry & Geo Intelligence Digest", geo_cats, digest_data, search_boost=2)
        with open(os.path.join(V2_DIR, "industry-digest.md"), "w", encoding="utf-8") as f:
            f.write(industry_md)

        log_event("[Digest] Generated tech-digest.md and industry-digest.md")

    async def _write_premium_files(self, data: Dict[str, Dict], mosaic_html: str, videos_html: str):
        # 1. Build Trending Now from digest data, or fallback to star-based pulse
        digest_data = {}
        digest_path = "data/news_digest.json"
        if os.path.exists(digest_path):
            try:
                with open(digest_path, "r", encoding="utf-8") as df:
                    digest_data = json.load(df)
            except Exception:
                pass

        if digest_data and "3_months" in digest_data:
            # --- Trending v2: momentum-weighted, category-diverse selection ---
            # Score = impact_weight * recency_decay so the section actually rotates
            # with fresh items instead of pinning evergreen/foundational tools.
            # Anchor "now" to the digest's analysis timestamp (not wall-clock) so
            # identical digest input always renders identical cards — re-renders on
            # later days must not shuffle ages/NEW pills and churn the committed HTML.
            now = datetime.now(MADRID_TZ)
            try:
                raw_now = digest_data.get("_meta", {}).get("last_updated", "")
                if raw_now:
                    now = datetime.fromisoformat(raw_now)
            except Exception as e:
                log_event(f"[WARN] trending now-anchor: {str(e)[:100]}")
            impact_weight = {"critical": 1.0, "high": 0.66, "medium": 0.4}
            impact_icons = {"critical": "🔴", "high": "🟡", "medium": "🔵"}

            def _parse_day(s):
                try:
                    return datetime.fromisoformat(
                        str(s).replace("Z", "+00:00").split("T")[0]
                    ).date()
                except Exception:
                    return None

            def _clean_title(t):
                t = nuclear_strip(t)
                # "github.com/owner/repo" -> "repo"
                if "github.com/" in t.lower():
                    t = t.rstrip("/").split("/")[-1]
                # "domain.tld: Real Name" -> "Real Name" (Gemini host-prefixed titles)
                m = re.match(r'^[\w.-]+\.[a-z]{2,}:\s*(.+)$', t, re.I)
                if m:
                    t = m.group(1)
                return t

            def _fmt_stars(n):
                if not n:
                    return ""
                if n >= 1000:
                    return f"{n / 1000:.1f}k★".replace(".0k", "k")
                return f"{n}★"

            def _select_lane(window_key, count, exclude_urls, score_fn):
                # Build a scored pool from the window's top-2 items per category,
                # then apply a per-category diversity quota. The scoring policy is
                # supplied by score_fn so each lane surfaces a different signal.
                pool = []
                for cat_name, items in digest_data.get(window_key, {}).items():
                    for item in (items or [])[:2]:
                        if not isinstance(item, dict) or item.get("url") in exclude_urls:
                            continue
                        d = _parse_day(item.get("date"))
                        age_days = (now.date() - d).days if d else 999
                        pool.append({**item, "digest_category": cat_name, "_age_days": age_days, "_score": score_fn(item, age_days)})
                pool.sort(key=lambda x: x["_score"], reverse=True)
                # Diversity quota: at most one card per category, then backfill.
                sel, used_cats, used = [], set(), set(exclude_urls)
                for it in pool:
                    if it["digest_category"] in used_cats or it.get("url") in used:
                        continue
                    sel.append(it)
                    used_cats.add(it["digest_category"])
                    used.add(it.get("url"))
                    if len(sel) >= count:
                        break
                if len(sel) < count:
                    for it in pool:
                        if it.get("url") in used:
                            continue
                        sel.append(it)
                        used.add(it.get("url"))
                        if len(sel) >= count:
                            break
                return sel

            def _render_cards(items, show_new=True, extra_from=None):
                html = ""
                for idx, item in enumerate(items):
                    extra_cls = " trending-card--extra" if extra_from is not None and idx >= extra_from else ""
                    impact = item.get("impact", "medium")
                    # Momentum: prefer real GitHub star count from the inventory join;
                    # fall back to the 1-5 Gemini impact score rendered as 🌟.
                    inv_meta = self.inventory.get(item.get("url")) if isinstance(self.inventory, dict) else None
                    gh_stars = inv_meta.get("gh_stars") if isinstance(inv_meta, dict) else None
                    metric = _fmt_stars(gh_stars)
                    if not metric:
                        score = item.get("stars") or 0
                        metric = "🌟" * score if score else ""
                    meta = item.get("date", "")
                    if metric:
                        meta += f" · {metric}"
                    new_pill = ' <span class="trending-card__new">🆕 NEW</span>' if show_new and item.get("_age_days", 999) <= 7 else ""
                    html += (
                        f'<div class="trending-card{extra_cls}">\n'
                        f'  <div class="trending-card__impact trending-card__impact--{impact}">{impact_icons.get(impact, "🔵")} {impact.upper()}{new_pill}</div>\n'
                        f'  <div class="trending-card__category">{item.get("digest_category", "")}</div>\n'
                        f'  <div class="trending-card__title"><a href="{item.get("url", "#")}">{_clean_title(item.get("title", "Unknown"))}</a></div>\n'
                        f'  <div class="trending-card__meta">{meta}</div>\n'
                        f'  <div class="trending-card__why">{item.get("why", "")}</div>\n'
                        f'</div>\n'
                    )
                return html

            def _render_lane(title_html, items, lane_id, visible, show_new=True):
                # Render a lane's grid; if it has more than `visible` cards, wrap the
                # overflow in a pure-CSS (checkbox-hack) "Show N more" disclosure so
                # the section stays dense without flooding the page. No JS required.
                collapsible = len(items) > visible
                grid = _render_cards(items, show_new=show_new, extra_from=visible if collapsible else None)
                if not collapsible:
                    return f'<div class="trending-lane">\n{title_html}\n<div class="trending-grid">\n{grid}</div>\n</div>\n'
                extra = len(items) - visible
                return (
                    f'<div class="trending-lane">\n{title_html}\n'
                    f'<input type="checkbox" id="{lane_id}" class="trending-toggle">\n'
                    f'<div class="trending-grid">\n{grid}</div>\n'
                    f'<label for="{lane_id}" class="trending-showmore">'
                    f'<span class="trending-showmore__more">▼ Show {extra} more</span>'
                    f'<span class="trending-showmore__less">▲ Show less</span></label>\n'
                    f'</div>\n'
                )

            # Proven-staying-power signal for lane 2: URLs that the digest ranks in
            # the top-2 of any category over the full 12-month window.
            twelve_mo_urls = {
                it.get("url")
                for items in digest_data.get("12_months", {}).values()
                for it in (items or [])
                if isinstance(it, dict)
            }

            def _impact(item):
                return impact_weight.get(item.get("impact", "medium"), 0.4)

            def _fresh_score(item, age_days):
                # Aggressive 21d half-life: surfaces the very newest high-impact items.
                recency = 0.5 ** (max(age_days, 0) / 21.0)
                return _impact(item) * (0.35 + 0.65 * recency)

            def _sustained_score(item, age_days):
                # "Rising this Quarter": reward proven staying power (present across
                # the 12-month window) and de-prioritise <7d items (those belong in
                # lane 1) so the two lanes surface genuinely different resources —
                # not just lane 1's leftovers under a different label.
                persistence = 1.0 if item.get("url") in twelve_mo_urls else 0.5
                maturity = 0.35 if age_days < 7 else 1.0
                decay = 0.5 ** (max(age_days, 0) / 120.0)
                return _impact(item) * persistence * maturity * (0.45 + 0.55 * decay)

            # Lane 1: fresh momentum (3-month window). Pull a deep, category-diverse
            # set; the lane shows the first few and tucks the rest behind "Show more".
            top_items = _select_lane("3_months", 16, set(), _fresh_score)
            # Lane 2: sustained momentum (6-month window), de-duplicated against lane 1.
            rising_items = _select_lane("6_months", 12, {it.get("url") for it in top_items}, _sustained_score)

            try:
                from datetime import datetime as _dt
                # Prefer _meta.last_updated (tracks actual Gemini analysis date)
                # over file mtime (which changes on every commit/render).
                raw_ts = digest_data.get("_meta", {}).get("last_updated", "")
                if raw_ts:
                    digest_updated = _dt.fromisoformat(raw_ts).strftime("%b %d, %Y")
                else:
                    digest_updated = _dt.fromtimestamp(
                        os.path.getmtime(digest_path)
                    ).strftime("%b %d, %Y")
            except Exception:
                digest_updated = ""
            updated_badge = f'<span class="trending-section__updated">Updated {digest_updated}</span>' if digest_updated else ""
            lane1_title = f'<div class="trending-section__title">🔥 Trending Now — Cloud Native Intelligence {updated_badge}</div>'
            cards_html = '<div class="trending-section">\n'
            cards_html += _render_lane(lane1_title, top_items, "trend-expand-now", 9, show_new=True)
            if rising_items:
                lane2_title = '<div class="trending-section__title trending-section__title--secondary">📈 Rising this Quarter — Sustained Momentum</div>'
                cards_html += _render_lane(lane2_title, rising_items, "trend-expand-rising", 6, show_new=False)
            cards_html += '<div class="digest-links">\n'
            cards_html += '  <a href="/tech-digest/" class="digest-link-card">📊 Full Tech & Cloud Digest →</a>\n'
            cards_html += '  <a href="/industry-digest/" class="digest-link-card">🌍 Industry & Geo Digest →</a>\n'
            cards_html += '</div>\n</div>\n'
            pulse_md = cards_html
        else:
            trending_pool = sorted([dict(meta, url=url) for url, meta in self.inventory.items() if isinstance(meta, dict) and (meta.get("stars") or 0) >= 4], key=lambda x: (str(x.get("year", "0000")) if str(x.get("year", "")).isdigit() else "0000", -(x.get("stars") or 0)), reverse=True)
            pulse_md = "## The Agentic Pulse\n" + "\n".join([f"- **({l.get('year', 'N/A')})** [**=={nuclear_strip(l['title'])}==**]({l['url'].strip()}) {'🌟'*l.get('stars',3)}" for l in trending_pool[:5]])
        
        # Calculate coverage for the index
        total_v1 = len(self.inventory)
        v2_links_all = [dict(meta, url=url) for url, meta in self.inventory.items() if isinstance(meta, dict) and meta.get("v2_locations")]
        total_v2 = len(v2_links_all)
        v2_efficiency = round((total_v2 / total_v1) * 100, 2) if total_v1 > 0 else 0
        enriched = len([l for l in v2_links_all if l.get('hierarchy') or l.get('ai_summary')])
        coverage_pct = round((enriched / total_v2) * 100, 2) if total_v2 > 0 else 0
        
        # GitHub Metadata Coverage for index
        gh_links = [l for l in v2_links_all if "github.com" in str(l.get('url', ''))]
        total_gh = len(gh_links)
        gh_meta = len([l for l in gh_links if l.get('gh_stars') is not None])
        gh_coverage = round((gh_meta / total_gh) * 100, 2) if total_gh > 0 else 0

        coverage_info = (
            "\n??? info \"Knowledge Architecture and AI Coverage Status\"\n"
            "    The Nubenetes Elite Portal operates on a dual-layer knowledge architecture:\n"
            "    1. **Elite Layer (AI-Enriched)**: Resources individually analyzed by our Agentic AI with high-density summaries and hierarchical indexing.\n"
            "    2. **Standard Layer (Mapped)**: Resources identified as candidates for Elite status but pending deep AI analysis.\n\n"
            "    **Current Inventory Coverage:**\n"
            f"    - **V1 Base Inventory**: {total_v1} total resources analyzed.\n"
            f"    - **V2 Elite Selection**: {total_v2} candidates identified ({v2_efficiency}% density ratio).\n"
            f"    - **AI Enrichment Coverage**: {enriched} / {total_v2} ({coverage_pct}%)\n"
            f"    - **GitHub Metadata Coverage**: {gh_meta} / {total_gh} ({gh_coverage}%) - *Critical for Maturity Tagging*\n"
            "    - **Status**: The system is incrementally processing pending resources to complete the knowledge graph.\n"
        )

        # Label Heatmap for the index: identical tag aggregation to the Tags page
        # (deterministic slugs), but each label deep-links across to /tags/#slug.
        heat_sorted, heat_meta, _ = self._aggregate_tags(data)
        index_heatmap = self._render_tag_heatmap(
            heat_sorted, heat_meta, href_base="/tags/",
            intro=(
                "Every technical label across Nubenetes, sized by how many "
                "resources carry it. Click any label to open it on the "
                "[Technical Tags](/tags/) page."
            ),
        )

        index_md = (
            "# Nubenetes Elite Portal (V2) | Awesome Kubernetes & Cloud [![Awesome](https://cdn.jsdelivr.net/gh/sindresorhus/awesome@d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)](https://github.com/sindresorhus/awesome)\n\n"
            "!!! tip \"Nubenetes V2 Elite Portal: AI-Curated & High-Density\"\n"
            "    You are browsing the AI-Curated V2 Elite Edition of Nubenetes. Looking for the complete historical archive? Explore the [**V1 Historical Archive**](/v1/).\n\n"
            "<center markdown=\"1\">\n"
            "<div class=\"hero-showcase-wrapper\">\n"
            "  <a href=\"https://www.cncf.io/certification/software-conformance\" class=\"hero-showcase-link\">\n"
            "    <img src=\"/images/container_with_cars_v2.png\" alt=\"container_with_cars\" class=\"hero-showcase-image\" />\n"
            "    <div class=\"hero-showcase-footer\">\n"
            "      <span class=\"hero-showcase-badge\">CNCF Conformance</span>\n"
            "      <span class=\"hero-showcase-caption\">Standardized conformance guarantees seamless workload portability across the Cloud Native landscape.</span>\n"
            "    </div>\n"
            "  </a>\n"
            "</div>\n"
            "</center>\n\n"
            "<div class=\"quote-card-container\">\n"
            "  <a href=\"https://en.wikipedia.org/wiki/Horatio_Nelson_Jackson\" class=\"quote-card-link\">\n"
            "    <div class=\"quote-card\">\n"
            "      <div class=\"quote-card-text\">\"I do not believe you can do today's job with yesterday's methods and be in business tomorrow\"</div>\n"
            "      <div class=\"quote-card-author\">Horatio Nelson Jackson</div>\n"
            "    </div>\n"
            "  </a>\n"
            "</div>\n\n"
            "## Explore the Ecosystem\n\n"
            "<div class=\"hero-badge-row\">\n"
            "  <a href=\"/kubernetes/\" style=\"text-decoration: none; color: inherit; display: block;\">\n"
            "    <div class=\"hero-badge-card hero-badge-card--cyan\">\n"
            "      <img src=\"/images/kubernetes_logo.png\" alt=\"Kubernetes\"/>\n"
            "      <div class=\"hero-badge-title\">Ecosystem Core</div>\n"
            "      <div class=\"hero-badge-subtitle\">Explore Kubernetes</div>\n"
            "    </div>\n"
            "  </a>\n"
            "  <a href=\"/ai-agents-mcp/\" style=\"text-decoration: none; color: inherit; display: block;\">\n"
            "    <div class=\"hero-badge-card hero-badge-card--purple\">\n"
            "      <img src=\"/images/ai_agents_logo.png\" alt=\"AI & MCP Agents\"/>\n"
            "      <div class=\"hero-badge-title\">AI & MCP Agents</div>\n"
            "      <div class=\"hero-badge-subtitle\">Agentic Ecosystem</div>\n"
            "    </div>\n"
            "  </a>\n"
            "  <a href=\"/tech-digest/\" style=\"text-decoration: none; color: inherit; display: block;\">\n"
            "    <div class=\"hero-badge-card hero-badge-card--amber\">\n"
            "      <div class=\"hero-badge-icon\">📊</div>\n"
            "      <div class=\"hero-badge-title\">Intelligence Digest</div>\n"
            "      <div class=\"hero-badge-subtitle\">Top picks · 3/6/12 months</div>\n"
            "    </div>\n"
            "  </a>\n"
            "  <a href=\"/videos/\" style=\"text-decoration: none; color: inherit; display: block;\">\n"
            "    <div class=\"hero-badge-card hero-badge-card--pink\">\n"
            "      <img src=\"/images/video_hub_logo.png\" alt=\"Agentic Video Hub\"/>\n"
            "      <div class=\"hero-badge-title\">Agentic Video Hub</div>\n"
            "      <div class=\"hero-badge-subtitle\">Architect Video Library</div>\n"
            "    </div>\n"
            "  </a>\n"
            "  <a href=\"/topic-map/\" style=\"text-decoration: none; color: inherit; display: block;\">\n"
            "    <div class=\"hero-badge-card hero-badge-card--indigo\">\n"
            "      <div class=\"hero-badge-icon\">🗺️</div>\n"
            "      <div class=\"hero-badge-title\">Topic Map</div>\n"
            "      <div class=\"hero-badge-subtitle\">All Categories · Directory</div>\n"
            "    </div>\n"
            "  </a>\n"
            "  <a href=\"/introduction/\" style=\"text-decoration: none; color: inherit; display: block;\">\n"
            "    <div class=\"hero-badge-card hero-badge-card--teal\">\n"
            "      <img src=\"/images/hero-car.png\" alt=\"Nubenetes Car\"/>\n"
            "      <div class=\"hero-badge-title\">Get Started</div>\n"
            "      <div class=\"hero-badge-subtitle\">Introduction Guide</div>\n"
            "    </div>\n"
            "  </a>\n"
            "  <a href=\"./other-awesome-lists/\" style=\"text-decoration: none; color: inherit; display: block;\">\n"
            "    <div class=\"hero-badge-card hero-badge-card--gold\">\n"
            "      <img src=\"/images/awesome-lists-cover.svg\" alt=\"Awesome Lists\"/>\n"
            "      <div class=\"hero-badge-title\">Awesome Lists</div>\n"
            "      <div class=\"hero-badge-subtitle\">Curated awesome-* directory</div>\n"
            "    </div>\n"
            "  </a>\n"
            "</div>\n\n"
            "!!! abstract \"The High-Density Vision\"\n"
            "    The V2 Edition is a curated, high-density version of the Nubenetes archive. Using **Agentic AI Orchestration**, "
            "the system selects only the most relevant, stable, and impactful resources for the modern Cloud Native ecosystem (2026 and beyond).\n\n"
            f"{coverage_info}\n\n"
            # Altitude fix: surface the fresh, dynamic Trending/Digest BEFORE the
            # signature YouTube mosaic (which now closes the page as a brand showcase).
            "## Trending Now\n\n"
            f"{pulse_md}\n\n"
            "## The Cloud Native Universe We Track\n\n"
            f"<center markdown=\"1\">\n{mosaic_html}\n</center>\n\n"
            # Label Heatmap: full tag cloud sized by resource count, deep-linking
            # to the matching section on the Technical Tags page (cross-page).
            f"{index_heatmap}"
            "---\n\n"
            "**Reference:** [🗺️ Full Topic Map](./topic-map/) · "
            "[📐 Methodology &amp; Maturity Taxonomy](./methodology/) · "
            "[🎥 Agentic Video Hub](./videos/index.md)\n"
        )

        # Group by dimension (shared by the Topic Map directory page below).
        dim_groups = {}
        for f_name, info in data.items():
            dim_groups.setdefault(info["dim"], []).append(f_name)

        with open(os.path.join(V2_DIR, "index.md"), "w") as f:
            f.write(index_md)

        # --- Topic Map: full category directory in a multi-column grid -----------
        def _count_links(node):
            total = len(node.get("__links__", []))
            for k, v in node.items():
                if k != "__links__" and isinstance(v, dict):
                    total += _count_links(v)
            return total

        # Resource-density heatmap: a true colour matrix (distinct from the
        # size-based Label cloud on the index/Tags pages). One tile per category,
        # grouped by the same strategic dimensions as the directory below, with
        # tile warmth encoding how many AI-curated resources it holds. Counts span
        # ~1..160, so a LOG scale is used to avoid collapsing everything into the
        # lowest bucket. Six levels map onto .th-1..6.
        cat_counts = {f_name: _count_links(info["content"]) for f_name, info in data.items()}
        _all_counts = [c for c in cat_counts.values() if c > 0] or [1]
        _hmin, _hmax = math.log(min(_all_counts)), math.log(max(_all_counts))

        def _topic_heat(count):
            if count <= 0:
                return 1
            if _hmax == _hmin:
                return 3
            return 1 + round((math.log(count) - _hmin) / (_hmax - _hmin) * 5)  # 1..6

        heatmap_md = (
            "## Resource Density Heatmap\n\n"
            "Each tile is a category; the warmer the colour, the more AI-curated "
            "resources it holds. A fast read of where the Cloud Native ecosystem's "
            "depth concentrates — click any tile to open its page.\n\n"
            "<div class=\"topic-heatmap\">\n"
            "<div class=\"topic-heatmap__legend\">"
            "<span class=\"topic-heatmap__cap\">Fewer</span>"
            "<span class=\"topic-heatcell th-1\"></span>"
            "<span class=\"topic-heatcell th-2\"></span>"
            "<span class=\"topic-heatcell th-3\"></span>"
            "<span class=\"topic-heatcell th-4\"></span>"
            "<span class=\"topic-heatcell th-5\"></span>"
            "<span class=\"topic-heatcell th-6\"></span>"
            "<span class=\"topic-heatmap__cap\">More</span>"
            "</div>\n"
        )
        for dim in self.dimensions.keys():
            if dim not in dim_groups:
                continue
            heatmap_md += "<div class=\"topic-heatmap__row\">\n"
            heatmap_md += f"<div class=\"topic-heatmap__dim\">{dim}</div>\n"
            heatmap_md += "<div class=\"topic-heatmap__cells\">\n"
            for f in sorted(dim_groups[dim], key=lambda x: cat_counts[x], reverse=True):
                count = cat_counts[f]
                lvl = _topic_heat(count)
                slug = f[:-3] if f.endswith(".md") else f
                heatmap_md += (
                    f"<a class=\"topic-heatcell th-{lvl}\" href=\"/{slug}/\" "
                    f"title=\"{data[f]['title']} — {count} resources\">"
                    f"<span class=\"topic-heatcell__name\">{data[f]['title']}</span>"
                    f"<span class=\"topic-heatcell__n\">{count}</span></a>\n"
                )
            heatmap_md += "</div>\n</div>\n"
        heatmap_md += "</div>\n\n"

        topic_md = (
            "---\n"
            "description: \"The complete Nubenetes V2 directory: every curated Kubernetes, "
            "Cloud Native and DevOps category by strategic dimension, with resource counts.\"\n"
            "---\n"
            "# Topic Map\n\n"
            "!!! tip \"The complete Nubenetes V2 directory\"\n"
            "    Every curated category across all strategic dimensions, with the number of "
            "AI-selected resources in each. Looking for the landing page? Back to the "
            "[**2026 Vision**](/).\n\n"
            + heatmap_md +
            "## Full Category Directory\n\n"
            "<div class=\"topic-map-grid\" markdown=\"1\">\n\n"
        )
        for dim in self.dimensions.keys():
            if dim in dim_groups:
                topic_md += "<section class=\"topic-map-dim\" markdown=\"1\">\n\n"
                # h2 (not h3): the page H1 is "Topic Map", so dimensions must
                # increment by one level (markdownlint MD001). Also gives the
                # right-hand TOC a clean per-dimension index.
                topic_md += f"## {dim}\n\n"
                for f in sorted(dim_groups[dim]):
                    count = _count_links(data[f]["content"])
                    topic_md += f"- **[{data[f]['title']}](./{f})** <span class=\"topic-count\">{count}</span>\n"
                topic_md += "\n</section>\n\n"
        topic_md += "</div>\n"
        with open(os.path.join(V2_DIR, "topic-map.md"), "w") as f:
            f.write(topic_md)

        # --- Methodology: maturity taxonomy + technical impact reference ---------
        methodology_md = (
            "---\n"
            "description: \"How Nubenetes V2 classifies and ranks resources: the maturity "
            "taxonomy and technical impact (star) scoring used across the Elite portal.\"\n"
            "---\n"
            "# Methodology\n\n"
            "!!! abstract \"How Nubenetes V2 classifies and ranks resources\"\n"
            "    The reference legends below explain the maturity tags and the technical "
            "impact (star) scores applied to every resource in the portal.\n\n"
            "## The Maturity Taxonomy\n\n"
            "To ensure industrial-grade precision, every resource in V2 is classified using our proprietary 5-tier maturity system:\n\n"
            "| Tag | Description | Engineering Context |\n"
            "| :--- | :--- | :--- |\n"
            "| <a href=\"/tags/#de-facto-standard\"><span class=\"md-tag md-tag--success\">[DE FACTO STANDARD]</span></a> | The industry baseline. | Tools like Kubernetes, Terraform, or Prometheus that define the current architecture. |\n"
            "| <a href=\"/tags/#enterprise-stable\"><span class=\"md-tag md-tag--success\">[ENTERPRISE-STABLE]</span></a> | Battle-tested and reliable. | Proven solutions with strong community and commercial support. |\n"
            "| <a href=\"/tags/#emerging\"><span class=\"md-tag md-tag--warning\">[EMERGING]</span></a> | The cutting edge. | High-potential tools and patterns (e.g., AI Agents, MCP) shaping the future. |\n"
            "| <a href=\"/tags/#guide\"><span class=\"md-tag md-tag--secondary\">[GUIDE]</span></a> | Strategic knowledge. | High-quality tutorials, architectural deep-dives, and decision matrices. |\n"
            "| <a href=\"/tags/#case-study\"><span class=\"md-tag md-tag--secondary\">[CASE STUDY]</span></a> | Real-world evidence. | Practical implementations and architectural lessons from production environments. |\n"
            "| <a href=\"/tags/#community-tool\"><span class=\"md-tag md-tag--info\">[COMMUNITY-TOOL]</span></a> | Open-source ecosystem. | Valuable community-driven tools that enrich the ecosystem but may not have enterprise-grade support. |\n"
            "| <a href=\"/tags/#legacy\"><span class=\"md-tag md-tag--critical\">[LEGACY]</span></a> | Historical context. | Established tools that are being replaced or are primarily for maintaining older stacks. |\n"
            "| <a href=\"/tags/#spanish-content\"><span class=\"md-tag md-tag--warning\">[SPANISH CONTENT]</span></a> | Localized knowledge. | Resources in Spanish preserved for native speakers while indexed in English (Mandate 10). |\n\n"
            "## Technical Impact (Relevance Score)\n\n"
            "The stars accompanying each resource represent its **Technical Impact** and **Architectural Relevance** for a 2026 Senior Architect:\n\n"
            "| Impact | Level | Meaning | Visual Code |\n"
            "| :---: | :--- | :--- | :--- |\n"
            "| 🌟🌟🌟🌟🌟 | **Platinum Standard** | Critical industry foundation. Essential knowledge for any Cloud Native architecture. | `==[Highlighted Link]==` |\n"
            "| 🌟🌟🌟🌟 | **Gold Standard** | Highly recommended. Proven value and significant community/enterprise momentum. | `**[Bold Link]**` |\n"
            "| 🌟🌟🌟 | **Silver Standard** | Solid technical reference. Useful for specific use cases or established patterns. | Standard Link |\n"
            "| 🌟🌟 | **Bronze Standard** | Interesting alternative or niche tool. Good to have in the toolkit for specific scenarios. | Standard Link |\n"
            "| 🌟 | **Reference Only** | Basic documentation or historical reference without major current impact. | Standard Link |\n"
        )
        
        with open(os.path.join(V2_DIR, "methodology.md"), "w") as f: f.write(methodology_md)

        async def render_node(node, depth, base_slug, used_headers, is_intro=False):
            md = ""
            # Mandate: Process links at this level FIRST if they have NO further hierarchy
            # This handles links that are candidates but haven't been deeply classified yet (orphans)
            if "__links__" in node and depth == -1:
                orphan_links = node["__links__"]
                if orphan_links:
                    md += "## Standard Reference\n\n"
                    for l in orphan_links:
                        md += await self._render_single_link(l, is_intro)
                    md += "\n"

            for name, subnode in sorted(node.items()):
                if name == "__links__": continue
                clean_name = clean_toc_text(name)
                
                # Mandate 30: MD024 - Deduplicate headings to prevent Linter errors
                h_name = clean_name
                counter = 1
                while h_name in used_headers:
                    h_name = f"{clean_name} ({counter})"
                    counter += 1
                used_headers.add(h_name)
                
                slug = f"{base_slug}-{h_name.lower().replace(' ', '-')}"
                # MD025: Ensure only one H1. Main title is H1, so internal headers start at H2 (depth + 3)
                header_level = min(6, depth + 3) 
                md += f"{'#' * header_level} {h_name}\n\n"
                
                if depth == 1 and "__links__" in subnode: 
                    md += await self._generate_comparison_table(subnode["__links__"])
                
                md += await render_node(subnode, depth + 1, slug, used_headers, is_intro)
            
            if "__links__" in node and depth >= 0:
                for l in node["__links__"]:
                    md += await self._render_single_link(l, is_intro)
            return md

        for f_name, info in data.items():
            used_headers = {info['long_title']} # Mandate 30: MD024 - Pre-populate with H1 to avoid duplicates
            # Formulate V1 counterpart link dynamically
            v1_link = f"/v1/{f_name.replace('.md', '/')}"
            # Unique per-page SEO meta description (front-matter) so each page no
            # longer falls back to the identical global site_description. Material
            # emits it as <meta name="description"> + og:description. Enrich it with
            # the page's top resource names (long-tail keywords), filtering out
            # URL/path-like titles for readability; fall back to a clean template.
            def _collect_links(node, acc):
                if "__links__" in node:
                    acc.extend(node["__links__"])
                for _k, _v in node.items():
                    if _k != "__links__" and isinstance(_v, dict):
                        _collect_links(_v, acc)
                return acc
            _page_links = _collect_links(info["content"], [])
            _page_links.sort(key=lambda x: (-(x.get("stars") or 0), -(int(x["year"]) if str(x.get("year", "")).isdigit() else 0)))
            _names, _seen_names = [], set()
            for _l in _page_links:
                _nm = nuclear_strip(str(_l.get("title", "")))
                # Drop emojis/stars and edge punctuation that leak into titles.
                _nm = re.sub(r'[\U0001F000-\U0001FAFF☀-➿⭐⭕️]', '', _nm)
                _nm = re.sub(r'\s+', ' ', _nm).strip(" -–—·:|")
                _low = _nm.lower()
                if not (3 <= len(_nm) <= 26):
                    continue
                if "/" in _nm or "http" in _low or any(d in _low for d in (".com", ".io", ".org", ".net", ".dev", ".sh", ".ai", ".xyz")):
                    continue
                if _low in _seen_names:
                    continue
                _seen_names.add(_low)
                _names.append(_nm)
                if len(_names) >= 2:
                    break
            _seo_title = str(info.get('title') or info['long_title'])[:60].strip()
            if len(_names) >= 2:
                _seo_desc = (
                    f"Top {_seo_title} resources for 2026, AI-ranked: {', '.join(_names)} and more "
                    f"— curated Cloud Native tools, guides and references."
                )
            else:
                _seo_desc = (
                    f"Curated, AI-ranked {_seo_title} resources for the 2026 Cloud Native "
                    f"architect: top-tier tools, guides and references ({info['dim']})."
                )
            _seo_desc = _seo_desc.replace("\\", " ").replace('"', "'").replace("\n", " ").strip()
            if len(_seo_desc) > 165:
                _seo_desc = _seo_desc[:162].rsplit(" ", 1)[0].rstrip(" ,;:—-") + "."
            md = (
                f"---\n"
                f"description: \"{_seo_desc}\"\n"
                f"---\n"
                f"# {info['long_title']}\n\n"
                f"!!! tip \"Nubenetes V2 Elite Portal\"\n"
                f"    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**]({v1_link}).\n\n"
                f"!!! info \"Architectural Context\"\n"
                f"    Detailed reference for {info['long_title']} in the context of {info['dim']}.\n\n"
            )

            # Provider hub: surface the substantial sub-pages that remain after
            # consolidation so the landing page is a navigable index, not a stub.
            _hub_slug = f_name.replace(".md", "")
            if _hub_slug in self.subpage_hubs:
                _children = [
                    (c, lbl) for (c, lbl) in self.subpage_hubs[_hub_slug]
                    if (f"{c}.md" in data) or os.path.exists(os.path.join(V2_DIR, f"{c}.md"))
                ]
                if _children:
                    _child_links = " · ".join(f"[{lbl}](./{c}/)" for (c, lbl) in _children)
                    md += (
                        f"!!! abstract \"Deep-Dive Topic Pages\"\n"
                        f"    {_child_links}\n\n"
                    )

            # In-page Markdown Table of Contents intentionally omitted.
            # The MkDocs Material theme renders a native, sticky "On this page" TOC
            # (right sidebar) from the headings below, so a duplicated Markdown TOC
            # only added redundant scroll — extreme on large pages (e.g. 250+ links).
            # See v2-mkdocs.yml (toc.integrate removed) and static/v2_filter.js (?v=2.9.12).

            if f_name == "introduction.md":
                md += "## Vision 2026\n\n!!! quote \"The Evolution of Autonomy\"\n    From manual curation to agentic intelligence.\n\n### Ecosystem Map\n\n\n```mermaid\ngraph TD\n    A[Foundations] --> B[AI & Intelligence]\n    A --> C[Hardened Infra]\n    B --> D[Agentic Curation]\n    C --> E[Enterprise Stability]\n    D --> F[Nubenetes Portal]\n    E --> F\n```\n\n\n"

            if f_name == "about.md":
                md += (
                    "## The Nubenetes Engineering Manifest\n\n"
                    "!!! quote \"The Positive Sum Game\"\n"
                    "    ==*\"Open Source is most successful when is played as a positive sum game\" (Sarah Novotny)*==\n\n"
                    "<div class=\"video-embed-grid\">\n"
                    "  <div class=\"video-embed\"><iframe src=\"https://www.youtube-nocookie.com/embed/GZl7N8sXyEo\" title=\"Cowboy Bebop - Tank!\" loading=\"lazy\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe></div>\n"
                    "  <div class=\"video-embed\"><iframe src=\"https://www.youtube-nocookie.com/embed/t_hdOVsdRSE\" title=\"Jimmy Sax - Time\" loading=\"lazy\" frameborder=\"0\" allow=\"accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share\" allowfullscreen></iframe></div>\n"
                    "</div>\n\n"
                    "### 1. The Genesis: Munich 2018\n"
                    "Nubenetes was forged in the internals of a massive Cloud Native transformation for a **major multinational car manufacturer** in Munich. Coordinating hundreds of microservices, thousands of developers, and millions of end-users taught us a fundamental truth: **Standardization, Automation, and GitOps are not \"best practices\"—they are survival requirements.**\n\n"
                    "!!! quote \"The Standardization Thesis\"\n"
                    "    ==*\"Kubernetes is not for application development but for platform development. Its magic is in enterprise standardization, not app portability.\"*== — **[Kelsey Hightower](https://www.techrepublic.com/article/kubernetes-magic-is-in-enterprise-standardization-not-app-portability)**\n\n"
                    "    This is the core insight Nubenetes was built on. Kubernetes' real value is not app portability—it is a **standardized platform substrate** that lets an entire organization build on common ground, eliminating per-team snowflakes and person-dependent silos.\n\n"
                    "### 2. Our Engineering Philosophy\n"
                    "We reject technical obfuscation as a competitive advantage. Solutions that are \"the hard way\" by design do not scale and create fragile, person-dependent silos. \n\n"
                    "!!! abstract \"2.1. Correctness by Design\"\n"
                    "    We believe in doing DevOps correctly through the **GitOps pattern**. Automation without correctness is just faster failure. This architectural rigor ensures enterprise-grade stability at scale.\n\n"
                    "!!! abstract \"2.2. The Scientific Method\"\n"
                    "    We build bridges based on **evidence**, not politics or hype. If a solution cannot be empirically verified and automated, it is a liability. Engineers rely on evidence to solve problems.\n\n"
                    "#### 2.3. Anti-Bikeshining: Abstractions over Reinvention\n"
                    "We prioritize established frameworks and enterprise standards over ad-hoc, unmaintainable tooling. Reinventing the wheel is often a symptom of misaligned incentives in the IT sector.\n\n"
                    "#### 2.4. Avoiding Engineering Anti-Patterns\n"
                    "We combat the culture of **Promotion-Based Development (PBD)**, where complexity is manufactured for personal career visibility rather than business value. \n\n"
                    "  - [Promotion-Based Development: A Fast Track to Mediocrity](https://vadimkravcenko.com/shorts/promotion-based-development/) <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Dissects how rewarding \"shiny new things\" over battle-tested stability leads to fragile architectures.\n"
                    "  - [Reddit: The Reality of Promotion-Driven Development](https://www.reddit.com/r/ExperiencedDevs/comments/pw6vuv/promotion_driven_development) <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A raw, evidence-based discussion from senior engineers on the industry's most common misaligned incentives.\n\n"
                    "### 3. The Architectural North Star\n"
                    "We advocate for decoupled, maintainable architectures that survive the test of time and organizational growth.\n\n"
                    "  - [Domain-Driven Design (DDD) for Microservices](https://learn.microsoft.com/en-us/azure/architecture/microservices/model/domain-analysis) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The foundational blueprint for defining service boundaries based on business domains rather than technical layers.\n"
                    "  - [Hexagonal Architecture (Ports and Adapters)](https://medium.com/@sandeepsharmaster/modernize-your-cloud-microservices-apps-hexagonal-architecture-769696494c0) <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Decoupling the application core from external infrastructure (Databases, APIs, UI) to ensure high testability and vendor neutrality.\n\n"
                    "### 4. Comparative Maturity Framework\n\n"
                    "| Principle | Strategic Focus | Primary Toolset | Architectural Impact |\n"
                    "| :--- | :--- | :--- | :--- |\n"
                    "| **DevOps** | Automation & Frequency | CI/CD Pipelines | Operational Speed |\n"
                    "| **GitOps** | ==Correctness & Drift Control== | Git + Kubernetes | ==Enterprise Stability== |\n"
                    "| **SRE** | Reliability & Prevention | Observability | Scalable Quality |\n\n"
                    "#### 4.1. SRE vs. DevOps Responsibility Matrix\n\n"
                    "| **Site Reliability Engineer (SRE) team** | **Developers** | **Operations team** |\n"
                    "| :--- | :--- | :--- |\n"
                    "| Provide and teach effective use of platform tooling to empower developers to be self-sufficient | Treat SREs as application operation partners, not only as first responders to incidents | Provide self-service platform deployment and observability, and enable visibility into ramifications of actions |\n"
                    "| Document clear escalation paths for developers struggling in production | Turn to ops teams for the \"paved path\" or centralized developer control plane | Provide opinionated \"paved path\" platform or developer control plane (DCP), but allow developers to swap platform components if they also want to be accountable |\n\n"
                    "### 5. Strategic Standards and Cultural Shifts\n"
                    "Engineering excellence is as much about **culture** as it is about code. These foundational resources define the strategic landscape of modern Cloud Native organizations:\n\n"
                    "  - [The Agile Manifesto](https://agilemanifesto.org) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — The primary root of modern iterative development and the shift away from monolithic planning.\n"
                    "  - [Google: SRE vs. DevOps — Competing Standards or Close Friends?](https://cloud.google.com/blog/products/gcp/sre-vs-devops-competing-standards-or-close-friends) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An essential blueprint for understanding the symbiotic relationship between reliability engineering and delivery speed.\n"
                    "  - [The 4 Levels of GitOps Maturity](https://cloudnativenow.com/features/the-4-levels-of-gitops-maturity) <span class='md-tag md-tag--secondary'>[GUIDE]</span> — A roadmap for evolving from manual deployments to a fully automated, self-healing state.\n"
                    "  - [Necessary Culture Change with GitOps](https://itnext.io/necessary-culture-change-with-gitops-2c63f4fe9604) <span class='md-tag md-tag--secondary'>[CASE STUDY]</span> — Dissects the organizational friction and the necessary mindset shift required to adopt declarative infrastructure.\n\n"
                    "#### 5.1. Red Hat's Standardization Thesis\n"
                    "Industry momentum has aligned behind Kubernetes as the **de facto orchestration standard** for Linux® containers—choosing it means running the standard regardless of which cloud providers are in your future. The following perspectives, gathered in [Red Hat's approach to Kubernetes](https://www.redhat.com/en/solutions/kubernetes-approach), articulate why standardization—not novelty—is the strategic win:\n\n"
                    "| Insight | Source |\n"
                    "| :--- | :--- |\n"
                    "| *\"Given the difficulty of navigating the cloud-native ecosystem, especially the one around Kubernetes, there is a high demand for **easy-to-administer development platforms** that deliver applications in Kubernetes-managed containers.\"* | [OMDIA](https://www.redhat.com/en/solutions/kubernetes-approach) |\n"
                    "| *\"Choosing Kubernetes means you'll be running the **de facto standard** regardless of which cloud environments and providers are in your future.\"* | [CNCF Survey 2019](https://www.redhat.com/en/solutions/kubernetes-approach) |\n"
                    "| *\"It's not just enough to do Kubernetes. **You do need to do CI/CD.** You need to use alerting. You need to understand how the security model of the cloud and your applications interplay.\"* | [Clayton Coleman](https://www.redhat.com/en/solutions/kubernetes-approach) — Senior Distinguished Engineer, Red Hat |\n"
                    "| *\"Kubernetes is scalable. It helps develop applications faster. It does hybrid and multicloud. These are not just technology buzzwords, they're real, legitimate business problems.\"* | [Brian Gracely](https://www.redhat.com/en/solutions/kubernetes-approach) — Director, Product Strategy, Red Hat OpenShift |\n"
                    "| *\"Our job is to **make it easier and easier to use**, either from an ops point of view or a developer point of view—while acknowledging it is complex, because we're solving a complex problem.\"* | [Chris Wright](https://www.redhat.com/en/solutions/kubernetes-approach) — Chief Technology Officer, Red Hat |\n\n"
                    "### 6. Scaling with Evidence: DORA and Value Streams\n"
                    "We advocate for data-driven engineering management to avoid the trap of \"gut-feeling\" decision making.\n\n"
                    "  - [Driving DevOps with Value Stream Management](https://www.infoq.com/articles/DevOps-value-stream) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Dissects how to align microservice delivery with business outcomes through flow metrics.\n"
                    "  - [Better Metrics for Building High Performance Teams](https://www.infoq.com/articles/better-metrics-team-performance) <span class='md-tag md-tag--warning'>[EMERGING]</span> — Beyond LOC and commits: using DORA metrics to cultivate a culture of systemic stability.\n\n"
                    "### 7. Technical Leadership and The 'Glue' Factor\n"
                    "True seniority is measured by the ability to hold teams together through communication and shared context.\n\n"
                    "  - [Being Glue](https://noidea.dog/glue) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — An industry-standard analysis of the essential, non-coding technical tasks that ensure project success.\n"
                    "  - [How Big Tech Runs Tech Projects](https://blog.pragmaticengineer.com/project-management-at-big-tech) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — A seminal critique of ceremonial Scrum versus result-oriented engineering pragmatism.\n"
                    "  - [Martin Fowler: Retrospectives Antipatterns](https://martinfowler.com/articles/retrospective-antipatterns.html) <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Essential guide for transforming team feedback loops from blame games into architectural improvement cycles.\n\n"
                    "### 8. Meritocracy and Careers in 2026\n"
                    "We advocate for a technical sector where quality and evidence-based decisions take precedence over corporate politics.\n\n"
                    "  - [HBR: Stop Hiring for Culture Fit](https://hbr.org/2019/11/stop-hiring-for-culture-fit) <span class='md-tag md-tag--warning'>[EMERGING]</span> — A critical perspective on how \"culture fit\" often hides bias and hinders technical innovation.\n"
                    "  - [Defining Day-2 Operations](https://dzone.com/articles/defining-day-2-operations) <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Shifts the focus from the excitement of the first deployment to the long-term reality of maintaining production stability.\n\n"
                    "#### 8.1. Automation Anxiety\n"
                    "A human barrier to adoption deserves naming. Sysadmins and engineers may carry a personal fear about adopting automation, since much of their typical day revolves around the very manual tasks and processes that automation promises to eliminate. **Automation anxiety** is the fear that if these tasks can be handled by automated tools, there will no longer be any reason to keep a person in that role—and nobody likes being automated out of a job.\n\n"
                    "This fear is largely unfounded, however: automating manual tasks **frees up people's time** that can instead be spent on more innovative, more strategic, and higher-value projects. The cattle service model does not eliminate engineers—it elevates them from repetitive operators to platform builders.\n\n"
                    "### 9. The 2026 Vision: Agentic Intelligence\n"
                    "Nubenetes has evolved from a historical manual archive into an **Agentic Knowledge Graph**. \n\n"
                    "#### 9.1. V1 Archive (Exhaustive)\n"
                    "Preserves historical context, the original curator's voice, and every technically valid link discovered since 2018. It serves as the foundational truth for the entire ecosystem.\n\n"
                    "#### 9.2. V2 Elite Portal (Distilled)\n"
                    "An O'Reilly-style technical library where 18k+ resources are filtered, ranked by impact, and enriched with AI-driven architectural summaries for high-speed reference.\n\n"
                    "### 10. DevOps Demystified: Role Ambiguity and the OpsDev Pivot\n"
                    "DevOps has suffered significant semantic dilution, often misused as a catch-all role. We define DevOps as the engineering of pipelines and Infrastructure as Code (IaC) using standard tooling under a **cattle service model**, rather than ad-hoc script-writing or monitoring development. A DevOps specialist is not a general full-stack developer who handles QA and Ops on the side. To eliminate confusion, the term **OpsDev** is often a more accurate representation of this infrastructure-first engineering discipline.\n\n"
                    "### 11. The Certification Trap vs. Empirical Skill\n"
                    "While certifications like CKA are prominent on CVs, they are frequently utilized by recruiters as an artificial filter. True engineering value is built by doing—writing automated, testable, and declarative GitOps pipelines, rather than mastering manual CLI execution. Relying purely on certifications often encourages memorizing exam patterns over learning design abstractions. Seniority is measured by empirical evidence and day-2 operational stability, not exam certificates.\n\n"
                    "> *\"I am a big fan of the scientific method. Engineers do not build bridges from a right or left perspective... hello! I have a problem, can you help me? Engineers rely on evidence.\"* — **Mark Stevenson**\n\n"
                    "---\n\n"
                )


            _body = await render_node(info["content"], -1, f_name.replace(".md", ""), used_headers, is_intro=(f_name=="introduction.md" or f_name=="about.md"))
            
            if f_name == "jenkins.md":
                dsl_injection = """
!!! info "Jenkins Configuration as Code (CasC) Architectural Reference"
    To design a robust, modern, and reproducible Jenkins infrastructure in 2026, you must understand the distinction and interplay between the three complementary Configuration-as-Code layers.
    
    ### 1. The Controller Layer: [Jenkins Configuration as Code (JCasC)](https://plugins.jenkins.io/configuration-as-code)
    Managing the controller's settings, plugin installations, and credentials via the web UI creates operational snowflakes. JCasC solves this by defining the entire controller configuration in declarative YAML files.
    - **Key Resources**:
        - [Official JCasC Plugin 🌟](https://plugins.jenkins.io/configuration-as-code) — The entry point for declaring your Jenkins configuration in YAML.
        - [Example of JCasC for Kubernetes 🌟](https://github.com/figaw/configuration-as-code-jenkins-k8s) — A practical bootstrap reference.
        - [Read-only Jenkins Configuration 🌟](https://www.jenkins.io/blog/2020/05/25/read-only-jenkins-announcement/) — Lock down the UI configuration screens using JEP-224 to enforce CasC immutability.
    
    ### 2. The Job Generation Layer: [Job DSL Plugin](https://plugins.jenkins.io/job-dsl)
    If you have hundreds of repositories, manually creating Jenkins jobs is non-viable. The Job DSL plugin allows you to describe Jenkins jobs programmatically using a Groovy-based DSL.
    - **Key Resources**:
        - [Job DSL Plugin 🌟](https://plugins.jenkins.io/job-dsl) — Programmatic job generation.
        - [Jenkins Job DSL API Reference 🌟](https://jenkinsci.github.io/job-dsl-plugin) — Comprehensive API reference documentation.
        - [Guide: Jenkins Jobs as Code with Groovy DSL 🌟](https://tech.gogoair.com/jenkins-jobs-as-code-with-groovy-dsl-c8143837593a) — A step-by-step introduction.
    
    ### 3. The Pipeline Execution Layer: [Jenkins Declarative Pipeline](https://www.jenkins.io/solutions/pipeline)
    The execution steps of your build, test, and deploy pipeline belong in the application repository. The `Jenkinsfile` defines this using the Declarative Pipeline syntax, which provides a structured, version-controlled delivery flow.
    - **Key Resources**:
        - [Pipeline as Code with Jenkins 🌟](https://www.jenkins.io/solutions/pipeline) — Conceptual overview.
        - [Jenkinsfile Syntax Book 🌟](https://www.jenkins.io/doc/book/pipeline/jenkinsfile) — Official syntax and grammar reference.
        - [DZone Refcard: Declarative Pipeline with Jenkins 🌟](https://dzone.com/refcardz/declarative-pipeline-with-jenkins) — Quick reference sheet.
        - [Dzone Refcard: Continuous Delivery with Jenkins Pipeline 🌟](https://dzone.com/refcardz/continuous-delivery-with-jenkins-pipeline) — CD workflow design.

    ### 4. The Visual/User Interface Layer: [Pipeline Graph View Plugin](https://plugins.jenkins.io/pipeline-graph-view)
    With the official deprecation of the Blue Ocean plugin, the Pipeline Graph View plugin is the de-facto standard for interactive pipeline visualizations directly embedded in the native Jenkins UI.
    - **Key Resources**:
        - [Pipeline Graph View Plugin 🌟](https://plugins.jenkins.io/pipeline-graph-view) — The modern interactive UI to view execution graphs and stages.
        - [pipeline-graph-view-plugin repository 🌟](https://github.com/jenkinsci/pipeline-graph-view-plugin) — Open-source repository for the Pipeline Graph View project.

    ---
    💡 **Architectural Recommendation**: Use **JCasC** to set up the controller, **Job DSL** to generate your multibranch pipeline jobs automatically, and a **Declarative Jenkinsfile** inside each repo to define the build steps. Enrich the visual feedback loop by deploying the **Pipeline Graph View Plugin**, and lock the UI down to read-only mode to prevent configuration drift.
"""
                _body = _body.replace("### Configuration As Code\n\n", f"### Configuration As Code\n{dsl_injection}\n")
                
                pipeline_code_injection = """
!!! info "[Pipeline as Code with Jenkins: Architectural Core Principles](https://www.jenkins.io/solutions/pipeline)"
    As defined in the official [Jenkins Pipeline Book](https://www.jenkins.io/doc/book/pipeline), Jenkins is fundamentally an automation engine that supports diverse delivery patterns. Modeling your delivery workflow as a **Pipeline** adds a powerful set of automation capabilities:
    
    *   **Code**: Pipelines are implemented directly in code (usually a `Jenkinsfile`) and checked into version control, enabling peer code reviews and auditability.
    *   **Durable**: Pipelines are built to survive both planned and unplanned restarts of the Jenkins controller.
    *   **Pausable**: Pipelines can pause execution to wait for human approval or input before proceeding to deployment.
    *   **Versatile**: They naturally support complex real-world CD topologies, including parallel execution, looping, and fork/join patterns.
    *   **Extensible**: The Pipeline [DSL](https://en.wikipedia.org/wiki/Domain-specific_language) supports custom extensions (e.g., Shared Libraries) and integrations with external plugins.

!!! info "[Jenkins Pipeline Best Practices: Declarative, Scripted, and Shared Libraries](https://www.cloudbees.com/blog/top-10-best-practices-jenkins-pipeline-plugin)"
    Based on CloudBees' strategic guide: [Top 10 Jenkins Pipeline Best Practices](https://www.cloudbees.com/blog/top-10-best-practices-jenkins-pipeline-plugin):
    
    *   **Prefer Declarative Syntax**: Declarative syntax (introduced in 2017) is the modern standard. Many advanced features—such as matrix builds—are exclusively available in Declarative. Avoid legacy Scripted syntax (2014) unless absolutely necessary.
    *   **Use Shared Libraries to Avoid Inline Scripts**: Using `script` tags inside a Declarative pipeline is an anti-pattern. Instead of inline Groovy scripting, encapsulate complex logic as custom steps inside a version-controlled **Shared Library**.
    *   **Do Not Treat Shared Libraries as General Programming Projects**: Pipelines should only orchestrate CI tasks, not run complex business logic. Heavy computations or scripting inside a Shared Library execute on the Jenkins controller (master) rather than the build agents, causing severe memory leaks and performance bottlenecks.
    *   **Scripted Syntax Fallback**: Only resort to Scripted syntax when a task cannot be achieved using a combination of Declarative syntax and a custom Shared Library step.
    *   **Declarative inside Shared Libraries**: **Shared-libraries with scripted pipeline syntax are not recommended** since more custom coding involves more maintenance issues. Use **Declarative Pipeline Syntax** as much as possible inside your libraries.


!!! info "[Building Declarative Pipelines with OpenShift: Jenkinsfile as Code and Syntax Structures](https://www.redhat.com/en/blog/building-declarative-pipelines-openshift-dsl-plugin)"
    As detailed in Red Hat's engineering guide: [Building Declarative Pipelines with OpenShift DSL Plugin](https://www.redhat.com/en/blog/building-declarative-pipelines-openshift-dsl-plugin):
    
    *   **Jenkinsfiles as the De-Facto Standard**: Since Jenkins 2, Jenkinsfiles have quickly become the **de-facto standard for building continuous delivery pipelines**, allowing teams to track, review, audit, and manage the pipeline lifecycle inside source version control just like application code.
    *   **Scripted vs. Declarative Execution**: While the Groovy-based **scripted syntax** was the default in Jenkins 2, the **declarative syntax** (introduced in Jenkins 2.5) offers a simplified way to control all pipeline aspects. Ultimately, **both syntaxes translate to the same execution blocks** in Jenkins and achieve the same result.
    *   **Structure of Declarative Pipelines**: In its simplest form, a declarative pipeline is composed of an **`agent`** (defining the build executor/slave) and a series of **`stages`**, with each stage containing the specific **`steps`** to be executed.
"""
                _body = _body.replace("## CICD\n\n", f"## CICD\n{pipeline_code_injection}\n")
                
                _body = _body.replace(
                    "#### Docker Deployment\n\n",
                    "#### Docker Deployment\n\n"
                    "  - **[Official Jenkins Docker Image](https://github.com/jenkinsci/docker)** <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official Docker templates and build scripts for Jenkins controllers.\n"
                    "  - **[jenkins-in-docker Swarm Cluster setup](https://github.com/shazChaudhry/docker-jenkins)** <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — A reference setup demonstrating how to run scalable Jenkins workers inside a Docker Swarm environment.\n"
                )
                
                _body = _body.replace(
                    "#### Kubernetes Operators\n\n",
                    "#### Kubernetes Operators\n\n"
                    "  - **[Kubernetes Native Jenkins Operator](https://github.com/jenkinsci/kubernetes-operator)** <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Fully-featured Kubernetes Operator to manage Jenkins controllers declaratively.\n"
                    "  - **[Jenkins Operator documentation](https://jenkinsci.github.io/kubernetes-operator/)** <span class='md-tag md-tag--primary'>[DOCUMENTATION]</span> — Setup, configuration, backup and restore guides for Jenkins Operator.\n"
                )

                _body = _body.replace(
                    "#### Security and Hardening\n\n",
                    "#### Security and Hardening\n\n"
                    "  - **[Jenkins Security Guide](https://www.jenkins.io/doc/book/security/)** <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Official hardening guide for configuring access control, credentials, protocols, and plugins safely.\n"
                    "  - **[OWASP Jenkins Security Assessment](https://owasp.org/www-project-integration-standards/writeups/jenkins/)** <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Threat modeling and vulnerability checks to secure CI/CD pipelines.\n"
                )

                _body = _body.replace(
                    "#### Helm Deployments\n\n",
                    "#### Helm Deployments\n\n"
                    "  - **[Official Red Hat Jenkins Image for OpenShift](https://github.com/openshift/jenkins)** <span class='md-tag md-tag--success'>[DE FACTO STANDARD]</span> — Red Hat's official repository containing container image templates, configurations, and plugins customized for OpenShift.\n"
                    "  - **[Deploy Helm charts with Jenkins on OpenShift 4](https://developers.redhat.com/articles/2021/05/24/deploy-helm-charts-jenkins-cicd-red-hat-openshift-4)** <span class='md-tag md-tag--secondary'>[GUIDE]</span> — Practical Red Hat tutorial demonstrating Helm deployment orchestration within Jenkins pipelines on OpenShift.\n"
                )

                _body = _body.replace(
                    "#### Troubleshooting\n\n",
                    "#### Troubleshooting\n\n"
                    "  - **[CloudBees: Troubleshooting Jenkins Performance](https://support.cloudbees.com/hc/en-us/articles/204856094-Troubleshooting-Jenkins-Performance)** <span class='md-tag md-tag--success'>[ENTERPRISE-STABLE]</span> — Exhaustive reference for debugging heap usage, thread dumps, garbage collection pauses, and pipeline serialization bottlenecks.\n"
                    "  - **[Jenkins Health Advisor by CloudBees](https://plugins.jenkins.io/jenkins-health-advisor-by-cloudbees/)** <span class='md-tag md-tag--info'>[COMMUNITY-TOOL]</span> — Automatically scans Jenkins controllers for known issues, security vulnerabilities, and performance anomalies.\n"
                )
                
                media_section = """
## Curated Slides and Videos

??? note "Jenkinsfile Runner slides. Click to expand!"

    <center markdown="1">

    <script async class="speakerdeck-embed" data-id="c8dea2f5571a4067868401e4316382af" data-ratio="1.77777777777778" src="https://speakerdeck.com/assets/embed.js" data-host="speakerdeck.com"></script>

    </center>

??? note "Cloudbees Flow Videos. Click to expand!"

    <center markdown="1">

    <iframe width="560" height="315" src="https://www.youtube.com/embed/tuhGzaQx8gY" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    <iframe width="560" height="315" src="https://www.youtube.com/embed/4RFlwU9klQ8" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

    </center>
"""
                _body += media_section
                
                # Permanent Safeguard Validation (Mandate check)
                # Enforce that critical callout injections were successfully merged and did not fail silently due to heading schema drift.
                assert "Jenkins Configuration as Code (CasC) Architectural Reference" in _body, "Safety assertion failed: JCasC callout injection was skipped in V2 jenkins.md!"
                assert "Pipeline as Code with Jenkins: Architectural Core Principles" in _body, "Safety assertion failed: Jenkins Pipeline principles callout was skipped in V2 jenkins.md!"
                assert "Jenkins Pipeline Best Practices" in _body, "Safety assertion failed: Jenkins Pipeline best practices callout was skipped in V2 jenkins.md!"
                assert "Building Declarative Pipelines with OpenShift" in _body, "Safety assertion failed: OpenShift pipeline callout was skipped in V2 jenkins.md!"
            # The flagship "Awesome Lists" page gets a high-impact hero + a grid
            # of its categories (auto-derived from the rendered H2 sections).
            if f_name == "other-awesome-lists.md":
                try:
                    md += build_awesome_lists_header(_body)
                except Exception as e:
                    log_event(f"[WARN] awesome-lists header failed: {str(e)[:100]}")
            md += _body

            # Add Semantic "See Also" — same dimension + cross-dimension by shared tags
            same_dim = [f for f in data if f != f_name and data[f]["dim"] == info["dim"]]
            cross_dim = []
            if info.get("content") and isinstance(info["content"], dict):
                page_tags = set()
                for node_links in self._collect_tags_from_tree(info["content"]):
                    page_tags.update(node_links)
                if page_tags:
                    for f in data:
                        if f != f_name and data[f]["dim"] != info["dim"]:
                            other_tags = set()
                            if isinstance(data[f].get("content"), dict):
                                for t in self._collect_tags_from_tree(data[f]["content"]):
                                    other_tags.update(t)
                            if page_tags & other_tags:
                                cross_dim.append(f)
            related = [f"[{data[f]['title']}](./{f})" for f in same_dim[:3]]
            cross = [f"[{data[f]['title']}](./{f})" for f in cross_dim[:2]]
            if related or cross:
                md += "\n---\n"
                if related:
                    md += f"💡 **Explore Related:** {' | '.join(related)}\n\n"
                if cross:
                    md += f"🔗 **See Also:** {' | '.join(cross)}\n\n"
            
            # Smart Write: Only update disk if content changed
            target_path = os.path.join(V2_DIR, f_name)
            existing_content = ""
            if os.path.exists(target_path):
                with open(target_path, "r") as f: existing_content = f.read()
            
            if md != existing_content:
                with open(target_path, "w") as f: f.write(md)

    def _aggregate_tags(self, v2_structure: Dict[str, Dict]):
        """Collect every active resource's tags into deterministic, slug-stable
        metadata shared by the Technical Tags page and the index Label Heatmap.

        Returns (sorted_tags, tag_meta, by_tag) where tag_meta[tag] holds
        ``display``, ``slug``, ``count`` and ``kind`` (maturity | language |
        domain). The slug logic is identical to (and deterministic with) what the
        Tags page renders, so the heatmap on the index can deep-link to the right
        ``/tags/#slug`` section even though it is generated in a separate pass.
        """
        active_links = {}
        def collect_links(node):
            if "__links__" in node:
                for l in node["__links__"]:
                    active_links[normalize_url(l["url"])] = l
            for k, v in node.items():
                if k != "__links__" and isinstance(v, dict):
                    collect_links(v)

        for f_name, info in v2_structure.items():
            collect_links(info["content"])

        # Group by tags
        by_tag = {}
        for l in active_links.values():
            tags_to_process = list(l.get("tags", []))
            # Include language indexing for non-English resources (Mandate 10)
            lang = l.get("language") or "English"
            # Skip non-language values the AI sometimes emits, so the tag index
            # is not polluted with meaningless "X Content" buckets.
            _lang_junk = {
                "english", "en", "n/a", "na", "none", "null", "unknown", "",
                "not applicable", "multiple", "multi-language", "polyglot", "various",
            }
            if lang.lower() in ["spanish", "es", "english/spanish"]:
                tags_to_process.append("[SPANISH CONTENT]")
            elif lang.lower() not in _lang_junk:
                tags_to_process.append(f"[{lang.upper()} CONTENT]")

            for t in tags_to_process:
                by_tag.setdefault(t, []).append(l)

        # Sort tags
        standard_order = [
            "[DE FACTO STANDARD]",
            "[ENTERPRISE-STABLE]",
            "[EMERGING]",
            "[GUIDE]",
            "[CASE STUDY]",
            "[COMMUNITY-TOOL]",
            "[LEGACY]",
            "[SPANISH CONTENT]"
        ]

        sorted_tags = [st for st in standard_order if st in by_tag]
        sorted_tags.extend(sorted(t for t in by_tag.keys() if t not in standard_order))

        # Precompute display name + UNIQUE slug for every tag, shared by both the
        # grouped TOC and the section headers so anchors always match. This fixes
        # collisions where C / C# / C++ all slugged to "c-content" (broken links).
        def _tag_display(tag):
            d = tag.replace("[", "").replace("]", "").replace("&", "and").title()
            if d.upper() in ["EBPF", "WASM", "GITOPS", "IAC", "SRE", "AI", "MCP", "DB", "MLOPS"]:
                d = d.upper()
            return d

        _seen_slugs = set()
        def _tag_slug(tag):
            s = tag.replace("[", "").replace("]", "").lower()
            s = s.replace("#", "-sharp").replace("++", "-plus-plus").replace("&", "-and-").replace("/", "-")
            s = re.sub(r'[^a-z0-9-]', '-', s)
            s = re.sub(r'-+', '-', s).strip('-')
            base, n = s, 1
            while s in _seen_slugs:
                n += 1
                s = f"{base}-{n}"
            _seen_slugs.add(s)
            return s

        def _tag_kind(tag):
            if tag in standard_order:
                return "maturity"
            if tag.endswith("CONTENT]"):
                return "language"
            return "domain"

        tag_meta = {
            tag: {
                "display": _tag_display(tag),
                "slug": _tag_slug(tag),
                "count": len(by_tag[tag]),
                "kind": _tag_kind(tag),
            }
            for tag in sorted_tags
        }
        return sorted_tags, tag_meta, by_tag

    def _render_tag_heatmap(self, sorted_tags, tag_meta, href_base: str = "", intro: str = None) -> str:
        """Confluence-style "popular labels" Label Heatmap: every label is listed
        alphabetically and sized/coloured by how many resources carry it, so the
        most-used tags read biggest/warmest. Sizing uses a LOG scale because counts
        span ~1..2800; a linear scale would collapse everything except the few giant
        maturity tags into the smallest bucket. Six levels map onto .v2-heat-1..6.

        ``href_base`` is prefixed before each ``#slug`` so the same cloud can live on
        the Tags page (same-page anchors, "") or the index (cross-page, "/tags/").
        """
        counts = [tag_meta[t]["count"] for t in sorted_tags]
        if not counts:
            return ""
        lmin, lmax = math.log(min(counts)), math.log(max(counts))

        def _heat_level(count):
            if lmax == lmin:
                return 3
            return 1 + round((math.log(count) - lmin) / (lmax - lmin) * 5)  # 1..6

        if intro is None:
            intro = (
                "Bigger, warmer labels cover more resources. "
                "Click any label to jump to its section below."
            )
        md = f"## Label Heatmap\n\n{intro}\n\n"
        md += '<div class="v2-tag-heatmap">\n'
        for t in sorted(sorted_tags, key=lambda x: tag_meta[x]["display"].lower()):
            m = tag_meta[t]
            disp = m["display"].replace(" Content", "")
            lvl = _heat_level(m["count"])
            md += (
                f'<a class="v2-heat-tag v2-heat-{lvl}" href="{href_base}#{m["slug"]}" '
                f'title="{m["count"]} resources">{disp}'
                f'<span class="v2-heat-n">{m["count"]}</span></a>\n'
            )
        md += "</div>\n\n"
        return md

    async def _generate_global_tag_index(self, v2_structure: Dict[str, Dict]):
        sorted_tags, tag_meta, by_tag = self._aggregate_tags(v2_structure)

        md = (
            "# Technical Tags Index\n\n"
            "!!! tip \"Nubenetes V2 Elite Portal\"\n"
            "    You are browsing the AI-Curated V2 Elite Edition. Looking for the exhaustive list of references? Check out the [**V1 Historical Archive**](/v1/).\n\n"
            "!!! info \"Universal Tag Index\"\n"
            "    Browse all V2 resources grouped by maturity levels and technical domains.\n\n"
        )

        def _count_label(n):
            return f"{n} resource" + ("" if n == 1 else "s")

        # Partition custom tags: language/format ("X CONTENT") vs technical domains,
        # so the long, low-signal language tail does not bury the maturity tags.
        maturity_tags = [t for t in sorted_tags if tag_meta[t]["kind"] == "maturity"]
        lang_tags = sorted(
            [t for t in sorted_tags if tag_meta[t]["kind"] == "language"],
            key=lambda t: -tag_meta[t]["count"],
        )
        other_tags = sorted(
            [t for t in sorted_tags if tag_meta[t]["kind"] == "domain"],
            key=lambda t: -tag_meta[t]["count"],
        )

        # Label Heatmap at the top of the Tags page (same-page anchors).
        md += self._render_tag_heatmap(sorted_tags, tag_meta, href_base="")

        # Build a grouped TOC: maturity as a clean numbered list; domains and the
        # language/format tail as compact, count-sorted inline pill rows.
        md += "## Table of Contents\n\n"
        if maturity_tags:
            md += "### Maturity and Quality\n\n"
            for t in maturity_tags:
                m = tag_meta[t]
                md += f"1. [{m['display']}](#{m['slug']}) ({_count_label(m['count'])})\n"
            md += "\n"
        if other_tags:
            md += "### Technical Domains\n\n"
            md += " · ".join(
                f"[{tag_meta[t]['display']}](#{tag_meta[t]['slug']}) ({tag_meta[t]['count']})"
                for t in other_tags
            ) + "\n\n"
        if lang_tags:
            md += "### Language and Format\n\n"
            md += "Resources indexed by their primary source language or document format.\n\n"
            md += " · ".join(
                f"[{tag_meta[t]['display'].replace(' Content', '')}](#{tag_meta[t]['slug']}) ({tag_meta[t]['count']})"
                for t in lang_tags
            ) + "\n\n"

        for tag in sorted_tags:
            m = tag_meta[tag]
            tag_display = m["display"]
            # Wrap section inside a .v2-tag-section div and details block for performance.
            # Explicit {#slug} keeps the heading anchor unique and TOC-matching.
            md += f"<div class=\"v2-tag-section\" markdown=\"1\">\n\n"
            md += f"## {tag_display} {{#{m['slug']}}}\n\n"
            total_count = len(by_tag[tag])
            if total_count > 100:
                summary_text = f"Click to view top 100 of {total_count} resources under {tag_display}"
            else:
                summary_text = f"Click to view {total_count} resources under {tag_display}"
            
            md += f"<details markdown=\"1\">\n"
            md += f"<summary>{summary_text}</summary>\n\n"
            
            # Sort links under this tag by impact stars and then by year
            sorted_links = sorted(by_tag[tag], key=lambda x: (-(x.get("stars") or 1), -(int(x["year"]) if str(x.get("year", "")).isdigit() else 0)))
            
            rendered_links = sorted_links[:100]
            for l in rendered_links:
                md += self._render_compact_tag_link(l)
            
            if total_count > 100:
                md += f"\n*... and {total_count - 100} more resources. For the full exhaustive list, search the [V1 Historical Archive](/v1/).*\n"
            else:
                md += "\n"
            md += f"</details>\n\n"
            md += f"</div>\n\n"

        target_path = os.path.join(V2_DIR, "tags.md")
        
        # Smart Write
        existing_content = ""
        if os.path.exists(target_path):
            with open(target_path, "r") as f: existing_content = f.read()
        if md != existing_content:
            with open(target_path, "w") as f: f.write(md)

    async def _sync_enterprise_navigation(self, data: Dict[str, Dict]) -> bool:
        try:
            with open("v2-mkdocs.yml", "r") as f: content = f.read()
            nav = [
                "nav:",
                "  - \"🔙 Back to V1 (Exhaustive)\": https://nubenetes.com/v1/",
                "  - \"The 2026 Vision\": index.md",
                # Flagship: the curated Awesome Lists directory, promoted to a
                # prominent top-level entry (also surfaced in Portal Guide below).
                "  - \"⭐ Awesome Lists\": other-awesome-lists.md",
                # Portal Guide: collapsible hub for the site-orientation / meta
                # pages — the topic directory, how the portal is curated, the tag
                # index and the project About. about.md and other-awesome-lists.md
                # are pulled out of their dimension here (see _FIXED_PAGES below).
                "  - \"Portal Guide\":",
                "    - \"Topic Map\": topic-map.md",
                "    - \"Awesome Lists\": other-awesome-lists.md",
                "    - \"Methodology\": methodology.md",
                "    - \"Technical Tags\": tags.md",
                "    - \"About\": about.md",
                # Videos: prominent top-level dropdown, kept high in the nav with
                # its category subpages as children.
                "  - \"Agentic Video Hub\":",
                "    - videos/index.md",
                "    - \"AI Agents and MCP\": videos/ai-agents.md",
                "    - \"DevOps, IaC, and SRE\": videos/devops-iac.md",
                "    - \"Cloud Native Core\": videos/cloud-native.md",
                "    - \"Fundamentals\": videos/fundamentals.md",
                "  - \"Intelligence Digest\":",
                "    - \"Tech & Cloud Digest\": tech-digest.md",
                "    - \"Industry & Geo Digest\": industry-digest.md"
            ]

            # Topic pages promoted into a fixed header group above; skip them in
            # the dimension loop so they are not also listed under their dimension.
            _FIXED_PAGES = {"about.md", "other-awesome-lists.md"}

            dim_groups = {}
            for f_name, info in data.items():
                dim_groups.setdefault(info["dim"], []).append(f_name)

            for dim in self.dimensions.keys():
                if dim in dim_groups:
                    dim_files = [f for f in sorted(dim_groups[dim]) if f not in _FIXED_PAGES]
                    if not dim_files:
                        continue
                    dim_nav = [f"  - \"{dim}\":"]
                    for f in dim_files:
                        dim_nav.append(f"    - \"{data[f]['title']}\": {f}")
                    nav.extend(dim_nav)

            # Replace only the nav section (from 'nav:' to end of file)
            # Use a marker to ensure we don't accidentally eat extra_css etc.
            if "nav:" not in content:
                log_event("[WARN] _sync_enterprise_navigation: 'nav:' not found in v2-mkdocs.yml")
                return False
            nav_start = content.index("nav:")
            updated = content[:nav_start] + "\n".join(nav) + "\n"
            with open("v2-mkdocs.yml", "w") as f: f.write(updated)
            log_event(f"  [OK] Nav synced: {len(nav)} entries written")
            return True
        except Exception as e:
            log_event(f"[WARN] sync enterprise navigation: {str(e)[:100]}")
            return False

import argparse
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--render-only", action="store_true")
    args = parser.parse_args()

    engine = V2VisionEngine(render_only=args.render_only)
    asyncio.run(engine.analyze_and_cluster())
    
    # --- PLATINUM GITOPS REPORTING (Multi-Comment) ---
    from src.gitops_manager import RepositoryController
    from src.config import TARGET_REPO
    
    # 1. High-Density Metrics Calculation
    total_v1_links = len(engine.inventory)
    v2_links_all = [dict(meta, url=url) for url, meta in engine.inventory.items() if isinstance(meta, dict) and meta.get("v2_locations")]
    total_v2_links = len(v2_links_all)
    
    # Coverage Metrics (Mandate: Transparency in Knowledge Discovery)
    enriched_v2 = [l for l in v2_links_all if l.get('hierarchy') or l.get('ai_summary')]
    total_enriched = len(enriched_v2)
    coverage_pct = round((total_enriched / total_v2_links) * 100, 2) if total_v2_links > 0 else 0
    
    # GitHub Metadata Coverage
    gh_links = [l for l in v2_links_all if "github.com" in str(l.get('url', ''))]
    total_gh = len(gh_links)
    gh_with_metadata = len([l for l in gh_links if l.get('gh_stars') is not None])
    gh_coverage_pct = round((gh_with_metadata / total_gh) * 100, 2) if total_gh > 0 else 0
    
    # Delta & Efficiency
    density_ratio = round((total_v2_links / total_v1_links) * 100, 2) if total_v1_links > 0 else 0
    reduction_delta = total_v1_links - total_v2_links
    
    # Maturity Distribution
    maturity_counts = {}
    for l in v2_links_all:
        tags = l.get('tags', ['[COMMUNITY-TOOL]'])
        for tag in tags:
            maturity_counts[tag] = maturity_counts.get(tag, 0) + 1

    # 2. Document Architecture Audit
    v2_files = sorted([f for f in os.listdir(V2_DIR) if f.endswith(".md")])
    file_list_md = "| # | Document Name | Description |\n| :--- | :--- | :--- |\n"
    for i, f in enumerate(v2_files, 1):
        # Quick extract title from file
        title = "Elite Category"
        try:
            with open(os.path.join(V2_DIR, f), "r") as doc:
                line = doc.readline()
                if line.startswith("# "): title = line.replace("# ", "").strip()
        except Exception as e:
            log_event(f"[WARN] extract title from V2 file {f}: {str(e)[:100]}")
        file_list_md += f"| {i} | `{f}` | {title} |\n"

    # 3. Decision Matrix (Maturity Audit)
    matrix_rows = []
    header_table = "| # | Status | Maturity | Stars | Dimension | Resource |\n| :--- | :--- | :--- | :---: | :--- | :--- |\n"
    for idx, entry in enumerate(engine.maturity_audit, 1):
        status = "💎 ELITE" if entry.get('v2_locations') else "📦 ARCHIVE"
        row = f"| {idx} | {status} | {entry.get('tag', 'N/A')} | {'🌟'*(entry.get('stars') or 0)} | {entry.get('dimension', 'N/A')} | {entry.get('url', 'N/A')} |\n"
        matrix_rows.append(row)

    # 4. Generate PR Body (Main Report)
    with open("pr_description.md", "w") as f:
        f.write(f"## 🏆 V2 Elite: Agentic Optimization Sync (2026)\n\n")
        f.write(f"The V2 Portal has been synchronized with the latest V1 changes. This update enforces the **Minimum Viable Quality (MVQ)** and O'Reilly-style architectural standards.\n\n")
        
        f.write(f"### 📊 High-Density Efficiency\n")
        f.write(f"| Metric | V1 Archive | V2 Elite | Delta / Efficiency |\n")
        f.write(f"| :--- | :---: | :---: | :---: |\n")
        f.write(f"| **Total Resources** | {total_v1_links} | {total_v2_links} | -{reduction_delta} ({density_ratio}% Density) |\n")
        f.write(f"| **AI Enrichment** | N/A | {total_enriched} / {total_v2_links} | {coverage_pct}% Coverage |\n")
        f.write(f"| **GitHub Metadata** | N/A | {gh_with_metadata} / {total_gh} | {gh_coverage_pct}% Coverage |\n")
        f.write(f"| **Maturity Tagging** | Manual | AI-Vetted | 100% Coverage |\n")
        f.write(f"| **Hierarchical Depth** | Flat | Recursive | Max Depth: {engine.max_depth} |\n\n")

        f.write("### 🏗️ Evidence of Elite Status\n")
        f.write("<details><summary>📊 Clic para ver Gráfico de Distribución</summary>\n\n")
        f.write("```mermaid\npie title V2 Maturity Distribution\n")
        for tag, count in maturity_counts.items():
            tag_name = tag.replace('[','').replace(']','')
            f.write(f"    \"{tag_name}\" : {count}\n")
        f.write("```\n\n</details>\n\n")
        
        from src.gemini_utils import SESSION_TRACKER
        f.write(SESSION_TRACKER.get_intelligence_report())
        f.write("\n\n---\n**Detailed Architectural Audit and Decision Matrix follow in comments.**\n")

    # 5. Save Supplementary Reports for Workflow/GitOps
    with open("v2_file_audit.md", "w") as f:
        f.write("### 📜 V2 Document Architecture\n")
        f.write(f"Exhaustive list of {len(v2_files)} generated elite documents.\n\n")
        f.write(file_list_md)

    with open("v2_decision_matrix.md", "w") as f:
        f.write("### 📋 Elite Decision Matrix\n")
        f.write("Detailed logs of maturity promotions and elite selections.\n\n")
        f.write(header_table)
        for row in matrix_rows: f.write(row)
