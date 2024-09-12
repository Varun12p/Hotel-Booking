from operator import index

import pandas
from numpy.ma.core import squeeze
from pandas.core.interchange.from_dataframe import primitive_column_to_ndarray

df = pandas.read_csv("hotels.csv", dtype={"id": str})

print(df)

class Hotel():
    def __init__(self, hotel_id):
        self.hotel_id = hotel_id
        self.name = df.loc[df["id"]== self.hotel_id,"name"].squeeze()

    def available(self):
        availability = df.loc[df["id"]== self.hotel_id, "available"].squeeze()
        if availability == "yes":
            return True
        else:
            return False

    def book(self):
        df.loc[df["id"] == self.hotel_id, "available"] ="no"
        df.to_csv("hotels.csv", index=False)


class ReservationTicket():
    def __init__(self, customer_name, hotel_object):
        self.customer_name = customer_name
        self.hotel = hotel_object

    def reservation(self):
        content = f""" 
        Thank you for your reservation.
        Here are your booking details:
        Name: {self.customer_name}
        Hotel: {self.hotel.name} 
            """
        return content


HOTEL_ID = input("Enter the hotel id:")
hotel = Hotel(HOTEL_ID)
customer_name = input("Enter your name:")


if hotel.available():
    hotel.book()
    reservation = ReservationTicket(customer_name,hotel)
    print(reservation.reservation())
else:
    print("Hotel not available")