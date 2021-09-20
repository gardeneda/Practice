from twilio.rest import Client
import os
from flight_data import FlightData

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.

    def __init__(self):
        self.TWILIO_SID = "AC68ea024145801e9cc13b53752d501aa8"
        self.TWILIO_AUTH = os.environ.get("TWILIO TOKEN")

    def check_lowest_price(self, data: FlightData, registered_data):
        # Use this in a for-loop
        client = Client(self.TWILIO_SID, self.TWILIO_AUTH)
        for city in registered_data:
            if city["lowestPrice"] > data.price:
                message = client.messages.create(body=f"{}",
                                                 from_='+16264145685',
                                                 to='+17789530112'
                )

        pass




