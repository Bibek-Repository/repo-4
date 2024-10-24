from numpy import random

# Generating a random int
x = random.randint(100)
print(x)

# Generating a random float
x = random.rand()   # It will generate random float from 0 to 1
print(x)

# Generating a 1D array of 5 random numbers
x = random.randint(100, size=(5))
print(x)

# Generating a 2D array with 3 rows each containing 5 random numbers
x = random.randint(10, size=(3,5))
print(x)

# Generating a 1D array containing 5 random floats
x = random.rand(5)
print(x)

# Generating a 2D array with 3 rows each containing 5 random floats
x = random.rand(3, 5)
print(x)

# Generating random number from array
x = random.choice([3,5,7,9])
print(x)

# Generating an array of random number from an array
x = random.choice([1,5,4,7,3,77], size=(3,5))
print(x)