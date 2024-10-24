# NumPy Sorting Arrays

import numpy as np

arr = np.array([3,1,7,3,9,4])
print(np.sort(arr))   # Returns the copy of the array not a view

# Sorting array of string
arr = np.array(['bibek', 'apple', 'banana'])
print(np.sort(arr))

# Sorting a boolean array
arr = np.array([True, False, True])
print(np.sort(arr))

# Sorting 2D Array
arr = np.array([[3,6,1],[7,1,4]])
print(np.sort(arr))   # Both the arrays will be sorted

