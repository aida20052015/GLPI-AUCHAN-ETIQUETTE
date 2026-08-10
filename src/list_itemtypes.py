from get_assets import glpi_session
import os
from dotenv import load_dotenv
import requests
import urllib3

urllib3.disable_warnings()
load_dotenv()

GLPI_URL = os.getenv("GLPI_URL")

headers = glpi_session()

r = requests.get(
    f"{GLPI_URL}/listSearchOptions",
    headers=headers,
    verify=False
)

print(r.status_code)
print(r.text[:2000])