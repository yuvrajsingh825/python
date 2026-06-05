# Tuple is immutable but list is mutable 
fruit=("Mango","orange","kela","tarbuz")
print(fruit)
print(fruit[0])
print(fruit[3])

#tuple of 5 numbers
numbers=(1,2,3,5,5,)
for number in numbers:

    print(number)
print(len(numbers))
print(max(numbers))
print(min(numbers))
print(sum(numbers))

#Count how many times a value appears.
numbers1 = [1, 2, 3, 2, 4, 2, 5]

value = int(input("Enter value to count: "))
count = 0

for num in numbers1:
    if num == value:
        count += 1

print("Count =", count)


# student 
student = (
    "Yuvraj",
    19,
    "CSE AI",
    "Medicaps University"
)

print("Name:",student[0])
print("Age:",student[1])
print("Branch:",student[2])
print("Collage:",student[3])


