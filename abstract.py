from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self):
        pass


# Child Class 1
class UPI(Payment):

    def pay(self):
        print("Paid using UPI")


# Child Class 2
class Card(Payment):

    def pay(self):
        print("Paid using Card")


# Child Class 3
class NetBanking(Payment):

    def pay(self):
        print("Paid using Net Banking")


# Objects
upi = UPI()
card = Card()
netbanking = NetBanking()

# Call Methods
upi.pay()
card.pay()
netbanking.pay()