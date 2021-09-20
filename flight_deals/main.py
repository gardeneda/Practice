# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes
# to achieve the program requirements.

from data_manager import DataManager
from flight_search import FlightSearch
import datetime

time_now = datetime.datetime.now()
tomorrow = time_now + datetime.timedelta(days=1)
six_months = time_now + datetime.timedelta(weeks=24)

tomorrow_str = tomorrow.strftime("%d/%m/%Y")
six_months_str = six_months.strftime("%d/%m/%Y")

CITYFROM = "Vancouver"
CITYFROM_IATACODE = "YVR"

# --------------------------------------------------------------------------

manager = DataManager()
fly_search = FlightSearch()

test_data = [{'city': 'Paris', 'iataCode': 'PAR', 'lowestPrice': 54, 'id': 2},
             {'city': 'Berlin', 'iataCode': 'BER', 'lowestPrice': 42, 'id': 3},
             {'city': 'Tokyo', 'iataCode': 'TYO', 'lowestPrice': 485, 'id': 4},
             {'city': 'Sydney', 'iataCode': 'SYD', 'lowestPrice': 551, 'id': 5},
             {'city': 'Istanbul', 'iataCode': 'IST', 'lowestPrice': 95, 'id': 6},
             {'city': 'Kuala Lumpur', 'iataCode': 'KUL', 'lowestPrice': 414, 'id': 7},
             {'city': 'New York', 'iataCode': 'NYC', 'lowestPrice': 240, 'id': 8},
             {'city': 'San Francisco', 'iataCode': 'SFO', 'lowestPrice': 260, 'id': 9},
             {'city': 'Cape Town', 'iataCode': 'CPT', 'lowestPrice': 378, 'id': 10}]


list_data = manager.get_data()
list_data_iata = [city["iataCode"] for city in list_data]

for cityto_iataCode in list_data_iata:
    flight_data = fly_search.search_flight(
        tomorrow_str=tomorrow_str,
        six_months_str=six_months_str,
        cityto_iataCode=cityto_iataCode,
        cityfrom_iataCode=CITYFROM_IATACODE,
    )
    manager.put_data()
    for

# --------------------------------------------------------------------------



