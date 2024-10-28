NumPy unfuncs

ufuncs stands for "Universal Function". They are NumPy functions that operate on the ndarray object.
ufuncs are used to implement vectorization in Numpy which is way faster than iterating over elements. They also provide broadcasting and additional methods like reduce,accumulate etc. that are very helpful for computation. ufuncs also take additional arguments, like:
where boolean array or condition defining where the operations should take place. dtype defining the return type of elements. out output array where the return value should be copied. 
Vectorization is the process of converting iterative statements into vector based operation. It is faster as modern CPUs are optimized for such operations.

Add the Elements of two Lists. One way of doing it is to iterate over both of the lists and then sum each elements. add(x,y) function will add two lists. This is ufunc.

To create our own ufunc, we have to define a function, like we do with normal functions in Python, then we add it to our numpy unfunc library with the frompyfunc() method.
The frompyfunc() method takes the following arguments: 
function- the name of the function
inputs- the number of input arguments(arrays).
outputs- the number of output arrays.

Simple Arithmetic 
Arithmetic operators + - * / can be used directly between NumPy arrays. But any array like objects like lists, tuples etc. can be used for arithmetic operations conditionally. Arithmetic Conditionally means that we can define conditions where the arithmetic operations should happen. where parameter is used to specify the condition. Add() function sums the content of two arrays and return the results in a new array. Both mod() and remainder() function will return the remainder.

Rounding Decimals:
truncation, fix, rounding, floor, ceil are the functions to round off decimals. trunc() and fix() functions will return the float number closest to zero. around() function increments preceding digit or decimal by 1 if greater than or equal to 5 else does nothing. floor() method rounds off decimal to nearest lower integer while the ceil() method rounds off decimal to nearest upper integer. 

Logs:
numpy provides functions to perform log at the base 2, e, 10. To take log of any base ufunc can be used. inf or -inf will be returned if the log can not be computed.

LCM and GCD
lcm() and reduce() method can be used to do this operation as shown in code file. gcd() and reduce() method can be used to find the HCF.

Trigonometric functions
sin(), cos(), tan() can be used. They take value in radians and return the value in radians. hypot() is used for calculating hypotanuos and deg2rad() and rad2deg() method is used for radian to degree conversion and vice versa. sin() and arcsin() method is for finding the sine and angles correspondingly. Similar is for cosine and tangent. Similaryly, sinh() cosh() and tanh() are used for the hyperbolic functions. the angles can be found by using arcsinh(), arcosh() and arctanh().

Set in numpy
unique() method is used to find unique elements from an array. Set arrays are 1-D arrays.union() is used for one array union. Union between two arrays can be achieved by using union1d() function. intersect1d() for finding the intersection. the assume_unique parameter will speed up computation if set to True. setdiff1d() method is used for finding the difference of two array.






