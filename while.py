# While Conditions

i=1 
while i<6:
    print(i)
    i+=1

# The break Statement

print()
i=1
while i<10:
    print(i)                     # Here the break keyword stops the while loop though condition is true
    if (i==5):
        print("the start")
        break        
    i+=1

# The Continue Statement

print()
i=0
while i<6:
    i+=1
    if i == 3:
        continue        # the continue statement won't allow the execution of the code right after it but still remains in the loop
    print(i)            # the output skips 3

# The else Statement

i=1
while i<10:
    print(i)
    i+=1
else:
    print("i is no longer less than 10")

