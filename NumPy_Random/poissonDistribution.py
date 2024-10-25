# Poisson Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

x = random.poisson(lam=2, size=10)
print(x)

# Visualization of Poisson Distribution
sbn.distplot(random.poisson(lam = 2, size = 1000), label='Bibek Distribution of eating')
plt.legend()
plt.show()

# Demonstrating that Normal and poisson distribution are similar for large data points:

sbn.distplot(random.normal(loc=50, scale=7,size=1000,),hist=False,label='normal distribution')
sbn.distplot(random.poisson(lam=50, size=1000, ),hist=False,label='poisson distribution')
plt.legend()
plt.show()
