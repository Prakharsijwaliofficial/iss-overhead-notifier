import requests
from datetime import datetime
import smtplib
import time
MY_LAT = 29.209503 # Your latitude
MY_LONG = 79.504435 # Your longitude
my_email = "prakharsijwaliofficial@gmail.com"
password = "rcoztdhkoxjcmkcd"

#If the ISS is close to my current position
def is_iss_close():
    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        return True
    else:
        return False


    
    
# and it is currently dark
def is_dark():
    if time_now.hour < sunrise or time_now.hour > sunset:
        return True
    else:
        return False


    
# Then send me an email to tell me to look up.
def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)

        connection.sendmail(
            from_addr=my_email,
            to_addrs= "jssaerospaceteam@gmail.com",
            msg="Subject: ISS Alert\n\nLook up! The ISS is overhead."
        )



# BONUS: run the code every 60 seconds.
while True:
    
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.

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


    if is_iss_close() and is_dark():
        send_mail()
    time.sleep(60)
    



