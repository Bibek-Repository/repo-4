# Importing a python module 

import python_modules

python_modules.movie("the imitation game")
print(python_modules.student["name"])

# Creating an alias for the the import module using as keyword

import python_modules as ry

ry.movie("the shawshank redemption")

# Some of the builtin modules in python

import platform

x= platform.system()
print(x)

# Some Built in cmath function in python

import cmath
import math

z=4+3j
print(type(z))
print(z)
print(z.real)
print(z.imag)

#returning a value in polar format

x=cmath.polar(z)
print(x)

#This can be done in other way too

p=abs(z)
q=cmath.phase(z)
print(p,q)


# To convert the phase from radians to degree

phi_degrees=math.degrees(q)
print(phi_degrees)

print(x)
print(type(x))

# To convert the polar value to the rectangular values:

print(cmath.rect(x[0],x[1]))









