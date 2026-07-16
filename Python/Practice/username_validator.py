
username = input("Enter username (must not contain spaces and digits, no more than 12 char) : ") 

if not username.isalpha():
    print("Username must not contain digits.")
elif not username.find(" ") == -1:
    print("Username can't contain spaces.")
elif len(username) > 12:
    print("Username must not exceed 12 characters.")
else:
    print(f"Welcome {username}")


