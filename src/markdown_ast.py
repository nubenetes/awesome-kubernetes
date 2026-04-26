import re
import aiohttp
import asyncio
from typing import Tuple, Optional
from fake_useragent import UserAgent

class MarkdownSanitizer:
    def __init__(self):
        self.link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')
        self.ua = UserAgent()
        self.safe_domains = [
            'github.com', 'medium.com', 'dev.to', 'twitter.com', 'x.com', 
            'hashnode.com', 'hashnode.dev', 'linkedin.com', 'dzone.com', 
            'youtube.com', 'aws.amazon.com', 'kubernetes.io', 'cncf.io', 
            'microsoft.com', 'google.com', 'oracle.com', 'redhat.com', 
            'ibm.com', 'stackoverflow.com', 'substack.com', 'vimeo.com',
            'infoq.com', 'reddit.com', 'docker.com', 'terraform.io'
        ]

    async def _check_url_robust(self, session: aiohttp.ClientSession, url: str, retries: int = 3) -> Tuple[bool, Optional[str]]:
        url_lower = url.lower()
        if any(domain in url_lower for domain in self.safe_domains):
            return True, None

        for attempt in range(retries):
            headers = {
                'User-Agent': self.ua.random,
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
                'Accept-Language': 'en-US,en;q=0.5',
                'Referer': 'https://www.google.com/'
            }
            
            try:
                async with session.get(url, timeout=15, allow_redirects=True, headers=headers) as response:
                    if 200 <= response.status < 300:
                        final_url = str(response.url).rstrip('/')
                        original_url = url.split('#')[0].rstrip('/')
                        if final_url != original_url and response.status in [301, 308]:
                            return True, str(response.url)
                        return True, None
                    
                    if response.status == 404:
                        if attempt < retries - 1:
                            await asyncio.sleep(2 * (attempt + 1))
                            continue
                        return False, None
                    
                    # Para 403, 429, 5xx mantenemos el enlace
                    return True, None
                    
            except Exception:
                if attempt < retries - 1:
                    await asyncio.sleep(1 * (attempt + 1))
                    continue
                return True, None
        
        return True, None

    async def sanitize_document(self, markdown_content: str, full_health_check: bool = False) -> Tuple[str, dict]:
        lines = markdown_content.splitlines()
        new_lines = []
        stats = {"fixed": 0, "removed": 0, "duplicates": 0}
        seen_in_file = set()

        if full_health_check:
            connector = aiohttp.TCPConnector(limit=5, ssl=False)
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
                        stats["removed"] += 1
        else:
            for line in lines:
                match = self.link_pattern.search(line)
                if not match:
                    new_lines.append(line)
                    continue
                
                _, url = match.groups()
                clean_url = url.split('#')[0].rstrip('/')
                if clean_url in seen_in_file:
                    stats["duplicates"] += 1
                    continue
                seen_in_file.add(clean_url)
                new_lines.append(line)

        return "\n".join(new_lines), stats

    def inject_curated_link(self, markdown_text: str, category: str, title: str, url: str, description: str) -> str:
        clean_url = url.split('#')[0].rstrip('/')
        if clean_url in markdown_text:
            return markdown_text

        new_entry = f"  - [{title}]({url}) - {description}"
        lines = markdown_text.splitlines()
        
        # Buscar encabezado de categoría con soporte para múltiples formatos
        header_found = False
        for i, line in enumerate(lines):
            if category.lower() in line.lower() and (line.startswith("#") or line.startswith("-")):
                lines.insert(i + 1, new_entry)
                header_found = True
                break
        
        if not header_found:
            lines.append(f"\n## {category}\n")
            lines.append(new_entry)
            
        return "\n".join(lines)
