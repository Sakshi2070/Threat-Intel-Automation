from taxii2client.v21 import Server

# Public TAXII server discovery endpoint
DISCOVERY_URL = "https://cti-taxii.mitre.org/taxii/"

try:
    server = Server(DISCOVERY_URL)

    print("=" * 60)
    print("Connected Successfully!")
    print("=" * 60)

    print("\nAvailable API Roots:\n")

    for api_root in server.api_roots:
        print(api_root.url)

except Exception as e:
    print("Connection Failed")
    print(e)
