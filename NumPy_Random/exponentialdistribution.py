# Exponential Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

x = random.exponential(scale = 2, size= (2,3))
print(x)

# Visualization of Exponential Distribution
sbn.distplot(random.exponential(size=1000),hist = False)
plt.show()

# Relation between Exponential and Poisson Distribution
sbn.distplot(random.exponential(size=1000),hist = False, label='Exponential Distribution')
sbn.distplot(random.poisson(size=1000), hist = False, label='Poisson Distribution')
plt.legend()
plt.show()
