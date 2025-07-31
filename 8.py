class Bank_Account:
    def __init__(self, balance):
        self.balance = balance


    def get_interest(self):
        pass

    def withdraw(self, amount):
        pass


class Savings_Account(Bank_Account):
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f'{amount} sum pul yechib olindi')
        else:
            print("Bunday miqdorda pul yo'q") 


    def get_interest(self):
        interest = self.balance * 0.3 
        return f'Interest: {interest}'        

class Checking_Account(Bank_Account):
    pass


sa = Savings_Account(100_000)
sa.withdraw(10_000) 
print(sa.get_interest())


