import smtplib
import datetime as dt
import random

with open("quotes.txt") as quotes:
    today_quote = random.choice(quotes.readlines())
def send_email():
    smtp_server = '''
                  Gmail: smtp.gmail.com
                  Hotmail: smtp.live.com
                  Outlook: outlook.office365.com
                  Yahoo: smtp.mail.yahoo.com
                  '''
    my_email = "<your email>"
    password = "<generate a new application password from your email account"
    receiver_email = "<email address you want to send the email>"
    with smtplib.SMTP(smtp_server, port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=receiver_email,
            msg=f"Subject:Monday Motivation\n\n{today_quote}"
        )


now = dt.datetime.now()
year = now.year
day_of_week = now.weekday()

if day_of_week==4:
    send_email()
