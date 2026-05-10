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
        urls = re.findall(r'https?://[^\s<>\"]+|www\.[^\s<>\"]+', text)
        # Filtro de ruido masivo y dominios de marketing/tracking
        noise_domains = [
            "x.com", "twitter.com", "t.co", "abs.twimg", "pbs.twimg", 
            "notoriete-web.com", "google-analytics", "doubleclick", 
            "facebook.com", "linkedin.com/sharing", "buffer.com",
            "help.twitter", "archive.org", "nitter"
        ]
        valid_urls = []
        for u in urls:
            if all(d not in u.lower() for d in noise_domains):
                valid_urls.append(u)
        return list(set(valid_urls))

    async def _fetch_via_playwright(self, since_date: datetime) -> list[dict]:
        """Estrategia de Navegador Real con reintentos y control de tiempo."""
        try:
            from playwright.async_api import async_playwright
            import playwright_stealth
        except:
            self.log_audit("Playwright", False, "Librerías no disponibles.")
            return []
        
        self.log_audit("Playwright Browser", None, f"Buscando posts desde {since_date.date()}...")
        results = []
        
        for attempt in range(2): # 2 Intentos
            try:
                async with async_playwright() as p:
                    browser = await p.chromium.launch(headless=True)
                    context = await browser.new_context(user_agent=self.user_agents[0], locale="es-ES")
                    page = await context.new_page()
                    
                    try:
                        if hasattr(playwright_stealth, 'stealth_async'): await playwright_stealth.stealth_async(page)
                        elif hasattr(playwright_stealth, 'stealth'): playwright_stealth.stealth(page)
                    except: pass
                    
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

                    # Aumentar timeout y usar estrategia de carga más relajada
                    await page.goto(f"https://x.com/{self.target_account}", wait_until="domcontentloaded", timeout=90000)
                    await asyncio.sleep(15) # Tiempo extra para que X renderice el feed
                    
                    stop_scrolling = False
                    scroll_count = 0
                    max_scrolls = 20 # Suficiente para llegar a Oct 2024 si no hay miles de tweets
                    
                    while not stop_scrolling and scroll_count < max_scrolls:
                        articles = await page.query_selector_all('article[data-testid="tweet"]')
                        new_links_found = False
                        
                        for article in articles:
                            # Intentar extraer fecha del tweet
                            time_el = await article.query_selector('time')
                            if time_el:
                                datetime_str = await time_el.get_attribute('datetime')
                                tweet_dt = datetime.fromisoformat(datetime_str.replace('Z', '+00:00')).astimezone(MADRID_TZ)
                                if tweet_dt < since_date:
                                    stop_scrolling = True
                                    break
                            
                            text_el = await article.query_selector('[data-testid="tweetText"]')
                            tweet_text = await text_el.inner_text() if text_el else ""
                            
                            links = await article.query_selector_all('a')
                            found_in_tweet = []
                            for link in links:
                                href = await link.get_attribute('href')
                                if href and href.startswith('http') and all(x not in href for x in ["x.com", "twitter.com", "t.co", "abs.twimg", "pbs.twimg"]):
                                    found_in_tweet.append(href)
                            
                            found_in_tweet.extend(self._extract_urls_from_text(tweet_text))
                            
                            for u in set(found_in_tweet):
                                if all(x not in u for x in ["x.com", "twitter.com", "t.co", "archive.org", "help.twitter"]):
                                    results.append({
                                        "url": u, "context": tweet_text[:200], 
                                        "timestamp": tweet_dt.isoformat() if time_el else datetime.now(MADRID_TZ).isoformat(),
                                        "source_type": "X.com (@nubenetes)"
                                    })
                                    new_links_found = True

                        await page.evaluate("window.scrollBy(0, 2000)")
                        await asyncio.sleep(6)
                        scroll_count += 1
                        if not new_links_found and scroll_count > 5: break # Si no hay nada nuevo en 5 scrolls, parar
                
                await browser.close()
                unique_res = {r['url']: r for r in results}.values()
                return list(unique_res)
                
            except Exception as e:
                self.log_audit("Playwright", False, f"Intento {attempt+1} fallido: {str(e)[:50]}")
                if attempt == 0: await asyncio.sleep(10) # Pausa antes de reintentar
        return []

    async def fetch_links_since(self, since_date: datetime) -> list[dict]:
        play_links = await self._fetch_via_playwright(since_date)
        if play_links: 
            self.log_audit("Estrategia Playwright", True, f"Recuperados {len(play_links)} bookmarks en posts.")
            return play_links

        # Fallback a RSS con logs mejorados
        self.log_audit("RSS Fallback", None, "Consultando puentes RSS por fallo en navegador...")
        bridges = ["rssbridge.org", "rss.idoc.pub", "bridge.the-pankratz.de"]
        for b in bridges:
            url = f"https://{b}/?action=display&bridge=TwitterBridge&context=By+username&user={self.target_account}&format=Mrss"
            try:
                async with aiohttp.ClientSession() as session:
                    async with session.get(url, timeout=25) as resp:
                        if resp.status == 200:
                            xml = await resp.text()
                            urls = self._extract_urls_from_text(xml)
                            valid = [u for u in urls if all(x not in u for x in ["x.com", "twitter.com", "t.co", b])]
                            if valid:
                                self.log_audit(f"RSS-Bridge ({b})", True, f"Encontrados {len(valid)} enlaces.")
                                return [{"url": u, "context": "RSS Feed Fallback", "timestamp": datetime.now(MADRID_TZ).isoformat(), "source_type": "X.com (RSS)"} for u in valid]
                        else:
                            self.log_audit(f"RSS-Bridge ({b})", False, f"HTTP {resp.status}")
            except Exception as e:
                self.log_audit(f"RSS-Bridge ({b})", False, str(e)[:40])
        return []
