import json
student = {
    "name": "Yuvraj",
    "age": 19,
    "skills": ["Python", "Git"]
}  

# Convert Python object to JSON string
json_string = json.dumps(student, indent=4)
print(json_string)
