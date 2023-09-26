"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, wage, hours=0, fixed_bonus = 0, number_of_contracts = 0, commission_per_contract = 0):
        self.name = name
        self.contract = Contract(wage, hours)
        if fixed_bonus or number_of_contracts:
            self.commission = Commission(fixed_bonus, number_of_contracts, commission_per_contract)
        else:
            self.commission = None

    def get_pay(self):
        if self.commission:
            return self.contract.get_contracted_pay() + self.commission.get_commission()
        else:
            return self.contract.get_contracted_pay()

    def __str__(self):
        if self.commission:
            return f"{self.name} {str(self.contract)} {str(self.commission)}. Their total pay is {self.get_pay()}."
        else:
            return f"{self.name} {str(self.contract)}. Their total pay is {self.get_pay()}."


class Contract:
    def __init__(self, wage, hours=0):
        self.wage = wage
        self.hours = hours

    def get_contracted_pay(self):
        if self.hours:
            return self.wage*self.hours
        return self.wage
        
    def __str__(self):
        if self.hours:
            return f'works on a contract of {self.hours} hours at {self.wage}/hour'
        else:
            return f'works on a monthly salary of {self.get_contracted_pay()}'

class Commission:
    def __init__(self, fixed_bonus = 0, number_of_contracts = 0, commission_per_contract = 0):
        self.fixed_bonus = fixed_bonus
        self.number_of_contracts = number_of_contracts
        self.commission_per_contract = commission_per_contract
        
    def get_commission(self):
        if self.fixed_bonus:
            return self.fixed_bonus
        else:
            return self.number_of_contracts * self.commission_per_contract
        
    def __str__(self):
        if self.fixed_bonus:
            return f'and receives a bonus commission of {self.fixed_bonus}'
        else:
            return f'and receives a commission for {self.number_of_contracts} contract(s) at {self.commission_per_contract}/contract'



# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', wage=4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', wage=25, hours=100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', wage=3000, number_of_contracts=4, commission_per_contract=200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', wage=25, hours=150, number_of_contracts=3, commission_per_contract=220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', wage=2000, fixed_bonus=1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', wage=30, hours=120, fixed_bonus=600)
