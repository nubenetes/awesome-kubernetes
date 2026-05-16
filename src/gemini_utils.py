import httpx
import asyncio
import random
import json
import re
import os
import time
from datetime import datetime
from typing import Dict, Any, List, Optional
from src.config import GEMINI_API_KEYS, GEMINI_API_VERSION, GEMINI_API_KEYS_DATA
from src.logger import log_event

# Global state for rate limiting and discovery
CURRENT_KEY_INDEX = 0
DISCOVERED_MODELS = []
GLOBAL_COOLDOWN_UNTIL = 0
THROTTLED_MODELS = {} # {model_name: timestamp}

class GeminiSessionTracker:
    def __init__(self):
        self.model_usage = {} # {model_name: count}
        self.key_stats = {i: {"calls": 0, "429s": 0, "404s": 0, "type": GEMINI_API_KEYS_DATA[i]["type"], "label": GEMINI_API_KEYS_DATA[i]["label"]} for i in range(len(GEMINI_API_KEYS))}
        self.discovery_log = []
        self.start_time = datetime.now()
        self.total_throttles = 0

    def track_call(self, key_idx: int, model: str, status: int):
        if status == 200:
            self.model_usage[model] = self.model_usage.get(model, 0) + 1
        self.key_stats[key_idx]["calls"] += 1
        if status == 429: 
            self.key_stats[key_idx]["429s"] += 1
            self.total_throttles += 1
        if status == 404: self.key_stats[key_idx]["404s"] += 1

    def get_intelligence_report(self) -> str:
        report = "\n### 🧠 AI Intelligence & Observability Report\n\n"
        report += "#### 🤖 Model Selection Logic (Dynamic)\n"
        report += f"Execution started with discovery of top models based on May 2026 hierarchy.\n\n"
        
        report += "| Model Used | Successful Calls | Hierarchy Logic |\n| :--- | :---: | :--- |\n"
        usage_items = sorted(self.model_usage.items(), key=lambda x: x[1], reverse=True)
        for model, count in usage_items:
            logic = "Elite/Pro (Complex Reasoning)" if "pro" in model else "Flash/Lite (High Speed)"
            report += f"| `{model}` | **{count}** | {logic} |\n"
        if not self.model_usage: report += "| No AI calls | 0 | N/A |\n"
        
        report += "\n#### 🔑 API Infrastructure & Quota Management\n"
        report += "| Key Index | Type | Provider Label | Usage | Errors (429/404) |\n| :--- | :--- | :--- | :---: | :---: |\n"
        for idx, stats in self.key_stats.items():
            usage_bar = "█" * min(stats["calls"] // 5, 10) or "░"
            report += f"| Key {idx+1} | `{stats['type']}` | {stats['label']} | {usage_bar} ({stats['calls']}) | {stats['429s']} / {stats['404s']} |\n"
        
        status_msg = f"{len(DISCOVERED_MODELS)} models verified."
        if self.total_throttles > 0:
            status_msg += f" **Adaptive Tiering active ({self.total_throttles} throttles managed).**"
        
        report += f"\n*Status: {status_msg} System auto-adopted newest versions found.*"
        return report

SESSION_TRACKER = GeminiSessionTracker()

async def discover_optimal_models():
    global DISCOVERED_MODELS
    if DISCOVERED_MODELS: return DISCOVERED_MODELS
    
    log_event("[*] Starting AI Model Auto-Discovery...", section_break=True)
    all_supported = []
    
    for key in GEMINI_API_KEYS:
        try:
            async with httpx.AsyncClient() as client:
                url = f"https://generativelanguage.googleapis.com/v1beta/models?key={key}"
                resp = await client.get(url, timeout=10)
                if resp.status_code == 200:
                    models_data = resp.json().get("models", [])
                    for m in models_data:
                        name = m.get("name", "").replace("models/", "")
                        if "generateContent" in m.get("supportedGenerationMethods", []):
                            if name not in all_supported: all_supported.append(name)
                elif resp.status_code == 429:
                    log_event(f"  [!] Discovery Key is rate-limited (429). Skipping.")
        except: pass

    if not all_supported:
        log_event("  [!] Discovery failed. Falling back to safe defaults.")
        DISCOVERED_MODELS = ["gemini-1.5-flash-latest", "gemini-1.5-flash", "gemini-1.5-pro"]
        return DISCOVERED_MODELS

    def score_model(name: str) -> float:
        score = 0.0
        version_match = re.search(r'(\d+\.\d+)', name)
        if version_match:
            try:
                version = float(version_match.group(1))
                score += version * 50
            except: pass
        if "-ultra" in name: score += 100
        elif "-pro" in name: score += 50
        elif "-flash" in name: score += 25
        elif "-lite" in name: score += 10
        if "-latest" in name: score += 5
        if "experimental" in name or "exp" in name: score -= 15
        return score

    DISCOVERED_MODELS = sorted(all_supported, key=score_model, reverse=True)
    log_event(f"  [+] Discovered {len(DISCOVERED_MODELS)} suitable models.")
    log_event(f"  [+] Top Tier AI: {', '.join(DISCOVERED_MODELS[:3])}")
    return DISCOVERED_MODELS

class GeminiDiagnostics:
    def __init__(self):
        self.attempts = []

    def add_attempt(self, model: str, status: int, error: str = None, response_text: str = None):
        self.attempts.append({"model": model, "status": status, "error": error, "response_preview": response_text[:200] if response_text else None})

    def get_report(self) -> str:
        report = "DIAGNÓSTICO GEMINI:\n"
        for i, a in enumerate(self.attempts):
            report += f"  {i+1}. [{a['model']}] Status: {a['status']}"
            if a['error']: report += f" | Error: {a['error']}"
            if a['response_preview']: report += f" | Resp: {a['response_preview']}"
            report += "\n"
        return report

async def resolve_url(url: str) -> str:
    shorteners = ['t.co', 'bit.ly', 'buff.ly', 'goo.gl', 'tinyurl.com', 't.ly', 'rb.gy', 'is.gd', 'drp.li', 't.me', 'lnkd.in']
    try: domain = url.split("//")[-1].split("/")[0].lower()
    except: return url
    final_url, max_hops, current_hop = url, 5, 0
    async with httpx.AsyncClient(follow_redirects=True, timeout=8) as client:
        while current_hop < max_hops:
            try:
                current_domain = final_url.split("//")[-1].split("/")[0].lower()
                if current_hop > 0 and current_domain not in shorteners: break
                resp = await client.head(final_url, timeout=5)
                new_url = str(resp.url)
                if new_url == final_url: break
                final_url, current_hop = new_url, current_hop + 1
            except: break
    return final_url

def is_fuzzy_duplicate(url_a: str, url_b: str) -> bool:
    def clean(u):
        u = u.split('#')[0].rstrip('/').lower()
        u = re.sub(r'(\?|&)(utm_[^&]+|s=[^&]+|t=[^&]+|ref=[^&]+)', '', u)
        return u[:-1] if u.endswith('?') else u
    return clean(url_a) == clean(url_b)

async def call_gemini_with_retry(prompt: str, response_format: str = "json", max_retries: int = 3, prefer_flash: bool = False):
    global CURRENT_KEY_INDEX, GLOBAL_COOLDOWN_UNTIL
    if not GEMINI_API_KEYS: raise ValueError("No GEMINI_API_KEYS configured.")
    
    models_pool = await discover_optimal_models()
    
    # 1. Smart Re-ordering: If prefer_flash is True, put flash models first
    if prefer_flash:
        models = sorted(models_pool, key=lambda m: 0 if "flash" in m or "lite" in m else 1)
    else:
        models = models_pool

    diagnostics = GeminiDiagnostics()
    total_keys = len(GEMINI_API_KEYS)
    base_wait_time = 2.5
    consecutive_429s = 0
    
    for attempt_round in range(max_retries + 1):
        # Global Cooldown Check
        now = time.time()
        if now < GLOBAL_COOLDOWN_UNTIL:
            await asyncio.sleep(GLOBAL_COOLDOWN_UNTIL - now)

        for key_offset in range(total_keys):
            current_idx = (CURRENT_KEY_INDEX + key_offset) % total_keys
            api_key = GEMINI_API_KEYS[current_idx]
            
            async with httpx.AsyncClient() as client:
                for model in models:
                    # Skip throttled models for this specific execution
                    if THROTTLED_MODELS.get(model, 0) > time.time():
                        continue

                    full_model_name = f"models/{model}"
                    api_url = f"https://generativelanguage.googleapis.com/{GEMINI_API_VERSION}/{full_model_name}:generateContent?key={api_key}"
                    
                    try:
                        payload = {"contents": [{"parts": [{"text": prompt}]}]}
                        response = await client.post(api_url, json=payload, timeout=45)
                        SESSION_TRACKER.track_call(current_idx, model, response.status_code)
                        
                        if response.status_code == 200:
                            CURRENT_KEY_INDEX = current_idx
                            resp_json = response.json()
                            if 'candidates' in resp_json and resp_json['candidates']:
                                text_resp = resp_json['candidates'][0]['content']['parts'][0]['text']
                                if response_format == "json":
                                    match = re.search(r'\{.*\}|\[.*\]', text_resp, re.DOTALL)
                                    if match:
                                        data = json.loads(match.group(0))
                                        return data[0] if isinstance(data, list) and len(data) > 0 else data
                                    diagnostics.add_attempt(model, 200, "JSON not found")
                                    break 
                                return text_resp
                            diagnostics.add_attempt(model, 200, "No candidates")
                            break 
                            
                        elif response.status_code == 429:
                            consecutive_429s += 1
                            # 2. ADAPTIVE TIERING: Mark this specific model as throttled
                            throttle_duration = 30 if "pro" in model else 15
                            THROTTLED_MODELS[model] = time.time() + throttle_duration
                            
                            # 3. GLOBAL THROTTLING: Slow down entire engine
                            GLOBAL_COOLDOWN_UNTIL = time.time() + 3.0 
                            
                            wait = base_wait_time * (1.8 ** (consecutive_429s - 1)) + random.uniform(1.0, 2.0)
                            log_event(f"  [!] API 429 on `{model}` (Key {current_idx+1}). Tiering down & backing off {wait:.1f}s...")
                            await asyncio.sleep(wait)
                            
                            # Continue to next model in current key (likely Flash)
                            continue 
                            
                        elif response.status_code == 404:
                            diagnostics.add_attempt(model, 404, "Not Found")
                            break 
                        elif response.status_code in [500, 503, 504]:
                            diagnostics.add_attempt(model, response.status_code, "Server Error")
                            continue 
                        else:
                            diagnostics.add_attempt(model, response.status_code, "API Error", response.text)
                            break 
                            
                    except Exception as e:
                        SESSION_TRACKER.track_call(current_idx, model, 0)
                        diagnostics.add_attempt(model, 0, str(e))
                        break 
        
        if attempt_round < max_retries:
            wait_round = base_wait_time * (2 ** attempt_round)
            log_event(f"  [!] Exhausted tier options in round {attempt_round+1}. Cooling down {wait_round}s...")
            await asyncio.sleep(wait_round)

    raise Exception(f"Critical Gemini failure after adaptive tiering.\n{diagnostics.get_report()}")
