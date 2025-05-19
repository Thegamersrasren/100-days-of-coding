import requests
from datetime import datetime
import os
name = "Garen Agbaire"
time = datetime.now()
formated = time.strftime("%d/%m/%Y")  # Fixed date format

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = os.environ["SHEET_ENDPOINT"]  # Removed spaces
App_id = os.environ["NT_APP_ID"]
Api_key = os.environ["NT_API_KEY"]

exercise_text = input("What Exercise did you do today: ")

query = {
    "query": exercise_text
}

header = {
    'Content-Type': 'application/json',
    'x-app-id': App_id,
    'x-app-key': Api_key
}

# Nutritionix API call
response = requests.post(
    url=exercise_endpoint,
    headers=header,
    json=query
)
result = response.json()

# Sheety API call
for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": formated,  # Using formatted date string
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    
    row = requests.post(
        url=sheety_endpoint,
        json=sheet_inputs,
        auth=(name, os.environ['TOKEN'])  # Fixed auth syntax
    )

print(result)