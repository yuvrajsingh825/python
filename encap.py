class BankAccount:

    def __init__(self):
        self.__balance = 0

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Deposit amount must be positive!")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.__balance:
            print("Insufficient Balance!")
        else:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")


# Create object
account = BankAccount()

# Deposit
account.deposit(5000)
print("Balance:", account.get_balance())

# Withdraw
account.withdraw(2000)
print("Balance:", account.get_balance())    