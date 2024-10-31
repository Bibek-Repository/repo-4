# Exporting Data in Matlab format
from scipy import io
import numpy as np
arr = np.arange(10)
io.savemat('arr.mat', {"vec": arr})  # arr.mat is filename that is saved in the computer.

# Importing data from Matlab Format
mydata = io.loadmat('arr.mat')
print(mydata)
print(mydata['vec'])   # this will display only the array from the matlab data.

# the imported data is in 2D, we can change it to 1D
mydata = io.loadmat('arr.mat', squeeze_me=True)
print(mydata['vec'])

