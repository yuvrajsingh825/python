import json

data = {
    "name": "yuvraj",
    "age": 19
}

with open("student.json", "w") as file:
    json.dump(data, file, indent=4)

with open("student.json", "r") as file:
    student = json.load(file)
    print(student)

