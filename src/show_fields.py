from get_assets import get_session
import requests

headers, url = get_session()

r = requests.get(
    f"{url}/Computer/1?expand_dropdowns=true",
    headers=headers,
    verify=False
)

data = r.json()

print("=== Champs disponibles ===")
for k in sorted(data.keys()):
    print(k)