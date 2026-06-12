#Filter even numbers.
number = [7,5,89,36,21,45,10,20,24,26,82]
even_number = list(filter(lambda x : x % 2 == 0, number))
print("even_number:", even_number)

#Filter odd numbers.
odd_number = list(filter(lambda x: x%2!=0 , number))
print("Odd numbers :",odd_number)

#Filter numbers greater than 10.
greater = list(filter(lambda x: x > 10, number))
print("greater than 10 :",greater)

#Filter passed students.
marks={
    "Yuraj":45,
    "Yash":85,
    "XY":20,
    "shu":45
}

record = list(filter(lambda x: x[1] > 33, marks.items()))
print(record)


#filter names longer than 5 characters.
name = ["yuvraj","yahs","shivu","raj","salim","lala"]
compare=list(filter(lambda x : len(x) > 5,name))
print(compare)


#
marks = [35, 45, 90, 20, 80, 50]
passed = list(
    filter(lambda x: x >= 40, marks)
)
print("passes :\n",passed)
distinction = list(
    filter(lambda x: x >= 75, marks)
)
print("distinction :\n",distinction)

