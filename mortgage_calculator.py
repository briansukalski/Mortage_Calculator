def future_value_from_annuity(payment_amount, interest_rate, number_periods):
    pass

class Home_Ownership:
    def __init__(self, home_value, appreciation_rate):
        self.home_value = home_value
        self.appreciation_rate = appreciation_rate
        self.mortgage = None

    def calc_future_value(self, ownership_duration):
        if self.mortgage is not None:
            mortgage_future_value = future_value_from_annuity(self.mortgage.monthly_payment(), self.mortgage.pay_period_interest_rate, self.mortgage.pay_periods)

class Mortgage:
    def __init__(self, home_value, annual_interest_rate, duration=30, annual_payments=12, down_payment=None):
        self.home_value = home_value
        self.annual_interest_rate = annual_interest_rate / 100
        self.duration = duration
        self.annual_payments = annual_payments
        self.pay_period_interest_rate = self.annual_interest_rate / self.annual_payments
        self.pay_periods = self.duration * self.annual_payments
        #Default down payment is 20% if not specified
        if down_payment is None:
            self.down_payment = self.home_value*0.2
        else:
            self.down_payment = down_payment
        self.principal = self.home_value - self.down_payment
        self.monthly_payment = self.calculate_payment()
    def calculate_payment(self):
        payment = self.principal * (self.pay_period_interest_rate) / (1 - (1 + self.pay_period_interest_rate)**(-self.pay_periods))
        payment = round(payment, 2)
        return payment


my_next_house = Mortgage(1000000, 5)
print(my_next_house.monthly_payment)