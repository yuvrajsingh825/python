import csv
import os

file_name = "students.csv"


def create_file():
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Age", "Branch"])


def add_student():
    name = input("Enter name: ")
    age = input("Enter age: ")
    branch = input("Enter branch: ")

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, age, branch])

    print("Student added successfully.")


def show_students():
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)
        records = list(reader)

    if len(records) <= 1:
        print("No student records found.")
        return

    print("Student Records:")
    for row in records:
        print(row)


create_file()

while True:
    print("\n1. Add Student")
    print("2. Show Students")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_student()
    elif choice == "2":
        show_students()
    elif choice == "3":
        print("Exit")
        break
    else:
        print("Invalid choice.")
