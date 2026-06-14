# Student record file
file_name = "student_records.txt"
students = ["Yuvraj", "Ramesh", "Shivam", "Raj", "Salim"]

# Create student record file
with open(file_name, "w") as file:
    pass

# Append 5 student names
with open(file_name, "a") as file:
    for student in students:
        file.write(student + "\n")

# Read all records and count total lines
try:
    with open(file_name, "r") as file:
        records = file.readlines()

    print("Student Records:")
    for record in records:
        print(record.strip())

    print("Total lines:", len(records))

except FileNotFoundError:
    print("Student record file not found.")
