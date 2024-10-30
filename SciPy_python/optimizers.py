from scipy.optimize import root
from scipy.optimize import minimize
from math import cos
def eqn(x):
    return x + cos(x)
myroot = root(eqn, 0)
print(myroot.x)

# Printing all information about the solution
print(myroot)

print()
# Minimizing a Function
def eqn(x):
    return x**2 + x + 2
mymin = minimize(eqn, 0, method="BFGS")
print("minimum:", mymin.x)