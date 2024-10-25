# Uniform Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

x = random.uniform(size=(2,3))
print(x)

# Visualization

sbn.distplot(random.uniform(size=(2,3)))  # Default low and high parameter of 0.0 and 1.0
plt.show()

