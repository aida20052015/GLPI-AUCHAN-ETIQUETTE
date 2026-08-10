from get_assets import get_session
import requests
import json

headers, url = get_session()

r = requests.get(
    f"{url}/getGlpiConfig",
    headers=headers,
    verify=False
)

print(r.status_code)

with open("config_glpi.json","w",encoding="utf8") as f:
    json.dump(r.json(),f,indent=4,ensure_ascii=False)

print("Configuration enregistrée.")