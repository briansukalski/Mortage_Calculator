class Mortgage:
    def __init__(self, value, duration=30):
        self.value = value
        self.duration = duration
        self.monthly_payment = round(value / (self.duration*12), 2)

my_next_house = Mortgage(1000000)
print(my_next_house.monthly_payment)