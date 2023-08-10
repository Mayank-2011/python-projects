import requests
from twilio.rest import Client

OWM_endpoint = "http://api.weatherapi.com/v1/forecast.json"
api_key = "<your openweather api key"
account_sid = "twilio account sid"
auth_token = "twilio account auth token"
lat_long = "your latitude and longitude" #Format as string Ex.: "25.437500,75.646301"

parameters = {
    "key": api_key,
    "q": lat_long
}

response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

seven_to_seven_forecast = weather_data['forecast']['forecastday'][0]['hour'][6:18] #For weather forecast from 7AM to 7PM

will_rain = False

for key in seven_to_seven_forecast:
    if seven_to_seven_forecast[0]['chance_of_rain'] > 0:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an umbrella ☂️.",
                     from_='your twilio trial mobile number',
                     to='your twilio verified number'
                 )
    print(message.status)
# All twilio related details can be found on the twilio account dashboard.
