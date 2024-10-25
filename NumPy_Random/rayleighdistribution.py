# Rayleigh Distribution

import matplotlib.pyplot as plt
import seaborn as sbn
from numpy import random

x = random.rayleigh(scale=2, size=(2,3))
print(x)

# Visualization of the rayleigh Distribution
sbn.distplot(random.rayleigh(scale = 2, size = (2,3)), hist = False, label='Rayleigh distribution')
plt.legend()
plt.show()