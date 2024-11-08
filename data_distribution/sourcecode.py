# Random Data Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

# Generating a 1D array containing 100 values, where each value has to be 3,5,7 or 9
x = random.choice([3,5,7,9], p = [0.1, 0.3, 0.6, 0.0], size = (100))  # Here, the sum of all probabilites = 1
print(x)

x = random.choice([3,5,7,9], p = [0.1, 0.3, 0.6, 0.0], size = (3,5))
print(x)




