# Interpolation

from scipy.interpolate import interp1d
from scipy.interpolate import UnivariateSpline
from scipy.interpolate import Rbf
import numpy as np

xs = np.arange(10)
ys = 2*xs + 1
print(ys)

interp_func = interp1d(xs, ys)
arr1 = interp_func(np.arange(2.1, 3, 0.1))
print(arr1)

# Spline Interpolation
xs = np.arange(10)
ys = xs**2 + np.sin(xs)+1
interp_func = UnivariateSpline(xs, ys)
arr1 = interp_func(np.arange(2.1, 3, 0.1))
print(arr1)

# Radial Basis Function
xs = np.arange(10)
ys = xs**2 + np.sin(xs) + 1
interp_func = Rbf(xs, ys)
arr1 = interp_func(np.arange(2.1, 3, 0.1))
print(arr1)

