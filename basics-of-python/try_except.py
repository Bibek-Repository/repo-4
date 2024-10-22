# Exception handling in python

try:
    print(x)
except:
    print("An exception occurred")  # Since x is not defined, so the exception is generated

# defining multiple exceptions
try:
    print(x)
except NameError:
    print("Variable x in not defined")
except:
    print("Something else went wrong")

# Else keyword incase no errors are found
try:
    print("Bibekster")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Finally block will be raised whether there is error or not at the end
try:
    print(x)
except:
    print("Something went wrong")
finally:
    print("The 'try except in python' is finished")

# lets try to open and write to a file that is not writable:

try:
    f = open("demofile.txt", "a")   # opens the file demofile.txt in append mode
    try:
        f.write("Bibek")  # appends the string "Bibek" to the file
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()  # This is executed even if the exception occurs. But in this case no such exceptions occurred.
except:
    print("Something went wrong when opening the file")

# Raise an exception

x = -5
if x < 0:
    raise Exception("Sorry, no numbers below zero")

y = "bibek"
if not type(y) is int:
    raise TypeError("Only intergers are allowed")   # This is not working as the exception is caught above