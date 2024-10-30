Scipy 
It stands for Scientific python. It is a scientific computation library that uses NumPy. It provides more utility functions for optimization, statistics and signal processing. It is open source. It was created by Travis Olliphant.
SciPy has optimized and added functions that are frequently used in NumPy and Data Science. SciPy is written in python and some few segments in C. The github repository for SciPy is located at: https://github.com/scipy/scipy 


 Scipy Optimizers
 Optimizers are a set of procedures defined in scipy that either find the minimum value of a function, or the root of an equation. Essentially, all the algorithms in Machine Learning are nothing more than a complex equation that needs to be minimized with the help of given data.

 NumPy is capable of finding roots for polynomials and linear equations, but it can not find roots for non linear equations, like this one:
 x + cos(x)
 For this, we can use SciPy's optimize.root function. This function takes two required arguments:
 fun: a function representing an equation
 x0: an intial guess for the root.
 the function returns an object with information regarding the solution. The actual solution is given under attribute x of the returned object:

 Minimizing a Function
 A function, in this context, represents a cureve, curves have high points and low points. High points are called maxima. Low points are called minima. The highest point in the whole curve is called global maxima, whereas the rest of them are called local maxima. The lowest point in whole curve is called global minima, whereas the rest of them are called local minima.

Finding Minima
we can use scipy.optimize.minimize() function to mminimize the function. It takes two arguments:
fun: a function representing an equation
x0: an initail guess for the root.
method: name of the method to use. Legal values:
'CG', 'BFGS', 'Newton-CG', 'L-BFGS-B', 'TNC', 'COBYLA', 'SLSQP'
callback: function called after each iteration of optimization.
options: a dictionary defining extra params:
 {
    "disp": boolean - print detailed description
    "gtol": number - the tolerance of the error
     }

Sparse Data:
Sparse data is data that has mostly unused elements(that don't carry any information)
Sparse data is a data set where most of the item values are zero. Dense array is the opposite of a sparse array. Most of the values are not zero. In scientific computing, when we are dealling with partial derivatives in linear algebra we will come across sparse data.
scipy.sparse module provides functions to deal with sparse data. These are primarily two types of sparse matrices that we use:
Compressed Sparse Column. For efficient arithmetic, fast column slicing.
Compressed Sparse Row. For fast row slicing, faster matrix vector products.

SciPy Graphs
Graphs are an essential data structure. SciPy provides us with the module scipy.sparse.csgraph for working with such data structures.

Adjacency Matrix:
It is a nxn matrix where n is the number of elements in a graph. And the values represents the connection between the elements.   A 1 B: A 2 C
A and B are connected with weight 1. 
A and C are connected with weight 2.
C and B are not connected.

the adjency matrix would be:
    A B C
 A:[0 1 2]
 B:[1 0 0]
 C:[2 0 0] 

 Connected_components() will be used.

 Dijkstra:
 this method is used to find the shortest path in a graph from one element to another. It takes following arguments:
 return_predecessors: Boolean(True to return whole path of traversal otherwise False)
 indices: index of the element to return all paths from that element only.
 limit: max weight of path.

 Bellman Ford
 the bellman_ford() method will find the shortest path between all paris of elements including the negative weights.

 Depth First Order
 the depth_first_order() method returns a depth first traversal from a node. This function takes following arguments.
 the graph
 the starting element to traverse graph from

 Breadth First Order
 breadth_first_order() method returns a breadth first traversal from a node