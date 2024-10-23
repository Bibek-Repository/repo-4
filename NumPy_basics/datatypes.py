# Checking the data type of an array

import numpy as np

# Data type of integer array
array1 = np.array([1,2,3,4,5])
print(array1.dtype)

# Data type of string array
arr = np.array(['Bibek','harley','world'])
print(arr.dtype)

# Creating Arrays with a Defined Data type

# Creating a array with data type string:
arr = np.array([1,2,3,4], dtype='S')
print(arr)
print(arr.dtype)

# Creating an array with data type 4 bytes integer:
arr = np.array([1,2,3,4], dtype='i4')
print(arr)
print(arr.dtype)

# trying to convert a string to integer
# arr = np.array(['bibek', '2', '3'], dtype='i')   # Here, Bibek is a non-integer string, hence it cannot be converted.
# print(arr)
# print(arr.dtype)

# Converting Data Type on Existing Arrays
arr = np.array([1.1,2.1,3.1,4.1])
arr1 = arr.astype('i')
print(arr)
print(arr1)
print(arr1.dtype)

# Doing the above using int as a parameter
arr = np.array([1.2,2.2,3.2,4.2])
print(arr)
arr2 = arr.astype(int)
print(arr2)

# Changing data type from integer to boolean
arr = np.array([1,0,3])
arr1 = arr.astype(bool)
print(arr,arr1)
