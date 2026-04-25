import re
import aiohttp
import asyncio

class MarkdownSanitizer:
    def __init__(self):
        self.link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')

    async def _verify_link_health(self, session: aiohttp.ClientSession, url: str) -> bool:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'}
        try:
            async with session.head(url, timeout=15, allow_redirects=True, headers=headers) as response:
                if response.status < 400:
                    return True
                if response.status in [404, 405]:
                    async with session.get(url, timeout=15, headers=headers) as get_resp:
                        return get_resp.status < 400
        except:
            return False
        return False

    async def sanitize_document(self, markdown_content: str) -> str:
        all_links = self.link_pattern.findall(markdown_content)
        unique_url_registry = set()
        duplicates_flagged = set()
        unique_link_pairs = []
          
        for text, url in all_links:
            clean_url = url.split('#')[0].rstrip('/')
            if clean_url in unique_url_registry:
                duplicates_flagged.add((text, url))
            else:
                unique_url_registry.add(clean_url)
                unique_link_pairs.append((text, url))

        healthy_urls = set()
        connector = aiohttp.TCPConnector(limit=50)
        async with aiohttp.ClientSession(connector=connector) as session:
            tasks = [self._verify_link_health(session, url) for _, url in unique_link_pairs]
            health_results = await asyncio.gather(*tasks)
            
            for (text, url), is_healthy in zip(unique_link_pairs, health_results):
                if is_healthy:
                    healthy_urls.add(url.split('#')[0].rstrip('/'))

        reconstructed_lines = []
        for line in markdown_content.splitlines():
            links_in_line = self.link_pattern.findall(line)
            should_retain_line = True
            for txt, uri in links_in_line:
                clean_uri = uri.split('#')[0].rstrip('/')
                if (txt, uri) in duplicates_flagged or clean_uri not in healthy_urls:
                    should_retain_line = False
                    if (txt, uri) in duplicates_flagged:
                        duplicates_flagged.remove((txt, uri))
                    break
            if should_retain_line:
                reconstructed_lines.append(line)
        return "\n".join(reconstructed_lines)

    def inject_curated_link(self, markdown_text: str, category: str, title: str, url: str, description: str) -> str:
        new_entry = f"  - [{title}]({url}) - {description}"
        lines = markdown_text.splitlines()
        for index, line in enumerate(lines):
            if category.lower() in line.lower() and (line.startswith("#") or line.startswith("-")):
                lines.insert(index + 1, new_entry)
                return "\n".join(lines)
        lines.append(f"\n### {category}")
        lines.append(new_entry)
        return "\n".join(lines)
