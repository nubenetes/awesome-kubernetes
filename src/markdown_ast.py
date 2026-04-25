import re
import aiohttp
import asyncio
from typing import Tuple, Optional

class MarkdownSanitizer:
    def __init__(self):
        # Captura [texto](url)
        self.link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')
        
        # 1. WHITELIST: Dominios de alta confianza que NUNCA se borran.
        # No validamos estos para evitar bloqueos de bots o errores temporales.
        self.safe_domains = [
            'github.com', 'medium.com', 'dev.to', 'twitter.com', 'x.com', 
            'hashnode.com', 'hashnode.dev', 'linkedin.com', 'dzone.com', 
            'youtube.com', 'aws.amazon.com', 'kubernetes.io', 'cncf.io', 
            'microsoft.com', 'google.com', 'oracle.com', 'redhat.com', 
            'ibm.com', 'stackoverflow.com', 'substack.com', 'vimeo.com',
            'infoq.com', 'reddit.com', 'docker.com', 'terraform.io'
        ]

    async def _check_url_robust(self, session: aiohttp.ClientSession, url: str, retries: int = 4) -> Tuple[bool, Optional[str]]:
        """
        Validador conservador de URLs.
        Retorna (is_alive, final_url). 
        """
        url_lower = url.lower()
        
        # Regla de oro: Si está en la whitelist, es válido.
        if any(domain in url_lower for domain in self.safe_domains):
            return True, None

        # Headers realistas para evitar ser detectados como bot básico
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.9',
            'Referer': 'https://www.google.com/'
        }
        
        for attempt in range(retries):
            try:
                # Usamos GET porque muchos sitios bloquean HEAD
                async with session.get(url, timeout=15, allow_redirects=True, headers=headers) as response:
                    if response.status < 400:
                        final_url = str(response.url).rstrip('/')
                        original_url = url.split('#')[0].rstrip('/')
                        # Detectar redirecciones permanentes para limpiar el repo
                        if final_url != original_url and response.status in [301, 308]:
                            print(f"[REDIRECCIÓN] {url} -> {final_url}")
                            return True, str(response.url)
                        return True, None
                    
                    # SOLO borramos si es un 404 confirmado
                    if response.status == 404:
                        if attempt < retries - 1:
                            await asyncio.sleep(2 ** attempt)
                            continue
                        print(f"[BORRADO 404] {url}")
                        return False, None
                    
                    # Ante 403, 401, 429 o 5xx, MANTENEMOS el enlace por seguridad.
                    # Son errores que suelen ser temporales o bloqueos de seguridad al bot.
                    print(f"[AVISO] Saltando validación de {url} por estado {response.status}")
                    return True, None
                    
            except Exception as e:
                if attempt < retries - 1:
                    # Backoff exponencial: 1s, 2s, 4s...
                    await asyncio.sleep(2 ** attempt)
                    continue
                # Si hay timeout persistente, lo mantenemos vivo.
                return True, None
        
        return True, None

    async def sanitize_document(self, markdown_content: str) -> Tuple[str, dict]:
        lines = markdown_content.splitlines()
        new_lines = []
        stats = {"fixed": 0, "removed": 0, "duplicates": 0}
        seen_in_file = set()

        # Limitamos concurrencia para no saturar
        connector = aiohttp.TCPConnector(limit=5)
        async with aiohttp.ClientSession(connector=connector) as session:
            for line in lines:
                match = self.link_pattern.search(line)
                if not match:
                    new_lines.append(line)
                    continue

                text, url = match.groups()
                clean_url = url.split('#')[0].rstrip('/')

                # Limpieza de duplicados en el mismo archivo
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

        return "\n".join(new_lines), stats

    def inject_curated_link(self, markdown_text: str, category: str, title: str, url: str, description: str) -> str:
        # No inyectar si ya existe
        if url.split('#')[0].rstrip('/') in markdown_text:
            return markdown_text

        new_entry = f"  - [{title}]({url}) - {description}"
        lines = markdown_text.splitlines()
        
        # Buscar encabezado de categoría
        for i, line in enumerate(lines):
            if category.lower() in line.lower() and (line.startswith("#") or line.startswith("-")):
                lines.insert(i + 1, new_entry)
                return "\n".join(lines)
        
        # Si no existe la sección, crearla al final
        lines.append(f"\n## {category}\n")
        lines.append(new_entry)
        return "\n".join(lines)
