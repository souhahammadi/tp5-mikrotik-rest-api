import os
import requests
from dotenv import load_dotenv

load_dotenv()
host = os.getenv("DEVICE_HOST")
user = os.getenv("DEVICE_USER")
pwd = os.getenv("DEVICE_PASSWORD")

r = requests.get(f"http://{host}/rest/system/resource", auth=(user, pwd), timeout=5)
print(r.status_code)
print(r.json())
