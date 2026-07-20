import re

def extract_iocs(bundle):
    """
    Extract IOC indicators from a STIX bundle.
    """

    indicators = []

    regex = r"'([^']+)'"

    for obj in bundle.get("objects", []):

        if obj.get("type") != "indicator":
            continue

        pattern = obj.get("pattern", "")

        match = re.search(regex, pattern)

        if not match:
            continue

        value = match.group(1)

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

        indicators.append({
            "Name": obj.get("name", "N/A"),
            "Type": ioc_type,
            "Value": value
        })

    return indicators

