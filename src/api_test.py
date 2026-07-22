import os
import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

load_dotenv()

GLPI_URL = os.getenv("GLPI_URL")
APP_TOKEN = os.getenv("APP_TOKEN")
USER_TOKEN = os.getenv("USER_TOKEN")

headers = {
    "App-Token": APP_TOKEN,
    "Authorization": f"user_token {USER_TOKEN}"
}

try:
    response = requests.get(
        f"{GLPI_URL}/initSession",
        headers=headers,
        verify=False,
        timeout=10
    )

    print("Code HTTP :", response.status_code)
    print(response.text)

except Exception as e:
    print("Erreur :", e)