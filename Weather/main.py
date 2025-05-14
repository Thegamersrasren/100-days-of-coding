import requests
from twilio.rest import Client

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = "709549e501c65d6901770280712825ea"
account_sid = "AC51ac1fd41b050e11925552fffb554825"
auth_token = "afd1d3aed7b8a8042dbf08af9a6fe41f"
weather_params = {
    "lat": 9.076479,
    "lon": 7.398574,
    "appid": api_key,
    "cnt": 4
}

will_rain = False
response = requests.get(OWN_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

for hour_data in weather_data["list"]:
    weather_id = hour_data["weather"][0]["id"]
    if weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It is going to rain bring an Umbrella",
        from_="+19342390638",
        to="+2348052285586"  # Removed spaces in phone number
    )
    print(message.status)