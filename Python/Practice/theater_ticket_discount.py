

age = -1
ticket_qty = 0
price = 0
genre = 0
discount = 0

while True:
    print("*****Theater Ticket Counter*****")
    print(f"[1] Action PHP 250.00")
    print(f"[2] Horror PHP 350.00")
    while True:
        try:
            genre = int(input("Choose a genre : ")) 
        except ValueError:
            print("Invalid data type")
        else:
            break
    if genre == 1:
        price = 250
        break
    elif genre == 2:
        price =  350
        break
    else:
        print("Please select between numbers 1 and 2")


while not ticket_qty > 0:
    ticket_qty = int(input("Enter number of tickets : "))

while True:
    age = int(input("Enter your age : "))
    if  not age < 0: 
        break
    if age > 60:
        discount = 0.25 * (price * ticket_qty)

total_price = price * ticket_qty - discount
print(f"Total : PHP {total_price : 10,.2f}")