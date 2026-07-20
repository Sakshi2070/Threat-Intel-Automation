from parser import load_bundle, get_attack_patterns, get_malware
from exporter import export_csv
from ioc_parser import extract_iocs
from enricher import enrich_ip
from summary import generate_summary
import os

os.makedirs("reports", exist_ok=True)

try:
    print("=" * 60)
    print("Threat Intelligence Automation")
    print("=" * 60)

    # Load sample IOC bundle
    sample_bundle = load_bundle("data/sample_stix.json")

    # Load MITRE ATT&CK bundle
    attack_bundle = load_bundle("data/enterprise_attack.json")

    # Extract ATT&CK data
    attack_patterns = get_attack_patterns(attack_bundle)
    malware = get_malware(attack_bundle)

    # Extract IOCs
    iocs = extract_iocs(sample_bundle)

    # Enrich only IPv4 indicators
    for ioc in iocs:
        ioc["Country"] = ""
        ioc["City"] = ""
        ioc["Organization"] = ""

        if ioc["Type"] == "IPv4":
            enrichment = enrich_ip(ioc["Value"])

            ioc["Country"] = enrichment["Country"]
            ioc["City"] = enrichment["City"]
            ioc["Organization"] = enrichment["Organization"]

    # Export reports
    export_csv(attack_patterns, "attack_patterns.csv")
    export_csv(malware, "malware.csv")
    export_csv(iocs, "ioc_report.csv")

    # Generate summary
    generate_summary(
        attack_patterns,
        malware,
        iocs
    )

    print("\nSummary")
    print("-" * 40)
    print(f"ATT&CK Techniques : {len(attack_patterns)}")
    print(f"Malware Families  : {len(malware)}")
    print(f"IOCs Extracted    : {len(iocs)}")

    print("\nReports generated successfully!")

except Exception as e:
    print("\nPipeline Failed!")
    print(f"Error: {e}")

