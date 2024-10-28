NumPy unfuncs

ufuncs stands for "Universal Function". They are NumPy functions that operate on the ndarray object.
ufuncs are used to implement vectorization in Numpy which is way faster than iterating over elements. They also provide broadcasting and additional methods like reduce,accumulate etc. that are very helpful for computation. ufuncs also take additional arguments, like:
where boolean array or condition defining where the operations should take place. dtype defining the return type of elements. out output array where the return value should be copied. 
Vectorization is the process of converting iterative statements into vector based operation. It is faster as modern CPUs are optimized for such operations.

Add the Elements of two Lists. One way of doing it is to iterate over both of the lists and then sum each elements. add(x,y) function will add two lists. This is ufunc.