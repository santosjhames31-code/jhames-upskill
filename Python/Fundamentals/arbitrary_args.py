"""
def introduce(*args):
    for value in args:
        print(value)

introduce("Jhames", "Andrew", "Santos")

def gmail(**kwargs):
    for key, values in kwargs.items():
        print(f"{key} - {values}")

gmail(email= "santosx", password= "1221", age="19",)


def total(*args):
    sum = 0 
    for num in args:
        sum+= num
    return sum

print(total(1, 2, 3))


def greet(*args):
    for name in args:
        print(f"Hello {name}!")

greet("Jhames", "Mark", "Gian", "Shaenna")
"""
"""
Q3 — Intermediate
Write a function describe_pet(*args, **kwargs) where:

*args holds the pet's names (could be multiple)
**kwargs holds details like species and color


def describe_pet(*args, **kwargs):
    print("Details:", end=" ")
    for value in args:
        print(value, end=", ")
    print()
    for key, val in kwargs.items():
        print(f"{key} - {val} ")

describe_pet("Jekjek", "Kiara", species= "Shi Tzu", color="Black/White")
"""

def total(numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

i = [1,2,3,4,5,6]

print(total(i))
