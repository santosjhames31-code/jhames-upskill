#Diamond

"""
     0
    0 0
   0 0 0
"""

for x in range(5, 0, -1):
    for y in range(x):
        print("", end=" ")
    
    for z in range(y, 5):
        print("*", end= " ")

    for i in range(x, 0):
        print("*", end=" ")

    print()
    
   