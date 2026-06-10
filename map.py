#Double every number using map().
number = [1,54,78,20,32,10,21]
double = list(map(lambda x : x*2,number))
print("Number after double : ", double)

#Square every number using map().
square = list(map(lambda x : x*x , number))
print("Square of numbers :",square)

#convert string into integers
data = ["10", "20", "30", "40"]
convert = list(map(int, data))
print(convert)

#Convert names to uppercase.
names = ["yuvraj", "singh", "tomar"]
upper = list(map(str.upper, names))


#