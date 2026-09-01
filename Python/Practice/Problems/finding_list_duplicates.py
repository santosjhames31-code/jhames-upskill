num_list = [1, 2, 3, 4, 5, 3, 2, 2, 4, 2, 1, 4]

duplicates = []

for i in num_list:
    if num_list.count(i) > 1 and i not in duplicates:
        duplicates.append(i)

print(duplicates)