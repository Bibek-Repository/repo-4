import numpy as np
import math
from math import log

# using zip() method to add two lists:
x = [1,2,3,4,5]
y = [6,7,8,9,0]
z = []
print(zip(x,y))
print(type(zip(x,y)))
for i, j in zip(x,y):   # It will loop through x an y for each elements simultaneously.
    z.append(i+j)
print(z)

# Let us try to add string and numbers
# x = [1,2,3,4,5]
# y = ['Bibek', 'Baiju', 'Ram', 'hari', 'Shyam']
# z = []
# for i, j in zip(x,y):
#     z.append(i+j)    # Since y has string and x has int they can not be added together.
# print(z)

# Doing above code using python numpy functions
z = np.add(x,y)
print(z)   # This will do the same as above.

# Creating my own ufunc function
def myadd(x,y):
    return x+y
myadd = np.frompyfunc(myadd, 2,1)
print(myadd([1,2,3,4], [5,6,7,8]))

# To check if a function is a ufunc or not
print(type(np.add))  # It returns numpy.ufunc. It is a ufunc
print(type(np.concatenate)) # It returns numpy.ArrayFunctionDispatcher. It is not ufunc
# print(type(np.asdkfjasd))  # It returns an error

# To check if a function in if statement if a ufunc or not:
if type(np.add) == np.ufunc:
    print("add is ufunc")
else:
    print("add is not ufunc")

# Adding the values in two array
arr1 = np.array([10, 11, 12 , 13,14, 15])
arr2 = np.array([20, 21, 22 ,23 , 24 , 25])
arr3 = np.add(arr1, arr2)
print(arr3)

# Subtraction
arr4 = np.subtract(arr3, arr2) # arr3 - arr2 = arr1
print(arr4)

# Multiplication
arr5 = np.multiply(arr1, arr2)
print(arr5)

# Division
arr6 = np.divide(arr2, arr1)
print(arr6)

# Let us try to divide by zero
arr7 = [0]
arr8 = [1]
arr9 = np.divide(arr8, arr7)
print(arr9)  # It returns inf as it something divided by 0 is infinite

# Power
arr3 = np.power(arr1, arr2)
print(arr3)

# Remainder
arr3 = np.remainder(arr1, arr2)
arr4 = np.mod(arr1, arr2)
print(arr3, arr4)

# Quotient and Mod
arr5 = np.divmod(arr1, arr2)  # This function will return both the quotient and Mod 
print(arr5)   

# Absolute Values
arr = np.array([1,-2,3, 0, -5])
print(np.absolute(arr))

# Rounding Decimals
arr = ([-1.336, 6.333])
print(np.trunc(arr))   # Use readme file to understand the operation
print(np.fix(arr))
print(np.around(arr))
print(np.floor(arr))
print(np.ceil(arr))

# Logs
# log at base 2
arr = ([1,10,3,18])
print(np.log2(arr))

print(np.arange(1,10))  # This will construct an array from 1 to 9. 10 is excluded.
arr = np.arange(1,6)
print(np.log10(arr))

# Natural log or base at e
arr = np.array([1,2,math.e,3,5])
print(np.log(arr))

# log at any base (frompyfunc)
nplog = np.frompyfunc(log, 2, 1)  # This creates a function which can be used to calculate the log of any base.
print(nplog(100, 15))   

# Summation of all the elements in the array
arr1 = np.array([1,3,6,8])
arr2 = np.array([4,5,6,7])
print(np.sum([arr1, arr2]))

# Summation over an Axis
arr1 = np.array([1,2,3,5])
arr2 = np.array([6,7,8,9])
arr3 = np.sum([arr1, arr2], axis = 1)  # This will do summation in each axis
print(arr3)

# Cummulative Sum
arr3 = np.cumsum(arr1)  # This will sum from index 0 to the current index
print(arr3)

# Numpy products
arr3 = np.prod(arr1)  # This will multiply each element in the array
print(arr3)
arr4 = np.prod([arr1, arr2])  # This will multiply all elements in both array
print(arr4)

# Product over an axis
arr8 = np.prod([arr1,arr2], axis = 1)  # It returns an array with two products as axis is defined.
print(arr8)

# Cummulative Product
arr1 = np.array([1,2,3,4,5])  # This will multiply the current index with all the index before it.
print(np.cumprod(arr1))

# Discrete Differences
arr = np.arange(1,10)  
arr1 = np.diff(arr)   # It will subtract current index with the index just before it
print(arr1)

# Repeatative Difference
arr = np.array([1,5,6,3,6])
arr1 = np.diff(arr, n = 2)  # first it returns: 4,1,-3,3 and after n =2, -3,-4,6
print(arr1)

# Finding LCM
num1 = 4
num2 = 6
x = np.lcm(num1, num2)
print(x)

# Finding LCM in arrays
arr = np.array([3,6,9])
print(np.lcm.reduce(arr))

# Finding GCD (HCF)
num1 = 6
num2 = 9
x = np.gcd(num1, num2)
print(x)

# Finding GCd in the array
arr = np.array([20, 8, 32, 36, 16])
print(np.gcd.reduce(arr))

# Trigonometric Function
x = np.sin(np.pi)
y = np.cos(np.pi)
z = np.tan(np.pi)
print(x, y, z)

# Trigonometric Function in array
arr = np.array([np.pi/2, np.pi/3, np.pi/5])
x = np.sin(arr)
y = np.cos(arr)
z = np.tan(arr)
print(x,y,z)

# Conversion from degree to radian:
arr = np.array([90, 180, 270, 360])
x = np.deg2rad(arr)
print(x)

# Conversion from radian to degree:
arr = np.array([np.pi, np.pi/2, np.pi/3])
x = np.rad2deg(arr)
print(x)

# Finding angles that is arc of sin, cos and tan
x = np.arcsin(1.0)
print(x)
print(np.rad2deg(x))   # This means that the sin90 = 1, We can do similar to cos and tan

# Finding angles in an array
arr = np.array([1, math.inf, 0])
print(np.arctan(arr))
print(np.rad2deg(arr))

# Hypotenues
base = 3
perp = 4
x = np.hypot(base, perp)
print(x)

# Hyperbolic Functions
x = np.sinh(np.pi/2)
print(x)

# Hyperbolic Functions of array
arr = np.array([1,5,234,34,336])
print(np.sinh(arr))   # Note here that the values are returned in radians

# Finding the angle
y = np.arcsinh(x)
print(y)
print(np.rad2deg(y))

# Finding the angle for each element in an array
arr = np.array([1,23,5,6,334])
arr1 = np.sinh(arr)
print(arr1)

# Creating an set out of an array
arr = np.array([1,1,1,2,2,33,3,3,33,4,4,4,4])
x = np.unique(arr)
print(x)

# Finding Union
arr1 = np.array([1,2,3,4])
arr2 = np.array([3,4,5,6])
arr3 = np.union1d(arr1,arr2)
print(arr3)

# Finding Intersection
arr4 = np.intersect1d(arr1, arr2, assume_unique= True)  # the assume_unique parameter will speed up computation if set to True
print(arr4)

# Finding the Difference
arr3 = np.setdiff1d(arr1, arr2, assume_unique= True)
print(arr3)

# Finding the symmetric Difference
arr3 = np.setxor1d(arr1, arr2, assume_unique= True)   # the assume_unique parameter will speed up computation if set to True
print(arr3)

 

