#List 
courses = ["BSIT", "BSCE", "BSIS", "BSCS", "BSHM"]
print(courses[0])

print(courses[ : : -1]) # Reverse 

#To add an item to list
courses.append("BSME")

#To add an item in a specified place
courses.insert(0, "XXX")

#Remove
courses.remove("BSIT")

#Pop - removes an item from a specified position
courses.pop(1)
del courses

a = ["p", "q", "r"]
b = ["x", "y", "z"]
c = a+b
c.sort()
print(c)

#Tuple
a = ("p", "q", "r")
b = ("x", "y", "z")
print(a)

#Type Casting
a = list(a)
b = list(b)

a = tuple(a)
b = tuple(b)
