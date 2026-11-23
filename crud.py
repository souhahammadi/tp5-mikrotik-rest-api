import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE = f"http://{os.getenv('DEVICE_HOST')}/rest"
AUTH = (os.getenv("DEVICE_USER"), os.getenv("DEVICE_PASSWORD"))

# READ: lister les interfaces
r = requests.get(f"{BASE}/interface", auth=AUTH, timeout=5)
for i in r.json():
    print(i["name"], i["type"], i[".id"])

# CREATE: ajouter une adresse IP sur ether1
r = requests.put(f"{BASE}/ip/address", auth=AUTH, timeout=5,
                 json={"address": "10.10.10.1/24", "interface": "ether1"})
print("CREATE", r.status_code, r.json())
created_id = r.json().get(".id")

# READ: lister les adresses
r = requests.get(f"{BASE}/ip/address", auth=AUTH, timeout=5)
print("LIST", r.status_code, r.json())

# UPDATE: changer le commentaire
r = requests.patch(f"{BASE}/ip/address/{created_id}", auth=AUTH, timeout=5,
                   json={"comment": "cree par python"})
print("UPDATE", r.status_code)

# DELETE: supprimer l'adresse
r = requests.delete(f"{BASE}/ip/address/{created_id}", auth=AUTH, timeout=5)
print("DELETE", r.status_code)
