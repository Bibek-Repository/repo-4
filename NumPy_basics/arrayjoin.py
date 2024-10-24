# NumPy Joing Array

import numpy as np

# Joining two Arrays
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.concatenate((arr1, arr2))
print(arr)

# Joining two 2D arrays
arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr = np.concatenate((arr1, arr2), axis=1)  # Returns 2D array. Each index is concatenated to form a new array
# arr3 = np.concatenate((arr1, arr2), axis=2)   # This is error as axis 2 is out of bounds for array of dimension 2
print(arr)

# Joining Arrays Using Stack Functions
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.stack((arr1,arr2), axis=1)  # Returns 2D array. Each element are joined to make an array
print(arr)

# Stacking Along Rows
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.hstack((arr1,arr2))  # This is horizontal join
print(arr)

# Stacking along columns
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr = np.vstack((arr1,arr2))  # This is vertical join
print(arr)

# Stacking Along Height
arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6]) 
arr = np.dstack((arr1,arr2))   # This is done along depth and kept in arrays as shown in output.
print(arr)


