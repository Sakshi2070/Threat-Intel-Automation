import json

with open("data/sample_stix.json", "r") as file:
    bundle = json.load(file)

print("=" * 60)
print("STIX Bundle Loaded Successfully")
print("=" * 60)

print(f"\nTotal Objects: {len(bundle['objects'])}\n")

for obj in bundle["objects"]:
    print("Type:", obj["type"])
    print("Name:", obj["name"])
    print("Pattern:", obj["pattern"])
    print("-" * 50)

