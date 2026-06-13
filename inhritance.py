#Animal
class Animal:

    def eat(self):
        print("Eating")

class Dog(Animal):
    pass

dog = Dog()

dog.eat()

# vehicle
class Vehicle:

    def start(self):
        print("Vehicle Started")

class Car(Vehicle):
    pass

car = Car()

car.start()

#student
class Person:

    def __init__(self, name):
        self.name = name

    def show_name(self):
        print(self.name)

class Student(Person):
    pass

s1 = Student("Yuvraj")

s1.show_name()

#College Management System
class Person1 :
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch
    def show_details(self):
        print(self.name,self.age,self.branch)

class Student1(Person1):
    pass

st1 = Student1("Yuvraj",20,"CseAI")
st1.show_details()

