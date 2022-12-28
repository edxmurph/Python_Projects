### NOTE:To make your code run on pythonanywhere, uncomment those commented codes.

import requests
# import os   
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient

# proxy_client = TwilioHttpClient(proxy={'http': os.environ['http_proxy'], 'https': os.environ['https_proxy']})

API_KEY = "118168a663ea10c99d37c4474ce083d4"
API_WEATHER = "https://api.openweathermap.org/data/2.5/onecall"
PARAMETERS = {
    "lat": 21.027763,
    "lon": 105.834160,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

ACCOUNT_SID = "AC59e366d5b8a25e6553f58105f1964f18"
AUTH_TOKEN = "9b456a8cebe803de7e8b9b3800d00ff3"
TWILIO_NUMBER = "+19033005166"
VERIFIED_NUMBER = "+84372371650"

response = requests.get(url=API_WEATHER, params=PARAMETERS)
response.raise_for_status()
data = response.json()

will_rain = False
for i in range(12):
    condition_code = data["hourly"][i]["weather"][0]["id"]
    if int(condition_code) < 600:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN) # ,http_client=proxy_client)

    message = client.messages \
                    .create(
                        body="It's going to rain today. Remember to bring an ☔",
                        from_= TWILIO_NUMBER,
                        to= VERIFIED_NUMBER
                    )

    print(message.status)

