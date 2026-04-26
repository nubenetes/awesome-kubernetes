import re
from typing import Tuple, Dict, List

class MarkdownSanitizer:
    def __init__(self):
        # Captura [texto](url)
        self.link_pattern = re.compile(r'\[([^\]]+)\]\((https?://[^\)]+)\)')

    def _calculate_link_score(self, line: str) -> int:
        """
        Calcula la calidad de un enlace:
        - Cada estrella 🌟 suma 1000 puntos.
        - Cada carácter de longitud suma 1 punto.
        """
        stars = line.count("🌟")
        return (stars * 1000) + len(line)

    async def sanitize_document(self, markdown_content: str, full_health_check: bool = False) -> Tuple[str, dict]:
        """
        MODO INTELIGENTE: 
        1. Identifica todos los enlaces y sus puntuaciones.
        2. Para duplicados, decide cuál es el 'mejor'.
        3. Mantiene el mejor en su posición original y elimina los peores.
        """
        lines = markdown_content.splitlines()
        url_to_best_score = {}
        url_to_best_line_index = {}
        
        # Primera pasada: Encontrar el mejor representante de cada URL
        for i, line in enumerate(lines):
            match = self.link_pattern.search(line)
            if match:
                _, url = match.groups()
                clean_url = url.split('#')[0].rstrip('/')
                score = self._calculate_link_score(line)
                
                if clean_url not in url_to_best_score or score > url_to_best_score[clean_url]:
                    url_to_best_score[clean_url] = score
                    url_to_best_line_index[clean_url] = i

        # Segunda pasada: Reconstruir el documento
        new_lines = []
        stats = {"fixed": 0, "removed": 0, "duplicates": 0}
        processed_urls = set()

        for i, line in enumerate(lines):
            match = self.link_pattern.search(line)
            if not match:
                new_lines.append(line)
                continue
            
            _, url = match.groups()
            clean_url = url.split('#')[0].rstrip('/')
            
            # Si esta línea es la 'ganadora' para esta URL, la mantenemos
            if url_to_best_line_index.get(clean_url) == i:
                new_lines.append(line)
                processed_urls.add(clean_url)
            else:
                # Es un duplicado 'peor', lo eliminamos
                stats["duplicates"] += 1
                continue

        return "\n".join(new_lines), stats

    def inject_curated_link(self, markdown_text: str, category: str, title: str, url: str, description: str) -> str:
        clean_url = url.split('#')[0].rstrip('/')
        if clean_url in markdown_text:
            return markdown_text

        new_entry = f"  - [{title}]({url}) - {description}"
        lines = markdown_text.splitlines()
        
        header_found = False
        category_pattern = re.compile(rf'^[#-]+\s*{re.escape(category)}', re.IGNORECASE)
        
        for i, line in enumerate(lines):
            if category_pattern.match(line):
                lines.insert(i + 1, new_entry)
                header_found = True
                break
        
        if not header_found:
            lines.append(f"\n## {category}\n")
            lines.append(new_entry)
            
        return "\n".join(lines)
