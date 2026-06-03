#print number from 1 to 10 
print("number from 1 to 10 ")
for i in range(1,11):
  print(i)

#print name 5 times
print("name")
for i in range(5):
    print("Yuvraj")


# print number from 10 to 1 
print("number from 10 to 1")
for i in range(10,0,-1):
    print(i)

# print even number from 1 to 20 
print("Print even number ")
for i in  range(1,21):
    if i % 2 == 0:
        print(i)

# print odd number from 1 to 15 
print("Print odd number ")
for i in range(1,16):
    if i % 2 != 0:
        print( i)


#Calculate the sum of number from 1 to 100
print("Calculate that sum of number from 1 to 100")
sum = 0
for i in range(1,101):
    sum+=i
print(sum)


#Table of 7
print("table of 7")
for i in range(1,11):
    print(7*i)


#Count vowel in a string
print("count vowel in a string")
string = "Hello, how are you?"
vowel_count = 0
for char in string:
    if char in "aeiouAEIOU":
        vowel_count += 1
print("Number of vowels:", vowel_count)


