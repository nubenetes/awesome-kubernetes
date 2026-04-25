import re
import aiohttp
import asyncio
from typing import Tuple, Optional

class MarkdownSanitizer:
    def __init__(self):
        # Captura [texto](url)
        self.link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')
        # Dominios de alta confianza que NUNCA se borran
        self.safe_domains = [
            'github.com', 'medium.com', 'dev.to', 'twitter.com', 'x.com', 
            'hashnode.com', 'linkedin.com', 'dzone.com', 'youtube.com',
            'aws.amazon.com', 'kubernetes.io', 'cncf.io', 'microsoft.com',
            'google.com', 'oracle.com', 'redhat.com', 'ibm.com', 'stackoverflow.com'
        ]

    async def _check_url_robust(self, session: aiohttp.ClientSession, url: str, retries: int = 5) -> Tuple[bool, Optional[str]]:
        """
        Retorna (is_alive, final_url). 
        Implementa User-Agent realista y backoff exponencial.
        """
        if any(domain in url.lower() for domain in self.safe_domains):
            return True, None

        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
        }
        
        for attempt in range(retries):
            try:
                # Usamos HEAD primero por eficiencia, si falla probamos GET
                async with session.get(url, timeout=15, allow_redirects=True, headers=headers) as response:
                    if response.status < 400:
                        final_url = str(response.url).rstrip('/')
                        original_url = url.split('#')[0].rstrip('/')
                        if final_url != original_url and response.status in [301, 308]:
                            return True, str(response.url)
                        return True, None
                    
                    if response.status == 429 or response.status >= 500:
                        # Rate limiting o error de servidor: esperar y reintentar
                        await asyncio.sleep((2 ** attempt) + 1)
                        continue
                    
                    # Si es un error 404/403 definitivo después de varios reintentos
                    return False, None
            except Exception as e:
                if attempt < retries - 1:
                    await asyncio.sleep((2 ** attempt) + 1)
                    continue
        
        # Por defecto, si hay duda (timeout persistente), lo mantenemos vivo
        return True, None

    async def sanitize_document(self, markdown_content: str) -> Tuple[str, dict]:
        lines = markdown_content.splitlines()
        new_lines = []
        stats = {"fixed": 0, "removed": 0, "duplicates": 0}
        seen_in_file = set()

        # Reducimos concurrencia de 30 a 10 para ser más "amigables" con los servidores
        connector = aiohttp.TCPConnector(limit=10)
        async with aiohttp.ClientSession(connector=connector) as session:
            for line in lines:
                match = self.link_pattern.search(line)
                if not match:
                    new_lines.append(line)
                    continue

                text, url = match.groups()
                clean_url = url.split('#')[0].rstrip('/')

                if clean_url in seen_in_file:
                    stats["duplicates"] += 1
                    continue
                
                is_alive, new_url = await self._check_url_robust(session, url)
                
                if is_alive:
                    seen_in_file.add(clean_url)
                    if new_url:
                        line = line.replace(url, new_url)
                        stats["fixed"] += 1
                    new_lines.append(line)
                else:
                    print(f"[-] Eliminando enlace caído confirmado: {url}")
                    stats["removed"] += 1

        return "\n".join(new_lines), stats

    def inject_curated_link(self, markdown_text: str, category: str, title: str, url: str, description: str) -> str:
        # Evitar duplicados antes de inyectar
        if url.split('#')[0].rstrip('/') in markdown_text:
            return markdown_text

        new_entry = f"  - [{title}]({url}) - {description}"
        lines = markdown_text.splitlines()
        
        # Buscar el mejor sitio (debajo del encabezado de la categoría o al final)
        for i, line in enumerate(lines):
            if category.lower() in line.lower() and (line.startswith("#") or line.startswith("-")):
                lines.insert(i + 1, new_entry)
                return "\n".join(lines)
        
        lines.append(f"\n## {category}\n")
        lines.append(new_entry)
        return "\n".join(lines)
