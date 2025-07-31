class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_info(self):
        return f"({self.brand} {self.model})"

class Car(Vehicle):
    def show_info(self):    
        return f"({self.brand}. {self.model})"

class Bike(Vehicle):
    def show_info(self):
        return f"({self.model}. {self.brand})"

c = Car('Rolls Royce', 'Culinnan')
b = Bike('something', 'something')

print(f'{c.show_info()}\n{b.show_info()}')

