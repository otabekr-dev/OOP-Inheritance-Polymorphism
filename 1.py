class Animal:
    def speak(self):
        return 'some kind of animal voice'

class Dog(Animal):
    def speak(self):
        return 'Woof woof'



class Cat(Animal):
    def speak(self):
        return 'Meow'


dog = Dog()
cat = Cat()

print(f'Dog: {dog.speak()}\nCat: {cat.speak()}')
        