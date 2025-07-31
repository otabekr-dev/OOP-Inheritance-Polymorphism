class Character:
    def attack(self):
        pass

    def defend(self):
        pass


class Warrior(Character):
    def attack(self):
        return "Warrior strikes with a sword!"

    def defend(self):
        return "Warrior blocks with a shield!"


class Mage(Character):
    def attack(self):
        return "Mage casts a fireball!"

    def defend(self):
        return "Mage conjures a magic barrier!"


class Archer(Character):
    def attack(self):
        return "Archer shoots an arrow!"

    def defend(self):
        return "Archer dodges quickly!"


w = Warrior()
m = Mage()
a = Archer()

print(w.attack(), "|", w.defend())
print(m.attack(), "|", m.defend())
print(a.attack(), "|", a.defend())
