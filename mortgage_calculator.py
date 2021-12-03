class Mortgage:
    def __init__(self, value, interest_rate, duration=30):
        self.value = value
        self.interest_rate = interest_rate / 100
        self.duration = duration
        self.monthly_payment = self.calculate_payment()
    
    def calculate_payment(self):
        payment = self.value * (self.interest_rate /12) / (1 - (1 + self.interest_rate / 12)**(-self.duration*12))
        payment = round(payment, 2)
        return payment


my_next_house = Mortgage(1000000, 2.5)
print(my_next_house.monthly_payment)