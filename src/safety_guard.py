import os
import yaml
import re
import hashlib
from datetime import datetime
from src.logger import log_event
from src.gemini_utils import normalize_url, clean_toc_text
from src.config import INVENTORY_PATH

V1_DIR = "docs"
V2_DIR = "v2-docs"
SPECIAL_ASSETS_PATH = "data/special_assets.yaml"
CURATION_SOURCES_PATH = "data/curation_sources.yaml"
WORKFLOW_PATH = ".github/workflows/agentic_cron.yml"

class SafetyGuard:
    def __init__(self):
        self.errors = []
        self.warnings = []
        self.inventory = self._load_inventory()

    def _load_inventory(self):
        if os.path.exists(INVENTORY_PATH):
            try:
                with open(INVENTORY_PATH, "r") as f:
                    return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def _load_exempt_files(self):
        try:
            with open("data/link_rules.yaml", "r") as f:
                rules = yaml.safe_load(f)
                return rules.get("hierarchy_rules", {}).get("toc_exempt_files", [])
        except: return []

    def validate_data_integrity(self, old_inventory: dict):
        """Mandate 1: Información Preservation."""
        for url, old_meta in old_inventory.items():
            new_meta = self.inventory.get(url)
            if not new_meta: continue
            if old_meta.get("stars", 0) > new_meta.get("stars", 0):
                self.errors.append(f"❌ **Star Loss**: `{url}` ({old_meta['stars']} -> {new_meta['stars']})")
            if old_meta.get("description") and not new_meta.get("description"):
                self.errors.append(f"❌ **V1 Desc Loss**: `{url}`")

    def validate_semantic_interlinking(self):
        """Mandate 5: Semantic Interlinking validation."""
        for url, meta in self.inventory.items():
            related = meta.get("related_categories", [])
            for rel_cat in related:
                path = os.path.join(V1_DIR, f"{rel_cat}.md")
                if os.path.exists(path):
                    content = open(path, "r").read()
                    if url not in content:
                        self.warnings.append(f"🔗 **Interlink Missing**: `{meta.get('title', url)}` in `{rel_cat}.md` (See also)")

    def validate_special_assets_completeness(self):
        """Mandate 27: Special Assets Exhaustive Inclusion."""
        if not os.path.exists(SPECIAL_ASSETS_PATH): return
        try:
            with open(SPECIAL_ASSETS_PATH, "r") as f:
                special = yaml.safe_load(f).get("special_assets", [])
        except: return
        
        for sa in special:
            if "Include 100%" in sa.get("v2_rule", "") or "Exhaustive" in sa.get("v2_rule", ""):
                file_name = sa["file"]
                v1_path = os.path.join(V1_DIR, file_name)
                if os.path.exists(v1_path):
                    with open(v1_path, "r") as f:
                        v1_links = re.findall(r'\[.*?\]\((https?://.*?)\)', f.read())
                    for link in v1_links:
                        nu = normalize_url(link)
                        if nu in self.inventory and self.inventory[nu].get("status") == "online":
                            if not self.inventory[nu].get("is_special"):
                                self.errors.append(f"💎 **VIP Flag Missing**: `{link}` from `{file_name}` is not marked as Special")

    def validate_mvq_compliance(self):
        """Mandate 3 & 16: Minimum Viable Quality (MVQ)."""
        for url, meta in self.inventory.items():
            if "github.com" in url and meta.get("v2_locations"):
                pushed = meta.get("gh_pushed", "")
                if pushed:
                    try:
                        last_date = datetime.fromisoformat(pushed.replace("Z", "+00:00"))
                        inactive_years = (datetime.now(last_date.tzinfo) - last_date).days / 365
                        stars = meta.get("gh_stars", meta.get("stars", 0) * 100) 
                        if inactive_years > 4 and stars < 30:
                            self.warnings.append(f"🏚️ **MVQ Violation**: Stale repo `{url}` (>4yrs) in V2 with low impact")
                    except: pass

    def validate_linguistic_tagging(self):
        """Mandate 10: Explicit Language Tagging."""
        if not os.path.exists(V2_DIR): return
        for file in os.listdir(V2_DIR):
            if file.endswith(".md"):
                with open(os.path.join(V2_DIR, file), "r") as f:
                    content = f.read()
                for url, meta in self.inventory.items():
                    lang = meta.get("language", "English")
                    if lang.lower() != "english" and url in content:
                        tag = f"[{lang.upper()} CONTENT]"
                        if tag not in content:
                            self.warnings.append(f"🌐 **Missing Lang Tag**: `{meta.get('title', url)}` in `{file}` needs `{tag}`")

    def validate_platinum_schema(self):
        """Mandate 22: Platinum Metadata Lifecycle."""
        required = ["content_hash", "health_score", "hierarchy", "v1_locations"]
        new_count = 0
        for url, meta in self.inventory.items():
            if url.startswith("INTRO:"): continue
            missing = [f for f in required if f not in meta]
            if missing:
                new_count += 1
                if new_count < 10:
                    self.warnings.append(f"🧬 **Schema Incomplete**: `{url}` missing {missing}")

    def has_valid_toc(self, content: str) -> bool:
        """Checks if content has a valid Table of Contents."""
        if "## Table of Contents" in content: return True
        toc_pattern = r'^\d+\.\s+\[.*?\]\(#.*?\)'
        matches = re.findall(toc_pattern, content, re.MULTILINE)
        return len(matches) >= 3

    def validate_structural_standards(self):
        """Mandate 30: Universal Title and TOC Standards."""
        exempt_files = self._load_exempt_files()
        for root, dirs, files in os.walk(V1_DIR):
            for file in files:
                if file.endswith(".md") and file not in exempt_files:
                    path = os.path.join(root, file)
                    with open(path, "r") as f: content = f.read()
                    
                    # 1. No Emojis or & in titles (H2-H6)
                    titles = re.findall(r'^#{2,6}\s+(.*)', content, re.M)
                    for t in titles:
                        if "&" in t:
                            self.errors.append(f"🚫 **Standard Violation**: Ampersand `&` found in title `{t}` in `{file}`. Use 'and'.")
                        # Basic emoji detection (not exhaustive but covers most common ones in project)
                        if any(char in t for char in "🧠☁️🌟🛡️🧪💎🕵️✨⚠️🔴🟡✅📍"):
                            self.errors.append(f"🚫 **Standard Violation**: Emoji found in title `{t}` in `{file}`.")

                    # 2. HTML block rendering check (Mandate 19)
                    if "<center>" in content and 'markdown="1"' not in content:
                        self.warnings.append(f"🖼️ **Rendering Risk**: `<center>` tag missing `markdown=\"1\"` in `{file}`.")
                    
                    # 3. Anchor Integrity
                    toc_entries = re.findall(r'\[(.*?)\]\(#([^\)]+)\)', content)
                    for text, anchor in toc_entries:
                        # Mandate 30: Lowercase anchors
                        if any(c.isupper() for c in anchor):
                            self.warnings.append(f"⚓ **Non-Standard Anchor**: `{anchor}` in `{file}` should be strictly lowercase.")
                        
                        # Verify anchor exists in the document
                        slug = clean_toc_text(text).lower().replace(" ", "-")
                        if anchor != slug and anchor not in content.lower():
                             self.warnings.append(f"🔗 **Broken Anchor**: TOC link `#{anchor}` in `{file}` might be broken.")

    def validate_v2_architecture(self):
        """Mandate 28: V2 Architecture & Navigation."""
        if not os.path.exists(V2_DIR): return
        exempt_files = self._load_exempt_files()
        for file in os.listdir(V2_DIR):
            if file.endswith(".md") and file != "index.md":
                if file in exempt_files: continue
                with open(os.path.join(V2_DIR, file), "r") as f:
                    content = f.read()
                if not self.has_valid_toc(content):
                    self.errors.append(f"📚 **V2 TOC Missing**: `{file}`")
                if "### " not in content:
                    self.errors.append(f"📚 **V2 Too Flat**: `{file}` (Missing H3 subtopics)")

    def validate_navigation_sync(self):
        """Mandate 11: Workflow-Config Synchronization."""
        if not os.path.exists(WORKFLOW_PATH) or not os.path.exists(CURATION_SOURCES_PATH): return
        try:
            with open(CURATION_SOURCES_PATH, "r") as f:
                sources = yaml.safe_load(f).get("sources", [])
        except: return
        
        topics = [s["topic"] for s in sources]
        with open(WORKFLOW_PATH, "r") as f:
            workflow_content = f.read()
        
        for topic in topics:
            # Check if topic is present in the workflow's input options
            if topic not in workflow_content:
                self.warnings.append(f"🔄 **Sync Failure**: Topic `{topic}` missing from `{WORKFLOW_PATH}` input options.")

    def get_license_compliance_report(self) -> str:
        """Mandate 33: License Compliance Dashboard."""
        stats = {}
        restrictive = []
        for url, meta in self.inventory.items():
            lic = meta.get("gh_license", "N/A")
            stats[lic] = stats.get(lic, 0) + 1
            if any(x in lic.upper() for x in ["BSL", "SSPL", "PROPRIETARY"]):
                restrictive.append(f"- `{meta.get('title', url)}` ({lic})")
        
        report = "### ⚖️ License & Compliance Dashboard\n"
        report += "| License Type | Count |\n| :--- | :---: |\n"
        for lic, count in sorted(stats.items(), key=lambda x: x[1], reverse=True):
            report += f"| {lic} | {count} |\n"
        
        if restrictive:
            report += "\n> 🔴 **CRITICAL ALERT**: Restrictive licenses detected in core projects:\n"
            report += "\n".join(restrictive) + "\n"
        else:
            report += "\n> ✅ **Compliance**: All monitored projects follow permissive Open Source standards.\n"
        return report

    def generate_audit_report(self, old_inv_path=None) -> str:
        """Generates a comprehensive Markdown report based on ALL Mandates."""
        log_event("[Safety] Executing Full Platinum Mandate Audit...")
        
        # 1. Identify Pending Reviews (Mandate 31)
        pending_reviews = []
        for url, meta in self.inventory.items():
            if meta.get("status") == "review_required":
                rev = meta.get("review_metadata", {})
                pending_reviews.append(f"📍 `{meta.get('title', url)}`: Original: {rev.get('original_url')} | Proposed: {rev.get('proposed_url')}")

        # 2. Run standard validations
        if old_inv_path and os.path.exists(old_inv_path):
            try:
                with open(old_inv_path, "r") as f:
                    self.validate_data_integrity(yaml.safe_load(f) or {})
            except: pass
        
        self.validate_semantic_interlinking()
        self.validate_special_assets_completeness()
        self.validate_mvq_compliance()
        self.validate_linguistic_tagging()
        self.validate_platinum_schema()
        self.validate_structural_standards() # Mandate 30 & 19
        self.validate_v2_architecture()
        self.validate_navigation_sync() # Mandate 11
        
        status = "✅ PASS" if not self.errors else "❌ FAILED"
        if not self.errors and self.warnings: status = "⚠️ WARNING"
        
        report = f"\n## 🛡️ Platinum Safety & Mandate Audit: {status}\n*Audit executed on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        
        if pending_reviews:
            report += "### 🔍 High-Value Pending Reviews\n"
            report += "> ⚠️ The following resources have been preserved in V1 but hidden from V2 for manual audit.\n\n"
            for pr in pending_reviews: report += f"- {pr}\n"
            report += "\n"

        report += self.get_license_compliance_report() # Mandate 33

        if not self.errors and not self.warnings:
            report += "\n✨ **All project mandates and technical integrity checks passed successfully.**\n"
        else:
            if self.errors:
                report += "\n### 🔴 Critical Failures\n"
                for err in self.errors: report += f"- {err}\n"
                report += "\n"
            if self.warnings:
                report += "\n### 🟡 Warnings & Recommendations\n"
                report += "<details><summary>Click to view " + str(len(self.warnings)) + " recommendations</summary>\n\n"
                for warn in self.warnings: report += f"- {warn}\n"
                report += "\n> 💡 **Note**: Align with Nubenetes Excellence standards.\n</details>\n"
        return report

if __name__ == "__main__":
    guard = SafetyGuard()
    print(guard.generate_audit_report())
