import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 49.282730
MY_LNG = -123.120735


def iss_in_vicinity():

    response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
    response_iss.raise_for_status()
    data_iss = response_iss.json()

    iss_latitude = float(data_iss["iss_position"]["latitude"])
    iss_longitude = float(data_iss["iss_position"]["longitude"])

    iss_relative_lat = abs(iss_latitude - MY_LAT)
    iss_relative_lng = abs(iss_longitude - MY_LNG)

    if iss_relative_lng and iss_relative_lat <= 5:
        return True


# Your position is within +5 or -5 degrees of the ISS position.


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if sunrise > time_now > sunset:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
# ^ run it under a while loop with time.sleep(60)


while True:
    if iss_in_vicinity() and is_night():
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user="", password="mockpassword")
            connection.sendmail(from_addr="",
                                to_addrs=",
                                msg="Subject: ISS is OVERHEAD!\n\n"
                                    "Look outside your window!")
    time.sleep(60)
