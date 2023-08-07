import requests
from datetime import datetime
import smtplib
import time

# You can find the latitude and longitude of your location on www.latlong.net
MY_LAT =   # Your longitude
MY_LONG =  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def close_to_my_location():
    if -5 <= MY_LAT - iss_latitude <= 5 and -5 <= MY_LONG - iss_longitude <= 5:
        return True


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

time_now = datetime.now().hour - 6   # -6 because subtracting timezone difference as sunrise and sunset are in UTC and this code is running on IST timezone machine

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if close_to_my_location() and sunrise < time_now > sunset:
        my_email = "<your email"
        password = "<your app password"
        smtp_server = '''
                  Gmail: smtp.gmail.com
                  Hotmail: smtp.live.com
                  Outlook: outlook.office365.com
                  Yahoo: smtp.mail.yahoo.com
                  '''
        with smtplib.SMTP(smtp_server, port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=my_email,
                msg=f"Subject:ISS IS HERE.\n\nHey! Look up ISS is above you")

