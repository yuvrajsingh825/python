# main.py

from datetime import datetime

from file_handler import (
    load_expenses,
    save_expenses
)

from expense_manager import (
    add_expense,
    view_expenses,
    total_expense,
    category_summary
)


def menu():

    expenses = load_expenses()

    while True:

        print("\n" + "=" * 30)
        print(" EXPENSE TRACKER ")
        print("=" * 30)

        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Total Expense")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            add_expense(expenses)
            save_expenses(expenses)

        elif choice == "2":
            view_expenses(expenses)

        elif choice == "3":
            total_expense(expenses)

        elif choice == "4":
            category_summary(expenses)
            print(f"Current Date and Time: {datetime.now().strftime('%Y-%m-%d %H:%M')}")


        elif choice == "5":
            save_expenses(expenses)
            print("Goodbye!")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    menu()