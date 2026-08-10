from get_assets import get_session
import requests
import json

headers, url = get_session()

r = requests.get(
    url,
    headers=headers,
    verify=False
)

print("Code :", r.status_code)

try:
    print(json.dumps(r.json(), indent=4))
except:
    print(r.text)