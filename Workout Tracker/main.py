import json
import os
import requests
from datetime import *

time_now = datetime.now()

USER_WEIGHT = 65
height_cm = 170
age = 24
gender = 'male'

NUTRITIONIX_API_ID = os.environ.get("NUTRITIONIX_API_ID")
NUTRITIONIX_API_KEY = os.environ.get('NUTRITIONIX_API_KEY')

NUTRITIONIX_HEADERS = {
    'x-app-id': NUTRITIONIX_API_ID,
    'X-app-key': NUTRITIONIX_API_KEY,
}

NUTRITIONIX_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

query = input("What exercise did you do?: ")

NUTRITIONIX_PARAMETER = {
    'query': query,
    'gender': 'male',
    'weight_kg': 65,
    'height_cm': 170,
    'age': 24,
}

nutri_response = requests.post(url=NUTRITIONIX_ENDPOINT, json=NUTRITIONIX_PARAMETER, headers=NUTRITIONIX_HEADERS)
exercise_text = nutri_response.text
exercise_json = json.loads(exercise_text)
exercise_type = exercise_json["exercises"][0]['user_input']
exercise_duration = round(exercise_json["exercises"][0]["duration_min"])
exercise_calories = exercise_json["exercises"][0]["nf_calories"]

print(exercise_json)
print(exercise_type)
print(exercise_duration)
print(exercise_calories)


SHEETY_ENDPOINT = 'https://api.sheety.co/8c5b4d159911156aa18c8c0316f42959/myWorkouts/workouts'
SHEETY_HEADER = {

}

SHEETY_PARAMS = {
    "workout": {
        "date": time_now.strftime("%d/%m/%Y"),
        "time": time_now.strftime("%X"),
        "exercise": exercise_type.title(),
        "duration": exercise_duration,
        "calories": exercise_calories,
    }
}

sheety_post = requests.post(url=SHEETY_ENDPOINT, json=SHEETY_PARAMS, headers=SHEETY_HEADER)
print(sheety_post.text)

sheety_response = requests.get(SHEETY_ENDPOINT, headers=SHEETY_HEADER)
sheety_response.raise_for_status()
print(sheety_response.status_code)
data = sheety_response.json()
print(data)


