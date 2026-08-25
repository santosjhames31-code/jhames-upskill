import os


path = "file.txt"
with open(path, "w") as file:
    file.write("hello world")

import json

employee = {
    "name" : "Jhames",
    "age" : "19",
    "sex" : "Male"
}

with open("file.json", "w") as file:
    json.dump(employee, file, indent = 4)

import csv

students = [
    ["Name", "Age", "ID"],
    ["Jhames", 19, "1234"],
    ["Gian", 19, "6767"],
    ["Bertz", 21, "9999"]
    ]

with open("file.csv", "w", newline = "") as file:
    writer = csv.writer(file)
    for row in students:
        writer.writerow(row)


