NumPy

It stands for Numerical Python. It is a Python Library which is used for working with arrays.
It can also be used for working with linear algebra, fourier transform, and matrices.
It is open source. NumPy has array object which is faster than the python lists. The array object in NumPy is called ndarray. It is frequently used in data science. Data Science is a branch of computer science where we study how to store, use and analyze data for deriving information from it.

NumPy arrays are stored at one continuous place in memory so it is faster. This is known as locality of reference in computer science. It is optimized to work with latest CPU architectures.

NumPy is written in Python, but for the parts that require fast computation c and c++ are used.
Source Code for NumPy: https://github.com/numpy/numpy

Installation of NumPy
pip install numpy. Python distribution such as Anaconda, Spyder etc can be used instead of pip. import keyword can be used to import the numpy library as shown in code file NumPy1.py.

In python, alias are the alternate names for the same thing.

To check the NumPy Version, we can use __version__ attribute.

Creating Arrays
array() function can be used to create NumPy Object: ndarray.
To create an ndarray, we can pass a list, tuple or any array like object into the array() method which will be converted to ndarray.

Dimensions in Arrays:
A dimension in arrays is one level of array depth (nested arrays). Nested arrays have arrays as their elements.

0-D Arrays:
They are scalars. Each value in an array is a 0-D array.

1-D Arrays:
These are the most common and basic arrays. It has 0-D arrays as its elements. It is also called uni-dimensional array.

2-D Arrays:
This array has 1-D arrays as its elements. These are used for matrix or 2nd order tensors. numpy.mat is a module in python used for matrix operations.

3-D Arrays:
It has 2-D arrays(matrices) as its elements. These are often used to represent a 3rd order tensor.

Checking the number of Dimensions:
ndim attribute can be used to check the number of Dimensions. It returns an integer value.

Higher Dimensional Arrays
An array can have any number of dimensions. ndmin argument can be used to define the number of dimensions.
In 5th dimension arrays, 5th dim has 4 elements, 4th dim has 1 element: vector, 3rd dim has 1 element: matrix, 2nd dim has 1 element that is 3D array and 1st dim has 1 element that is a 4D array.

NumPy Array Indexing

Access Array Elements
Array Elements can be accessed by index number. The index in NumPy array stars with 0 and so on.
multi dimensional arrays can be indexed using numbers separated by commas as shown in code file. Negative index will see the elements from backward.

NumPy Array Slicing
Slicing in python means taking elements from one given index to another given index. 
[start:step:end]
If we don't pass start it will start at 0
If we don't pass end it will end at the length of array
If we don't pass step, it will consider 1 as step.

The number after the colon in a slice is excluded. The negative index starts at the end with index -1 and second last -2 and so on. If the number before : in a slice is left empty it will start from 0 and after the colon : if it is left empty then it will end at the last. Steps can be used to skip elements. Double :: will list all the elements. Steps can be added after the double colon, :: to skip elements. 2-D arrays can be sliced by similar way using comma to separate the arrays as shown in code file. 
