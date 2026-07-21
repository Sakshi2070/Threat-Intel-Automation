from parser import load_bundle

bundle = load_bundle("data/enterprise_attack.json")

print("=" * 60)
print("Bundle Loaded Successfully")
print("=" * 60)

print("Total Objects:", len(bundle["objects"]))

