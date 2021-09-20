class FlightData:

    def __init__(self, city_from, city_to, from_iataCode, to_iataCode, price, local_arrival, local_departure):
        self.city_from = city_from
        self.city_to = city_to
        self.city_from_iata = from_iataCode
        self.city_to_iata = to_iataCode
        self.arrival_time = local_arrival
        self.departure_time = local_departure
        self.price = price

