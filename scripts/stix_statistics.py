print("Script started")
import json
from collections import Counter

# Load the STIX bundle
with open("data/enterprise_attack.json", "r", encoding="utf-8") as file:
    bundle = json.load(file)

# Count object types
object_types = [obj["type"] for obj in bundle["objects"]]

counts = Counter(object_types)

print("=" * 60)
print("MITRE ATT&CK STIX Statistics")
print("=" * 60)

print(f"\nTotal Objects: {len(bundle['objects'])}\n")

print("Object Type Counts:\n")

for object_type, count in sorted(counts.items()):
    print(f"{object_type:<25} {count}")

