# NumPy Filter Array

import numpy as np

arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
arr1 = arr[x]
print(arr1)

# Creating the Filter Array
arr = np.array([41, 42, 43, 44])
filter_arr = []
for element in arr:
    if element > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
arr1 = arr[filter_arr]
print(filter_arr)
print(arr1)

# Repractising above code
arr = np.array([1,2,3,4,5])
fa = []
for x in arr:
    if x>2:
      fa.append(True)
    else:
        fa.append(False)
arr1 = arr[fa]   # Only the Boolean having True value is extracted 
print(arr1)

# Create a filter array that will return only even elements from the original array:
arr = np.array([1,2,3,4,5,6,7,8,9])
fa = []
for x in arr:
    if x%2==0:
        fa.append(True)
    else:
        fa.append(False)
arr1 = arr[fa]
print(arr1)

# Creating a filter directly from Array
arr = np.array([1,2,3,4,5])
fa = arr>2   # This will append true values where the original array has element greater than 2
arr1 = arr[fa]
print(arr1)

# Creating a filter that will return even numbers
arr = np.array([1,2,3,4,5,6,7,8])
fa = arr%2==0
arr1 = arr[fa]
print(arr1)


