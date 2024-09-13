import pandas


df = pandas.read_csv("hotels.csv", dtype={"id": str})
df_cards = pandas.read_csv("cards.csv", dtype=str).to_dict(orient="records")
df_cards_security = pandas.read_csv("card_security.csv",dtype=str)
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

class CreditCardSecurity(CreditCard):
    def authenticate(self,given_password):
        password = df_cards_security.loc[df_cards_security["number"]==self.number, "password"].squeeze()
        if password == given_password:
            return True
        else:
            return False


HOTEL_ID = input("Enter the hotel id:")
hotel = Hotel(HOTEL_ID)

if hotel.available():
    number = input("Enter you CreditCard number:")
    creditcard = CreditCardSecurity(number)
    if creditcard.validate("12/26","JOHN SMITH", "123"):
        passw = input("Enter Your CreditCard Password:")
        if creditcard.authenticate(passw):
            hotel.book()
            customer_name = input("Enter your name:")
            reservation = ReservationTicket(customer_name,hotel)
            print(reservation.reservation())
        else:
            print("CreditCard authentication failed.")
    else:
        print("There is a problem with payment.")
else:
    print("Hotel not available")