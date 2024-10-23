# Copy 

import numpy as np

arr = np.array([1,2,3,4,5])
arr1 = arr.copy()
arr[0] = 7
print(arr)
print(arr1)

arr = np.array(['b',1,2,3])
print(arr)
print(arr.dtype)

# View
arr = np.array([1,2,3,4,5])
arr1 = arr.view()
arr[0] = 19
print(arr)
print(arr1)

arr1[2] = 45   # change the view
print(arr)      # there is corresponding change in the original

# To check if an Array owns its Data or not
arr = np.array([1,2,3,4,5])
x = arr.view()  # It returns the original array 
y = arr.copy()  # It returns none
print(x.base, y.base)