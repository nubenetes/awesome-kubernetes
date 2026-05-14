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

from src.logger import log_event

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
        log_event(entry)

    def _extract_urls_from_text(self, text: str) -> list[str]:
        urls = re.findall(r'https?://[^\s<>\"]+|www\.[^\s<>\"]+', text)
        noise_domains = [
            "x.com", "twitter.com", "abs.twimg", "pbs.twimg", 
            "notoriete-web.com", "google-analytics", "doubleclick", 
            "facebook.com", "linkedin.com/sharing", "buffer.com",
            "help.twitter", "archive.org", "nitter"
        ]
        valid_urls = []
        for u in urls:
            if all(d not in u.lower() for d in noise_domains):
                valid_urls.append(u)
        return list(set(valid_urls))

    async def _fetch_via_playwright(self, since_date: datetime, until_date: Optional[datetime] = None, strategy: str = "scroll") -> list[dict]:
        try:
            from playwright.async_api import async_playwright
            import playwright_stealth
        except:
            self.log_audit("Playwright", False, "Librerías no disponibles.")
            return []
        
        self.log_audit(f"Playwright ({strategy})", None, f"Cronología: Desde {since_date.date()} hasta {until_date.date() if until_date else 'hoy'}.")
        results = []
        
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

                if strategy == "search":
                    import urllib.parse
                    search_query = f"from:{self.target_account} since:{since_date.date().isoformat()}"
                    if until_date:
                        search_query += f" until:{until_date.date().isoformat()}"
                    
                    encoded_query = urllib.parse.quote(search_query)
                    target_url = f"https://x.com/search?q={encoded_query}&f=live"
                    self.log_audit("Advanced Search", None, f"Query: {search_query}")
                else:
                    target_url = f"https://x.com/{self.target_account}"
                    self.log_audit("Profile Scroll", None, "Navegando al muro directo.")

                await page.goto(target_url, wait_until="domcontentloaded", timeout=90000)
                await asyncio.sleep(15)
                
                stop_scrolling = False
                scroll_count = 0
                max_scrolls = 100 # Reducido de 300
                collected_tweets = {} # URL -> tweet_data para evitar duplicados en scroll
                target_link_count = 300 # Reducido de 1000
                
                while not stop_scrolling and scroll_count < max_scrolls:
                    articles = await page.query_selector_all('article[data-testid="tweet"]')
                    
                    if not articles and scroll_count > 3:
                        self.log_audit("Extraction", False, "No se detectan más tweets en el DOM.")
                        break

                    for article in articles:
                        # 1. Ignorar Pinned Posts (Solo en Profile Scroll)
                        if strategy == "scroll":
                            social_context = await article.query_selector('[data-testid="socialContext"]')
                            if social_context:
                                sc_text = await social_context.inner_text()
                                if "Fijado" in sc_text or "Pinned" in sc_text:
                                    continue

                        # 2. Extraer Fecha
                        time_el = await article.query_selector('time')
                        if not time_el: continue
                        
                        datetime_str = await time_el.get_attribute('datetime')
                        tweet_dt = datetime.fromisoformat(datetime_str.replace('Z', '+00:00')).astimezone(MADRID_TZ)
                        
                        if tweet_dt < since_date:
                            self.log_audit("Timeline", True, f"Alcanzado horizonte temporal: {tweet_dt.date()}")
                            stop_scrolling = True
                            break

                        # 3. Extraer Enlaces
                        text_el = await article.query_selector('[data-testid="tweetText"]')
                        tweet_text = await text_el.inner_text() if text_el else ""
                        
                        links = await article.query_selector_all('a')
                        found_in_tweet = []
                        for link in links:
                            href = await link.get_attribute('href')
                            if href and href.startswith('http'):
                                if all(x not in href for x in ["x.com", "twitter.com", "abs.twimg", "pbs.twimg"]):
                                    found_in_tweet.append(href)
                        
                        found_in_tweet.extend(self._extract_urls_from_text(tweet_text))
                        
                        for u in set(found_in_tweet):
                            if u not in collected_tweets:
                                collected_tweets[u] = {
                                    "url": u, "context": tweet_text[:200], 
                                    "timestamp": tweet_dt.isoformat(),
                                    "source_type": f"X.com ({strategy})"
                                }
                                if len(collected_tweets) >= target_link_count:
                                    stop_scrolling = True
                                    break
                        if stop_scrolling: break

                    if stop_scrolling: break
                    # Scroll más agresivo y menos esperas
                    await page.evaluate("window.scrollBy(0, 8000)")
                    await asyncio.sleep(5)
                    scroll_count += 1
                
                if not stop_scrolling and scroll_count >= max_scrolls:
                    self.log_audit("Scrolling", False, f"Alcanzado límite de scrolls ({max_scrolls}) usando {strategy}.")
                
                await browser.close()
                
                # Ordenar por fecha: Antiguos a Recientes
                results = list(collected_tweets.values())
                results.sort(key=lambda x: x["timestamp"])
                return results
                
        except Exception as e:
            self.log_audit("Playwright", False, str(e)[:60])
        return []

    async def fetch_links_since(self, since_date: datetime, until_date: Optional[datetime] = None, strategy: str = "scroll") -> list[dict]:
        play_links = await self._fetch_via_playwright(since_date, until_date=until_date, strategy=strategy)
        if play_links: 
            self.log_audit("Estrategia Playwright", True, f"Recuperados {len(play_links)} bookmarks en el rango {since_date.date()} a {until_date.date() if until_date else 'hoy'}.")
            return play_links

        # Fallback a RSS (menos preciso en fechas, pero útil como respaldo)
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
