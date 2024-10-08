# polymorphism in python

#function polymorphism

# len() method as the polymorphism in python

#len() method to return number of characters in a string

x="Bibek Baiju"
print(len(x))         # number of characters in x

# len() in tuple

x=("ram", "shyam", "hari")
print(len(x))         # number of values in the tuple

#class Polymorphism

class Car:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model

    def move(self):
        print("drive!")

class Boat:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("sail!")

class Plane:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("fly!")

c1=Car("ford","v12")
b1=Boat("Rup","7lm4")
p1=Plane("jip","rrt67")

for x in (c1,b1,p1):
    x.move()

# Inheritance Class Polymorphism

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("move")

class motorcycle(Vehicle):
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("ride")

class car(Vehicle):
    pass

m1=motorcycle(brand="royal enfield", model="bullet 350")
c1=car("tata","nexon")

for x in (m1, c1):
    print(x.model) 
    print(x.brand)
    x.move()
    




        


