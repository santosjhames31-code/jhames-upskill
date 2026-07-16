num1 = int(input("First number  : "))
num2 = int(input("Second number : "))

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return round(float(num1 / num2), 2)
print("""
---- Operation -----
[1] Add
[2] Subtract
[3] Divide
[4] Multiply
""")
while True:
    choice = int(input("Enter choice (1 - 4) : "))
    if choice == 1:
       ans = add(num1, num2)
       break
    elif choice == 2:
        ans = subtract(num1, num2)
        break
    elif choice == 3:
        ans = divide(num1, num2)
        break
    elif choice == 4:
        ans = multiply(num1, num2)
        break
    else:
        print("Please select from choices (1 - 4)")

print(f"Answer : {ans}")