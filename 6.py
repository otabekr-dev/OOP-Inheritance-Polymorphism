class Employee:
    def calculate_bonus(self):
        pass


class Dev(Employee):
    def __init__(self, salary):
        self.salary = salary
    
    def calculate_bonus(self):    
        return f'Sizga 10% miqdorida bonus berildi: ({self.salary * 0.1 + self.salary})'      

class Mngr(Employee):
    def __init__(self, salary):
        self.salary = salary

    def calculate_bonus(self):
        return f'Sizga 15% miqdorida bonus berildi: ({self.salary * 0.15 + self.salary}) '


dev = Dev(100_000)
manager = Mngr(200_000)

print(f'{dev.calculate_bonus()}\n{manager.calculate_bonus()}')
