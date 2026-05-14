import os
from datetime import datetime

# Ruta por defecto para el log local (fuera del repo)
DEFAULT_LOG_PATH = "/home/inafev/.gemini/tmp/awesome-kubernetes/curation_progress.log"

def log_event(message: str, section_break: bool = False):
    """
    Logs an event to both console (STDOUT) and local log file if it exists.
    In GitHub Actions, this will appear in the workflow logs.
    """
    timestamp = datetime.now().strftime('%H:%M:%S')
    formatted_msg = f"[{timestamp}] {message}"
    
    if section_break:
        separator = "=" * 60
        print(f"\n{separator}\n{formatted_msg}\n{separator}")
        _write_to_file(f"\n{separator}\n{formatted_msg}\n{separator}")
    else:
        print(formatted_msg)
        _write_to_file(formatted_msg)

def _write_to_file(message: str):
    # Only try to write to file if not in GitHub Actions
    if not os.getenv("GITHUB_ACTIONS"):
        try:
            # Ensure directory exists
            os.makedirs(os.path.dirname(DEFAULT_LOG_PATH), exist_ok=True)
            with open(DEFAULT_LOG_PATH, "a") as f:
                f.write(message + "\n")
        except:
            pass
