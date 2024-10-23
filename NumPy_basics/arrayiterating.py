# Iterating Arrays

import numpy as np

# Iterating 1D arrays
arr = np.array([1,2,3])
for x in arr:  # It will iterate one by one to each element
    print(x)

# Iterating 2D arrays
arr = np.array([[1,2,3],[4,5,6]])
for x in arr:  # It will iterate each row
    print(x)

# To iterate on each scalar element of 2D array one by one
arr = np.array([[1,3,4],[3,6,8]])
for x in arr:  # Here, x takes each row and again is a 1 D array which can be iterated again as illustrated below
    for y in x:
        print(y)

# To iterate 3D array
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,13]]])
for x in arr:
    print(x)

# To return all the values the scalars
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
for x in arr:
    for y in x:
        for z in y:
            print(z)

# Iterating Arrays Using nditer()
arr = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
for x in np.nditer(arr):
    print(x)

# Iterating Array with Different Data types
arr = np.array([1,2,3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):   # Here the flags will enable the op_dtypes and store it in buffer.
    print(x)

# Iterating with Different Step Size
arr = np.array([[1,2,3,4],[5,6,7,8]])
for x in np.nditer(arr[:, ::2]):   # Here, the first colon will say to iterate both row, and the second one will give step size of 2
    print(x)

# Enumerated Iteration Using ndenumerate()
arr = np.array([1,2,3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

# Enumerate 2D array
arr = np.array([[1,2,3,4],[5,6,7,8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)