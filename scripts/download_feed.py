import requests

url = "https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json"

response = requests.get(url, timeout=30)

if response.status_code == 200:
    with open("data/enterprise_attack.json", "w") as file:
        file.write(response.text)

    print("Download Successful!")
    print("Saved to data/enterprise_attack.json")
else:
    print("Download Failed")
    print("Status Code:", response.status_code)

