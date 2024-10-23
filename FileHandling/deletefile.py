# To delete a file in python

import os

# f = open("samplefile4.txt", "w") # creates a file
# f.close()

# Now let us delete the created file samplefile4.txt
# os.remove("samplefile4.txt")

# The file has been deleted
# Using if else to check if the file to be deleted exists or not. 

if os.path.exists("samplefile4.txt"):
    os.remove("samplefile4.txt")
else:
    print("The file doesn't exist!")

# To delete a folder
# os.rmdir("deletefolder")   # This will delete the entire folder

# Trying to delete file out side the folder
file_path = r"C:\Users\Bibekster\pythonproject\checkfile.txt"  # r is used here because \ in python is escape character.
if os.path.exists(file_path):
    os.remove(file_path)