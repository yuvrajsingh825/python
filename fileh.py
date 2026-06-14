#read from file
file = open("name.txt","r")
data = file.read()
print(data)
file.close()

#append
file = open("name.txt","a")
file.write("Indore")
file.close()


#readlines
file = open("name.txt","r")
print(file.readlines())
file.close()

#readline
file=open("name.txt","r")
print(file.readline())
file.close()
