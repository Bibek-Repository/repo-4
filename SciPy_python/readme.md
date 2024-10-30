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
