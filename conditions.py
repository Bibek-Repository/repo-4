# python conditions

# if condition

a=5
b=2
if a>b:
    print("a is greater than b")
c=10
d=10
if c>d:
    print("mission success")
elif d<c:
    print("mission failed")
else:
    print("there is some error")

# one line if statement

if c==d: print("c is equal to d")

# one line else if statement

print("this is true") if c==d else print("this is false")

# multiple if condition

print("C") if c>d else print("D") if c==d else print("you are in god mode")   # notice here that the method print() is called before the if statement

# And operator

x=200
y=300
z=500

if z>x and z>y:
    print("you are in god mode")

# or statement

if z>y or x<y:
    print("you are in god mode")

# not keyword

if not x>y:
    print("y is greater then x")

# nested if 

a = 13

if a>10:
    print("a is greater than 10")
    if a>20:
        print("a is greater than 20")
    else:
        print("a is smaller than 20")

# the pass statement

if True:
    pass

