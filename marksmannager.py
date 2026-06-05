marks = [78, 85, 92, 67, 88]
print("Marks:",marks)
print("Highest Marks :", max(marks))
print("Lowest Marks :", min(marks))
print("Total marks :", sum(marks))
print("Average marks :", sum(marks)/len(marks))


# using list Methods 
list1 =["python","java","c","rust"]
list1.append("node.js")
list1.append("sql")
list1.append("c#")
print(list1)
list1.remove("c#")
list1.pop(3) 
print(list1)
list1.reverse()
print(list1)

#Remove all occurrences of a number using loops.
numbers=[1,2,4,8,10,445,5,21,0,10]
for i in numbers:
    if i == 10:
        numbers.remove(i)
print(numbers)

#while
numbers = [1, 2, 3, 2, 4, 2, 5]
remove_num = 2

while remove_num in numbers:
    numbers.remove(remove_num)

print(numbers)