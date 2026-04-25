import re
import aiohttp
import asyncio
from typing import Tuple, Optional

class MarkdownSanitizer:
    def __init__(self):
        # Captura [texto](url)
        self.link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')

    async def _check_url_robust(self, session: aiohttp.ClientSession, url: str, retries: int = 3) -> Tuple[bool, Optional[str]]:
        """
        Retorna (is_alive, final_url). 
        Si final_url es distinto a url, significa que hubo una redirección permanente.
        """
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        for attempt in range(retries):
            try:
                async with session.get(url, timeout=20, allow_redirects=True, headers=headers) as response:
                    if response.status < 400:
                        final_url = str(response.url).rstrip('/')
                        original_url = url.split('#')[0].rstrip('/')
                        if final_url != original_url and response.status in [301, 308]:
                            return True, str(response.url) # Actualización recomendada
                        return True, None
                    if response.status >= 500: # Error de servidor, reintentar
                        await asyncio.sleep(2 ** attempt)
                        continue
                    return False, None
            except:
                if attempt < retries - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
        return False, None

    async def sanitize_document(self, markdown_content: str) -> Tuple[str, dict]:
        lines = markdown_content.splitlines()
        new_lines = []
        stats = {"fixed": 0, "removed": 0, "duplicates": 0}
        seen_in_file = set()

        connector = aiohttp.TCPConnector(limit=30)
        async with aiohttp.ClientSession(connector=connector) as session:
            for line in lines:
                match = self.link_pattern.search(line)
                if not match:
                    new_lines.append(line)
                    continue

                text, url = match.groups()
                clean_url = url.split('#')[0].rstrip('/')

                # 1. Check Duplicados dentro del mismo archivo
                if clean_url in seen_in_file:
                    stats["duplicates"] += 1
                    continue # Eliminar duplicado literal
                
                # 2. Check Salud e Inteligencia de redirección
                is_alive, new_url = await self._check_url_robust(session, url)
                
                if is_alive:
                    seen_in_file.add(clean_url)
                    if new_url: # El enlace se ha movido permanentemente
                        line = line.replace(url, new_url)
                        stats["fixed"] += 1
                    new_lines.append(line)
                else:
                    stats["removed"] += 1
                    # No añadimos la línea, por lo que se elimina

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
