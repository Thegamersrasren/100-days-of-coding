import os
import requests
from twilio.rest import Client
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Get credentials from environment variables
OWN_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.getenv("OPENWEATHER_API_KEY")  # From .env
account_sid = os.getenv("TWILIO_ACCOUNT_SID")  # From .env
auth_token = os.getenv("TWILIO_AUTH_TOKEN")  # From .env

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
        to="+2348052285586"
    )
    print(message.status)