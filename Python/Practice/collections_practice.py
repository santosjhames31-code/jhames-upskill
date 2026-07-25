import time as t
list = []

size = int(input("Enter Size: "))
for x in range(size):
    num = int(input(f"Enter element {x+1} : "))
    list.append(num)

class Arithmetic:
    sumOdd = 0
    sumEven = 0
    list = []

    def __init__(self, list):
        self.list = list

    def display_odd(self, list):
        for element in list:
            if element % 2 == 1:
                print(element, end= " ")
                self.sumOdd += element
        print()

    def display_even(self, list):
        for element in list:
            if element % 2 == 0 and not element == 0:
                print(element, end= " ")
                self.sumEven += element
        print()

a = Arithmetic(list)

while(True):
    print("[1] Display Odd")
    print("[2] Display Even")
    print("[3] Sum Odd")
    print("[4] Sum even")
    print("[5] Exit")
    choice = int(input("Enter choice : "))

    match(choice):
        case 1: 
            print("====================")
            print("Odd Numbers : ", end= "")
            a.display_odd(list)
            print("====================")
        case 2:
            print("====================")
            print("Even Numbers : ", end= "")
            a.display_even(list)
            print("====================")
        case 3:
            print("====================")
            print(f"Sum Odd  : {a.sumOdd}")
            print("====================")
        case 4:
            print("====================")
            print(f"Sum Even : {a.sumEven}")
            print("====================")
        case 5:
            print(f"Exiting program...")
            break
