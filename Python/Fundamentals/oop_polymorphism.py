
class Animal:

    def speak(self):
        print("Nothing")

class Dog(Animal):

    def speak(self):
        print("Arf")

class Cat(Animal):

    def speak(self):
        print("Meow")

    
animals = {Animal(), Dog(), Cat()}

for animal in animals:
    animal.speak()