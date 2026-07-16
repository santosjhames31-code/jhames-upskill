x  = {2, 4, 6, 8,}
x.add(10)
print(f"Add{x}")

#Update
x  = {2, 4, 6, 8,}
y = [1, 3, 5, 7, 9]
x.update(f"Update : {y}")

#Remove
x  = {2, 4, 6, 8,}
x.remove(2)
print(f"Remove : {x}")

#Discard
x  = {2, 4, 6, 8,}
x.discard(1)
print(f"Discard : {x}")

#Pop (removes 1st value)
x  = {2, 4, 6, 8,}
x.pop()
print(f"Pop : {x}")

#Copy
x  = {2, 4, 6, 8,}
z = x.copy()
print(f"Copy : {z}")

#Union
x  = {2, 4, 6, 8,}
y = {12, 14, 16}
u = x.union(y)
print(f"Union : {u}")

#Difference
x  = {2, 4, 6, 8,}
d = {2, 4}
print(f"Difference : {x.difference(d)}")

#Intersection (returns all the same values)
x  = {2, 4, 6, 8,}
y = {2, 4}
i = x.intersection(y)
print(f"Intersection : {i}")

#Symmetric difference (removes all the same values)
x  = {2, 4, 6, 8,}
y = {2, 4, 1, 3}
z = x.symmetric_difference(y)
print(f"Symmetric Diff : {z}")

#Isdisjoint (no same values)
x  = {2, 4, 6, 8,}
y = {1, 3, 5, 7}
i = x.isdisjoint(y)
print(f"Is Disjoint : {i}")

#Issubset (Child set, all the values of set x should be in set y)
x  = {2, 4, 6}
y = {2, 4, 6, 8, 10}
s = x.issubset(y)
print(f"Is Subset : {s}")

#Issuperset (Parent set, all the values of set y should be in set x )
x  = {2, 4, 6}
y = {2, 4, 6, 8, 10}
s = x.issuperset(y)
print(f"Is Superset : {s}")