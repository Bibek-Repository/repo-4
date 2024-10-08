# scope in python

# local scope

def myfunc():
    x=10;
    print(x)

myfunc()
# print(x) This line of code is an error, as x is locally defined.

# Global Scope

x=10

def myfunc_1():
    print(x)       # since x is a global variable, it can be accessed locally inside a method.

# method within a method

def my_func2():
    y=2                # here, y is the local variable
    def my_func3():
        print(y)       # the local variable y is used by the method within the method.
    my_func3()

my_func2()

# local and global variable:

x=300  # global variable

def my_func4():
    x=400
    print(x)

print(x)         #global variable is printed
my_func4()      #local variable is printed

# the global keyword

def func():
    # global x
    x=500
    print(x)

func()
print(x)      # Since, the x variable is global, it retains its value outside the method

x=400
print(x)

def func5():
    global x
    x="apple"
    print(x)

print(x)

# non local keyword

def myfunc1():
    y="bibek"
    def myfunc2():
        nonlocal y
        y="hello"
    myfunc2()
    return y        # since y is nonlocal variable, myfunc1() method can call the value of y inside myfunc2()

print(myfunc1())


