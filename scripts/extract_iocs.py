import json
import re

# Load the STIX bundle
with open("data/sample_stix.json", "r") as file:
    bundle = json.load(file)

print("=" * 60)
print("Extracted Indicators of Compromise")
print("=" * 60)

# Regular expression to capture the IOC value inside single quotes
pattern_regex = r"'([^']+)'"

for obj in bundle["objects"]:

    if obj["type"] != "indicator":
        continue

    pattern = obj["pattern"]

    match = re.search(pattern_regex, pattern)

    if match:
        ioc = match.group(1)

        print(f"\nIndicator Name : {obj['name']}")
        print(f"Pattern        : {pattern}")
        print(f"IOC            : {ioc}")

