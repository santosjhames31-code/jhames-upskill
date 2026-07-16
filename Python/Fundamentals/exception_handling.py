while True:
    try:
        num = int(input("Only enter a integer : "))
    except ValueError: 
        print("I said only integer 😡")
    except Exception:
        print("Caught here")
    else: 
        print("Well Done!")
        break