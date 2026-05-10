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
        """Estrategia Definitiva: Navegador Real con Playwright."""
        try:
            from playwright.async_api import async_playwright
            from playwright_stealth import stealth_async
        except ImportError:
            self.log_audit("Playwright", False, "Librerías no instaladas.")
            return []
        
        self.log_audit("Playwright Browser", None, "Lanzando navegador real (Stealth Mode)...")
        results = []
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context(user_agent=self.user_agents[0])
                page = await context.new_page()
                await stealth_async(page)
                
                env_cookies = os.getenv("TWITTER_COOKIES")
                if env_cookies:
                    try:
                        cookies = json.loads(env_cookies)
                        formatted_cookies = []
                        for c in cookies:
                            if isinstance(c, dict) and 'name' in c and 'value' in c:
                                # Playwright necesita dominio sin el punto inicial a veces, o con el dominio correcto
                                c['domain'] = c.get('domain', '.x.com')
                                # Eliminar campos incompatibles si existen
                                for k in ['sameSite', 'storeId']: c.pop(k, None)
                                formatted_cookies.append(c)
                        await context.add_cookies(formatted_cookies)
                        self.log_audit("Playwright", True, "Cookies inyectadas.")
                    except: pass

                await page.goto(f"https://x.com/{self.target_account}", wait_until="networkidle", timeout=60000)
                await asyncio.sleep(10)
                
                # Scroll para cargar contenido
                for i in range(3):
                    content = await page.content()
                    urls = self._extract_urls_from_text(content)
                    for u in urls:
                        if all(x not in u for x in ["x.com", "twitter.com", "t.co", "abs.twimg"]):
                            results.append({"url": u, "context": "Playwright Scrape", "timestamp": datetime.now(MADRID_TZ).isoformat()})
                    await page.evaluate("window.scrollBy(0, 1000)")
                    await asyncio.sleep(3)
                
                await browser.close()
                return results
        except Exception as e:
            self.log_audit("Playwright", False, f"Error: {str(e)[:50]}")
        return []

    async def fetch_links_since(self, since_date: datetime) -> list[dict]:
        # 1. Intentar Playwright (Navegador Real)
        play_links = await self._fetch_via_playwright(since_date)
        if play_links: 
            self.log_audit("Estrategia Playwright", True, f"Encontrados {len(play_links)} recursos.")
            return play_links

        # 2. RSS-Bridge Fallback
        self.log_audit("RSS Fallback", None, "Intentando vía RSS-Bridge...")
        bridges = ["rssbridge.org", "rss.idoc.pub"]
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

        return []
