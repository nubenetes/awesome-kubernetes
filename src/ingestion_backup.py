import json
import re
from datetime import datetime
from src.config import MADRID_TZ

class BackupDataExtractor:
    def __init__(self, file_path: str):
        self.file_path = file_path
        self.audit_trail = []

    def log_audit(self, method: str, success: bool, msg: str):
        icons = {True: "✅ SUCCESS", False: "❌ FAILURE", None: "⚡ ATTEMPT"}
        entry = f"**{method}** - {icons.get(success, 'ℹ️ INFO')}: {msg}"
        self.audit_trail.append(entry)
        print(entry)

    def _extract_urls_from_text(self, text: str) -> list[str]:
        # Regex para URLs comunes
        urls = re.findall(r'https?://[^\s<>\"]+|www\.[^\s<>\"]+', text)
        noise_domains = [
            "x.com", "twitter.com", "abs.twimg", "pbs.twimg", 
            "t.co", "nitter.net"
        ]
        valid_urls = []
        for u in urls:
            u_clean = u.rstrip('.,!?;:)(')
            if all(d not in u_clean.lower() for d in noise_domains):
                valid_urls.append(u_clean)
        return list(set(valid_urls))

    async def fetch_links(self) -> list[dict]:
        self.log_audit("Backup Ingestion", None, f"Processing: {self.file_path}")
        results = []
        
        try:
            if self.file_path.endswith('.json'):
                with open(self.file_path, 'r') as f:
                    data = json.load(f)
                    
                for item in data:
                    # Formato standard de exportación de X (o similar)
                    text = item.get('full_text', '') or item.get('text', '')
                    timestamp_raw = item.get('created_at', '')
                    
                    # Intentar extraer de entities.urls si existe (más limpio)
                    extracted_urls = []
                    if 'entities' in item and 'urls' in item['entities']:
                        for u_obj in item['entities']['urls']:
                            expanded = u_obj.get('expanded_url')
                            if expanded: extracted_urls.append(expanded)
                    
                    # Fallback a regex si no hay entities
                    if not extracted_urls:
                        extracted_urls = self._extract_urls_from_text(text)
                    
                    # Filtrar ruido de nuevo por si acaso
                    noise_domains = ["x.com", "twitter.com", "t.co"]
                    for url in set(extracted_urls):
                        if any(d in url.lower() for d in noise_domains):
                            continue
                            
                        results.append({
                            "url": url,
                            "context": text[:250],
                            "timestamp": timestamp_raw,
                            "source_type": "Backup JSON"
                        })
                        
            elif self.file_path.endswith('.md'):
                with open(self.file_path, 'r') as f:
                    content = f.read()
                
                # En MD, buscamos todos los links que no sean de X
                # El usuario mencionó que hay links al post original si se cortó,
                # pero nos interesan los links EXTERNOS curados.
                urls = self._extract_urls_from_text(content)
                for u in urls:
                    results.append({
                        "url": u,
                        "context": "Extraído de Backup Markdown",
                        "timestamp": datetime.now(MADRID_TZ).isoformat(),
                        "source_type": "Backup MD"
                    })
            
            # Ordenar por fecha si es posible (JSON suele tenerla)
            try:
                # 'Tue Oct 01 19:56:51 +0000 2024'
                def parse_date(x):
                    try:
                        return datetime.strptime(x["timestamp"], '%a %b %d %H:%M:%S +0000 %Y')
                    except:
                        return datetime.min
                results.sort(key=parse_date)
            except:
                pass

            self.log_audit("Backup Ingestion", True, f"Total links extracted: {len(results)}")
            return results

        except Exception as e:
            self.log_audit("Backup Ingestion", False, f"Error: {str(e)}")
            return []
