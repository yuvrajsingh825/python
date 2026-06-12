#Combines name using reduce().
from functools import reduce

names = ["Yuvraj", "Rahul", "Aman"]

result = reduce(
    lambda a, b: a + " " + b,
    names
)

print(result)

#Find sum using reduce().
num = [20,50,47,89,63,21,25]
sum = reduce(lambda a,b: a+b,num)
print("Sum of the number :",sum)

#Find maximum value.
max_value = reduce(
    lambda a,b: a if a>b else b , num
)
print("MAximum Number :",max_value)

#Find minimum value.
min_value = reduce(
    lambda a,b : a if a<b else b, num
)
print("Minimun value :",min_value)

#product of all number
mul_value = reduce(
    lambda a,b: a*b ,num  
)
print("Product pf all numbers :",mul_value)

#Shopping Cart Calculator
prices = [1200, 500, 800, 1500]
total_bill = reduce(
    lambda a,b :a+b , prices
)
print("Total amount :",total_bill)

highest_price = reduce(
    lambda a,b: a if a>b else b , prices
)
print("Highest product price :",highest_price)