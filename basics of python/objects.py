# Objects or classes in python

# creating a class named Myclass

class Myclass:          
    x=5

# creating an object of the class

obj1=Myclass()
print(obj1.x)

# the __init__() function

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age

p1=Person("Bibek",28)

print(p1.name,p1.age)

# the __str__() function

class Student:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    
    def __str__(self):
        return f"{self.name},{self.age}"  # this will return the strings within the curly braces

p2= Student("ramesh",54)
print(p2)

p3=Student("Jyoti",52)
print(p3)

# inserting methods in the class

class Programmer:
    def __init__(self, name, number):
        self.coder=name
        self.ratings=number
    
    def func_1(self):                           # the self parameter helps to access the properties of the class
        print("Python programmer:"+self.coder)

c1=Programmer("Bibek", 99)
c1.func_1()

class Gamer:
    def __init__(abc, name, rate):                   # Here we can see the first parameter self can have any name
        abc.gamer=name
        abc.rate=rate
    def func_2(xyz):
        print("The gamer is "+xyz.gamer+" the rating is "+str(xyz.rate))

g1=Gamer("bibek", 9)
g1.func_2()

# Modify the property of the class

g1.gamer="Bibek Baiju"
g1.func_2()

# Deleting the property of the object


# del obj1.x
# print(obj1.x)      # This line of code cannot be executed because property in obj1 is already deleted

# deleting object using del keyword

# del obj1

# The pass statement

class Temp:          # For any reason, if there is no content in the class, pass keyword can be used to prevent the error
    pass





