import requests

URL = "your sheety prices sheet API endpoint URL"


class DataManager:

    def __init__(self):
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        bearer_token = "your bearer token for sheety authentication"
        headers = {"Authorization": f"Bearer {bearer_token}"}
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
        bearer_token = "your bearer token for sheety API authentication"
        headers = {"Authorization": f"Bearer {bearer_token}"}
        customer_endpoint = "your sheety users sheet endpoint URL"
        response = requests.get(customer_endpoint, headers=headers)
        data = response.json()
        self.customer_data = data['users']
        return self.customer_data
