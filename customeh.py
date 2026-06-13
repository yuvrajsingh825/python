# ==============================
# Custom Exceptions in One File
# ==============================

# 1. Insufficient Balance Error
class InsufficientBalanceError(Exception):
    pass


# 2. Invalid Marks Error
class InvalidMarksError(Exception):
    pass


# 3. Attendance Shortage Error
class AttendanceShortageError(Exception):
    pass


# 4. Invalid Salary Error
class InvalidSalaryError(Exception):
    pass


# 5. Product Out Of Stock Error
class ProductOutOfStockError(Exception):
    pass


# ==============================
# Bank Withdrawal System
# ==============================

try:
    balance = 5000
    withdraw = int(input("Enter withdrawal amount: "))

    if withdraw > balance:
        raise InsufficientBalanceError

    print("Withdrawal Successful")

except InsufficientBalanceError:
    print("Insufficient Balance")


# ==============================
# Student Marks Validation
# ==============================

try:
    marks = int(input("\nEnter Marks: "))

    if marks < 0 or marks > 100:
        raise InvalidMarksError

    print("Valid Marks")

except InvalidMarksError:
    print("Marks must be between 0 and 100")


# ==============================
# Attendance Validation
# ==============================

try:
    attendance = int(input("\nEnter Attendance Percentage: "))

    if attendance < 75:
        raise AttendanceShortageError

    print("Eligible For Exam")

except AttendanceShortageError:
    print("Attendance Below 75%")


# ==============================
# Salary Validation
# ==============================

try:
    salary = int(input("\nEnter Salary: "))

    if salary < 0:
        raise InvalidSalaryError

    print("Valid Salary")

except InvalidSalaryError:
    print("Salary Cannot Be Negative")


# ==============================
# Product Stock Validation
# ==============================

try:
    stock = int(input("\nEnter Product Stock: "))

    if stock == 0:
        raise ProductOutOfStockError

    print("Product Available")

except ProductOutOfStockError:
    print("Product Out Of Stock")