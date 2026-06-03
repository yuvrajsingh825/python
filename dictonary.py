student = {
    "name": "Yuvraj",
    "age": 19,
    "skills": ["Python", "Git"]
}

print(student)

print(student["name"], student["age"], student["skills"])

student["city"] = "Indore"
print(student)

for key in student:
    print(key,":", student[key])
    

for key, value in student.items():
    print(key, ":", value)    