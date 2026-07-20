import json
import pandas as pd

# Load the STIX bundle
with open("data/enterprise_attack.json", "r", encoding="utf-8") as file:
    bundle = json.load(file)

attack_patterns = []

for obj in bundle["objects"]:

    if obj.get("type") != "attack-pattern":
        continue

    technique_id = "N/A"

    # Extract ATT&CK Technique ID
    for ref in obj.get("external_references", []):
        if ref.get("source_name") == "mitre-attack":
            technique_id = ref.get("external_id", "N/A")

    attack_patterns.append({
        "Technique ID": technique_id,
        "Technique Name": obj.get("name", "N/A"),
        "Description": obj.get("description", "N/A")
    })

# Convert to DataFrame
df = pd.DataFrame(attack_patterns)

# Create reports directory if it doesn't exist
import os
os.makedirs("reports", exist_ok=True)

# Export CSV
output_file = "reports/attack_patterns.csv"
df.to_csv(output_file, index=False)

print("=" * 60)
print("ATT&CK Techniques Exported Successfully")
print("=" * 60)
print(f"Total Techniques: {len(df)}")
print(f"Saved to: {output_file}")

print("\nFirst 5 Techniques:\n")
print(df.head())

