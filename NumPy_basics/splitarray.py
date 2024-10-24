# Splitting Array

import numpy as np

arr = np.array(['bibek', 'land', 'kathmandu', 'environment', 'school'])
arr1 = np.array_split(arr,2)   # It splits array into two arrays  # It returns the list of array
print(arr1)

arr = np.array([1,2,3,4,5,6])
arr1 = np.array_split(arr,3)  # It splits array into three arrays
print(arr1)

arr = np.array([1,2,3,4,5,6])
arr1 = np.array_split(arr,4) # Here it will split by adjusting the elements required
print(arr1)

# Accessing the splitted Arrays:
arr = np.array([1,2,3,4,5,6])
arr1 = np.array_split(arr,3)
print(arr1[0])
print(arr1[1])
print(arr1[2])

# Splitting the 2D Arrays
arr = np.array([[1,2],[3,4],[5,6],[7,8],[9,10],[11,12]])
arr1 = np.array_split(arr,3)
print(arr1)

# Splitting the 2D array into three 2D arrays
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
arr1 = np.array_split(arr,3)
print(arr1)

# To split along the row, axis = 1
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
arr1 = np.array_split(arr, 3, axis=1)
print(arr1)

# Using hsplit() to split 2D array into three 2D array
arr = np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12],[13,14,15],[16,17,18]])
arr1 = np.hsplit(arr,3)  # It splits into three arrays which have the elements of same index from each array. 
print(arr1)


