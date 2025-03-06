import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 11.367998
MY_LONG = 77.928786

MY_EMAIL = "sampgoogsamp@gmail.com"
MY_PASSWORD = "vqgidxmajuhxabdg"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

def is_iss_overhead():
    if iss_latitude <= MY_LAT + 5 and iss_latitude >= MY_LAT - 5 and iss_longitude <= MY_LONG + 5 and iss_longitude >= MY_LONG - 5:
        print("The ISS is close to your current position. 🤩")
        return True

    else:
        print("The ISS is not close to your current position. 😢")
        return False

def if_dark():
    current_hour = time_now.hour
    if sunset <= current_hour <= sunrise:
        print("It is dark. Look up! 🚀")
        return True
    else:
        print("It is not dark. Try again later. 🌙")
        return False

while True:
    time.sleep(10)
    if is_iss_overhead() and if_dark():
        print("Sending email notification...")
        connection = smtplib.SMTP("smtp.gmail.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="elayabarathiedison@gmail.com",
            msg="Subject:Look Up👆\n\nThe ISS is above you in the sky. Look up! 🚀"
        )
    



