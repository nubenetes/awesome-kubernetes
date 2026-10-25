import httpx
import asyncio
import random
import json
import re
import os
import time
from datetime import datetime
from typing import Dict, Any, List, Optional, Tuple
from tenacity import retry, stop_after_attempt, wait_exponential, retry_if_exception_type
from src.config import GEMINI_API_KEYS, GEMINI_API_VERSION, GEMINI_API_KEYS_DATA
from src.logger import log_event

# Global state for rate limiting and discovery
CURRENT_KEY_INDEX = 0
DISCOVERED_MODELS = []
GLOBAL_COOLDOWN_UNTIL = 0
THROTTLED_MODELS = {} # {model_name: timestamp}
GLOBAL_AI_SEMAPHORE = asyncio.Semaphore(15) # Increased to 15 for high-tier processing

class GeminiSessionTracker:
    def __init__(self):
        self.model_usage = {} # {model_name: count}
        self.key_stats = {i: {"calls": 0, "429s": 0, "404s": 0, "type": GEMINI_API_KEYS_DATA[i]["type"], "label": GEMINI_API_KEYS_DATA[i]["label"]} for i in range(len(GEMINI_API_KEYS))}
        self.discovery_log = []
        self.start_time = datetime.now()
        self.total_throttles = 0
        self.total_tokens_prompt = 0
        self.total_tokens_completion = 0
        self.cache_hits = 0
        self.est_tokens_saved = 0

    def track_cache_hit(self, est_tokens: int = 1500):
        self.cache_hits += 1
        self.est_tokens_saved += est_tokens

    def track_call(self, key_idx: int, model: str, status: int, usage: Dict = None, role: str = "General"):
        if status == 200:
            self.model_usage[model] = self.model_usage.get(model, 0) + 1
            # Track by Role for Agentic Observability
            self.key_stats[key_idx].setdefault("roles", {})
            self.key_stats[key_idx]["roles"][role] = self.key_stats[key_idx]["roles"].get(role, 0) + 1
            
            if usage:
                self.total_tokens_prompt += usage.get("promptTokenCount", 0)
                self.total_tokens_completion += usage.get("candidatesTokenCount", 0)
        
        self.key_stats[key_idx]["calls"] += 1
        if status == 429: 
            self.key_stats[key_idx]["429s"] += 1
            self.total_throttles += 1
        if status == 404: self.key_stats[key_idx]["404s"] += 1

    def get_intelligence_report(self) -> str:
        report = "\n### 🧠 AI Intelligence & Observability Report\n\n"
        report += "#### 🤖 Agentic Roles & Model Selection (Dynamic)\n"
        report += f"Execution utilized a multi-agent Analyst-Auditor workflow for maximum robustness.\n\n"
        
        report += "| Agent Role | Model Used | Successes |\n| :--- | :--- | :---: |\n"
        role_stats = {}
        for idx, stats in self.key_stats.items():
            for role, count in stats.get("roles", {}).items():
                role_stats[role] = role_stats.get(role, 0) + count
        
        for role, count in role_stats.items():
            report += f"| **{role}** | Dynamic Selection | **{count}** |\n"
        
        report += "\n#### 🤖 Model Performance Matrix\n"
        report += "| Model Used | Successful Calls | Hierarchy Logic |\n| :--- | :---: | :--- |\n"
        usage_items = sorted(self.model_usage.items(), key=lambda x: x[1], reverse=True)
        for model, count in usage_items:
            logic = "Elite Auditor (High Reasoning)" if "pro" in model else "Fast Analyst (High Speed)"
            report += f"| `{model}` | **{count}** | {logic} |\n"
        if not self.model_usage: report += "| No AI calls | 0 | N/A |\n"
        
        report += "\n#### 🔑 API Infrastructure & Quota Management\n"
        report += "| Key Index | Type | Provider Label | Usage | Errors (429/404) |\n| :--- | :--- | :--- | :---: | :---: |\n"
        for idx, stats in self.key_stats.items():
            usage_bar = "█" * min(stats["calls"] // 5, 10) or "░"
            report += f"| Key {idx+1} | `{stats['type']}` | {stats['label']} | {usage_bar} ({stats['calls']}) | {stats['429s']} / {stats['404s']} |\n"
        
        report += f"\n#### 📊 Consumption and Efficiency Metrics (2026 Units)\n"
        report += f"- **Total Prompt Tokens**: {self.total_tokens_prompt:,}\n"
        report += f"- **Total Completion Tokens**: {self.total_tokens_completion:,}\n"
        
        # Financial Cost (EUR) based on Gemini 1.5 Flash approx rates
        est_cost_eur = (self.total_tokens_prompt * 0.075 / 1_000_000) + (self.total_tokens_completion * 0.30 / 1_000_000)
        report += f"- **💰 Estimated Cost**: **{est_cost_eur:.4f} €**\n"
        
        # Cache-First Metrics
        hit_ratio = (self.cache_hits / (self.cache_hits + sum(self.model_usage.values())) * 100) if (self.cache_hits + sum(self.model_usage.values())) > 0 else 0
        report += f"- **Database-First Cache Hits**: **{self.cache_hits}** ({hit_ratio:.1f}% hit ratio)\n"
        report += f"- **Estimated Tokens Saved**: ~{self.est_tokens_saved:,} (Zero-API cost)\n"
        report += f"- **Execution Efficiency**: {((self.total_tokens_completion / self.total_tokens_prompt * 100) if self.total_tokens_prompt > 0 else 0):.1f}% (Completion/Prompt)\n"

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
        except Exception as e:
            log_event(f"[WARN] model discovery for key: {str(e)[:100]}")

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
            except Exception as e:
                log_event(f"[WARN] parse model version for {name}: {str(e)[:100]}")
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
    except Exception as e:
        log_event(f"[WARN] parse domain from URL {url[:50]}: {str(e)[:100]}")
        return url
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
            except Exception as e:
                log_event(f"[WARN] resolve URL hop for {final_url[:50]}: {str(e)[:100]}")
                break
    
    # Mandate 34: Prevent multiple trailing slashes using centralized utility
    return sanitize_trailing_slashes(final_url)

def clean_toc_text(text: str) -> str:
    """
    Ensures technical titles and TOC entries are robust.
    Strips emojis, replaces ampersands, and removes special chars.
    """
    if not text: return ""
    # 1. Replace ampersands
    text = text.replace("&", "and")
    # 2. Strip Emojis (Regex for Unicode emoji ranges)
    text = re.sub(r'[\U00010000-\U0010ffff]', '', text)
    # 3. Strip other common problematic non-alphanumeric chars (except spaces and hyphens)
    text = re.sub(r'[^\w\s\-.]', '', text)
    return text.strip()

async def get_github_activity(url: str) -> Dict:
    """
    Mandate 15: Fetch real-time GitHub metadata (stars, license, last push).
    """
    default_meta = {
        "gh_stars": 0,
        "gh_pushed": None,  # date field: unknown = None, never the string "N/A"
        "gh_license": "N/A"
    }
    match = re.search(r'github\.com/([^/]+/[^/]+)', url)
    if not match: return default_meta
    repo = match.group(1).split('#')[0].split('?')[0].rstrip('/')
    api_url = f"https://api.github.com/repos/{repo}"
    
    # Import GH_TOKEN from config locally to avoid circular dependencies
    try:
        from src.config import GH_TOKEN
        headers = {"Authorization": f"token {GH_TOKEN}"} if GH_TOKEN else {}
    except Exception as e:
        log_event(f"[WARN] import GH_TOKEN for GitHub activity: {str(e)[:100]}")
        headers = {}

    try:
        async with httpx.AsyncClient() as client:
            resp = await client.get(api_url, headers=headers, timeout=10.0)
            if resp.status_code == 200:
                data = resp.json()
                lic = data.get("license")
                lic_id = lic.get("spdx_id", "N/A") if isinstance(lic, dict) else "N/A"
                return {
                    "gh_stars": data.get("stargazers_count", 0),
                    "gh_pushed": data.get("pushed_at"),
                    "gh_license": lic_id
                }
    except Exception as e:
        log_event(f"[WARN] fetch GitHub activity for {url}: {str(e)[:100]}")
    return default_meta


def sanitize_trailing_slashes(url: str) -> str:
    """
    Mandate 34: Enforces a ZERO trailing slash policy.
    Removes ALL trailing slashes and question marks from the end of the URL.
    Also repairs malformed protocol prefixes (e.g. 'ttps://', 'https:/https://')
    and duplicated locale path segments (e.g. '/en-us/en-us/').
    """
    if not url: return url
    url = url.strip()
    # Repair malformed protocol prefixes
    url = re.sub(r'^https?:/+(?=https?://)', '', url, flags=re.IGNORECASE)
    if url.lower().startswith('ttps://'):
        url = 'h' + url
    elif url.lower().startswith('ttp://'):
        url = 'h' + url
    url = re.sub(r'^(https?):/+([^/])', r'\1://\2', url, flags=re.IGNORECASE)
    if '://' not in url: return url
    # Collapse duplicated locale path segments (e.g. /en-us/en-us/ or /en-us/en-gb/)
    url = re.sub(r'/(en-us|en-gb)/(?:en-us|en-gb)(/|$)', r'/\1\2', url, flags=re.IGNORECASE)
    # Remove all trailing slashes and question marks from the end of the entire string
    return url.rstrip('/').rstrip('?')


# Patterns in redirect target URLs that indicate a soft-404, login wall, or parked/spam redirect
INVALID_REDIRECT_SUBSTRINGS = (
    "article_not_found",
    "page-removed",
    "page-not-found",
    "?404=",
    "showredirectnotfoundbanner=true",
    "oauth2/v2.0/authorize",
    "oauth2/authorize",
    "login.microsoftonline.com",
    "ciamlogin.com",
    "id.atlassian.com/login",
    "accounts.google.com/servicelogin",
    "platform.qa.com/login",
    "newsletter.thelongcommit.com/subscribe",
    "acg-notice.pluralsight.com",
    "ww-landing-azure-for-architects.html",
    "ambking1234.limo",
    "jnetoto808.com",
    "andara88do.com",
    "visittheswamp.com",
    "koterstore.nl",
    "travelrasik.com",
    "ww547.coffeeapplied.com",
    "x1f.one",
    "yellow-scope.com",
    "frontdeskchat.com",
    "uniquedresses.nl",
)

PARKING_TEXT_INDICATORS = (
    "buy this domain",
    "parked free",
    "domain is for sale",
    "this domain is for sale",
    "hugedomains.com",
    "sedoparking.com",
    "dan.com",
    "afternic.com",
)

GENERIC_REDIRECT_PATH_RE = re.compile(
    r"^/?(en|en-us|en-gb|es|fr|de|en_us|fr-fr)?/?"
    r"(blog|blogs|resources|resources/blog|products|product|company/blog|"
    r"devops|cloud|learn|training|training/browse|community|insights|perspectives|"
    r"think|index\.html|home|login|subscribe|l/products|what-we-do/entertainment|"
    r"service/payment-methods|category/asia|idira|cloud-foundation|products/nginx|"
    r"products/continuous-delivery|products/ai-sre|solutions/observability-for-developers|"
    r"en/blog/channel/open-source-communities|en/blog/channel/red-hat-ansible-automation|"
    r"en/technologies/management/ansible|en_us/about-splunk/acquisitions/splunk-on-call\.html|"
    r"en_us/appdynamics-joins-splunk\.html|observability|cloud-guru|releases|demos|juju|"
    r"selenium|garage|capabilities/ci-cd-workflows|topic/development|software-development)?/?$",
    re.IGNORECASE,
)


def is_invalid_or_generic_redirect(original_url: str, final_url: str, response_text: str = "") -> Tuple[bool, str]:
    """
    Validates whether a redirect from `original_url` to `final_url` (or `final_url` itself)
    is a soft-404, login wall, domain-parking/spam page, or a precision-destroying
    generic homepage/hub redirect.
    Returns (is_invalid: bool, reason: str).
    """
    from urllib.parse import urlparse
    if not final_url:
        return True, "empty_url"

    f_lower = final_url.lower()
    for bad_sub in INVALID_REDIRECT_SUBSTRINGS:
        if bad_sub in f_lower:
            return True, f"soft_404_or_login_redirect ({bad_sub})"
    if re.search(r"(?:^|/)(?:404(?:\.html?|\.php|\.aspx)?)(?:/|$|\?)", urlparse(final_url).path.lower()):
        return True, "soft_404_or_login_redirect (/404)"

    if response_text:
        t_lower = response_text[:15000].lower()
        if any(pk in t_lower for pk in PARKING_TEXT_INDICATORS):
            return True, "parked_domain"

    p_final = urlparse(final_url)
    # Reject missing-slash domain corruption like https://blog.openshift.comintroduction-...
    if re.search(r"\.(com|io|org|net|dev)[a-z0-9]{3,}-", p_final.netloc.lower()):
        return True, "corrupted_domain_missing_slash"

    if not original_url:
        return False, "OK"

    u_clean = sanitize_trailing_slashes(original_url)
    f_clean = sanitize_trailing_slashes(final_url)
    if u_clean.lower() == f_clean.lower():
        return False, "OK"

    p_orig = urlparse(u_clean)
    orig_path = p_orig.path.rstrip("/")
    final_path = p_final.path.rstrip("/")

    orig_segs = [s for s in orig_path.split("/") if s and s.lower() not in ("en", "en-us", "en-gb", "es", "fr", "de")]
    final_segs = [s for s in final_path.split("/") if s and s.lower() not in ("en", "en-us", "en-gb", "es", "fr", "de")]

    # If the original URL was a specific deep link (>= 1 meaningful segment) and redirected to a generic root/hub path
    if len(orig_segs) >= 1:
        if GENERIC_REDIRECT_PATH_RE.match(final_path):
            return True, "generic_redirect_loss"
        if len(orig_segs) >= 2 and len(final_segs) == 0:
            return True, "generic_redirect_loss"
        if any(kw in final_path.lower() for kw in ("/training/browse", "/page-removed", "/page-not-found", "/login")):
            return True, "generic_redirect_loss"

    return False, "OK"

def normalize_url(url: str) -> str:
    """
    Normalización de URLs de alta precisión para Nubenetes.
    Preserva anclajes de línea (#L) y evita forzar minúsculas en rutas profundas.
    """
    if not url: return ""
    
    # 0. Mandate 34: Cleanup redundant slashes first
    url = sanitize_trailing_slashes(url)
    
    # 1. Separar fragmento (pero preservar si es técnico como #L123)
    fragment = ""
    if "#" in url:
        url, fragment = url.split("#", 1)
        if not re.match(r'^L\d+', fragment): fragment = "" # Solo preservamos anclajes de línea
    
    # 2. Limpiar parámetros de tracking social (UTM, etc.)
    # Mandate 24: Systematically remove trackers (X.com, LinkedIn, RedHat intcmp)
    url = re.sub(r'(\?|&)(utm_[^&]+|s=[^&]+|t=[^&]+|ref=[^&]+|fbclid=[^&]+|intcmp=[^&]+|mc_cid=[^&]+|mc_eid=[^&]+)', '', url)
    # Mandate 34: Remove all trailing slashes and question marks for internal canonical comparison
    url = url.rstrip("/").rstrip("?")
    
    # 3. Normalizar protocolo y dominio (Case Insensitive)
    match = re.match(r'^(https?://)([^/]+)(.*)', url, re.IGNORECASE)
    if match:
        proto, domain, path = match.groups()
        # El dominio es Case-Insensitive, el path puede ser Case-Sensitive
        url = f"https://{domain.lower()}{path}"
    
    return f"{url}#{fragment}" if fragment else url

def is_fuzzy_duplicate(url_a: str, url_b: str) -> bool:
    return normalize_url(url_a) == normalize_url(url_b)
class GeminiQuotaExhausted(Exception):
    pass

def handle_retry_error(retry_state):
    import sys
    exc = retry_state.outcome.exception()
    log_event(f"  [🚨] CIRCUIT BREAKER TRIPPED: Tenacity exhausted retries. Exception: {exc}")
    log_event("  Emitting exit code 42.")
    sys.exit(42)

@retry(
    stop=stop_after_attempt(3),
    wait=wait_exponential(multiplier=2, min=4, max=60),
    retry=retry_if_exception_type(GeminiQuotaExhausted),
    retry_error_callback=handle_retry_error
)
async def call_gemini_with_retry(prompt: str, response_format: str = "json", max_retries: int = 3, prefer_flash: bool = False, use_grounding: bool = False, role: str = "General"):
    global CURRENT_KEY_INDEX, GLOBAL_COOLDOWN_UNTIL
    
    if os.environ.get("MOCK_DEBATE") == "true":
        log_event(f"    [MOCK AI] Intercepted call for role '{role}' in mock mode.")
        if "Analyst-Fast" in role or "Analyst-Grounded" in role:
            results = []
            for line in prompt.splitlines():
                line = line.strip()
                match = re.match(r'^(\d+)\.\s+(.*?)\s+\((https?://.*?)\)', line)
                if match:
                    idx = int(match.group(1))
                    title = match.group(2)
                    url = match.group(3)
                    stars = 3
                    if "awesome" in title.lower() or "best" in title.lower():
                        stars = 5
                    elif "operator" in title.lower() or "kubernetes" in title.lower():
                        stars = 4
                    results.append({
                        "idx": idx,
                        "year": "2026",
                        "stars": stars,
                        "hierarchy": ["Platform", "Reference"],
                        "tags": ["Resource", "Documentation"],
                        "summary": f"A curated reference on {title} for modern cloud native architectures.",
                        "language": "English",
                        "type": "Reference",
                        "complexity": "Intermediate",
                        "is_microservice": False
                    })
            return {"results": results}
        
        elif "Curator" in role:
            results = []
            for line in prompt.splitlines():
                line = line.strip()
                match = re.match(r'^-\s+(https?://[^\s:]+):', line)
                if match:
                    url = match.group(1)
                    results.append({
                        "url": url,
                        "impact_score": 60,
                        "reputation_penalty": False,
                        "reputation_summary": "Clean reputation on community channels.",
                        "pub_date": "2026-01-01",
                        "primary_category": "Kubernetes",
                        "suggested_new_category": "Kubernetes",
                        "title": "Reference Resource",
                        "desc": "A validated Cloud Native resource.",
                        "en_summary": "A high-density reference guide containing validated implementation practices.",
                        "language": "English",
                        "type": "Reference",
                        "level": "Intermediate",
                        "technical_hierarchy": ["Kubernetes"],
                        "tags": ["RESOURCE", "DOCKER"],
                        "is_microservice": False
                    })
            return results
            
        elif "Link-Rescue" in role:
            results = []
            for line in prompt.splitlines():
                line = line.strip()
                match = re.match(r'^-\s+(.*?)\s*\|\s*(https?://[^\s]+)', line)
                if match:
                    title = match.group(1)
                    url = match.group(2)
                    results.append({
                        "old_url": url,
                        "new_url": url
                    })
            return results

        elif "PR-Guardian" in role:
            return "APPROVED\nNo violations found. Compliance with Nubenetes standards is 100%."

        if response_format == "json":
            return {}
        else:
            return "APPROVED"

    if not GEMINI_API_KEYS: raise ValueError("No GEMINI_API_KEYS configured.")
    
    models_pool = await discover_optimal_models()
    diagnostics = GeminiDiagnostics()
    consecutive_429s = 0
    base_wait_time = 2.0
    
    # 1. Smart Filtering and Re-ordering
    if use_grounding:
        # For grounding, we MANDATE Pro models as they have superior search/reasoning capabilities
        models = [m for m in models_pool if "pro" in m]
        if not models:
            models = ["gemini-1.5-pro", "gemini-1.5-pro-latest"]
    elif prefer_flash:
        # Strict filter: Only allow flash/lite models
        models = [m for m in models_pool if "flash" in m or "lite" in m]
        if not models:
            models = ["gemini-1.5-flash", "gemini-1.5-flash-latest"]
    else:
        models = models_pool

    total_keys = len(GEMINI_API_KEYS)
    
    async with GLOBAL_AI_SEMAPHORE:
        for attempt_round in range(max_retries + 1):
            now = time.time()
            if now < GLOBAL_COOLDOWN_UNTIL:
                await asyncio.sleep(GLOBAL_COOLDOWN_UNTIL - now)

            for key_offset in range(total_keys):
                current_idx = (CURRENT_KEY_INDEX + key_offset) % total_keys
                api_key = GEMINI_API_KEYS[current_idx]
                key_label = GEMINI_API_KEYS_DATA[current_idx]["label"]
                
                async with httpx.AsyncClient() as client:
                    # Limit the number of models to try per key to avoid excessive timeouts
                    for model in models[:5]:
                        if THROTTLED_MODELS.get(f"{current_idx}_{model}", 0) > time.time():
                            continue
                        
                        # Mandate 13: Detailed tracing for long-running workflows
                        # log_event(f"    [AI] Attempt: Key {current_idx+1} ({key_label}) | Model: {model}")

                        full_model_name = f"models/{model}"
                        api_url = f"https://generativelanguage.googleapis.com/{GEMINI_API_VERSION}/{full_model_name}:generateContent?key={api_key}"
                        
                        try:
                            # --- TOOL ENABLING (MCP-LIKE GROUNDING) ---
                            payload = {
                                "contents": [{"parts": [{"text": prompt}]}],
                                "tools": [{"google_search": {}}] if use_grounding else []
                            }
                            
                            # TELEMETRY: Log Payload Size
                            payload_size = len(json.dumps(payload))
                            log_event(f"    [TELEMETRY] Attempting Key {current_idx+1} | Model: {model} | Payload: ~{payload_size//4} tokens")
                            
                            response = await client.post(api_url, json=payload, timeout=180.0)
                            
                            resp_json = {}
                            try: resp_json = response.json()
                            except Exception as e:
                                log_event(f"[WARN] parse Gemini response JSON: {str(e)[:100]}")
                            
                            usage = resp_json.get("usageMetadata", {})
                            SESSION_TRACKER.track_call(current_idx, model, response.status_code, usage, role=role)
                            
                            if response.status_code == 200:
                                log_event(f"    [AI] Success: Key {current_idx+1} | Model: {model} | Role: {role} | Tokens: P={usage.get('promptTokenCount',0)} C={usage.get('candidatesTokenCount',0)}")
                                CURRENT_KEY_INDEX = current_idx
                                if 'candidates' in resp_json and resp_json['candidates']:
                                    text_resp = resp_json['candidates'][0]['content']['parts'][0]['text']
                                    if response_format == "json":
                                        match = re.search(r'\{.*\}|\[.*\]', text_resp, re.DOTALL)
                                        if match:
                                            try:
                                                data = json.loads(match.group(0))
                                                return data
                                            except Exception as e:
                                                log_event(f"[WARN] parse Gemini content JSON for model {model}: {str(e)[:100]}")
                                        
                                        # QUALITY UPGRADE: If flash failed parsing, don't give up on the key, try a Pro model
                                        if ("flash" in model or "lite" in model) and any("pro" in m for m in models):
                                            diagnostics.add_attempt(model, 200, "Flash JSON error - Upgrading to Pro...")
                                            continue 
                                            
                                        diagnostics.add_attempt(model, 200, "JSON not found")
                                        break 
                                    return text_resp
                                diagnostics.add_attempt(model, 200, "No candidates")
                                break 
                                
                            elif response.status_code == 429:
                                consecutive_429s += 1
                                
                                # TELEMETRY: Log Exact Rejection Reason
                                log_event(f"    [TELEMETRY] 429 Details: {response.text[:200]}")
                                
                                # 2. ADAPTIVE TIERING: Mark this specific model as throttled
                                throttle_duration = 30 if "pro" in model else 15
                                THROTTLED_MODELS[f"{current_idx}_{model}"] = time.time() + throttle_duration
                                
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
                                log_event(f"    [TELEMETRY] Server Error {response.status_code}: {response.text[:200]}")
                                diagnostics.add_attempt(model, response.status_code, "Server Error")
                                continue 
                            else:
                                log_event(f"    [TELEMETRY] Unknown Error {response.status_code}: {response.text[:200]}")
                                diagnostics.add_attempt(model, response.status_code, "API Error", response.text)
                                break 
                                
                        except Exception as e:
                            log_event(f"    [TELEMETRY] Exception during request: {type(e).__name__} - {e}")
                            SESSION_TRACKER.track_call(current_idx, model, 0, {}, role=role)
                            diagnostics.add_attempt(model, 0, str(e))
                            break 
        
        if attempt_round < max_retries:
            wait_round = base_wait_time * (2 ** attempt_round)
            log_event(f"  [!] Exhausted tier options in round {attempt_round+1}. Cooling down {wait_round}s...")
            await asyncio.sleep(wait_round)

    log_event("  [!] QUOTA EXHAUSTED: All keys and models rate-limited. Triggering Tenacity backoff...")
    raise GeminiQuotaExhausted(f"Critical Gemini failure after adaptive tiering.\n{diagnostics.get_report()}")

async def fetch_youtube_metadata(url: str) -> Optional[Dict]:
    """
    Fetches high-fidelity basic metadata (title, description) from a YouTube page.
    Prioritizes Official YouTube Data API v3 if YOUTUBE_API_KEY is available.
    Fallbacks to yt-dlp and eventually standard fetch.
    """
    from src.config import YOUTUBE_API_KEY
    
    # Extract Video ID
    vid = None
    if "/embed/" in url: vid = url.split("/embed/")[-1].split("?")[0]
    elif "youtu.be/" in url: vid = url.split("youtu.be/")[-1].split("?")[0]
    elif "v=" in url: vid = url.split("v=")[-1].split("&")[0]
    
    if not vid: return None

    # STRATEGY 1: Official YouTube Data API v3 (Guaranteed success)
    if YOUTUBE_API_KEY:
        try:
            api_url = f"https://www.googleapis.com/youtube/v3/videos?part=snippet&id={vid}&key={YOUTUBE_API_KEY}"
            async with httpx.AsyncClient() as client:
                resp = await client.get(api_url, timeout=10.0)
                if resp.status_code == 200:
                    data = resp.json()
                    if data.get("items"):
                        snippet = data["items"][0]["snippet"]
                        log_event(f"    [YT-API] Success for {vid}: {snippet.get('title')}")
                        return {
                            "raw_title": snippet.get("title", "").strip(),
                            "raw_description": snippet.get("description", "").strip()[:3000]
                        }
        except Exception as e:
            log_event(f"    [YT-API] Failed for {vid}: {e}")

    # STRATEGY 2: Robust Extraction (yt-dlp)
    try:
        import yt_dlp
        from youtube_transcript_api import YouTubeTranscriptApi
        
        ydl_opts = {
            'quiet': True,
            'skip_download': True,
            'force_generic_extractor': False,
            'no_warnings': True,
            'extractor_args': {
                'youtube': {
                    'player_client': ['android', 'web_embedded'],
                    'skip': ['dash', 'hls']
                }
            }
        }

        # Extract basic info
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=False)
            title = info.get('title', 'YouTube Video')
            description = info.get('description', '')

        # Attempt to get transcript
        transcript_text = ""
        try:
            transcript = YouTubeTranscriptApi.get_transcript(vid, languages=['en', 'es'])
            transcript_text = " ".join([t['text'] for t in transcript[:100]])
        except Exception as e:
            log_event(f"[WARN] fetch YouTube transcript for {vid}: {str(e)[:100]}")

        full_description = f"{description}\n\n[Transcript Snippet]: {transcript_text}" if transcript_text else description

        return {
            "raw_title": title.strip(),
            "raw_description": full_description.strip()[:3000]
        }
    except Exception as e:
        log_event(f"    [!] Robust fetch failed for {url}: {e}")
        return None
