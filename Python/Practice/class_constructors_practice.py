#Make an Order class for ChickIT! with item, quantity, price_per_item. Add a method total() that returns quantity * price_per_item.

class Order:
    overall_price = 0
    def __init__(self, item, qty, price):
        self.item = item
        self.qty = qty 
        self.price = price
        Order.overall_price += qty * price
    def total(self):
        return self.qty * self.price    
    
order1 = Order("Garlic Parmesan", 3, 225)
order2 = Order("Jack Daniels", 2, 250)

print(order1.total())
print(order2.total())
print(f"total :", Order.overall_price)


"""
Default parameters (Python's answer to overloading)
Make a Car class where fuel_type defaults to "Gasoline" if not provided. Create one car with 3 args, one with only 2.
"""

class Car:
    def __init__(self, brand, type, fuel_type = "Gasoline"):
        self.brand = brand
        self.type = type
        self.fuel_type = fuel_type

    def details(self):
        print(f"Name  : {self.brand}")
        print(f"Type  : {self.type}")
        print(f"Fuel  : {self.fuel_type}")

car1 = Car("Ford", "4 Wheels")
car2 = Car("Tesla", "Tesla.inc", "Electric")       
car1.details()
print()
car2.details()

""". 
Methods that use self
Add a method is_long() to Book that returns True if pages > 300. Test it on both books.
"""
class Book:
    def __init__(self, book_name, pages):
        self.pages = pages
        self.book_name = book_name

    def is_long(self):
        if self.pages > 300:
            return True

b1 = Book("Harry Potter", 2500)
b2 = Book("Noli Me Tangere", 150)

print(b1.is_long())
print(b2.is_long())