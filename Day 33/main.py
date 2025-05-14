import requests
from datetime import datetime
import smtplib
lat = 9.076479
long =7.398574
MY_EMAIL = "garenagbaire@gmail.com"
MY_PASSWORD = "tllbpnoucekcowda"



#Your position is within +5 or -5 degrees of the ISS position.
def overhead_iss():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    if lat-5 <= iss_latitude <= lat+5 and long-5 <= iss_longitude <= long+5:
        return True

def is_night():
    parameters = {
        "lat": lat,
        "lng": long,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    

    time_now = datetime.now()
    hour = time_now.hour
    if hour >= sunset or hour<=sunrise:
        return True

if overhead_iss and is_night:
    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(MY_EMAIL, MY_PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg=f"Subject: Look to the heavens \n\n Aliens named ISS is overhead"
    )
