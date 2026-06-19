import os
import json
import sqlite3
import yaml
from typing import Dict

INVENTORY_PATH = "data/inventory.yaml"
SQL_PATH = "data/inventory.sql"

try:
    from yaml import CSafeLoader as Loader, CSafeDumper as Dumper
except ImportError:
    from yaml import SafeLoader as Loader, SafeDumper as Dumper

def load_inventory(shard_file: str = None) -> Dict:
    """
    Loads the entire inventory.
    Option 3: Imports inventory.sql to temporary SQLite database in-memory,
    queries the database to reconstruct the Python dictionary, and returns it.
    Falls back to inventory.yaml if SQL file is not present.
    """
    if not os.path.exists(SQL_PATH) and os.path.exists(INVENTORY_PATH):
        try:
            with open(INVENTORY_PATH, "r", encoding="utf-8") as file:
                return yaml.load(file, Loader=Loader) or {}
        except Exception as e:
            pass
        return {}

    if not os.path.exists(SQL_PATH):
        return {}

    conn = sqlite3.connect(":memory:")
    try:
        with open(SQL_PATH, "r", encoding="utf-8") as f:
            conn.executescript(f.read())
    except Exception as e:
        conn.close()
        # Fallback to YAML if SQL import fails
        if os.path.exists(INVENTORY_PATH):
            try:
                with open(INVENTORY_PATH, "r", encoding="utf-8") as file:
                    return yaml.load(file, Loader=Loader) or {}
            except Exception as e:
                print(f"[WARN] YAML fallback load failed: {str(e)[:100]}")
        return {}

    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM resources")
        rows = cursor.fetchall()
        col_names = [description[0] for description in cursor.description]
    except Exception as e:
        conn.close()
        return {}
    
    inv = {}
    for row in rows:
        record = dict(zip(col_names, row))
        url = record.pop("url")
        
        # Deserialize JSON lists/dicts
        for json_field in ["hierarchy", "tags", "v1_locations", "v2_locations", "youtube_mosaic", "extra_metadata"]:
            val = record.get(json_field)
            if val:
                try:
                    record[json_field] = json.loads(val)
                except Exception as e:
                    print(f"[WARN] JSON parse failed for field '{json_field}': {str(e)[:100]}")
                    record[json_field] = [] if json_field not in ["youtube_mosaic", "extra_metadata"] else {}
            else:
                record[json_field] = [] if json_field not in ["youtube_mosaic", "extra_metadata"] else {}
                
        # Merge extra_metadata keys back into the record dictionary
        extra = record.pop("extra_metadata", {})
        if isinstance(extra, dict):
            record.update(extra)

        # Restore types
        if record.get("is_microservice") is not None:
            record["is_microservice"] = bool(record["is_microservice"])
        if record.get("needs_ai_refresh") is not None:
            record["needs_ai_refresh"] = bool(record["needs_ai_refresh"])
            
        inv[url] = record
        
    conn.close()
    return inv

def save_inventory(inv: Dict, shard_file: str = None):
    """
    Saves the entire inventory.
    Option 3: Creates an in-memory SQLite table, populates it, 
    and exports it back to inventory.sql.
    Also dual-saves a backup to inventory.yaml using fast CDumper.
    """
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS resources (
        url TEXT PRIMARY KEY,
        title TEXT,
        description TEXT,
        year TEXT,
        stars INTEGER,
        ai_summary TEXT,
        language TEXT,
        resource_type TEXT,
        complexity TEXT,
        is_microservice BOOLEAN,
        status TEXT,
        addition_method TEXT,
        content_hash TEXT,
        health_score REAL,
        last_checked INTEGER,
        needs_ai_refresh BOOLEAN,
        discovered_at TEXT,
        last_ai_eval TEXT,
        company TEXT,
        geo_region TEXT,
        hierarchy TEXT,
        tags TEXT,
        v1_locations TEXT,
        v2_locations TEXT,
        youtube_mosaic TEXT,
        extra_metadata TEXT
    );
    """)
    
    columns = [
        "url", "title", "description", "year", "stars", "ai_summary", "language",
        "resource_type", "complexity", "is_microservice", "status", "addition_method",
        "content_hash", "health_score", "last_checked", "needs_ai_refresh",
        "discovered_at", "last_ai_eval", "company", "geo_region",
        "hierarchy", "tags", "v1_locations", "v2_locations", "youtube_mosaic", "extra_metadata"
    ]
    
    for url, entry in inv.items():
        if not isinstance(entry, dict):
            continue

        # last_checked is a coarse staleness timestamp (epoch seconds). Normalize
        # it to int on the entry itself — before building the SQL record AND the
        # YAML dump below — so both serializations agree, and SQLite's
        # version-specific REAL->text float formatting can't rewrite every row on
        # dump. Sub-second precision is not used by any reader.
        lc = entry.get("last_checked")
        if isinstance(lc, float):
            entry["last_checked"] = int(lc)

        record = {col: entry.get(col) for col in columns if col not in ["hierarchy", "tags", "v1_locations", "v2_locations", "youtube_mosaic", "extra_metadata"]}
        record["url"] = url
        
        # Serialize lists/dicts
        record["hierarchy"] = json.dumps(entry.get("hierarchy", []))
        record["tags"] = json.dumps(entry.get("tags", []))
        record["v1_locations"] = json.dumps(entry.get("v1_locations", []))
        record["v2_locations"] = json.dumps(entry.get("v2_locations", []))
        record["youtube_mosaic"] = json.dumps(entry.get("youtube_mosaic", {}))
        
        # Pull arbitrary extra fields
        extra = {}
        for k, v in entry.items():
            if k not in columns:
                extra[k] = v
        record["extra_metadata"] = json.dumps(extra)
        
        # Conversions
        record["is_microservice"] = 1 if record.get("is_microservice") else 0
        record["needs_ai_refresh"] = 1 if record.get("needs_ai_refresh") else 0

        placeholders = ", ".join(["?"] * len(columns))
        values = [record[col] for col in columns]
        cursor.execute(f"INSERT OR REPLACE INTO resources ({', '.join(columns)}) VALUES ({placeholders})", values)
        
    conn.commit()
    
    # Dump to SQL
    os.makedirs(os.path.dirname(SQL_PATH), exist_ok=True)
    with open(SQL_PATH, "w", encoding="utf-8") as f:
        for line in conn.iterdump():
            f.write(f"{line}\n")
            
    conn.close()

    # Dual-Save to YAML (Fast C-Dumper)
    os.makedirs(os.path.dirname(INVENTORY_PATH), exist_ok=True)
    with open(INVENTORY_PATH, "w", encoding="utf-8") as file:
        yaml.dump(inv, file, Dumper=Dumper, sort_keys=False, allow_unicode=True)

def get_shard_name(url: str) -> str:
    return "inventory.yaml"

def update_inventory_entry(inventory: Dict, norm_url: str, new_data: Dict):
    if norm_url not in inventory:
        inventory[norm_url] = {}
    existing = inventory[norm_url]
    if isinstance(existing, dict):
        merged = existing.copy()
        existing_discovered = existing.get("discovered_at")
        merged.update(new_data)
        if existing_discovered:
            merged["discovered_at"] = existing_discovered
        inventory[norm_url] = merged
    else:
        inventory[norm_url] = new_data
