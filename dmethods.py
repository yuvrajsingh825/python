person={
    "name":"Yuvraj",
    "age":"20",
    "gender":"male",
    "height":"5.9",

}

print(person.get("age"))
print(person)
print(person.keys())
print(person.values())
print(person.items())
print(person.pop("gender"))
print(person)

# 1. Create a student dictionary and update age

student = {
    "name": "Yuvraj",
    "age": 19,
    "city": "Khachrod"
}

student["age"] = 20

print("Updated Student Dictionary:")
print(student)


# 2. Create a product dictionary and update stock

product = {
    "name": "Laptop",
    "price": 50000,
    "stock": 10
}

product["stock"] = 15

print("\nUpdated Product Dictionary:")
print(product)


# 3. Loop through all keys

print("\nKeys:")
for key in student.keys():
    print(key)


# 4. Loop through all values

print("\nValues:")
for value in student.values():
    print(value)


# 5. Loop through all key-value pairs using items()

print("\nKey-Value Pairs:")
for key, value in student.items():
    print(key, ":", value)