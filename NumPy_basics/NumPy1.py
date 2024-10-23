# NumPy 

import numpy as np    # np is alias for numpy

# To create a NumPy array:
array1 = np.array([1,2,3,4,5])
print(array1)
print(type(array1))

# Checking NumPy Version
print(np.__version__)

# Repractise to create NumPy array:
array2 = np.array(["bibek", "ram", "sita", "champ"])
print(array2)

# Tuple to create a NumPy array:
array3 = np.array((1,2,3,4,5))
print(array3)

# Creating 0-D array with value 54
array4 = np.array(54)
print(array4)

# Create a 1-D array 
array5 = np.array([1,2,3,4,5])
print(array5)

# Creating a 2-D array 
array6 = np.array([[1,2,3], [4,5,"Bibek"]])
print(array6)

# Creating a 3-D array
array7 = np.array([[[1,2,3],[1,2,3]],[[2,3,4],[3,4,5]]])
print(array7)

# Checking the value of dimension in an array
a = np.array(67)
b = np.array([1,2,3])
c = np.array([[1,2,3],[1,2,3]])
d = np.array([[[1,2,3],[1,2,3]],[[1,2,3],[1,2,3]]])
print(a.ndim)
print(b.ndim)
print(c.ndim)
print(d.ndim)

# Creating an array with 5 dimensions and verify it
array8 = np.array([1,2,3,4,5], ndmin=5)
print(array8)
print(f"the dimension of the array is:{array8.ndim}" )

#NumPy Array Indexing
arr = np.array([1,2,3,4])
print(arr[0])
print(arr[2])
print(arr[1]+arr[3])

# Accessing 2-D array
arr = np.array([[12,12,34],[34,55,56]])
print(arr[1,1],"is the required element")  # In the 2nd row 2nd column

arr = np.array([[1,2,3,4,5],[5,6,7,8,9]])
print(arr[1,3])   # 2nd row and 4th column

# Accessing 3-D array:
arr = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
print(arr[1,1,2])

# Negative Indexing
arr = np.array([[[1,2,3],[4,5,6]],[[1,2,5],[8,3,0]]])
print(arr[1,0,-1])  # The output should be 5
print(arr[-1,-1,0])  # The output should be 8
