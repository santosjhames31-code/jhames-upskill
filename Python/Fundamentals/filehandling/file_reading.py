

try: 
    with open("file.txt", "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("File does not exist")

import json

try: 
    with open("file.json", "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("File does not exist")

import csv
try:
    with open("file.csv", "r") as file:
        content = csv.reader(file)
        for row in content:
            print(row)
except FileNotFoundError:
    print("File does not exist")