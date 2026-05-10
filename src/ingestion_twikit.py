import asyncio
import os
import re
import random
import json
import aiohttp
from datetime import datetime
from twikit import Client
from src.config import MADRID_TZ, TWITTER_USERNAME, TWITTER_EMAIL, TWITTER_PASSWORD

class SocialDataExtractor:
    def __init__(self, target_account: str = "nubenetes"):
        self.client = Client('en-US')
        self.target_account = target_account
        self.cookies_file = 'cookies.json'
        self.timeout = aiohttp.ClientTimeout(total=40)
        self.diagnostics = []
        self.audit_trail = [] # Registro detallado de cada intento
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        ]

    def log_audit(self, method: str, success: Optional[bool], msg: str):
        if success is True: status = "✅ ÉXITO"
        elif success is False: status = "❌ FALLO"
        else: status = "ℹ️ INFO"
        entry = f"**Método: {method}** - {status}: {msg}"
        self.audit_trail.append(entry)
        print(entry)

    def _extract_urls_from_text(self, text: str) -> list[str]:
        url_pattern = re.compile(r'https?://[^\s<>\"]+|www\.[^\s<>\"]+')
        return url_pattern.findall(text)

    async def _authenticate(self) -> bool:
        try:
            # 1. Intentar cargar cookies desde Secreto de GitHub (Prioridad Máxima)
            env_cookies = os.getenv("TWITTER_COOKIES")
            if env_cookies:
                try:
                    raw_data = json.loads(env_cookies)
                    cookies_dict = {}
                    
                    # Convertir formato de extensión (lista) a formato twikit (dict)
                    if isinstance(raw_data, list):
                        for cookie in raw_data:
                            if 'name' in cookie and 'value' in cookie:
                                cookies_dict[cookie['name']] = cookie['value']
                    else:
                        cookies_dict = raw_data

                    # Guardar en el formato que twikit espera
                    with open(self.cookies_file, 'w') as f:
                        json.dump(cookies_dict, f)
                    
                    self.client.load_cookies(self.cookies_file)
                    self.log_audit("Auth Cookies", True, f"Sesión cargada ({len(cookies_dict)} cookies encontradas).")
                    return True
                except Exception as e:
                    self.log_audit("Auth Cookies", False, f"Error procesando formato: {str(e)[:50]}")

            # 2. Intentar cargar cookies locales si existen
            if os.path.exists(self.cookies_file):
                self.client.load_cookies(self.cookies_file)
                return True
            
            # 3. Intentar Login (solo si no hay cookies)
            if not TWITTER_USERNAME or not TWITTER_PASSWORD: return False
            self.log_audit("Twikit Login", None, "Intentando login tradicional...")
            await self.client.login(auth_info_1=TWITTER_USERNAME, auth_info_2=TWITTER_EMAIL, password=TWITTER_PASSWORD)
            self.client.save_cookies(self.cookies_file)
            return True
        except Exception as e:
            self.log_audit("Auth", False, f"Fallo: {str(e)[:100]}")
            return False

    async def _fetch_via_rss(self) -> list[dict]:
        """Estrategia Nueva: RSS Bridge / Nitter RSS (Muy estable)"""
        instances = ["nitter.net", "nitter.cz", "rssbridge.org", "nitter.it"]
        extracted = []
        for inst in instances:
            url = f"https://{inst}/{self.target_account}/rss"
            try:
                async with aiohttp.ClientSession(headers={"User-Agent": random.choice(self.user_agents)}) as session:
                    async with session.get(url, timeout=20) as resp:
                        if resp.status == 200:
                            xml = await resp.text()
                            # Extraer links de <description> o <link>
                            links = re.findall(r'<(?:link|description)>(.*?)</(?:link|description)>', xml)
                            for raw_link in links:
                                found_urls = self._extract_urls_from_text(raw_link)
                                for u in found_urls:
                                    if all(x not in u for x in ["x.com", "twitter.com", "t.co", inst]):
                                        extracted.append({"url": u, "context": f"RSS Feed ({inst})", "timestamp": datetime.now(MADRID_TZ).isoformat()})
                            if extracted:
                                self.log_audit(f"RSS ({inst})", True, f"Encontrados {len(extracted)} enlaces.")
                                return extracted
            except Exception as e:
                self.log_audit(f"RSS ({inst})", False, f"Error: {str(e)[:50]}")
        return []

    async def _fetch_via_wayback(self) -> list[dict]:
        cdx_url = f"https://web.archive.org/cdx/search/cdx?url=twitter.com/{self.target_account}&output=json&limit=5&sort=timestamp:desc"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(cdx_url, timeout=25) as resp:
                    if resp.status == 200:
                        snaps = await resp.json()
                        if len(snaps) > 1:
                            latest_ts = snaps[1][1]
                            snap_url = f"https://web.archive.org/web/{latest_ts}/https://twitter.com/{self.target_account}"
                            async with session.get(snap_url, timeout=30) as snap_resp:
                                html = await snap_resp.text()
                                urls = self._extract_urls_from_text(html)
                                valid = [u for u in set(urls) if all(x not in u for x in ["x.com", "twitter.com", "t.co", "archive.org"])]
                                if valid:
                                    self.log_audit("Wayback Machine", True, f"Recuperados {len(valid)} enlaces de la captura {latest_ts}")
                                    return [{"url": u, "context": "Wayback Machine Archive", "timestamp": datetime.now(MADRID_TZ).isoformat()} for u in valid]
                        self.log_audit("Wayback Machine", False, "No se encontraron snapshots recientes.")
        except Exception as e:
            self.log_audit("Wayback Machine", False, f"Error: {str(e)[:50]}")
        return []

    async def _fetch_via_nitter(self) -> list[dict]:
        instances = ["nitter.net", "nitter.cz", "nitter.privacydev.net", "nitter.d420.me"]
        for inst in instances:
            url = f"https://{inst}/{self.target_account}"
            try:
                async with aiohttp.ClientSession(headers={"User-Agent": random.choice(self.user_agents)}) as session:
                    async with session.get(url, timeout=15) as resp:
                        if resp.status == 200:
                            html = await resp.text()
                            urls = self._extract_urls_from_text(html)
                            valid = [u for u in set(urls) if all(x not in u for x in ["x.com", "twitter.com", "t.co", inst])]
                            if valid:
                                self.log_audit(f"Nitter ({inst})", True, f"Extraídos {len(valid)} enlaces.")
                                return [{"url": u, "context": f"Nitter ({inst})", "timestamp": datetime.now(MADRID_TZ).isoformat()} for u in valid]
                        self.log_audit(f"Nitter ({inst})", False, f"HTTP {resp.status}")
            except: continue
        return []

    async def fetch_links_since(self, since_date: datetime) -> list[dict]:
        all_results = []
        
        # 1. Intentar Twikit Pro
        self.log_audit("Twikit API", False, "Iniciando intento principal...")
        if await self._authenticate():
            try:
                user = await self.client.get_user_by_screen_name(self.target_account)
                tweets = await self.client.get_user_tweets(user.id, 'Tweets')
                if tweets:
                    for t in tweets:
                        txt = t.full_text if hasattr(t, 'full_text') else t.text
                        for u in self._extract_urls_from_text(txt):
                            if "x.com" not in u and "twitter.com" not in u:
                                all_results.append({"url": u, "context": txt, "timestamp": datetime.now(MADRID_TZ).isoformat()})
                    if all_results:
                        self.log_audit("Twikit API", True, f"Extraídos {len(all_results)} enlaces directamente.")
                        return all_results
            except Exception as e:
                self.log_audit("Twikit API", False, f"Fallo en lectura de tweets: {str(e)[:50]}")

        # 2. Intentar RSS (Nuevo y muy resiliente)
        rss_links = await self._fetch_via_rss()
        if rss_links: return rss_links

        # 3. Intentar Nitter
        nitter_links = await self._fetch_via_nitter()
        if nitter_links: return nitter_links

        # 4. Intentar Wayback Machine
        wayback_links = await self._fetch_via_wayback()
        if wayback_links: return wayback_links

        # 5. Intentar Guest Scrape (Último recurso)
        guest_links = await self._fetch_via_guest_scrape()
        if guest_links:
            self.log_audit("Guest Scrape", True, f"Extraídos {len(guest_links)} enlaces.")
            return guest_links
        else:
            self.log_audit("Estrategia Global", False, "Todos los métodos de evasión han sido agotados sin éxito.")
        
        return []

    async def _fetch_via_guest_scrape(self) -> list[dict]:
        url = f"https://x.com/{self.target_account}"
        headers = {"User-Agent": random.choice(self.user_agents), "Accept": "text/html"}
        try:
            async with aiohttp.ClientSession(headers=headers, read_bufsize=2**18, max_line_size=65536) as session:
                async with session.get(url, timeout=20) as response:
                    if response.status == 200:
                        html = await response.text()
                        urls = self._extract_urls_from_text(html)
                        return [{"url": u, "context": "Guest Scrape", "timestamp": datetime.now(MADRID_TZ).isoformat()} 
                                for u in set(urls) if all(x not in u for x in ["x.com", "twitter.com", "t.co"])]
                    self.log_audit("Guest Scrape", False, f"HTTP {response.status}")
        except Exception as e:
            self.log_audit("Guest Scrape", False, str(e)[:50])
        return []
