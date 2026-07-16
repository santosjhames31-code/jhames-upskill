#Odd numbers
odd = []
odd = [x for x in range(1, 11) if x % 2 == 1 ]
print(odd)


#Format list

fruits = {'apple', 'banana', 'grapes', 'dalandan'}
formatted_fruits = { fruit.capitalize() for fruit in fruits}
print(formatted_fruits)

#Abs 
numbers = [1, -2, -3, 4, -5 ,6, -7]
abs_numbers = [ abs(number) for number in numbers]
print(abs_numbers)