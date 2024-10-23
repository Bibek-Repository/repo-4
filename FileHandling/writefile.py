# Write to an Existing File
f = open("samplefile.txt", "a")  # a stands for append mode. This will append to the end of file
f.write("Bibek in the world of champs!")
f.close()

# Read the appended file
f = open("samplefile.txt", "r")
print(f.read())

# Open the file samplefile2.txt
f = open("samplefile2.txt", "w")    # In write mode, the file will be automatically created if it is not created.
f.write("This is a new samplefile")
f.close()

# Open the samplefile2.txt
f = open("samplefile2.txt", "r")
print(f.read())

# Creating a new file in python
# f = open("samplefile3.txt", "x")  # In x mode, file is created if the file has not been yet created else error is returned.
# f.write("This file is just created in x mode ")
# f.close()
f = open("samplefile3.txt", "r")
print(f.read())
f.close()