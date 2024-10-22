# Opening a file in python

f = open("samplefile.txt")

try:
    f = open("samplefile.txt")
    print("File opened successfully")
except FileNotFoundError:
    print("File not found. Please check the file path")

f= open("samplefile.txt", "rt") # here r is for read mode and t is for text mode which is default value.