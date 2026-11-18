
import requests
import json

API_KEY = "7a7ca0b23c874f469635e9dc05fdad3b"
STOP_ID = "740032188"

url = (
    "https://realtime-api.trafiklab.se/v1/departures/"
    + STOP_ID
    + "?key="
    + API_KEY
)

response = requests.get(url)

print("Status code:", response.status_code)

data = response.json()

print(json.dumps(data, indent=4, ensure_ascii=False))

response.close()
