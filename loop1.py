for i in range(10):
    print("hello")

    count = -1

while count <= 5:
    print(count)
    count += 1
    break

print("break")

for i in range(10):
    if i ==1:
        continue 
    print("i = " + str(i))


for i in range(6):
    if i == 0:
        continue
    print(i)



for i in range(10, 0, -1):
    print(i)


''''''
num = 7

for i in range(1, 11):
    print(i, "x", num, "=", i * num)