import requests
import datetime


class DataManager:

    def __init__(self):
        self.SHEETY_ENDPOINT = 'https://api.sheety.co/8c5b4d159911156aa18c8c0316f42959/flightDeals/prices'
        self.SHEETY_HEADERS = {
            'Authorization': 'Basic cGVyZmVjdGdhcmRlbjohVGVzdGluZ1BhcmFtczkwMTI='
        }
        self.destination_data = {}

    def get_data(self):
        response = requests.get(self.SHEETY_ENDPOINT, headers=self.SHEETY_HEADERS)
        response.raise_for_status()
        raw_data = response.json()
        self.destination_data = raw_data["prices"]
        return self.destination_data

    def put_data(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "Lowest Price": city["price"]
                }
            }
            response = requests.put(
                url=f"{self.SHEETY_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=self.SHEETY_HEADERS
            )
            print(response.text)