# Getting the shape of an array

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)   # Has two array with three elements which is displayed.

# creating an array with 5 dimensions using ndmin
arr = np.array([1,2,3,4,5], ndmin=5)
print(arr.shape)

# NumPy Array Reshape

# 1D to 2D
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr1 = arr.reshape(4,3)
print(arr1)

# 1D to 3D
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr1 = arr.reshape(3,2,2)
print(arr1)

# To check if the reshaped array is copy or view
print(arr1.base)   # It returns the original array, so it is a view

#let us change the original array
arr[0]=87  # This will change the value in arr1 as it is a view.
print(arr1)

# Converting 1D array with 8 elements to 3D array with 2x2 elements:

arr = np.array([1,2,3,4,5,6,7,8])
arr1 = arr.reshape(2,2,-1)
print(arr1)

# Flattening the arrays
arr = np.array([[1,2,3],[4,5,6]])
arr1 = arr.reshape(-1)    # This will convert the 2D array to 1D
print(arr1)

