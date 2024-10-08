# For Loops in python

# for loop in lists:

teachers = ["John", "Jack", "Kendra", "Michael"]
for x in teachers:
    print(x)

# Looping through the string

for x in "banana":
    print(x)   

# The break Statement

for x in teachers:    
    if x=="Kendra":
        break
    print(x)

print()
for x in teachers:
    print(x)
    if x=="Kendra":
        break

# The Continue Statement

print()
for x in teachers: 
    if x=="Kendra":
        continue
    print(x)

# The range() function

print()
for x in range(6):   # the last value 6 is excluded
    print(x)

print(range(6))
print()

for x in range(2,10):
    print(x)

# The range value can be incremented by a value

for x in range(3,15,4):
    print(x)

# Else keyword can be used to specify a block of code when the loop is executed

for x in teachers:
    print(x)
else:
    print("all the names of the teachers has been listed")

for x in range(10):
    if x==3:break            # Here, the else block is not executed
    print(x)
else:
    print("mission complete")

for x in range(15):
    if x==5: continue
    print(x)
else:
    print("the code is completed")

# Nested loops

a=["harley-davidson", "triumph", "Royal Enfield"]
b=["Ramesh", "Jyoti", "Bibek"]

for x in a:
    for y in b:     
        print(x,y)

for x in [0,1,2,3,4,5]:
    pass
