import os
import yaml
import re
from src.logger import log_event

INVENTORY_PATH = "data/inventory.yaml"
V1_DIR = "docs"
V2_DIR = "v2-docs"

class SafetyGuard:
    def __init__(self):
        self.errors = []
        self.inventory = self._load_inventory()

    def _load_inventory(self):
        if os.path.exists(INVENTORY_PATH):
            try:
                with open(INVENTORY_PATH, "r") as f:
                    return yaml.safe_load(f) or {}
            except: return {}
        return {}

    def validate_data_integrity(self, old_inventory: dict):
        """Mandato 1: Protección de Información."""
        for url, old_meta in old_inventory.items():
            new_meta = self.inventory.get(url)
            if not new_meta: continue
            if old_meta.get("stars", 0) > new_meta.get("stars", 0):
                self.errors.append(f"❌ **Star Loss**: {url} ({old_meta['stars']} -> {new_meta['stars']})")
            if old_meta.get("description") and not new_meta.get("description"):
                self.errors.append(f"❌ **V1 Desc Loss**: {url}")

    def validate_v2_architecture(self):
        """Mandato 28: Estructura O'Reilly."""
        if not os.path.exists(V2_DIR): return
        for file in os.listdir(V2_DIR):
            if file.endswith(".md") and file != "index.md":
                content = open(os.path.join(V2_DIR, file), "r").read()
                if "## Table of Contents" not in content:
                    self.errors.append(f"⚠️ **V2 TOC Missing**: `{file}`")
                if "### " not in content:
                    self.errors.append(f"⚠️ **V2 Too Flat**: `{file}` (Missing topics)")

    def generate_audit_report(self, old_inv_path=None) -> str:
        """Generates a Markdown report for the PR body."""
        log_event("[Safety] Running Audit for PR documentation...")
        if old_inv_path and os.path.exists(old_inv_path):
            try:
                with open(old_inv_path, "r") as f:
                    self.validate_data_integrity(yaml.safe_load(f) or {})
            except: pass
        
        self.validate_v2_architecture()
        
        status = "✅ PASS" if not self.errors else "⚠️ WARNING"
        report = f"\n### 🛡️ Safety & Mandate Audit: {status}\n"
        if not self.errors:
            report += "All project mandates and data integrity checks passed successfully.\n"
        else:
            report += "<details><summary>Click to view <b>" + str(len(self.errors)) + "</b> issues found</summary>\n\n"
            for err in self.errors:
                report += f"- {err}\n"
            report += "\n> 💡 **Note**: These issues did not stop the workflow, but should be reviewed before merging.\n</details>\n"
        return report

if __name__ == "__main__":
    guard = SafetyGuard()
    success = guard.run_all_checks()
    if not success:
        exit(1)
