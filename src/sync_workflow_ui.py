import os
import yaml
import re
from src.logger import log_event

CURATION_SOURCES_PATH = "data/curation_sources.yaml"
WORKFLOW_PATH = ".github/workflows/agentic_cron.yml"

class WorkflowUISync:
    """
    Automates Mandate 11: Workflow-Config Synchronization.
    Ensures the GitHub Actions UI checkboxes always match the categories in curation_sources.yaml.
    """
    def sync_ui(self):
        if not os.path.exists(CURATION_SOURCES_PATH) or not os.path.exists(WORKFLOW_PATH):
            return

        with open(CURATION_SOURCES_PATH, "r") as f:
            sources = yaml.safe_load(f).get("sources", [])
        
        # 1. Map topics to input IDs (e.g. "AI & Agents" -> "include_ai")
        # Predefined mapping for core topics
        mapping = {
            "kubernetes": "include_k8s",
            "cloud": "include_cloud",
            "ai": "include_ai",
            "productivity": "include_dev",
            "agents": "include_dev",
            "data": "include_data",
            "iac": "include_iac",
            "gitops": "include_iac"
        }

        with open(WORKFLOW_PATH, "r") as f:
            workflow_content = f.read()

        log_event("[Mandate 11] Synchronizing Workflow UI with Curation Sources...")
        
        for source in sources:
            topic = source["topic"].lower()
            found = False
            for keyword, input_id in mapping.items():
                if keyword in topic:
                    # Check if input_id is already in the workflow
                    if input_id in workflow_content:
                        found = True; break
            
            if not found:
                # If a new topic is detected that doesn't match any keyword, 
                # we should warn the user or attempt a generic injection.
                log_event(f"  [!] WARNING: New topic '{source['topic']}' detected. Please add it to Workflow UI manually.")

        # Note: In a fully automated version, we could use a YAML parser 
        # to re-write the workflow file, but re-writing GitHub Actions YAMLs 
        # is risky due to ${{ expression }} syntax potentially breaking.
        # For now, we perform an integrity check that the SafetyGuard will report.
        
if __name__ == "__main__":
    sync = WorkflowUISync()
    sync.sync_ui()
