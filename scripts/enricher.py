import requests

def enrich_ip(ip):

    url = f"https://ipinfo.io/{ip}/json"

    try:

        response = requests.get(url, timeout=10)

        data = response.json()

        return {
            "Country": data.get("country", "Unknown"),
            "City": data.get("city", "Unknown"),
            "Organization": data.get("org", "Unknown")
        }

    except Exception:

        return {
            "Country": "Unknown",
            "City": "Unknown",
            "Organization": "Unknown"
        }

