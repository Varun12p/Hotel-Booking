import pandas


df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
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

class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self, expiration, holder, cvc):
        card_data = {"number": self.number, "expiration":expiration,"holder":holder,"cvc":cvc}
        if card_data in df_cards:
            return True
        else:
            return False


HOTEL_ID = input("Enter the hotel id:")
hotel = Hotel(HOTEL_ID)

if hotel.available():
    creditcard = CreditCard(number="1234567890123456")
    if creditcard.validate("12/26","JOHN SMITH", "123"):
        hotel.book()
        customer_name = input("Enter your name:")
        reservation = ReservationTicket(customer_name,hotel)
        print(reservation.reservation())
    else:
        print("There is a problem with payment.")
else:
    print("Hotel not available")