
name = input("Enter your name : ")
length = len(name) #int 
char = 'Jhamn'

print("First Letter : ", name[0])
print("Length : ", length)
print(f"is {char} is in {name}, {char in name}")

#String slicing 
x = name[2 : 7]
y = name[1 : ]
print(x, y)    

#Reverse of Name
print(name[ : :-1])  

uppercase_name = name.upper()
lowercase_name = name.lower()
_trim = name.strip()
_split = name.split()

print(help(str))
