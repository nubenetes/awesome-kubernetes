import json
import yaml
import os
import re

def normalize_url(url: str) -> str:
    url = url.split("#")[0].split("?")[0].rstrip("/")
    if url.startswith("http://"): url = "https://" + url[7:]
    return url.lower()

inventory_path = 'data/inventory.yaml'
cache_path = 'data/v2_cache.json'

if os.path.exists(cache_path):
    print(f"[*] Starting migration of {cache_path}...")
    with open(cache_path, 'r') as f:
        cache = json.load(f)
    
    inventory = {}
    if os.path.exists(inventory_path):
        with open(inventory_path, 'r') as f:
            inventory = yaml.safe_load(f) or {}

    merged = 0
    for url, data in cache.items():
        norm_url = normalize_url(url)
        if norm_url not in inventory:
            inventory[norm_url] = data
            merged += 1
        else:
            for k, v in data.items():
                if k not in inventory[norm_url]:
                    inventory[norm_url][k] = v
                    merged += 1

    os.makedirs(os.path.dirname(inventory_path), exist_ok=True)
    with open(inventory_path, 'w') as f:
        yaml.dump(inventory, f, sort_keys=False, allow_unicode=True)
    
    print(f"SUCCESS: Merged {merged} data points into YAML.")
    os.remove(cache_path)
    print(f"DELETED: Legacy {cache_path} removed.")
else:
    print("[!] Legacy cache file not found. Skipping migration.")
