import asyncio
import os
import re
import random
import json
import aiohttp
from typing import List, Dict, Set, Optional
from datetime import datetime
from twikit import Client
from src.config import MADRID_TZ, TWITTER_USERNAME, TWITTER_EMAIL, TWITTER_PASSWORD

class SocialDataExtractor:
    def __init__(self, target_account: str = "nubenetes"):
        self.client = Client('en-US')
        self.target_account = target_account
        self.cookies_file = 'cookies.json'
        self.timeout = aiohttp.ClientTimeout(total=45)
        self.audit_trail = []
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.5 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        ]
        self.nitter_instances = [
            "nitter.net", "nitter.cz", "nitter.it", "nitter.privacydev.net",
            "nitter.d420.me", "nitter.perpmode.com", "nitter.esmailelbob.xyz"
        ]

    def log_audit(self, method: str, success: Optional[bool], msg: str):
        icons = {True: "✅ ÉXITO", False: "❌ FALLO", None: "⚡ INTENTO"}
        entry = f"**{method}** - {icons.get(success, 'ℹ️ INFO')}: {msg}"
        self.audit_trail.append(entry)
        print(entry)

    def _extract_urls_from_text(self, text: str) -> list[str]:
        return list(set(re.findall(r'https?://[^\s<>\"]+|www\.[^\s<>\"]+', text)))

    async def _authenticate(self) -> bool:
        env_cookies = os.getenv("TWITTER_COOKIES")
        if env_cookies:
            try:
                raw_data = json.loads(env_cookies)
                cookies_dict = {c['name']: c['value'] for c in raw_data} if isinstance(raw_data, list) else raw_data
                with open(self.cookies_file, 'w') as f: json.dump(cookies_dict, f)
                self.client.load_cookies(self.cookies_file)
                self.log_audit("Auth Cookies", True, "Sesión inyectada correctamente.")
                return True
            except Exception as e:
                self.log_audit("Auth Cookies", False, str(e)[:50])
        return False

    async def _fetch_via_rss_bridge(self) -> list[dict]:
        bridges = ["rssbridge.org", "rss.idoc.pub", "bridge.the-pankratz.de"]
        for b in bridges:
            url = f"https://{b}/?action=display&bridge=TwitterBridge&context=By+username&user={self.target_account}&format=Mrss"
            try:
                async with aiohttp.ClientSession(headers={"User-Agent": random.choice(self.user_agents)}) as session:
                    async with session.get(url, timeout=20) as resp:
                        if resp.status == 200:
                            urls = self._extract_urls_from_text(await resp.text())
                            valid = [u for u in urls if all(x not in u for x in ["x.com", "twitter.com", "t.co", b])]
                            if valid:
                                self.log_audit(f"RSS-Bridge ({b})", True, f"Encontrados {len(valid)} enlaces.")
                                return [{"url": u, "context": "RSS-Bridge", "timestamp": datetime.now(MADRID_TZ).isoformat()} for u in valid]
            except: continue
        return []

    async def fetch_links_since(self, since_date: datetime) -> list[dict]:
        all_results = []
        target_user_id = "1387348141150670850"
        
        self.log_audit("Twikit API", None, "Intentando bypass con ID directo...")
        if await self._authenticate():
            try:
                tweets = await self.client.get_user_tweets(target_user_id, 'Tweets')
                if tweets:
                    for t in tweets:
                        tweet_date = t.created_at_datetime.astimezone(MADRID_TZ)
                        if tweet_date < since_date: break
                        txt = t.full_text if hasattr(t, 'full_text') else t.text
                        for u in self._extract_urls_from_text(txt):
                            if "x.com" not in u and "twitter.com" not in u:
                                all_results.append({"url": u, "context": txt, "timestamp": tweet_date.isoformat()})
                    if all_results:
                        self.log_audit("Twikit API", True, f"Extraídos {len(all_results)} enlaces.")
                        return all_results
            except Exception as e:
                self.log_audit("Twikit API", False, "Bloqueo KEY_BYTE persistente.")

        links = await self._fetch_via_rss_bridge()
        if links: return links

        self.log_audit("Wayback Deep", None, "Buscando histórico profundo...")
        from_ts = since_date.strftime("%Y%m%d")
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(f"https://web.archive.org/cdx/search/cdx?url=twitter.com/{self.target_account}&output=json&from={from_ts}&limit=5", timeout=20) as resp:
                    if resp.status == 200:
                        snaps = await resp.json()
                        if len(snaps) > 1:
                            latest = snaps[-1][1]
                            async with session.get(f"https://web.archive.org/web/{latest}/https://twitter.com/{self.target_account}") as s_resp:
                                urls = self._extract_urls_from_text(await s_resp.text())
                                valid = [u for u in urls if all(x not in u for x in ["x.com", "twitter.com", "t.co", "archive.org"])]
                                if valid:
                                    self.log_audit("Wayback Deep", True, f"Recuperados {len(valid)} históricos.")
                                    return [{"url": u, "context": "Wayback", "timestamp": datetime.now(MADRID_TZ).isoformat()} for u in valid]
        except: pass

        return []
