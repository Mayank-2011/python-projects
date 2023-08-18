import requests
from bs4 import BeautifulSoup
import smtplib

product_url = "product url you want to chase the price for"
required_price = "price under which you want to receive an alert"
headers = {
    "User-Agent": "your user agent",
    "Accept-Language": "accep-language"
} # You can find the header details for
response = requests.get(product_url, headers=headers).text

soup = BeautifulSoup(response, "html.parser")
title = soup.select_one('#productTitle').getText().split("       ")[1]

price_tag = f"{soup.find(name='span', class_='a-price-whole').getText()}"
price = int(f"{price_tag.split(',')[0]}{price_tag.split(',')[1].split('.')[0]}")

if price <= required_price:
    my_email = "your email"
    password = "your application password"
    with smtplib.SMTP("your email smtp server", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject: Amazon Price drop alert\n\n{title} is now Rs {price}\n{product_url}".encode('utf-8')
        )
