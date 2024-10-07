# cmath module in python

# Power and Logarithmic Functions

import cmath
import math

x=7
y=cmath.exp(x)      # Returns e raised to the power of x
print(y)

base=4
z=cmath.log(x,base)  # Returns the complex number to z
print(z)


print(cmath.log10(x))    # returns the 10 base logarithm value of x
print(cmath.sqrt(4).real)     # returns the square root of 4 here the real is used to get the real value of the complex number returned by the cmath module

# trigonometric Functions 

print(cmath.asin(x))       # cosine and tangent functions have similar syntax
print(cmath.sin(x))

# Classification Functions

z=4.0+2.0j
b=cmath.isfinite(z)    # returns true or false
print(f"the complex {z} is finite: {b}")

b=cmath.isinf(z)       # returns true or false
print(f"the complex {z} is infinite: {b}")

c=cmath.isclose(3,3.15, rel_tol=0.05,abs_tol=0.0)    # here the numbers 3 and 3.15 are closer to eachother within  
print()                                               # the tolorence of 0.05. 
print(c)

z=float('inf')+3j
print(z)
d=cmath.isnan(z)
print(d)

# Constants in python

pie=cmath.pi                       # value of pi
exp=cmath.e                         # value of exponential
tauvalue=cmath.tau                  # value of tau constant
infinity=cmath.inf                  # value of infinity which returns float('inf')
imaginaryinfinity=cmath.infj        # value of complex number which returns complex(0.0,'float('inf')')
nan1=cmath.nan                      # value of not a number
nan2=cmath.nanj                     # value of not a number in complex form

print()
print(pie)
print(exp)
print(tauvalue)
print(infinity)
print(imaginaryinfinity)
print(nan1)
print(nan2)



