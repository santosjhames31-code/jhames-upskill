
personal_details = {
    "age" : 19,
    "address" : "Bulacan"
}

animal = {
    "name" : "Shaenna",
    "type" : "Cat",
    "details" : personal_details
}

print(animal.get("details").get("age"))