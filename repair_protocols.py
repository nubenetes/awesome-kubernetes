import os
import re

def fix_protocol(content):
    # Fix broken https:/ to https:// and http:/ to http://
    # Careful not to fix cases where it's already correct (https://)
    # The negative lookahead (?!/) ensures we only match single slashes
    content = re.sub(r'(https?):/(?!/)', r'\1://', content)
    return content

print("Repairing broken protocols...")
for root, _, files in os.walk("docs"):
    for f in files:
        if f.endswith(".md"):
            p = os.path.join(root, f)
            with open(p, 'r') as file:
                old_content = file.read()
            
            new_content = fix_protocol(old_content)
            
            if new_content != old_content:
                with open(p, 'w') as file:
                    file.write(new_content)
                print(f"  [REPAIRED] {p}")

print("Repairing inventory.yaml...")
inventory_path = "data/inventory.yaml"
if os.path.exists(inventory_path):
    with open(inventory_path, 'r') as f:
        content = f.read()
    new_content = fix_protocol(content)
    if new_content != content:
        with open(inventory_path, 'w') as f:
            f.write(new_content)
        print("  [REPAIRED] inventory.yaml")

print("Repair complete.")
