class Appliance:
    def turn_on(self):
        pass

    def turn_off(self):
        pass


class TV(Appliance):
    def turn_on(self):
        return f'TV turned on'

    def turn_off(self):
        return f'TV turned off'

class Fridge(Appliance):
    def turn_on(self):
        return f'Fridge is working'

    def turn_off(self):
        return f'Fridge is turned off'            

tv = TV()
fridge = Fridge()

print(tv.turn_on())
print(tv.turn_off())

print(fridge.turn_on())
print(fridge.turn_off())
