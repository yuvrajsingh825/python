student = {
    "name": "Yuvraj",
    "age": 19,
    "branch": "CSE AI"
}

print(student.keys())
print(student.values())
print(student.items())

#update collage name 
student.update({
    "Collage":" Medicaps"
})

print(student)
student.pop("age")
print(student)

#final dictinory
print(student.items())

