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
            return False

        try:
            with open(CURATION_SOURCES_PATH, "r") as f:
                sources = yaml.safe_load(f).get("sources", [])
        except Exception as e:
            log_event(f"  [!] Error loading curation sources: {e}")
            return False
        
        topics = [s["topic"] for s in sources]
        
        with open(WORKFLOW_PATH, "r") as f:
            content = f.read()

        log_event("[Mandate 11] Synchronizing Workflow UI with Curation Sources...")
        
        # Identify the checkboxes section (inputs)
        # We look for the 'inputs:' block and the start of job definitions
        match = re.search(r'(inputs:.*?\n)(  \w+:)', content, re.DOTALL)
        if not match:
            log_event("  [!] Could not find inputs block in workflow file.")
            return False

        changed = False
        new_content = content
        
        for topic in topics:
            if topic not in content:
                log_event(f"  [+] Adding new UI toggle for topic '{topic}'")
                
                # Logic to generate a safe ID
                safe_id = "include_" + re.sub(r'[^a-z0-9]', '_', topic.lower()).strip('_')
                
                # Construct the YAML block for the checkbox
                checkbox_yaml = f"\n      {safe_id}:\n        description: '{topic}'\n        type: boolean\n        default: true"
                
                # Inject before the next section
                # We find the end of the last boolean input
                inputs_block = re.search(r'inputs:(.*?)jobs:', new_content, re.DOTALL)
                if inputs_block:
                    block_text = inputs_block.group(1)
                    # Insert at the end of the block
                    last_input_match = list(re.finditer(r'default: \w+', block_text))
                    if last_input_match:
                        insert_pos = inputs_block.start(1) + last_input_match[-1].end()
                        new_content = new_content[:insert_pos] + checkbox_yaml + new_content[insert_pos:]
                        changed = True

        if changed:
            with open(WORKFLOW_PATH, "w") as f:
                f.write(new_content)
            log_event(f"  [OK] Workflow UI updated successfully.")
            return True

        log_event("  [OK] Workflow UI is already synchronized.")
        return False

if __name__ == "__main__":
    sync = WorkflowUISync()
    sync.sync_ui()
