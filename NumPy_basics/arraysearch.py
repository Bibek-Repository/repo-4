# NumPy Searching Arrays

import numpy as np

# Getting the index of the element in the array
arr = np.array([1,2,3,4,5,6,7])
x = np.where(arr==4)  # It returns index 3 as the element 4 is in index 3
print(x)

arr = np.array(['bibek', 2,3])
x = np.where(arr=='bibek')
print(x)

arr = np.array([1,2,3,4,5,6,7,8,9])
x = np.where(arr%2==0)  # where the values are even that is remainder is 0 when divided by 2
print(x)

arr = np.array([1,2,3,4,5,6,7,8,9])
x = np.where(arr%2==1) # where the values are odd
print(x)

# Search Sorted
arr = np.array([1,2,3,4,5])
y = np.searchsorted(arr, 5)
print(y)

# Search from the Right Side
arr = np.array([1,2,3,4,5,6,7])
y = np.searchsorted(arr, 5, side='right')
print(y)

# Multiple Values
arr = np.array([1,3,5,7,9])
x = np.searchsorted(arr, [2,4,6])  # The numbers to be inserted are in index [1 2 3]
print(x)
