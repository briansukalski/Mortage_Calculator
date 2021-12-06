class Mortgage:
    def __init__(self, home_value, interest_rate, duration=30, down_payment=None):
        self.home_value = home_value
        self.interest_rate = interest_rate / 100
        self.duration = duration
        #Default down payment is 20% if not specified
        if down_payment is None:
            self.down_payment = self.home_value*0.2
        else:
            self.down_payment = down_payment
        self.principal = self.home_value - self.down_payment
        self.monthly_payment = self.calculate_payment()
    def calculate_payment(self):
        payment = self.principal * (self.interest_rate /12) / (1 - (1 + self.interest_rate / 12)**(-self.duration*12))
        payment = round(payment, 2)
        return payment


my_next_house = Mortgage(1000000, 5)
print(my_next_house.monthly_payment)