from parser import load_bundle
from ioc_parser import extract_iocs

bundle = load_bundle("data/sample_stix.json")

iocs = extract_iocs(bundle)

print("=" * 60)
print("IOC Extraction Test")
print("=" * 60)

for ioc in iocs:
    print(ioc)

