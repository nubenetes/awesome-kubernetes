import feedparser
import asyncio
import re
import httpx
from fake_useragent import UserAgent
from datetime import datetime
from typing import List, Dict, Optional
from src.logger import log_event
from src.config import MADRID_TZ

class RSSDataExtractor:
    def __init__(self):
        self.audit_trail = []

    def log_audit(self, method: str, success: Optional[bool], msg: str):
        icons = {True: "✅ SUCCESS", False: "❌ FAILURE", None: "⚡ ATTEMPT"}
        entry = f"**RSS ({method})** - {icons.get(success, 'ℹ️ INFO')}: {msg}"
        self.audit_trail.append(entry)
        log_event(entry)

    async def fetch_links_since(self, since_date: datetime, feeds: List[str]) -> List[Dict]:
        all_articles = []
        ua = UserAgent()
        for url in feeds:
            self.log_audit("Discovery", None, f"Parsing feed: {url}")
            try:
                async with httpx.AsyncClient(follow_redirects=True, timeout=30.0, verify=False) as client:
                    headers = {'User-Agent': ua.random}
                    response = await client.get(url, headers=headers)
                    response.raise_for_status()
                    content = response.content
                
                # Use a thread for feedparser as it's blocking
                feed = await asyncio.to_thread(feedparser.parse, content)
                
                if feed.bozo and len(feed.entries) == 0:
                    self.log_audit("Parsing", False, f"Malformed feed: {url}")
                    continue

                for entry in feed.entries:
                    # Parse published date
                    published = None
                    if hasattr(entry, 'published_parsed') and entry.published_parsed:
                        published = datetime(*entry.published_parsed[:6]).replace(tzinfo=MADRID_TZ)
                    elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                        published = datetime(*entry.updated_parsed[:6]).replace(tzinfo=MADRID_TZ)
                    
                    if not published:
                        published = datetime.now(MADRID_TZ)

                    if published >= since_date:
                        all_articles.append({
                            "url": entry.link,
                            "title": entry.title,
                            "text": str(entry.get("summary") or "")[:500],
                            "timestamp": published.isoformat(),
                            "source_type": f"RSS Feed ({feed.feed.get('title', 'Unknown')})"
                        })
                
                self.log_audit("Parsing", True, f"Extracted {len(feed.entries)} entries from {url}")
            except Exception as e:
                self.log_audit("Error", False, f"Feed error {url}: {str(e)[:50]}")
        
        return all_articles
