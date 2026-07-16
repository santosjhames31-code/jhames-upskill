import datetime as d
import time
import random

balance = 0
"""
Show Balance
"""
def show_balance(balance):
    print('--------------------')
    print(f"Balance : PHP {balance : .2f}")
    print(f"Date    : {d.datetime.now()}")
    print(f"Ref No. : {d.datetime.now().year}{str(d.datetime.now().time()).replace(":", "")[0:6]}{random.randint(10, 999)}")
    print('--------------------')

"""
Deposit 
"""

def deposit():
    while True:
        try:
            print('------- Deposit Money -------')
            amount_deposit = float(input("Enter amount to deposit (Minimum of PHP 100): "))
        except ValueError:
            print("Invalid data type")  
        else: 
            if amount_deposit < 100: 
                print("Invalid amount")
            else:
                print("Successful Deposit")
                print(f"Amount  : PHP {amount_deposit : .2f}")
                print(f"Date    : {d.datetime.now()}")
                print(f"Ref No. : {d.datetime.now().year}{str(d.datetime.now().time()).replace(":", "")[0:6]}{random.randint(10, 999)}")
                print('--------------------')
                global balance
                balance += amount_deposit 
                print('--------------------')
            break

"""
Withdraw
"""
def withdraw():
    global balance
    while True:
        try:
            amount_withdraw = float(input("Enter amount to withdraw : "))
        except ValueError:
            print("Invalid data type")
        else:
            if amount_withdraw > balance:
                print("Insufficient balance")
            else:
                balance -= amount_withdraw 
                print("Succesful Withdraw")
                print(f"Withdraw Amount : PHP {amount_withdraw : .2f}")
                print(f"Current Balance : PHP {balance : .2f}")
                print(f"Date            : {d.datetime.now()}")
                print(f"Ref No.         : {d.datetime.now().year}{str(d.datetime.now().time()).replace(":", "")[0 : 6]}")
                break

mainLoop = True
while mainLoop:
        print("---- Banking Program ----")
        print("[1] Show Balance")
        print("[2] Deposit")
        print("[3] Withdraw")
        print("[4] Exit")

        choice = (input("Enter choice (1 - 4) : "))
        if choice not in ['1', '2', '3', '4']:
            print("Please Select from choices 1 - 4")
        else:
            match choice:
                case '1': 
                    show_balance(balance)
                case '2':
                    deposit()   
                case '3':
                    withdraw()
                case '4':
                    for i in range(3):
                        time.sleep(0.5)
                        print(".", end="") 
                    print("\nSuccessfully Exited")
                    mainLoop = False
            
        


