import requests
from datetime import datetime
import smtplib
import os


MY_LAT = 29.209503  # Your latitude
MY_LONG = 79.504435  # Your longitude

MY_EMAIL = os.environ["MY_EMAIL"]
PASSWORD = os.environ["MY_PASSWORD"]


# If the ISS is close to my current position
def is_iss_close():

    response = requests.get(
        url="http://api.open-notify.org/iss-now.json"
    )
    response.raise_for_status()

    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    print(f"ISS Latitude: {iss_latitude}")
    print(f"ISS Longitude: {iss_longitude}")

    # Your position is within +5 or -5 degrees of the ISS position.
    if (
        MY_LAT - 5 <= iss_latitude <= MY_LAT + 5
        and
        MY_LONG - 5 <= iss_longitude <= MY_LONG + 5
    ):
        return True
    else:
        return False


# Get sunrise and sunset
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(
    "https://api.sunrise-sunset.org/json",
    params=parameters
)
response.raise_for_status()

data = response.json()

sunrise = int(
    data["results"]["sunrise"].split("T")[1].split(":")[0]
)

sunset = int(
    data["results"]["sunset"].split("T")[1].split(":")[0]
)


# Check if it is currently dark
def is_dark():

    time_now = datetime.now()

    print(f"Current hour: {time_now.hour}")
    print(f"Sunrise hour: {sunrise}")
    print(f"Sunset hour: {sunset}")

    if time_now.hour < sunrise or time_now.hour > sunset:
        return True
    else:
        return False


# Send me an email to tell me to look up
def send_mail():

    with smtplib.SMTP("smtp.gmail.com", 587) as connection:

        connection.starttls()

        connection.login(
            user=MY_EMAIL,
            password=PASSWORD
        )

        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="jssaerospaceteam@gmail.com",
            msg="Subject: ISS Alert\n\nLook up! The ISS is overhead."
        )

        print("Email sent successfully!")


# Check the conditions once
if is_iss_close() and is_dark():

    print("ISS is overhead and it is dark.")

    send_mail()

else:

    print("No alert needed.")
