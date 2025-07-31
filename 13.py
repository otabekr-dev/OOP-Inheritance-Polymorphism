class Courier:
    def delivery_range(self):
        pass

    def calculate_fee(self, distance):
        pass


class BikeCourier(Courier):
    def delivery_range(self):
        return "5 km gacha"

    def calculate_fee(self, distance):
        return distance * 1000


class CarCourier(Courier):
    def delivery_range(self):
        return "20 km gacha"

    def calculate_fee(self, distance):
        return 5000 + distance * 1500


class DroneCourier(Courier):
    def delivery_range(self):
        return "10 km gacha"

    def calculate_fee(self, distance):
        return distance * 2000 


bike = BikeCourier()
car = CarCourier()
drone = DroneCourier()

print("Bike:")
print(bike.delivery_range())
print("To'lov:", bike.calculate_fee(4), "so'm")

print("\nCar:")
print(car.delivery_range())
print("To'lov:", car.calculate_fee(10), "so'm")

print("\nDrone:")
print(drone.delivery_range())
print("To'lov:", drone.calculate_fee(6), "so'm")
