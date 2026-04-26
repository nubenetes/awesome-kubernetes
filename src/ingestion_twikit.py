import asyncio
import os
import re
import random
import aiohttp
from datetime import datetime
from twikit import Client
from src.config import MADRID_TZ, TWITTER_USERNAME, TWITTER_EMAIL, TWITTER_PASSWORD

class SocialDataExtractor:
    def __init__(self, target_account: str = "nubenetes"):
        self.client = Client('en-US')
        self.target_account = target_account
        self.cookies_file = 'cookies.json'
        self.user_agents = [
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36',
            'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36'
        ]

    async def _authenticate(self) -> bool:
        try:
            # Intentamos obtener la IP para debug en logs
            async with aiohttp.ClientSession() as s:
                async with s.get('https://api.ipify.org') as r:
                    ip = await r.text()
                    print(f"[*] IP de ejecución: {ip}")

            if os.path.exists(self.cookies_file):
                self.client.load_cookies(self.cookies_file)
                return True
            
            if not TWITTER_USERNAME or not TWITTER_PASSWORD:
                return False

            # Espera aleatoria para no parecer bot puro
            await asyncio.sleep(random.uniform(5, 10))
            
            # Twikit no permite pasar UA directamente en login de forma fácil, 
            # pero el cliente interno sí lo usa.
            await self.client.login(
                auth_info_1=TWITTER_USERNAME,
                auth_info_2=TWITTER_EMAIL,
                password=TWITTER_PASSWORD
            )
            self.client.save_cookies(self.cookies_file)
            return True
        except Exception as e:
            print(f"[!] Error de acceso a X (Probable bloqueo Cloudflare): {e}")
            return False

    def _extract_urls_from_text(self, text: str) -> list[str]:
        url_pattern = re.compile(r'https?://[^\s<>\"]+|www\.[^\s<>\"]+')
        return url_pattern.findall(text)

    async def fetch_links_since(self, since_date: datetime) -> list[dict]:
        if not await self._authenticate():
            print("[~] Continuando sin datos de X debido al bloqueo.")
            return []

        try:
            user = await self.client.get_user_by_screen_name(self.target_account)
            extracted_data = []
            tweets = await self.client.get_user_tweets(user.id, 'Tweets')
            
            fetching = True
            while fetching and tweets:
                for tweet in tweets:
                    tweet_date = tweet.created_at_datetime.astimezone(MADRID_TZ)
                    if tweet_date < since_date:
                        fetching = False
                        break
                    
                    full_content = tweet.full_text if hasattr(tweet, 'full_text') else tweet.text
                    urls = self._extract_urls_from_text(full_content)
                    
                    for url in urls:
                        if "x.com" not in url and "twitter.com" not in url:
                            extracted_data.append({
                                "url": url,
                                "context": full_content,
                                "timestamp": tweet_date.isoformat()
                            })
                if fetching:
                    await asyncio.sleep(random.uniform(2, 5))
                    tweets = await tweets.next()
            return extracted_data
        except Exception as e:
            print(f"[!] Fallo extrayendo tweets: {e}")
            return []
