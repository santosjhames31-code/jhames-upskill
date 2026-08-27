import os

file_path = "file.txt"

print(os.path.exists(file_path))
print(os.path.isfile(file_path))

with open(file_path, "w") as file:
    file.write("hahaha")

f = open(file_path, "w")
f.write("jhames")