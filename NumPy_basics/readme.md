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

Data types in NumPy
i: integer
b: boolean
u: unsigned integer
f: float
c: complex float
m: timedelta
M: datetime
O: object
S: string
U: unicode string
V: fixed chunk of memory for other type (void)

Converting Data Type on Existing Arrays
The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
The astype() function creates a copy of the array, and allows us to specify the data type as a parameter.
The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or we can use the data type directly like float for float and int for integer.

The Difference Between Copy and View 
The main difference between a copy and a view of an array is that the copy is a new array, and the view is just a view of the original array.
Any changes made to the copy will not affect the original array, and any changes made to the original array will not affect the copy array. Any changes made to the view will affect the original array and vice-versa.

To check if array owns its Data or not
python has an attribute called base. The base attribute can be used identify if an array owns the Data or not. The copy does not own the data, so it returns none while the view owns the data, that is why it returns the original array.

Shape of an Array:
The shape of an array is the number of elements in each dimension. There is an attribute called shape that returns a tuple with each index having the number of corresponding elements. In the code file, (2,3) is shown which is a tuple which means that there are 2 dimensions each consisting of 3 elements. Integers at every index tells about the number of elements the corresponding dimension has. In the example above at index-4, so we can say that 5th(4+1th) dimension has 4 elements.

Reshaping an array:
Reshaping means to change the shape of an array. We can add or remove dimensions or change number of elements in each dimension.

NumPy Array Iteration
for loop is used for iteration. nditer() can be used for iteration

Iterating Array with Different Data Types:
op_dtypes argument can be used to change the datatype of elements while iterating. Numpy does not change the datatype of the element(where the element is in array) so it needs buffer and to enable it, we pass flags.
As shown in code file, we can define the step size and iterate through all the elements. ndenumerate() function will help to find the index to each element.

NumPy Joining Array
Joining means to combining two arrays together. concatenate() function along with the axis can be used to join the arrays. If axis is not defined, it explicitly takes 0. stack() method along with the axis can be used to join two arrays as shown in code file. hstack() method will join along rows while vstack() method will join along columns. dstack() method will join along height which is depth.

NumPy Splitting Array
Splitting is reverse to Joining. array_split() method is used for splitting arrays. It returns a values which is a list containing arrays. split() method will not adjust the elements but the array_split() method will adjust the elements to produce required array lists. splitted array can be accessed using index number as shown in code file. The array_split() method takes 2 or three parameters depending on the split character. If axis is to be mentioned, then the axis parameter can be passed. axis =1 is for row. An alternate solution in hsplit() which is opposite of hstack(). vsplit() and dsplit() are similar alternates to vstack() and dstack().

NumPy Searching Arrays
We can search an array for a certain value, and return the indexes that get a match.
To search an array, we shall use the where() method. 
The searchsorted() method is assumed to be used on sorted arrays. This method starts the search from the left and returns the first index where the number is no longer larger than the next value. Searching from the right side can be achieved by using parameter side = 'right' which will return the right most index. Here, the method starts the search from the right and returns the first index where the number is no longer less than the next value. To search for more than one value, an array with the specified value can be provided as a parameter as shown in code file. The return value is an array which would show where the values would be inserted in the original array to maintain the order.

NumPy Sorting Arrays
Sorting means putting elements in an ordered sequence. Ordered Sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending. The NumPy ndarray object has a function called sort(), that will sort a specified array. This method returns a copy of the array, leaving the original array unchanged. You can also sort arrays of strings, or any other data type.
