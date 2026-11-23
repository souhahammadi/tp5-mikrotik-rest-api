import os
import requests
from dotenv import load_dotenv

load_dotenv()
BASE = f"http://{os.getenv('DEVICE_HOST')}/rest"
AUTH = (os.getenv("DEVICE_USER"), os.getenv("DEVICE_PASSWORD"))

# CREATE route statique
r = requests.put(f"{BASE}/ip/route", auth=AUTH, timeout=5,
                 json={"dst-address": "172.16.0.0/16", "gateway": "192.168.233.2"})
print("CREATE", r.status_code, r.json())
rid = r.json().get(".id")

# READ
r = requests.get(f"{BASE}/ip/route", auth=AUTH, timeout=5)
for x in r.json():
    print(x.get("dst-address"), x.get("gateway"), x[".id"])

# DELETE
r = requests.delete(f"{BASE}/ip/route/{rid}", auth=AUTH, timeout=5)
print("DELETE", r.status_code)
