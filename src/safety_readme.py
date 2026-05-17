import re
import sys
import os

REQUIRED_SECTIONS = [
    "1. Introduction and Motivation",
    "2. Repository Metrics and Evolution",
    "3. The Agentic Stack",
    "4. The 2026 Architectural Shift",
    "5. Dual-Edition Architecture (V1 vs V2)",
    "6. The Unified Agentic Database (Knowledge Graph)",
    "7. AI Economic Architecture and Cost Analysis",
    "8. The Agentic AI Engine",
    "9. GitHub Workflows and Automation",
    "10. Branching Strategy and Lifecycle",
    "11. Contributing to the Archive",
    "12. Developer Experience and VSCode Setup",
    "13. Repository Inventory and Configuration",
    "14. Special Assets and Learning Paths",
    "15. Licensing and Legal Disclaimer"
]

def check_readme():
    if not os.path.exists("README.md"):
        print("❌ README.md not found!")
        return False

    with open("README.md", "r") as f:
        content = f.read()

    errors = []
    
    # 1. Check for mandatory headers
    headers = re.findall(r'^## (.*)', content, re.MULTILINE)
    
    for section in REQUIRED_SECTIONS:
        found = False
        for h in headers:
            if section in h:
                found = True
                break
        if not found:
            errors.append(f"Header missing or misnumbered: '## {section}'")

    # 2. Check for Table of Contents synchronization
    toc_links = re.findall(r'\[(\d+\. .*?)\]\(#.*?\)', content)
    for section in REQUIRED_SECTIONS:
        if section not in toc_links:
            errors.append(f"TOC entry missing or misnumbered: '{section}'")

    # 3. Check for drastic size reduction (Safety Guardrail)
    # Average size is > 30KB. If it drops below 20KB, it's suspicious.
    size_kb = len(content) / 1024
    if size_kb < 20:
        errors.append(f"README.md size is suspiciously small ({size_kb:.2f} KB). Possible data loss.")

    if errors:
        print("🛡️ README Integrity Audit: ❌ FAILED")
        for err in errors:
            print(f"- {err}")
        return False
    else:
        print("🛡️ README Integrity Audit: ✅ PASSED (15/15 Sections Validated)")
        return True

if __name__ == "__main__":
    if not check_readme():
        sys.exit(1)
