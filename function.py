# Function that prints my name
def print_name():
    print("Yuvraj")


# Function that prints a city
def print_city():
    print("Dhar")


# Function that prints numbers from 1 to 5
def print_number():
    for i in range(1, 6):
        print(i)


# Function that takes a number and returns its square
def calculate_square(num):
    return num * num


print_name()
print_city()
print_number()

a = int(input("Enter a number: "))
print("Square of", a, "is", calculate_square(a))
