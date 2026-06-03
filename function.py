def square(num):
    return num*num

def is_adult(age):
    if age < 18:
         print("Minor")
         return False
    else:
        print("Adult")
        return True
    
def calculate_total(a, b, c):
    print(" Total : ")
    return a + b + c


age = int(input("Enter your age: "))
print(is_adult(age))


a = int(input("Enter a number: "))
print(square(a))


num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
num3 = int(input("Enter num 3: "))
print(calculate_total(num1, num2, num3))