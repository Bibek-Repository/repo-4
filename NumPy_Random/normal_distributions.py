from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

x = random.normal(size = (2,3))
print(x)

x = random.normal(size=(4))
print(x)

# Generating a random normal distribution of size 2x3 with mean = 1 and standard deviation = 2:
x = random.normal(loc = 1, scale = 2, size = (2,3))
print(x)

# Visualization of Normal Distribution
sbn.distplot(random.normal(size=1000), hist=False)
plt.show()