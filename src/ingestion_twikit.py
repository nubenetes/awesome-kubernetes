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
        # No compartimos el conector para evitar "Session is closed" tras cerrar una sesión previa
        self.timeout = aiohttp.ClientTimeout(total=30)
        self.diagnostics = []
        self.user_agents = [
            'Mozilla/5.0 (iPhone; CPU iPhone OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (iPad; CPU OS 17_4 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.4 Mobile/15E148 Safari/604.1',
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'
        ]

    def log_diagnostic(self, msg: str):
        print(msg)
        self.diagnostics.append(msg)

    async def _authenticate(self) -> bool:
        try:
            # IP Check independiente
            async with aiohttp.ClientSession() as s:
                async with s.get('https://api.ipify.org') as r:
                    ip = await r.text()
                    self.log_diagnostic(f"[*] IP de ejecución: {ip}")

            if os.path.exists(self.cookies_file):
                self.client.load_cookies(self.cookies_file)
                return True
            
            if not TWITTER_USERNAME or not TWITTER_PASSWORD:
                self.log_diagnostic("[!] Sin credenciales de X. Intentando modo Guest.")
                return False

            await asyncio.sleep(random.uniform(5, 10))
            await self.client.login(
                auth_info_1=TWITTER_USERNAME,
                auth_info_2=TWITTER_EMAIL,
                password=TWITTER_PASSWORD
            )
            self.client.save_cookies(self.cookies_file)
            return True
        except Exception as e:
            err_msg = str(e)
            self.log_diagnostic(f"[!] Error de acceso a X: {err_msg}")
            if "KEY_BYTE" in err_msg:
                self.log_diagnostic("    - Causa: Twikit no pudo obtener claves criptográficas (Bloqueo WAF/JS desafiado).")
            return False

    async def _fetch_via_guest_scrape(self) -> list[dict]:
        url = f"https://x.com/{self.target_account}"
        headers = {
            "User-Agent": random.choice(self.user_agents[:2]),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "en-US,en;q=0.9",
        }
        
        self.log_diagnostic(f"[*] Intentando extracción Guest (Mobile Bypass) para {self.target_account}...")
        try:
            # Aumentamos agresivamente los límites del parser de HTTP
            # max_line_size y max_field_size controlan el tamaño máximo de una cabecera HTTP
            async with aiohttp.ClientSession(
                headers=headers, 
                read_bufsize=2**17,      # 128KB buffer
                max_line_size=65536,     # 64KB por línea de header (X usa CSPs gigantes)
                max_field_size=65536     # 64KB por campo de header
            ) as session:
                async with session.get(url, timeout=self.timeout) as response:
                    if response.status != 200:
                        self.log_diagnostic(f"[!] Error en modo Guest: HTTP {response.status}")
                        return []
                    
                    html = await response.text()
                    extracted_data = []
                    
                    if "Log in to X" in html or "Sign up" in html:
                        self.log_diagnostic("[!] Detectado Login Wall. X requiere login.")
                        self._update_learning("LoginWall")
                    
                    urls = self._extract_urls_from_text(html)
                    valid_urls = [u for u in urls if all(x not in u for x in ["x.com", "twitter.com", "t.co"])]
                    
                    if not valid_urls:
                        self.log_diagnostic("[~] Scrape finalizado: 0 enlaces útiles encontrados.")
                        self._update_learning("NoLinksFound")
                    else:
                        self._update_learning("Success")
                    
                    for url in set(valid_urls):
                        extracted_data.append({
                            "url": url,
                            "context": "Extraído vía Guest Scrape (Mobile Bypass)",
                            "timestamp": datetime.now(MADRID_TZ).isoformat()
                        })
                    
                    return extracted_data
        except Exception as e:
            err_msg = str(e)
            self.log_diagnostic(f"[!] Fallo crítico en extracción Guest: {err_msg}")
            if "8190" in err_msg:
                self._update_learning("HeaderSizeLimit")
            else:
                self._update_learning("TechnicalError")
            return []

    def _update_learning(self, failure_type: str):
        learning_file = "src/memory/health_learning.json"
        try:
            with open(learning_file, 'r+') as f:
                data = json.load(f)
                data["last_x_failure"] = failure_type
                f.seek(0); json.dump(data, f, indent=2); f.truncate()
        except: pass

    async def fetch_links_since(self, since_date: datetime) -> list[dict]:
        # Cargar aprendizaje previo
        learning_file = "src/memory/health_learning.json"
        try:
            with open(learning_file, 'r') as f:
                learning = json.load(f)
                if learning.get("last_x_failure") == "LoginWall":
                    self.log_diagnostic("[*] Memoria: El último run falló por LoginWall. Probando User-Agent alternativo.")
                    self.user_agents.reverse()
        except: pass

        if not await self._authenticate():
            self.log_diagnostic("[~] Autenticación fallida. Usando modo Guest Scrape.")
            links = await self._fetch_via_guest_scrape()
            # Guardar aprendizaje si falló
            if not links:
                try:
                    with open(learning_file, 'r+') as f:
                        data = json.load(f)
                        data["last_x_failure"] = "NoLinksFound"
                        f.seek(0); json.dump(data, f, indent=2); f.truncate()
                except: pass
            return links

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
