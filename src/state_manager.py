import os
import json
from datetime import datetime
from src.config import MADRID_TZ
from src.logger import log_event

STATE_FILE = "src/memory/state.json"

def load_state() -> dict:
    default_state = {
        "last_processed_tweet_date": "2024-10-01T00:00:00"
    }
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, 'r') as f:
                return json.load(f)
        except Exception as e:
            log_event(f"[!] Error loading state.json: {e}")
    return default_state

def save_state(last_date: datetime):
    state = load_state()
    state["last_processed_tweet_date"] = last_date.isoformat()
    
    os.makedirs(os.path.dirname(STATE_FILE), exist_ok=True)
    try:
        with open(STATE_FILE, 'w') as f:
            json.dump(state, f, indent=2)
        log_event(f"[*] State saved: last processed date {last_date.date()}")
    except Exception as e:
        log_event(f"[!] Error saving state.json: {e}")

def get_last_date() -> datetime:
    state = load_state()
    date_str = state.get("last_processed_tweet_date")
    return datetime.fromisoformat(date_str).replace(tzinfo=MADRID_TZ)
