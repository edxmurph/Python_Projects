# SMS Rain Alert

import requests
from twilio.rest import Client
from twilio.base.exceptions import TwilioRestException

# a random location in Europe from Day 33
MY_LAT = 21.027763
MY_LONG = 105.834160
# time span to check (in hours, max. 48)
TIME_SPAM = 12
OWM_API_URL = "https://api.openweathermap.org/data/2.5/onecall"

# keeping these here for simplicity, generally they would be stored more securely
OWM_API_KEY = "118168a663ea10c99d37c4474ce083d4"
ACCOUNT_SID = "AC59e366d5b8a25e6553f58105f1964f18"
AUTH_TOKEN = "9b456a8cebe803de7e8b9b3800d00ff3"
# Twilio phone number to send the SMS from
TWILIO_NUMBER = "+19033005166"
# real phone number to send the SMS to
VERIFIED_NUMBER = "+84372371650"

params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,minutely,daily",
    "appid": OWM_API_KEY
}
response = requests.get(OWM_API_URL, params=params)
# a simple error message, at least
if response.status_code != 200:
    print(response.text)
    print("Make sure the OWM_API_KEY is set properly.")
    response.raise_for_status()
# only need the "hourly" data, not the generic location, etc. part
weather_data = response.json()["hourly"]

rainy_forecast = True
# check the hourly forecast
for i in range(TIME_SPAM):
    # used just for testing, this prints out a simple description of the forecast
    # print(f"In {i} hour(s): {weather_data[i]['weather'][0]['main']}")
    # condition id codes listed at https://openweathermap.org/weather-conditions
    # 2xx: Thunderstorm, 3xx: Drizzle, 5xx: Rain, 6xx: Snow, etc.
    if int(weather_data[i]["weather"][0]["id"]) < 600:
        rainy_forecast = True
        # no need to check the rest
        break

if rainy_forecast:
    # Twilio python docs: https://www.twilio.com/docs/sms/quickstart/python
    try:
        client = Client(ACCOUNT_SID, AUTH_TOKEN)
        message = client.messages.create(body="It's going to rain today. Remember to bring an umbrella.",
                                         from_=TWILIO_NUMBER,
                                         to=VERIFIED_NUMBER)
    except TwilioRestException as ex:
        # a generic error message
        print(ex)
        print("Make sure the TWILIO_SID, TWILIO_TOKEN, TWILIO_NUMBER and TARGET_NUMBER are set properly.")
    else:
        # print the status for verification
        print(message.status)
