import random
import time

list = ["😝", "❤", "💲"]
slot1 = slot2 = slot3 = "😝"
attempts = 0
while True:

    choice = input("Do you want to spin? [y/N] : ")
    choice = choice.upper()
    match choice:
        case 'Y':
            slot1 = random.choice(list) 
            slot2 = random.choice(list) 
            slot3 = random.choice(list)
            attempts += 1
            print(f"Attempts : {attempts}")
            print("Slot Machine")
            print("***************")
            print(f"| {slot1} | {slot2} | {slot3} |")
            print("***************")

            if(slot1 == slot2 == slot3):
                print("--------------------")
                print(f"You won!, after {attempts} attempts")
                attempts = 0 
                print("--------------------")
            else:
                print("--------------------")
                print("You lost!")  
                print("--------------------")  
        case 'N':
            print("Exiting Program...")
            break
        case _ : 
            print("Invalid Choice")
