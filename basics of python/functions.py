# functions in python

def my_function():                                 # Defining a function in Python
    print("This is my first python function")

my_function()                                      # Calling the function in Python

def function_1(employee):
    print(employee+" is inserted")                 # The argument is employee

function_1("Ramesh")                               # string is passed to the argument during the calling
function_1("Jyoti")
function_1("Bibek")

def function_2(fname, lname):
    print(fname+" "+lname)           # two parameters 

function_2("Bibek", "Baiju")         # two Arguments

# Tuple of Argument

def function_2(*model):
    print(model[0]+" "+model[1]+" "+model[2])
    print(type(model))                              # model is tuple

function_2("00a","00t5","77ry")

# passing the dictionary to the function as an argument

def function_3(**a):
    print(a["fname"]+" "+a["lname"])
    print(type(a))                                  # a is dictionary(python **kwargs) 

function_3(fname="Bibek",lname="Baiju")

# Default parameter value

def function_4(country="Nepal"):
    print(country)

function_4()                 # Here, the default parameter value Nepal is passed as the argument
function_4("America")

# Passing a list as an Argument and a dictionary as an argument

list1=["apple", "orange", "banana"]
dict1={
    "major":"science",
    "faculty":"Computer",
    "shift":"morning"
}

def function_5(major):
    print(major[0],major[1], major[2])

function_5(list1)

def function_6(major):
    print(major["major"],major["faculty"], major["shift"])

function_6(dict1)

#we can use loop to access the values and keys in functions

def function_7(param):
    for x,y in param.items():
        print(x+" "+y)

function_7(dict1)

# Returning a Value in functions

def function_8():
    return "apple"

print(function_8())

def function_9(r):
    r*=2
    print("the double of the value is "+str(r))

function_9(4)

def function_10():
    pass                    # If there is no content for the function, then pass keyword can be used to prevent error

# keyword arguments in python

def function_11(name, age):
    print(name+" is "+str(age)+" years old")

function_11("bibek", 29)
function_11(age=29, name="the champ")     # Notice here that the name and age is altered, but still python recognizes the correct parameter using the keyword

# only positional arguments

def function_12(a, /):
    print(a)

# function_12(a="ram")  # python receives an error as , / in the parameter tells that it can have only positional arguments

# only keyword arguments

def function_13(*,a):               # Here, only the keyword arguments are used because of *, in the parameter
    print(a)

function_13(a="ramesh")

def function_14(a,b,/,*,d,e):        # any parameters before ,/ are positional parameters
    print(a,b,d,e)                   # any parameters after *, are keyword parameters

function_14(4,5,e=25,d=10)

# Recursion function

def tri_recursion(k):
    if(k>0):
        result = k + tri_recursion(k-1)   #tri_recursion() method is called until the parameter k-1 equals to 0 and else part is executed
        print(result)                     # after that the result is printed and the upper recursive calls are executed correspondingly
    else:
        result = 0
    return result                     # check this in the practise copy to understand the flow

print()
tri_recursion(6)


