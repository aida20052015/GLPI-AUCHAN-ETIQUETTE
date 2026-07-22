import os
import requests
import urllib3
from dotenv import load_dotenv

urllib3.disable_warnings()

load_dotenv()

GLPI_URL = os.getenv("GLPI_URL")
APP_TOKEN = os.getenv("APP_TOKEN")
USER_TOKEN = os.getenv("USER_TOKEN")


class GLPI:

    def __init__(self):
        self.headers = {
            "App-Token": APP_TOKEN,
            "Authorization": f"user_token {USER_TOKEN}"
        }

        response = requests.get(
            f"{GLPI_URL}/initSession",
            headers=self.headers,
            verify=False
        )

        self.session_token = response.json()["session_token"]

        self.headers["Session-Token"] = self.session_token


    def get(self, endpoint):

        response = requests.get(
            f"{GLPI_URL}/{endpoint}",
            headers=self.headers,
            verify=False
        )

        return response.json()