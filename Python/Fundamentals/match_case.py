

num = int(input("Enter a number (1 - 7) : "))

def day(num):
    match num:
        case 1:
            print("Sunday")
        case 2:
            print("Monday")
        case 3:
            print("Tuesday")
        case 4:
            print("Wednesday")
        case 5:
            print("Thursday")    
        case 6:
            print("Friday")
        case 7:
            print("Saturday")
        case _:
            print('Invalid number')

day(num)