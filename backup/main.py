from parser import load_bundle
from parser import get_attack_patterns
from parser import get_malware
from exporter import export_csv
from logger import logger

logger.info("Threat Intelligence Automation Started")

bundle = load_bundle("data/enterprise_attack.json")

logger.info("Bundle loaded successfully")

attack_patterns = get_attack_patterns(bundle)
malware = get_malware(bundle)

logger.info(f"Attack Patterns: {len(attack_patterns)}")
logger.info(f"Malware: {len(malware)}")

export_csv(attack_patterns, "attack_patterns.csv")
export_csv(malware, "malware.csv")

logger.info("Reports generated")

print("\nThreat Intelligence Automation Completed Successfully!")

