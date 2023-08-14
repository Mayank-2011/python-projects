import requests
import os

URL = "https://api.sheety.co/7f4eb7cf4cfa2d5a9d033ca21174766f/cheapFlightFinder/prices"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        headers = {"Authorization": "Bearer IAMGROOT"}
        response = requests.get(url=URL, headers=headers)
        data = response.json()
        self.destination_data = data['prices']
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city['iataCode']
                }
            }
            response = requests.put(
                url=f"{URL}/{city['id']}",
                json=new_data
            )
            print(response.text)

    def get_customer_emails(self):
        headers = {"Authorization": "Bearer IAMGROOT"}
        customer_endpoint = "https://api.sheety.co/7f4eb7cf4cfa2d5a9d033ca21174766f/cheapFlightFinder/users"
        response = requests.get(customer_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data['users']
        return self.customer_data
