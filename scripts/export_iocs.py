import json
import re
import pandas as pd

# Load STIX bundle
with open("data/sample_stix.json", "r") as file:
    bundle = json.load(file)

# Regex to extract IOC value
pattern_regex = r"'([^']+)'"

ioc_list = []

for obj in bundle["objects"]:

    if obj["type"] != "indicator":
        continue

    pattern = obj["pattern"]

    match = re.search(pattern_regex, pattern)

    if not match:
        continue

    ioc_value = match.group(1)

    # Detect IOC type
    if "ipv4-addr" in pattern:
        ioc_type = "IPv4"

    elif "domain-name" in pattern:
        ioc_type = "Domain"

    elif "url" in pattern:
        ioc_type = "URL"

    elif "file:hashes" in pattern:
        ioc_type = "Hash"

    else:
        ioc_type = "Unknown"

    ioc_list.append({
        "Indicator Name": obj["name"],
        "IOC Type": ioc_type,
        "IOC Value": ioc_value
    })

# Create DataFrame
df = pd.DataFrame(ioc_list)

# Save CSV
df.to_csv("reports/extracted_iocs.csv", index=False)

print("=" * 60)
print("Threat Intelligence Report Generated")
print("=" * 60)

print(df)

