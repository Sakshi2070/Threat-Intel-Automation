import json

def load_bundle(file_path):
    """
    Load a STIX bundle from disk.
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_attack_patterns(bundle):
    """
    Return all ATT&CK techniques.
    """
    techniques = []

    for obj in bundle["objects"]:

        if obj.get("type") != "attack-pattern":
            continue

        technique_id = "N/A"

        for ref in obj.get("external_references", []):

            if ref.get("source_name") == "mitre-attack":
                technique_id = ref.get("external_id", "N/A")

        techniques.append({
            "Technique ID": technique_id,
            "Technique Name": obj.get("name", "N/A"),
            "Description": obj.get("description", "N/A")
        })

    return techniques


def get_malware(bundle):
    """
    Return all malware objects.
    """
    malware = []

    for obj in bundle["objects"]:

        if obj.get("type") != "malware":
            continue

        malware.append({
            "Name": obj.get("name", "N/A"),
            "Description": obj.get("description", "N/A"),
            "Platforms": ", ".join(obj.get("x_mitre_platforms", [])),
            "Aliases": ", ".join(obj.get("aliases", []))
        })

    return malware

