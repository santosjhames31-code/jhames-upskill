"""Create two sets: A = {1, 2, 3, 4, 5} and B = {4, 5, 6, 7, 8}. Print their union, intersection, and difference (A - B).
"""
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
U = A.union(B)
print(f"Union : {U}")

"""
You have this list: [1, 2, 2, 3, 4, 4, 4, 5]. Convert it to a set and print it. What do you notice?
"""
list = [1, 2, 2, 3, 4, 4, 4, 5]
SET = set(list)
print(f"Set : {SET}")

"""
Create a set of 5 country names. Ask the user to input a country and print whether it is in the set or not.
"""
countries = {"PHILIPPINES", "USA", "FRANCE", "AUSTRALIA"}
inp = input(f"Enter a country : ")
inp = inp.upper()
print(inp in countries)

"""Given a list nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], use a set comprehension to create a set of all squared values that are greater than 25. Print the result.
"""
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
square_num = set([i**2 for i in nums if i**2 > 25])
print(square_num)

"""
You have two sets representing students who passed Math and students who passed English:
Students who passed both
Students who passed only Math
Students who passed only English
Students who passed neither 
"""
math = {"Ana", "Ben", "Cleo", "Dan", "Eva"}
english = {"Ben", "Eva", "Faye", "Gus", "Ana"}
all_students = math | english | {"Hank", "Iris"}

print(f"Both : {math.intersection(english)}")
print(f"Math Only : {math.difference(english)}")
print(f"English Only : {english.difference(math)}")
print(f"Neither : {all_students.difference(english.union(math))}")