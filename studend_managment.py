students = []

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. Remove Student")
    print("3. Show Students")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        name = input("Enter student name: ")
        students.append(name)
        print(f"{name} added successfully!")

    elif choice == "2":
        name = input("Enter student name to remove: ")
        if name in students:
            students.remove(name)
            print(f"{name} removed successfully!")
        else:
            print("Student not found!")

    elif choice == "3":
        if len(students) == 0:
            print("No students in the list.")
        else:
            print("\nStudent List:")
            for student in students:
                print(student)

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please enter 1-4.")