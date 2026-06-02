# expense_manager.py

from datetime import datetime


def add_expense(expenses):
    try:
        amount = float(input("Enter amount: ₹"))
    except ValueError:
        print("Invalid amount!")
        return

    category = input("Category: ")

    expense = {
        "amount": amount,
        "category": category,
        "date": datetime.now().strftime("%Y-%m-%d %H:%M")
    }

    expenses.append(expense)

    print("Expense Added Successfully")


def view_expenses(expenses):

    if not expenses:
        print("No expenses found.")
        return

    print("\nExpense History\n")

    for i, exp in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{exp['amount']} | "
            f"{exp['category']} | "
            f"{exp['date']}"
        )


def total_expense(expenses):

    total = sum(exp["amount"] for exp in expenses)

    print(f"\nTotal Expense = ₹{total}")


def category_summary(expenses):

    summary = {}

    for exp in expenses:

        category = exp["category"]

        summary[category] = (
            summary.get(category, 0)
            + exp["amount"]
        )

    print("\nCategory Wise Summary\n")

    for category, amount in summary.items():
        print(f"{category}: ₹{amount}")