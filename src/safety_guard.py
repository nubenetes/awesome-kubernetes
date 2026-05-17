import os
import yaml
import re
from datetime import datetime
from src.logger import log_event
from src.gemini_utils import normalize_url

INVENTORY_PATH = "data/inventory.yaml"
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
        """Mandate 1: Protección de Información."""
        for url, old_meta in old_inventory.items():
            new_meta = self.inventory.get(url)
            if not new_meta: continue
            if old_meta.get("stars", 0) > new_meta.get("stars", 0):
                self.errors.append(f"❌ **Star Loss**: `{url}` ({old_meta['stars']} -> {new_meta['stars']})")
            if old_meta.get("description") and not new_meta.get("description"):
                self.errors.append(f"❌ **V1 Desc Loss**: `{url}`")

    def validate_semantic_interlinking(self):
        """Mandate 5: Verificar interconexión semántica en V1."""
        log_event("[Safety] Auditing Semantic Interlinking...")
        for url, meta in self.inventory.items():
            related = meta.get("related_categories", [])
            for rel_cat in related:
                path = os.path.join(V1_DIR, f"{rel_cat}.md")
                if os.path.exists(path):
                    content = open(path, "r").read()
                    if url not in content:
                        self.warnings.append(f"🔗 **Interlink Missing**: `{meta['title']}` should be referenced in `{rel_cat}.md` (See also)")

    def validate_special_assets_completeness(self):
        """Mandate 27: Inclusión exhaustiva de Activos Especiales en V2."""
        if not os.path.exists(SPECIAL_ASSETS_PATH): return
        with open(SPECIAL_ASSETS_PATH, "r") as f:
            special = yaml.safe_load(f).get("special_assets", [])
        
        for sa in special:
            if "Include 100%" in sa.get("v2_rule", "") or "Exhaustive" in sa.get("v2_rule", ""):
                file_name = sa["file"]
                v1_path = os.path.join(V1_DIR, file_name)
                if os.path.exists(v1_path):
                    v1_links = re.findall(r'\[.*?\]\((https?://.*?)\)', open(v1_path, "r").read())
                    for link in v1_links:
                        nu = normalize_url(link)
                        if nu in self.inventory and self.inventory[nu].get("status") == "online":
                            # Check for inherited is_special flag instead of v2_locations (which are built later)
                            if not self.inventory[nu].get("is_special"):
                                self.errors.append(f"💎 **VIP Flag Missing**: `{link}` from `{file_name}` is not marked as Special")

    def validate_mvq_compliance(self):
        """Mandato 3 & 16: Verificar cumplimiento de MVQ en V2."""
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
        """Mandate 10: Verificar etiquetado de idioma en V2."""
        if not os.path.exists(V2_DIR): return
        for file in os.listdir(V2_DIR):
            if file.endswith(".md"):
                content = open(os.path.join(V2_DIR, file), "r").read()
                for url, meta in self.inventory.items():
                    lang = meta.get("language", "English")
                    if lang.lower() != "english" and url in content:
                        tag = f"[{lang.upper()} CONTENT]"
                        if tag not in content:
                            self.warnings.append(f"🌐 **Missing Lang Tag**: `{meta['title']}` in `{file}` needs `{tag}`")

    def validate_platinum_schema(self):
        """Mandate 22: Validar esquema Platinum en BBDD."""
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
        """Checks if content has an explicit header or an implicit list-based TOC."""
        if "## Table of Contents" in content: return True
        toc_pattern = r'^\d+\.\s+\[.*?\]\(#.*?\)'
        matches = re.findall(toc_pattern, content, re.MULTILINE)
        return len(matches) >= 3

    def validate_v2_architecture(self):
        """Mandato 28: Estructura O'Reilly y V2 Flat Navigation."""
        if not os.path.exists(V2_DIR): return
        exempt_files = self._load_exempt_files()
        for file in os.listdir(V2_DIR):
            if file.endswith(".md") and file != "index.md":
                if file in exempt_files: continue
                content = open(os.path.join(V2_DIR, file), "r").read()
                if not self.has_valid_toc(content):
                    self.errors.append(f"📚 **V2 TOC Missing**: `{file}`")
                if "### " not in content:
                    self.errors.append(f"📚 **V2 Too Flat**: `{file}` (Missing H3 subtopics)")

    def validate_navigation_sync(self):
        """Mandate 11: Sincronización entre Workflow y Config."""
        if not os.path.exists(WORKFLOW_PATH) or not os.path.exists(CURATION_SOURCES_PATH): return
        with open(CURATION_SOURCES_PATH, "r") as f:
            sources = yaml.safe_load(f).get("sources", [])
        topics = [s["topic"] for s in sources]
        workflow_content = open(WORKFLOW_PATH, "r").read()
        for topic in topics:
            keywords = re.findall(r'\w+', topic.lower())
            found = any(kw in workflow_content.lower() for kw in keywords)
            if not found:
                self.warnings.append(f"🔄 **Sync Warning**: Topic `{topic}` might not be represented in `{WORKFLOW_PATH}` inputs")

    def validate_toc_and_anchors(self):
        """🛠️ Structural Evolution: TOC Consistency & Lowercase Slugs."""
        exempt_files = self._load_exempt_files()
        for root, _, files in os.walk(V1_DIR):
            for file in files:
                if file.endswith(".md"):
                    if file in exempt_files or file == "index.md": continue
                    content = open(os.path.join(root, file), "r").read()
                    if not self.has_valid_toc(content) and len(re.findall(r'^## ', content, re.M)) > 2:
                        self.warnings.append(f"📍 **V1 TOC Missing**: `{file}` has many sections but no TOC")
                    anchors = re.findall(r'\(#([^\)]+)\)', content)
                    for a in anchors:
                        if any(c.isupper() for c in a):
                            self.warnings.append(f"⚓ **Upper Anchor**: `{file}` has non-lowercase anchor `#{a}`")

    def generate_audit_report(self, old_inv_path=None) -> str:
        """Generates a comprehensive Markdown report based on ALL Mandates."""
        log_event("[Safety] Executing Full Mandate Audit (GEMINI.md compliance)...")
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
        self.validate_v2_architecture()
        self.validate_navigation_sync()
        self.validate_toc_and_anchors()
        status = "✅ PASS" if not self.errors else "❌ FAILED"
        if not self.errors and self.warnings: status = "⚠️ WARNING"
        report = f"\n## 🛡️ Safety & Mandate Audit: {status}\n*Audit executed on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*\n\n"
        if not self.errors and not self.warnings:
            report += "✨ **All project mandates from GEMINI.md and technical integrity checks passed successfully.**\n"
        else:
            if self.errors:
                report += "### 🔴 Critical Failures (Mandate Violations)\n"
                for err in self.errors: report += f"- {err}\n"
                report += "\n"
            if self.warnings:
                report += "### 🟡 Warnings & Recommendations\n"
                report += "<details><summary>Click to view " + str(len(self.warnings)) + " recommendations</summary>\n\n"
                for warn in self.warnings: report += f"- {warn}\n"
                report += "\n> 💡 **Note**: Warnings suggest improvements to align with Nubenetes Excellence standards.\n</details>\n"
        return report

if __name__ == "__main__":
    guard = SafetyGuard()
    print(guard.generate_audit_report())
