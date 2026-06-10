#Create a lambda to square a number.
square = lambda num :num*num
print(square(10))

#Create a lambda to cube a number.
cube = lambda num :num*num*num
print(cube(10))

#Create a lambda to add two numbers.
sum = lambda a,b:a+b
print(sum(10,25))

#Create a lambda to multiply two numbers.
mul = lambda a,b:a*b
print(mul(10,25))

#Create a lambda that returns the larger of two numbers.
larger = lambda y,z: y if y > z else z
print(larger(50,25))


add = lambda a, b: a + b
subtract = lambda a, b: a - b
multiply = lambda a, b: a * b
divide = lambda a, b: a / b


a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))
value = add(a, b)
print("Addition:",value)

value = subtract(a,b)
print("Subtract:",value)

