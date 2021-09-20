import requests
from flight_data import FlightData
import pprint

class FlightSearch:

    def __init__(self):

        self.HEADER = {"apikey": "_aLjLkMcGSFEnzOSuEaPXB8_m9gxXJrz"}
        self.API_endpoint = "https://tequila-api.kiwi.com/v2/search"

    def search_flight(self, tomorrow_str, six_months_str, cityto_iataCode, cityfrom_iataCode):
        params = {
            "fly_from": cityfrom_iataCode,
            "fly_to": cityto_iataCode,
            "date_from": tomorrow_str,
            "date_to": six_months_str,
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "USD"
        }

        response = requests.get(url=self.API_endpoint, params=params, headers=self.HEADER)
        response.raise_for_status()
        # pprint.pprint(response.json(), indent=4)
        raw_data = response.json()

        try:
            data = raw_data['data'][0]
        except IndexError:
            print(f"No flights have been found flying to {cityto_iataCode}")
            return None

        flight_data = FlightData(
            city_from=data['cityFrom'],
            city_to=data['cityTo'],
            from_iataCode=data['cityCodeFrom'],
            to_iataCode=data['cityCodeTo'],
            price=data['price'],
            local_arrival=data['local_arrival'],
            local_departure=data['local_departure'],
        )

        print(f"{flight_data.city_to}: ${flight_data.price}")
        return flight_data






