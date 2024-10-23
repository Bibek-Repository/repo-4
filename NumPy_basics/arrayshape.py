# Getting the shape of an array

import numpy as np

arr = np.array([[1,2,3],[4,5,6]])
print(arr.shape)   # Has two array with three elements which is displayed.

# creating an array with 5 dimensions using ndmin
arr = np.array([1,2,3,4,5], ndmin=5)
print(arr.shape)
