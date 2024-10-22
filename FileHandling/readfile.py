# To read the content of a file

f = open("samplefile.txt", "r")
print(f.read())

# If the file is located in different location

f = open(r"C:\Users\Bibekster\pythonproject\basics-of-python\demofile.txt", "r") # Here r is used because \d is used as an escape character in python.
print(f.read())

# Reading only parts of file
f = open("samplefile.txt", "r")
print(f.read(5))    # Here, parameter 5 tells to read only 5 characters from the file. White spaces are counted.

# To read only one line
f = open("samplefile.txt", "r")
print(f.readline())
print(f.readline())  # It reads next line
print(f.readline())  # It reads the third line and so on

# Loop through the file line by line:
f = open("samplefile.txt", "r")
for x in f:
    print(x)

# To close a file
f = open("samplefile.txt", "r")
print(f.readline())
f.close()
