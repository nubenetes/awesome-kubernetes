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
        self.timeout = aiohttp.ClientTimeout(total=30)
        self.diagnostics = []
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1'
        ]

    def log_diagnostic(self, msg: str):
        print(msg)
        self.diagnostics.append(msg)

    def _extract_urls_from_text(self, text: str) -> list[str]:
        url_pattern = re.compile(r'https?://[^\s<>\"]+|www\.[^\s<>\"]+')
        return url_pattern.findall(text)

    async def _authenticate(self) -> bool:
        try:
            async with aiohttp.ClientSession() as s:
                async with s.get('https://api.ipify.org') as r:
                    ip = await r.text()
                    self.log_diagnostic(f"[*] IP de ejecución: {ip}")

            if os.path.exists(self.cookies_file):
                self.client.load_cookies(self.cookies_file)
                return True
            
            if not TWITTER_USERNAME or not TWITTER_PASSWORD:
                self.log_diagnostic("[!] Sin credenciales de X. Saltando login.")
                return False

            await asyncio.sleep(random.uniform(2, 5))
            await self.client.login(
                auth_info_1=TWITTER_USERNAME,
                auth_info_2=TWITTER_EMAIL,
                password=TWITTER_PASSWORD
            )
            self.client.save_cookies(self.cookies_file)
            return True
        except Exception as e:
            err_msg = str(e)
            self.log_diagnostic(f"[!] Error auth Twikit: {err_msg}")
            return False

    async def _fetch_via_wayback(self, since_date: datetime) -> list[dict]:
        """
        Estrategia Sofisticada 1: Wayback Machine (CDX API).
        Ideal para recuperar tweets cuando X.com bloquea el acceso directo.
        """
        self.log_diagnostic("[*] Intentando recuperación vía Wayback Machine...")
        # Buscamos capturas de la página de perfil desde la fecha solicitada
        cdx_url = f"https://web.archive.org/cdx/search/cdx?url=x.com/{self.target_account}&output=json&limit=5&sort=timestamp:desc"
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(cdx_url, timeout=20) as resp:
                    if resp.status == 200:
                        snapshots = await resp.json()
                        if len(snapshots) > 1:
                            # Tomar la captura más reciente (excluyendo cabecera CDX)
                            latest_ts = snapshots[1][1]
                            snap_url = f"https://web.archive.org/web/{latest_ts}/https://x.com/{self.target_account}"
                            self.log_diagnostic(f"[+] Snapshot encontrado: {snap_url}")
                            
                            async with session.get(snap_url, timeout=30) as snap_resp:
                                html = await snap_resp.text()
                                urls = self._extract_urls_from_text(html)
                                return [{
                                    "url": u, "context": "Wayback Machine Archive",
                                    "timestamp": datetime.now(MADRID_TZ).isoformat()
                                } for u in set(urls) if all(x not in u for x in ["x.com", "twitter.com", "t.co", "archive.org"])]
        except Exception as e:
            self.log_diagnostic(f"[!] Error Wayback: {e}")
        return []

    async def _fetch_via_nitter(self) -> list[dict]:
        """
        Estrategia Sofisticada 2: Nitter Instances (Public mirror sin WAF agresivo).
        """
        instances = ["nitter.net", "nitter.cz", "nitter.privacydev.net"]
        self.log_diagnostic("[*] Intentando extracción vía Nitter Instances...")
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
                                self.log_diagnostic(f"[+] Éxito con instancia {inst}")
                                return [{"url": u, "context": f"Nitter ({inst})", "timestamp": datetime.now(MADRID_TZ).isoformat()} for u in valid]
            except: continue
        return []

    async def fetch_links_since(self, since_date: datetime) -> list[dict]:
        # 1. Intentar Twikit (Modo Pro)
        if await self._authenticate():
            try:
                user = await self.client.get_user_by_screen_name(self.target_account)
                extracted_data = []
                tweets = await self.client.get_user_tweets(user.id, 'Tweets')
                
                fetching = True
                while fetching and tweets:
                    for tweet in tweets:
                        tweet_date = tweet.created_at_datetime.astimezone(MADRID_TZ)
                        if tweet_date < since_date:
                            fetching = False; break
                        
                        full_content = tweet.full_text if hasattr(tweet, 'full_text') else tweet.text
                        for url in self._extract_urls_from_text(full_content):
                            if "x.com" not in url and "twitter.com" not in url:
                                extracted_data.append({"url": url, "context": full_content, "timestamp": tweet_date.isoformat()})
                    if fetching:
                        await asyncio.sleep(random.uniform(2, 5))
                        tweets = await tweets.next()
                if extracted_data: return extracted_data
            except Exception as e:
                self.log_diagnostic(f"[!] Fallo Twikit Extracción: {e}")

        # 2. Fallback Sofisticado 1: Nitter (Espejo Público)
        nitter_links = await self._fetch_via_nitter()
        if nitter_links: return nitter_links

        # 3. Fallback Sofisticado 2: Wayback Machine
        wayback_links = await self._fetch_via_wayback(since_date)
        if wayback_links: return wayback_links

        # 4. Fallback Final: Guest Scrape (ya configurado antes)
        self.log_diagnostic("[~] Usando Guest Scrape como último recurso...")
        return await self._fetch_via_guest_scrape()

    async def _fetch_via_guest_scrape(self) -> list[dict]:
        url = f"https://x.com/{self.target_account}"
        headers = {"User-Agent": random.choice(self.user_agents), "Accept": "text/html"}
        try:
            async with aiohttp.ClientSession(headers=headers, read_bufsize=2**17, max_line_size=65536) as session:
                async with session.get(url, timeout=self.timeout) as response:
                    if response.status == 200:
                        html = await response.text()
                        urls = self._extract_urls_from_text(html)
                        return [{"url": u, "context": "Guest Scrape", "timestamp": datetime.now(MADRID_TZ).isoformat()} 
                                for u in set(urls) if all(x not in u for x in ["x.com", "twitter.com", "t.co"])]
        except: pass
        return []
