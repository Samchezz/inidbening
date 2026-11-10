import requests
from secrets import TRAFIKLAB_API_KEY

base_url = "https://realtime-api.trafiklab.se/v1/departures/"

def get_departures(stop_id):
  url = BASE_URL + str(stop_id) + "?key=" + TRAFIKLAB_API_KEY
  response = requests.get(url)

  try:
    if response.status_code != 200:
        raise Exception("HTTP error")

    data = response.json()
    return data.get("departures", [])

    finally:
      response.close()

def filter_departures(departures, transport_type="ALL"):
  transport_type = transport_type.upper()
  if transport_type == "ALL":
    return.departures

filterd = []
for departure in departures:
  route  = daparture.get("route", {})
  mode = route.get("transport_mode", "")

  if mode == transport_type:
    filtered.append(departure)

return filterd

def get_departure_status(departure):
  if departure.get("canceled", False):
        return "Cancelled"

  if not departure.get("is_realtime", False):
        return "Scheduled

  delay = departure.get("delay")

  if delay is None:
    Return "Realtime"

  if delay >= 60:
    minutes = (delay + 30) // 60
    return "Delayed " + str(minutes) + " min"

  return "On time"
