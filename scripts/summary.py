from collections import Counter

def generate_summary(attack_patterns, malware, iocs):

    counter = Counter()

    for ioc in iocs:
        counter[ioc["Type"]] += 1

    with open("reports/summary.txt", "w") as file:

        file.write("Threat Intelligence Automation Summary\n")
        file.write("=" * 45 + "\n\n")

        file.write(f"Attack Patterns : {len(attack_patterns)}\n")
        file.write(f"Malware Families: {len(malware)}\n")
        file.write(f"Total IOCs      : {len(iocs)}\n\n")

        file.write("IOC Breakdown\n")
        file.write("-" * 20 + "\n")

        for key, value in counter.items():
            file.write(f"{key}: {value}\n")

        file.write("\nReports Generated\n")
        file.write("-" * 20 + "\n")
        file.write("attack_patterns.csv\n")
        file.write("malware.csv\n")
        file.write("ioc_report.csv\n")

