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
        self.timeout = aiohttp.ClientTimeout(total=50)
        self.audit_trail = []
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_5 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1'
        ]

    def log_audit(self, method: str, success: Optional[bool], msg: str):
        icons = {True: "✅ ÉXITO", False: "❌ FALLO", None: "⚡ INTENTO"}
        entry = f"**{method}** - {icons.get(success, 'ℹ️ INFO')}: {msg}"
        self.audit_trail.append(entry)
        print(entry)

    def _extract_urls_from_text(self, text: str) -> list[str]:
        return list(set(re.findall(r'https?://[^\s<>\"]+|www\.[^\s<>\"]+', text)))

    async def _fetch_via_playwright(self, since_date: datetime) -> list[dict]:
        """Estrategia de Fuerza Bruta: Navegador Real."""
        try:
            from playwright.async_api import async_playwright
            try:
                from playwright_stealth import stealth_async as stealth
            except ImportError:
                from playwright_stealth import stealth # Fallback a nombre de función común
        except ImportError:
            self.log_audit("Playwright", False, "Librerías no disponibles.")
            return []
        
        self.log_audit("Playwright Browser", None, "Lanzando instancia Chromium...")
        results = []
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context(user_agent=self.user_agents[0])
                page = await context.new_page()
                
                try:
                    await stealth(page)
                except:
                    self.log_audit("Playwright", None, "Aviso: No se pudo aplicar modo stealth.")
                
                env_cookies = os.getenv("TWITTER_COOKIES")
                if env_cookies:
                    try:
                        cookies = json.loads(env_cookies)
                        formatted = []
                        for c in cookies:
                            if isinstance(c, dict) and 'name' in c and 'value' in c:
                                c['domain'] = c.get('domain', '.x.com')
                                for k in ['sameSite', 'storeId', 'id']: c.pop(k, None)
                                formatted.append(c)
                        await context.add_cookies(formatted)
                    except: pass

                await page.goto(f"https://x.com/{self.target_account}", wait_until="domcontentloaded", timeout=60000)
                await asyncio.sleep(8)
                
                for _ in range(4): # Scroll moderado
                    html = await page.content()
                    urls = self._extract_urls_from_text(html)
                    for u in urls:
                        if all(x not in u for x in ["x.com", "twitter.com", "t.co", "abs.twimg", "archive.org"]):
                            results.append({"url": u, "context": "Playwright Browser", "timestamp": datetime.now(MADRID_TZ).isoformat()})
                    await page.evaluate("window.scrollBy(0, 1200)")
                    await asyncio.sleep(4)
                
                await browser.close()
                return results
        except Exception as e:
            self.log_audit("Playwright", False, str(e)[:60])
        return []

    async def fetch_links_since(self, since_date: datetime) -> list[dict]:
        # 1. Intentar Playwright (Navegador Real)
        play_links = await self._fetch_via_playwright(since_date)
        if play_links: 
            self.log_audit("Estrategia Playwright", True, f"Recuperados {len(play_links)} enlaces vía DOM.")
            return play_links

        # 2. RSS-Bridge Fallback (Efectivo y rápido)
        self.log_audit("RSS Fallback", None, "Consultando puentes RSS...")
        bridges = ["rssbridge.org", "rss.idoc.pub", "bridge.the-pankratz.de"]
        for b in bridges:
            url = f"https://{b}/?action=display&bridge=TwitterBridge&context=By+username&user={self.target_account}&format=Mrss"
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, timeout=20) as resp:
                        if resp.status == 200:
                            urls = self._extract_urls_from_text(await resp.text())
                            valid = [u for u in urls if all(x not in u for x in ["x.com", "twitter.com", "t.co", b])]
                            if valid:
                                self.log_audit(f"RSS-Bridge ({b})", True, f"Encontrados {len(valid)} enlaces.")
                                return [{"url": u, "context": "RSS", "timestamp": datetime.now(MADRID_TZ).isoformat()} for u in valid]
            except: continue

        # 3. Wayback Deep Fallback (Histórico profundo)
        self.log_audit("Wayback Fallback", None, "Buscando histórico en Archive.org...")
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
                                    self.log_audit("Wayback", True, f"Recuperados {len(valid)} históricos.")
                                    return [{"url": u, "context": "Wayback", "timestamp": datetime.now(MADRID_TZ).isoformat()} for u in valid]
        except: pass
        return []
