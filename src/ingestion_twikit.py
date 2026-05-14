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
        icons = {True: "✅ SUCCESS", False: "❌ FAILURE", None: "⚡ ATTEMPT"}
        entry = f"**{method}** - {icons.get(success, 'ℹ️ INFO')}: {msg}"
        self.audit_trail.append(entry)
        log_event(entry)

    def _extract_urls_from_text(self, text: str) -> list[str]:
        urls = re.findall(r'https?://[^\s<>\"]+|www\.[^\s<>\"]+', text)
        noise_domains = [
            "x.com", "twitter.com", "abs.twimg", "pbs.twimg", 
            "notoriete-web.com", "google-analytics", "doubleclick", 
            "facebook.com", "linkedin.com/sharing", "buffer.com",
            "help.twitter", "archive.org", "nitter", "schema.org",
            "fonts.gstatic.com", "fonts.googleapis.com", "w.org",
            "wp.com", "gravatar.com", "xmlrpc.php", "youtube.com/channel",
            "youtube.com/user", "facebook.com/plugins"
        ]
        valid_urls = []
        for u in urls:
            u_lower = u.lower()
            if not any(d in u_lower for d in noise_domains):
                valid_urls.append(u)
        return list(set(valid_urls))

    async def _fetch_via_playwright(self, since_date: datetime, until_date: Optional[datetime] = None, strategy: str = "scroll", accounts: List[str] = None) -> list[dict]:
        if not accounts: accounts = [self.target_account]
        
        try:
            from playwright.async_api import async_playwright
            import playwright_stealth
        except:
            self.log_audit("Playwright", False, "Libraries not available.")
            return []
        
        collected_tweets = {}
        
        try:
            async with async_playwright() as p:
                browser = await p.chromium.launch(headless=True)
                context = await browser.new_context(user_agent=self.user_agents[0], locale="es-ES")
                
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

                for account in accounts:
                    page = await context.new_page()
                    try:
                        if hasattr(playwright_stealth, 'stealth_async'): await playwright_stealth.stealth_async(page)
                        elif hasattr(playwright_stealth, 'stealth'): playwright_stealth.stealth(page)
                    except: pass

                    if strategy == "search":
                        import urllib.parse
                        search_query = f"from:{account} since:{since_date.date().isoformat()}"
                        if until_date: search_query += f" until:{until_date.date().isoformat()}"
                        target_url = f"https://x.com/search?q={urllib.parse.quote(search_query)}&f=live"
                    else:
                        target_url = f"https://x.com/{account}"

                    self.log_audit(f"Playwright ({account})", None, f"Navigating to {target_url}")
                    try:
                        await page.goto(target_url, wait_until="load", timeout=60000)
                        await asyncio.sleep(5)
                        
                        stop_scrolling = False
                        scroll_count = 0
                        max_scrolls = 20
                        
                        while not stop_scrolling and scroll_count < max_scrolls:
                            articles = await page.query_selector_all('article[data-testid="tweet"]')
                            if not articles and scroll_count > 2: break

                            for article in articles:
                                time_el = await article.query_selector('time')
                                if not time_el: continue
                                
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
                                    if href and href.startswith('http') and not any(x in href.lower() for x in ["x.com", "twitter.com"]):
                                        found_in_tweet.append(href)
                                
                                found_in_tweet.extend(self._extract_urls_from_text(tweet_text))
                                
                                for u in set(found_in_tweet):
                                    if u not in collected_tweets:
                                        collected_tweets[u] = {
                                            "url": u, "context": tweet_text[:200], 
                                            "timestamp": tweet_dt.isoformat(),
                                            "source_type": f"X.com ({account})"
                                        }
                            
                            if stop_scrolling: break
                            await page.evaluate("window.scrollBy(0, 4000)")
                            await asyncio.sleep(3)
                            scroll_count += 1
                    except Exception as e:
                        self.log_audit(f"Playwright ({account})", False, f"Error: {str(e)[:50]}")
                    
                    await page.close()
                
                await browser.close()
                results = list(collected_tweets.values())
                results.sort(key=lambda x: x["timestamp"])
                return results
                
        except Exception as e:
            self.log_audit("Playwright Multi", False, str(e)[:100])
        return []

    async def fetch_links_since(self, since_date: datetime, until_date: Optional[datetime] = None, strategy: str = "scroll", accounts: List[str] = None) -> list[dict]:
        play_links = await self._fetch_via_playwright(since_date, until_date=until_date, strategy=strategy, accounts=accounts)
        if play_links: 
            self.log_audit("Playwright Strategy", True, f"Retrieved {len(play_links)} links from accounts: {', '.join(accounts) if accounts else self.target_account}")
            return play_links
        return []
