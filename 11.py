class Product:
    def __init__(self, name):
        self.name = name

    def get_delivery_method(self):
        pass

    def download(self):
        pass


 
class PhysicalProduct(Product):
    def get_delivery_method(self):
        return f"{self.name} pochta orqali yuboriladi"

    def download(self):
        return f"{self.name} — bu jismoniy mahsulot, yuklab bo'lmaydi"



class DigitalProduct(Product):
    def get_delivery_method(self):
        return f"{self.name} elektron pochta orqali yuboriladi"

    def download(self):
        return f"{self.name} yuklab olinmoqda..."



book = PhysicalProduct("Kitob")
e_book = DigitalProduct("Elektron kitob")

print(book.get_delivery_method())
print(book.download())

print(e_book.get_delivery_method())
print(e_book.download())
