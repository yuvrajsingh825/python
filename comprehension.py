number = [x for x in range(1,11)]
print("Number from 1 to 10 using comprenshion")
print(number)

#square of the numbers
square_number = [x*x for x in range(1,11)]
print("Square:", square_number)

# cube of the numbers 
cube_number = [x*x*x for x in range(1,6)]
print("Cube :",cube_number)

#ven number 
even_number = [x for x in range(1,21) if x % 2 == 0]
print("Even numbers :",even_number)

#odd number 
odd_number =[x for x in range(1,21) if x%2!=0]
print("odd_number:",odd_number)

#numbers divisible by 3 
division_number =[x for x in range(1,31) if x%3==0]
print("Divisible by 3 :",division_number)


#ToupperCase
name_upper = ["yuvraj","yashraj","om"]
upper =[names_upper.upper() for names_upper in name_upper]
print(upper)

#Add 10 to each
lists = [20,1,20,25,27,54,45,63,78,95,24,89,99]
add_num = [listss+10 for listss in  lists]
print("Add 10 to each :",add_num)

#filter number less than 50
filter_num = [num for num in lists if num < 50]
print("Filter numbers less than 50:", filter_num)

#length of  string 
name_string = ["hello", "Yuvraj", "Tomar"]

length_string = [len(names_string) for names_string in name_string]

print("Length of string:", length_string)


