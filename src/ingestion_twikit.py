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
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
        ]

    def log_audit(self, method: str, success: Optional[bool], msg: str):
        icons = {True: "✅ ÉXITO", False: "❌ FALLO", None: "⚡ INTENTO"}
        entry = f"**{method}** - {icons.get(success, 'ℹ️ INFO')}: {msg}"
        self.audit_trail.append(entry)
        print(entry)

    def _extract_urls_from_text(self, text: str) -> list[str]:
        return list(set(re.findall(r'https?://[^\s<>\"]+|www\.[^\s<>\"]+', text)))

    async def _fetch_via_playwright(self, since_date: datetime) -> list[dict]:
        """Estrategia de Fuerza Bruta: Navegador Real especializado en 'Bookmarks'."""
        try:
            from playwright.async_api import async_playwright
            import playwright_stealth
        except:
            self.log_audit("Playwright", False, "Librerías no disponibles.")
            return []
        
        self.log_audit("Playwright Browser", None, "Buscando referencias en posts reales...")
        results = []
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context(user_agent=self.user_agents[0], locale="es-ES")
                page = await context.new_page()
                
                # Intentar aplicar stealth de forma segura
                try:
                    if hasattr(playwright_stealth, 'stealth_async'): await playwright_stealth.stealth_async(page)
                    elif hasattr(playwright_stealth, 'stealth'): playwright_stealth.stealth(page)
                except: pass
                
                # Inyectar cookies si existen
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

                await page.goto(f"https://x.com/{self.target_account}", wait_until="networkidle", timeout=60000)
                await asyncio.sleep(10)
                
                # Extraer de posts (artículos) para evitar ruidos de sistema
                for _ in range(12): # Scroll más profundo
                    articles = await page.query_selector_all('article[data-testid="tweet"]')
                    for article in articles:
                        # 1. Extraer texto del tweet
                        text_el = await article.query_selector('[data-testid="tweetText"]')
                        tweet_text = await text_el.inner_text() if text_el else ""
                        
                        # 2. Extraer enlaces explícitos del texto y de las Cards
                        links = await article.query_selector_all('a')
                        found_in_tweet = []
                        for link in links:
                            href = await link.get_attribute('href')
                            if href and href.startswith('http'):
                                # Filtrar internos de X/Twitter
                                if all(x not in href for x in ["x.com", "twitter.com", "t.co", "abs.twimg", "pbs.twimg"]):
                                    found_in_tweet.append(href)
                        
                        # 3. Intentar capturar enlaces 'escondidos' en t.co (si el texto tiene el enlace real)
                        found_in_tweet.extend(self._extract_urls_from_text(tweet_text))
                        
                        for u in set(found_in_tweet):
                            if all(x not in u for x in ["x.com", "twitter.com", "t.co", "archive.org", "help.twitter"]):
                                results.append({
                                    "url": u, "context": tweet_text[:200], 
                                    "timestamp": datetime.now(MADRID_TZ).isoformat(),
                                    "source_type": "X.com (@nubenetes)"
                                })
                    
                    await page.evaluate("window.scrollBy(0, 2000)")
                    await asyncio.sleep(5)
                
                await browser.close()
                # Eliminar duplicados de la lista de resultados
                unique_res = {r['url']: r for r in results}.values()
                return list(unique_res)
        except Exception as e:
            self.log_audit("Playwright", False, str(e)[:60])
        return []

    async def fetch_links_since(self, since_date: datetime) -> list[dict]:
        # Prioridad absoluta a Playwright para posts reales
        play_links = await self._fetch_via_playwright(since_date)
        if play_links: 
            self.log_audit("Estrategia Playwright", True, f"Encontrados {len(play_links)} bookmarks en posts.")
            return play_links

        # Fallback a RSS si Playwright falla (aunque RSS es más ruidoso)
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
                                return [{"url": u, "context": "RSS Feed", "timestamp": datetime.now(MADRID_TZ).isoformat(), "source_type": "X.com (RSS)"} for u in valid]
            except: continue
        return []
