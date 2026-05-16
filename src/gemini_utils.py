import httpx
import asyncio
import random
import json
import re
import os
from datetime import datetime
from typing import Dict, Any, List, Optional
from src.config import GEMINI_API_KEYS, GEMINI_API_VERSION, GEMINI_API_KEYS_DATA
from src.logger import log_event

# Global para mantener el índice de la API Key actual y los modelos descubiertos
CURRENT_KEY_INDEX = 0
DISCOVERED_MODELS = []

class GeminiSessionTracker:
    def __init__(self):
        self.model_usage = {} # {model_name: count}
        self.key_stats = {i: {"calls": 0, "429s": 0, "404s": 0, "type": GEMINI_API_KEYS_DATA[i]["type"], "label": GEMINI_API_KEYS_DATA[i]["label"]} for i in range(len(GEMINI_API_KEYS))}
        self.discovery_log = []
        self.start_time = datetime.now()

    def track_call(self, key_idx: int, model: str, status: int):
        if status == 200:
            self.model_usage[model] = self.model_usage.get(model, 0) + 1
        self.key_stats[key_idx]["calls"] += 1
        if status == 429: self.key_stats[key_idx]["429s"] += 1
        if status == 404: self.key_stats[key_idx]["404s"] += 1

    def get_intelligence_report(self) -> str:
        report = "\n### 🧠 AI Intelligence & Observability Report\n\n"
        report += "#### 🤖 Model Selection Logic (Dynamic)\n"
        report += f"Execution started with discovery of top models based on May 2026 hierarchy.\n\n"
        
        report += "| Model Used | Successful Calls | Hierarchy Logic |\n| :--- | :---: | :--- |\n"
        # Sort model usage items for consistent reporting
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
        
        # Access DISCOVERED_MODELS globally
        report += f"\n*Status: {len(DISCOVERED_MODELS)} models verified in auto-discovery phase. System auto-adopted newest versions found.*"
        return report

SESSION_TRACKER = GeminiSessionTracker()

async def discover_optimal_models():
    """
    Queries the Google Model Service to find available models for the current keys.
    Ranks them by capability (Pro > Flash) and version (3.1 > 2.5 > 1.5).
    """
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
        """
        Calculates a score for a model to prioritize the most capable and recent ones.
        Dynamic version detection ensures auto-adoption of future models (e.g. 2.0, 3.1, 4.0).
        """
        score = 0.0
        
        # 1. Dynamic Version Score (e.g., gemini-1.5-pro -> 1.5)
        # Prioritizes higher numbers (3.1 > 1.5)
        version_match = re.search(r'(\d+\.\d+)', name)
        if version_match:
            try:
                version = float(version_match.group(1))
                score += version * 50  # 3.1 -> 155, 1.5 -> 75
            except: pass
        
        # 2. Tier Score (Capability)
        if "-ultra" in name: score += 100 # Future-proofing for high-end models
        elif "-pro" in name: score += 50
        elif "-flash" in name: score += 25
        elif "-lite" in name: score += 10
        
        # 3. Freshness & Stability
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

async def call_gemini_with_retry(prompt: str, response_format: str = "json", max_retries: int = 3):
    global CURRENT_KEY_INDEX
    if not GEMINI_API_KEYS: raise ValueError("No GEMINI_API_KEYS configured.")
    models = await discover_optimal_models()
    diagnostics = GeminiDiagnostics()
    for key_attempt in range(len(GEMINI_API_KEYS)):
        api_key = GEMINI_API_KEYS[CURRENT_KEY_INDEX]
        async with httpx.AsyncClient() as client:
            for model in models:
                full_model_name = f"models/{model}"
                api_url = f"https://generativelanguage.googleapis.com/{GEMINI_API_VERSION}/{full_model_name}:generateContent?key={api_key}"
                for attempt in range(max_retries):
                    try:
                        payload = {"contents": [{"parts": [{"text": prompt}]}]}
                        response = await client.post(api_url, json=payload, timeout=45)
                        SESSION_TRACKER.track_call(CURRENT_KEY_INDEX, model, response.status_code)
                        if response.status_code == 200:
                            resp_json = response.json()
                            if 'candidates' in resp_json and resp_json['candidates']:
                                text_resp = resp_json['candidates'][0]['content']['parts'][0]['text']
                                if response_format == "json":
                                    match = re.search(r'\{.*\}|\[.*\]', text_resp, re.DOTALL)
                                    if match:
                                        data = json.loads(match.group(0))
                                        return data[0] if isinstance(data, list) and len(data) > 0 else data
                                    diagnostics.add_attempt(model, 200, "JSON not found", text_resp)
                                    break
                                return text_resp
                            diagnostics.add_attempt(model, 200, "No candidates")
                            break
                        elif response.status_code == 429:
                            log_event(f"  [!] API 429 on Key {CURRENT_KEY_INDEX+1}. Rotating...")
                            CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(GEMINI_API_KEYS)
                            return await call_gemini_with_retry(prompt, response_format, max_retries)
                        elif response.status_code == 404:
                            diagnostics.add_attempt(model, 404, "Not Found")
                            break
                        elif response.status_code in [500, 503, 504]:
                            await asyncio.sleep(2 * (attempt + 1))
                            continue
                        else:
                            diagnostics.add_attempt(model, response.status_code, "API Error", response.text)
                            break
                    except Exception as e:
                        SESSION_TRACKER.track_call(CURRENT_KEY_INDEX, model, 0)
                        diagnostics.add_attempt(model, 0, str(e))
                        break
            CURRENT_KEY_INDEX = (CURRENT_KEY_INDEX + 1) % len(GEMINI_API_KEYS)
    raise Exception(f"Critical Gemini failure after key rotation.\n{diagnostics.get_report()}")
