import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE_URL = f"http://{os.getenv('DEVICE_HOST')}/rest"
AUTH = (os.getenv("DEVICE_USER"), os.getenv("DEVICE_PASSWORD"))

ROUTES = [
    ("172.16.0.0/16", "192.168.233.2"),
    ("10.50.0.0/24", "192.168.233.2"),
]

def main():
    resp = requests.get(f"{BASE_URL}/ip/route", auth=AUTH, timeout=5)
    resp.raise_for_status()
    existing = {(r.get("dst-address"), r.get("gateway")) for r in resp.json()}

    for dst, gw in ROUTES:
        if (dst, gw) in existing:
            print(f"[SKIP] {dst} via {gw} existe deja")
            continue
        payload = {"dst-address": dst, "gateway": gw}
        r = requests.post(f"{BASE_URL}/ip/route", json=payload, auth=AUTH, timeout=5)
        if not r.ok:
            r = requests.put(f"{BASE_URL}/ip/route", json=payload, auth=AUTH, timeout=5)
        r.raise_for_status()
        print(f"[CREATE] {dst} via {gw}")

if __name__ == "__main__":
    try:
        main()
    except requests.exceptions.RequestException as e:
        print("Erreur API:", e)
