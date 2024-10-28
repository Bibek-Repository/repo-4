import numpy as np

# using zip() method to add two lists:
x = [1,2,3,4,5]
y = [6,7,8,9,0]
z = []
print(zip(x,y))
print(type(zip(x,y)))
for i, j in zip(x,y):   # It will loop through x an y for each elements simultaneously.
    z.append(i+j)
print(z)

# Let us try to add string and numbers
# x = [1,2,3,4,5]
# y = ['Bibek', 'Baiju', 'Ram', 'hari', 'Shyam']
# z = []
# for i, j in zip(x,y):
#     z.append(i+j)    # Since y has string and x has int they can not be added together.
# print(z)

# Doing above code using python numpy functions
z = np.add(x,y)
print(z)   # This will do the same as above.
