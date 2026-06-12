#creating a class 
class student :
    pass

student1 = student()
student2 = student()
student1.name = "Yuvraj"
student2.name ="Ramesh"
print(student1.name)
print(student2.name)

#Create a Book class with title and author.
class Book :
    def __init__(self, title, author):
        self.title = title
        self.author = author
book1 = Book("The lie","Yuvraj")
print(book1.author)


#Create three objects of the same class.
class Place:
    def __init__(self,destiny,count):
        self.destiny = destiny
        self.count = count
place1 = Place("mussory",1)
place2 = Place("indore",10)
place3 = Place("ghar",500)
places = [place1, place2, place3]
for place in places:
    print("places and count ",place.destiny, place.count)
    
#Bank Account
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

account = BankAccount(
    "Yuvraj",
    5000
)

print(account.owner)
print(account.balance)


# Student Management System
class students:
    def __init__(self,name,branch,age):
        self.name = name
        self.branch = branch
        self.age = age
student1 = students("Yuvraj","cseAI",19)
student2 = students("Yash","It",20)
student3 = students("yashi","ECE",18)
student_list = [student1,student2,student3]
for students in student_list:
    print("Student detail :\n",students.name,students.branch,students.age)
