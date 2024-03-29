import datetime as dt
import pandas
import random
import smtplib


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
            to_addrs=detail['email'],
            msg=f"Subject:Happy Birthday.\n\n{content}"
        )


letters = ['letter_1.txt', 'letter_2.txt', 'letter_3.txt']

date = dt.date.today()
month = date.month
day = date.day

birthday_file = pandas.read_csv("birthdays.csv")
birthday_list = birthday_file.to_dict(orient='records')
birthday_letter = random.choice(letters)
name = "[NAME]"
for detail in birthday_list:
    if month == detail['month'] and day == detail['day']:
        with open(f"./letter_templates/{birthday_letter}") as letter_file:
            content = letter_file.read()
            content = content.replace(name, detail['name'])
        send_email()
