import csv
import os

file_name = "employee.csv"


def create_file():
    if not os.path.exists(file_name) or os.path.getsize(file_name) == 0:
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Salary"])


def add_employee():
    try:
        name = input("Enter name: ")
        salary = input("Enter salary: ")
    except EOFError:
        print("\nInput not available. Run this program in an interactive terminal.")
        return

    with open(file_name, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([name, salary])

    print("Employee added successfully.")


def show_employees():
    with open(file_name, "r", newline="") as file:
        reader = csv.reader(file)
        records = list(reader)

    if len(records) <= 1:
        print("No employee records found.")
        return

    print("Employee Records:")
    for row in records:
        print(row)


create_file()

while True:
    print("\n1. Add Employee")
    print("2. Show Employees")
    print("3. Exit")

    try:
        choice = input("Enter your choice: ")
    except EOFError:
        print("\nInput not available. Run this program in an interactive terminal.")
        break

    if choice == "1":
        add_employee()
    elif choice == "2":
        show_employees()
    elif choice == "3":
        print("Exit")
        break
    else:
        print("Invalid choice.")
