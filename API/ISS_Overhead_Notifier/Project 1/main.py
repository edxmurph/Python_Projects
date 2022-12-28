import requests
import datetime
import smtplib
import time

MY_EMAIL = "khanhha.smil@gmail.com"
PASSWORD = "khanhha14042013"
MY_LATITUDE = 21.027763
MY_LONGITUDE = 105.834160

def is_overhead():
    """Return True if the distance between iss position and your position less than 5 degrees."""

    # Get the data from the endpoint.
    response = requests.get(url="http://api.open-notify.org/iss-now.json")

    # Check status code
    #print(response.status_code)
    # 1xx: Hold on.
    # 2xx: Here you go.
    # 3xx: Go away.
    # 4xx: You screwed up.
    # 5xx: Website/Serve... screwed up. 

    # Raise an HTTPError if the HTTP request return an unsuccessful status code.
    response.raise_for_status()

    # Get json data.
    data = response.json()
    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    return MY_LATITUDE -5 < iss_latitude < MY_LATITUDE +5 and MY_LONGITUDE - 5 < iss_longitude < MY_LONGITUDE +5

def is_dark():
    """Return True if it's dark."""
    
    parameters = {
        "lat": MY_LATITUDE,
        "lng":  MY_LONGITUDE, 
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    now = datetime.datetime.now()

    return sunset < now.hour < sunrise


while is_overhead() and is_dark():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs="dungnguyentuan95@gmail.com",
                            msg=f"Object:Look Up👌\n\nISS is on your head.")
    # Send email every 60s.
    time.sleep(60)





