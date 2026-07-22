from get_assets import get_session
import requests
import json

headers, url = get_session()

headers["Content-Type"] = "application/json"

payload = {
    "input": [
        {
            "id": 1,
            "otherserial": "AUCH-PC-00001"
        }
    ]
}

response = requests.put(
    f"{url}/Computer/1",
    headers=headers,
    data=json.dumps(payload),
    verify=False
)

print("Code HTTP :", response.status_code)
print(response.text)