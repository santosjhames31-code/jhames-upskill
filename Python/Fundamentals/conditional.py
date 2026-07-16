"""
# Conditional Calculator

operator = input("Select operation (+ - * /) : ")
num1 = float(input("Enter num 1 : "))
num2 = float(input("Enter num 2 : "))


if operator == "+": 
    result = num1 + num2
    print(f"Sum : {round(result, 2)}")
elif operator == "-":
    result = num1 - num2
    print(f"Difference : {round(result, 2)}")
elif operator == "*":
    result = num1 * num2
    print(f"Product : {round(result, 2)}")
elif operator == "/":
    result = num1 / num2
    print(f"Quotient : {round(result, 2)}")
else:
    print("Invalid operator.")
"""
"""
import math
#Temperature Calculator

print("Temperature Calculator")
print("[1] Celcius to Farenheit")
print("[2] Farenheit to Celcius]")
choice = int(input("Select between choice [1] and [2]: "))



if choice == 1:
    temp = float(input("Temperature (Celcius) : "))
    formula = temp * 9/5 + 32
    print(f"Farenheit             : {round(formula, 2)} F")
elif choice == 2:
    temp = float(input("Temperature (Farenheit) : "))
    formula = temp * 1.8 + 32
    print(f"Celcius                 : {round(formula, 2)} C")
else:
    print(f"{choice} is an invalid choice")

i = 1
if not i == 0:
    print("not zero")   
"""

#Conditional Expressions
num = 6

print("Even" if num % 2 == 0 else "Odd")
is_even = True if num % 2 == 0 else False

print(is_even)