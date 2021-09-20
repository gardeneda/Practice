import requests
from twilio.rest import Client
import os

MY_LAT = 49.259879
MY_LNG = -122.889395

OWM_APPID = os.environ.get("OWM_APPID")
print(OWM_APPID)
OWM_ENDPOINT = ""
TWILIO_SID = ""
TWILIO_AUTH = os.environ.get("TWILIO TOKEN")
PARAM = {
    "lat": MY_LAT,
    "lon": MY_LNG,
    "appid": OWM_APPID,
    "exclude": ["current,minutely,daily"]
}

weather_response = requests.get(OWM_ENDPOINT, params=PARAM)
weather_response.raise_for_status()
weather_data = weather_response.json()

weather_twelve_hours = [(weather_data["hourly"][_]["weather"][0]["id"]) for _ in range(0, 12)]
print(weather_twelve_hours)

will_rain = False

for id in weather_twelve_hours:
    if int(id) < 700:
        will_rain = True

if will_rain:
    client = Client(TWILIO_SID, TWILIO_AUTH)
    message = client.messages \
                    .create(
                         body="It's going to rain today. Remember to bring a ☂️",
                         from_='+16264145685',
                         to='+17789530112'
                     )
    print(message.status)

