import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = f"http://{os.getenv('DEVICE_HOST')}/rest"
AUTH = (os.getenv("DEVICE_USER"), os.getenv("DEVICE_PASSWORD"))

def create(path, payload):
    resp = requests.post(f"{BASE_URL}{path}", json=payload, auth=AUTH, timeout=5)
    if not resp.ok:  # MikroTik REST: creation via PUT
        resp = requests.put(f"{BASE_URL}{path}", json=payload, auth=AUTH, timeout=5)
    resp.raise_for_status()
    return resp.json()

try:
    # Etape 2: GET
    resp = requests.get(f"{BASE_URL}/ip/address", auth=AUTH, timeout=5)
    resp.raise_for_status()
    print("GET:", resp.json())

    # Etape 3: creation
    payload = {"address": "192.168.20.1/24", "interface": "ether1"}
    created = create("/ip/address", payload)
    print("CREATE:", created)

    # Etape 4: GET filtre pour recuperer l'id
    resp = requests.get(f"{BASE_URL}/ip/address", params={"address": "192.168.20.1/24"},
                        auth=AUTH, timeout=5)
    resp.raise_for_status()
    addr_id = resp.json()[0][".id"]

    # PATCH
    resp = requests.patch(f"{BASE_URL}/ip/address/{addr_id}", json={"comment": "TP5 python"},
                          auth=AUTH, timeout=5)
    resp.raise_for_status()
    print("PATCH:", resp.json())

    input("Fait /ip/address print sur le routeur + capture, puis Entree pour supprimer...")

    # DELETE
    resp = requests.delete(f"{BASE_URL}/ip/address/{addr_id}", auth=AUTH, timeout=5)
    resp.raise_for_status()
    print("DELETE:", resp.status_code)

except requests.exceptions.RequestException as e:
    print("Erreur API:", e)
