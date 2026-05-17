import os
import re
import yaml
import json
from src.logger import log_event

GEMINI_MD_PATH = "GEMINI.md"
PROMPTS_DIR = "src/ai_prompts"
MANDATES_JSON = os.path.join(PROMPTS_DIR, "system_mandates.json")

class MandateIngestor:
    """
    Transforms GEMINI.md natural language mandates into structured system instructions 
    consumable by Python scripts. This creates a direct bridge between documentation and AI behavior.
    """
    def __init__(self):
        os.makedirs(PROMPTS_DIR, exist_ok=True)

    def extract_mandates(self) -> dict:
        if not os.path.exists(GEMINI_MD_PATH): return {}
        
        content = open(GEMINI_MD_PATH, "r").read()
        # Extract the Core Mandates section
        mandates_section = re.search(r'## 🧠 Core Mandates\n(.*?)\n##', content, re.DOTALL)
        if not mandates_section: return {}

        # Extract individual numbered mandates
        mandates = re.findall(r'(\d+)\.\s+\*\*(.*?)\*\*:\s*(.*?)(?=\n\d+\.|\n\n|\Z)', mandates_section.group(1), re.DOTALL)
        
        structured = {}
        for num, title, desc in mandates:
            structured[num] = {
                "title": title.strip(),
                "instruction": desc.strip().replace("\n    - ", " ").replace("\n", " ")
            }
        
        # Extract Architecture mandates (27 & 28 are critical for V2)
        architecture_mandates = re.findall(r'(\d+)\.\s+\*\*(.*?)\*\*:\s*(.*?)(?=\n\d+\.|\n\n|\Z)', content, re.DOTALL)
        for num, title, desc in architecture_mandates:
            if int(num) >= 20: # Specialized metadata/architecture rules
                structured[num] = {
                    "title": title.strip(),
                    "instruction": desc.strip().replace("\n    - ", " ").replace("\n", " ")
                }

        return structured

    def save_system_instructions(self):
        mandates = self.extract_mandates()
        if not mandates:
            log_event("[!] No mandates found in GEMINI.md to ingest.")
            return

        # Create a consolidated system prompt snippet
        system_snippet = "NUBENETES SYSTEM MANDATES:\n"
        for num, data in sorted(mandates.items(), key=lambda x: int(x[0])):
            system_snippet += f"- [{num}] {data['title']}: {data['instruction']}\n"

        with open(MANDATES_JSON, "w") as f:
            json.dump({"system_snippet": system_snippet, "raw_mandates": mandates}, f, indent=2)
        
        log_event(f"[OK] Ingested {len(mandates)} mandates from GEMINI.md into {MANDATES_JSON}")

def get_system_mandates() -> str:
    """Helper for other scripts to load the current mandates."""
    if os.path.exists(MANDATES_JSON):
        try:
            return json.load(open(MANDATES_JSON, "r")).get("system_snippet", "")
        except: return ""
    return ""

if __name__ == "__main__":
    ingestor = MandateIngestor()
    ingestor.save_system_instructions()
