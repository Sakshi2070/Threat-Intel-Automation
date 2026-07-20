import json

# Load the downloaded STIX bundle
with open("data/enterprise_attack.json", "r", encoding="utf-8") as file:
    bundle = json.load(file)

print("=" * 60)
print("MITRE ATT&CK STIX Bundle Information")
print("=" * 60)

print(f"\nBundle Type: {bundle['type']}")
print(f"Bundle ID: {bundle['id']}")
print(f"Total Objects: {len(bundle['objects'])}")

print("\nFirst 10 Object Types:\n")

for obj in bundle["objects"][:10]:
    print(obj["type"])

