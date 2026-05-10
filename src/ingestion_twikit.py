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
        # Límites de buffer aumentados para evitar errores de lectura de headers grandes
        self.connector = aiohttp.TCPConnector(limit=10)
        self.timeout = aiohttp.ClientTimeout(total=30)
        # User agents modernos, incluyendo móviles para evasión
        self.user_agents = [
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        ]

    async def _authenticate(self) -> bool:
        try:
            # Intentamos obtener la IP para debug en logs
            async with aiohttp.ClientSession(connector=self.connector) as s:
                async with s.get('https://api.ipify.org') as r:
                    ip = await r.text()
                    print(f"[*] IP de ejecución: {ip}")

            if os.path.exists(self.cookies_file):
                self.client.load_cookies(self.cookies_file)
                return True
            
            if not TWITTER_USERNAME or not TWITTER_PASSWORD:
                print("[!] Sin credenciales de X. Intentando modo Guest.")
                return False

            # Espera aleatoria para no parecer bot puro
            await asyncio.sleep(random.uniform(5, 10))
            
            await self.client.login(
                auth_info_1=TWITTER_USERNAME,
                auth_info_2=TWITTER_EMAIL,
                password=TWITTER_PASSWORD
            )
            self.client.save_cookies(self.cookies_file)
            return True
        except Exception as e:
            print(f"[!] Error de acceso a X (Probable bloqueo Cloudflare/WAF): {e}")
            return False

    def _extract_urls_from_text(self, text: str) -> list[str]:
        url_pattern = re.compile(r'https?://[^\s<>\"]+|www\.[^\s<>\"]+')
        return url_pattern.findall(text)

    async def _fetch_via_guest_scrape(self) -> list[dict]:
        """
        Método de último recurso: Scraping de la página pública usando headers móviles.
        Efectivo contra bloqueos básicos de bots en X.com.
        """
        url = f"https://x.com/{self.target_account}"
        headers = {
            "User-Agent": random.choice(self.user_agents[:2]), # Preferir móvil
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
        
        print(f"[*] Intentando extracción Guest (Mobile Bypass) para {self.target_account}...")
        try:
            # Aumentamos los límites del parser de HTTP para manejar headers enormes de X
            async with aiohttp.ClientSession(
                headers=headers, 
                connector=self.connector,
                read_bufsize=2**16 # 64KB buffer
            ) as session:
                # El parámetro 'max_line_size' y 'max_field_size' se pasan al HttpParser vía la sesión
                async with session.get(url, timeout=self.timeout) as response:
                    if response.status != 200:
                        print(f"[!] Error en modo Guest: HTTP {response.status}")
                        return []
                    
                    html = await response.text()
                    extracted_data = []
                    
                    # Estrategia 1: LD+JSON (Suele contener los últimos tweets para SEO)
                    ld_matches = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html)
                    for ld_text in ld_matches:
                        try:
                            ld_data = json.loads(ld_text)
                        except: continue

                    # Estrategia 2: Regex de enlaces status/
                    state_match = re.search(r'window\.__INITIAL_STATE__\s*=\s*({.*?});', html)
                    if state_match:
                        print("[+] Se encontró estado inicial de la página.")
                    
                    urls = self._extract_urls_from_text(html)
                    for url in set(urls):
                        if "x.com" not in url and "twitter.com" not in url and "t.co" not in url:
                            extracted_data.append({
                                "url": url,
                                "context": "Extraído vía Guest Scrape (Mobile Bypass)",
                                "timestamp": datetime.now(MADRID_TZ).isoformat()
                            })
                    
                    return extracted_data
        except Exception as e:
            print(f"[!] Fallo en extracción Guest: {e}")
            return []

    async def fetch_links_since(self, since_date: datetime) -> list[dict]:
        if not await self._authenticate():
            print("[~] Autenticación fallida. Usando modo Guest Scrape.")
            return await self._fetch_via_guest_scrape()

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
