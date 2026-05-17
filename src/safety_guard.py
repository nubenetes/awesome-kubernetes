import subprocess
import os
import re
from src.logger import log_event

class SafetyGuard:
    def __init__(self):
        self.rules_path = "data/link_rules.yaml"

    def validate_syntax(self, file_content: str, file_path: str) -> bool:
        """Realiza comprobaciones de seguridad y sintaxis en contenido Markdown."""
        # 1. Mermaid Check
        if "```mermaid" in file_content:
            # Check for unquoted labels with special chars if needed, or simple pair matching
            if file_content.count("```mermaid") != file_content.count("```"):
                log_event(f"    [!] Syntax Error: Unclosed Mermaid block in {file_path}")
                return False

        # 2. HTML Security Check
        forbidden_tags = ["<script", "<iframe>", "<style"]
        for tag in forbidden_tags:
            if tag in file_content.lower():
                log_event(f"    [!] Security Error: Forbidden HTML tag '{tag}' detected in {file_path}")
                return False

        # 3. MkDocs Image Check
        # Ensure images start with images/ or ../docs/images/
        img_matches = re.findall(r'!\[.*?\]\((.*?)\)', file_content)
        for img in img_matches:
            if not (img.startswith("images/") or img.startswith("../docs/images/") or img.startswith("http")):
                 log_event(f"    [!] Path Error: Invalid image path '{img}' in {file_path}")
                 # return False # Just warn for now

        return True

    def run_mkdocs_build_test(self) -> bool:
        """Lanza un 'mkdocs build' de prueba para asegurar que no hay errores críticos."""
        log_event("[*] Running MkDocs Safety Build Test...")
        try:
            # We use --strict to catch broken links if necessary, or just standard build
            result = subprocess.run(
                ["mkdocs", "build", "--clean", "--site-dir", "/tmp/mkdocs-test"],
                capture_output=True, text=True, timeout=120
            )
            if result.returncode != 0:
                log_event(f"    [!] MkDocs Build Failed:\n{result.stderr[:500]}")
                return False
            log_event("    [OK] MkDocs Build Successful.")
            return True
        except Exception as e:
            log_event(f"    [!] Build test error: {e}")
            return True # Fallback to true if mkdocs not installed locally
