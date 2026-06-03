import json

def save_student(student):
    with open("student.json", "w") as f:
        json.dump(student, f, indent=4)

student = {
    "name": "Yuvraj",
    "age": 19,
    "skills": ["Python", "Git"]
}

save_student(student)

print("Student data saved successfully!")