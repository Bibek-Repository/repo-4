# Random Permutations

import numpy as np
from numpy import random

# Shuffling Arrays
arr = np.array([1,2,3,4,5])
random.shuffle(arr)
print(arr)

# Permutation
arr = np.array([1,2,3,4,5])
arr1 = random.permutation(arr)
print(arr1)
