#Polymorphism
class Dog:

    def sound(self):
        print("Bark")

class Cat:

    def sound(self):
        print("Meow")

dog = Dog()
cat = Cat()

dog.sound()
cat.sound()

#car
class Car:

    def move(self):
        print("Driving")

class Plane:

    def move(self):
        print("Flying")

c = Car()
p = Plane()

c.move()
p.move()

#Action 
class Bird:

    def action(self):
        print("Flying")

class Fish:

    def action(self):
        print("Swimming")

Bird().action()
Fish().action()