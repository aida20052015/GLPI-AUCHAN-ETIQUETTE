import os
import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings()

load_dotenv()

GLPI_URL = os.getenv("GLPI_URL")
APP_TOKEN = os.getenv("APP_TOKEN")
USER_TOKEN = os.getenv("USER_TOKEN")


def glpi_session():

    headers = {
        "App-Token": APP_TOKEN,
        "Authorization": f"user_token {USER_TOKEN}"
    }

    session = requests.get(
        f"{GLPI_URL}/initSession",
        headers=headers,
        verify=False
    )

    session_token = session.json()["session_token"]

    headers["Session-Token"] = session_token

    return headers


# >>> AJOUTÉ <<<
def get_session():
    """
    Retourne les en-têtes de session GLPI
    ainsi que l'URL de l'API.
    """
    headers = glpi_session()
    return headers, GLPI_URL


def get_assets():

    headers = glpi_session()

    assets = []

    categories = {
        "Computer": "PC",
        "Monitor": "MON",
        "Printer": "IMP",
        "Peripheral": "PER",
        "Phone": "TEL"
    }

    for endpoint, prefix in categories.items():

        response = requests.get(
            f"{GLPI_URL}/{endpoint}",
            headers=headers,
            verify=False
        )

        if response.status_code == 200:

            items = response.json()

            for item in items:

                item["asset_type"] = endpoint
                item["prefix"] = prefix

                assets.append(item)

    return assets


if __name__ == "__main__":

    assets = get_assets()

    print("Nombre total de matériels :", len(assets))

    for asset in assets:
        print(
            asset["asset_type"],
            asset["id"],
            asset["name"]
        )