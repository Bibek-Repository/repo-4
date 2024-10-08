# Python Inheritance

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func_1(self):
        print(self.name+""+":"+str(self.age))

class Student(Person):                               
    pass

s1=Student("bibek",28)
s1.func_1()

print()
class Parent:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def func_2(self):
        print(self.name, self.age)

class Child(Parent):
    def __init__(self,name,age):                      # In this case, we have defined __init__() function in child class 
        Parent.__init__(self,name,age)                # which will overide the same class in parent class
                                                    #thus we call the __init__() function from parent class and initialize the parameters
c1=Child("Bibek", 28)
c1.func_2()

# super() function

class child1(Parent):                        
    def __init__(self,name,age):
       super().__init__(name,age)               # The super function is used to call the __init__() from Parent class

c2 =child1("bibek", 28)
c2.func_2()

# Add Properties

class child2(Parent):
    def __init__(self,name, age):
        super().__init__(name,age)
        self.year=2024

c3=child2("bibek",28)
c3.func_2()

class child3(Parent):
    def __init__(self,name, age,year):
        super().__init__(name,age)
        self.year=year

c4=child3("bibek",28,2025)
c4.func_2()
print(c4.year)

# Adding a method

class House:
    def __init__(self, number, coordinate):
        self.number=number
        self.coordinate=coordinate

class Room(House):
    def __init__(self,number, coordinate, year):
        super().__init__(number,coordinate)
        self.year=year
    def service(self):
        print(self.number,self.coordinate,self.year)

r1=Room(47,0.3,2024)
r1.service()
        
        

