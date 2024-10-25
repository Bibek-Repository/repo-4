# Binomial distributions 

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

x = random.binomial(n=10, p=0.5, size=10)
print(x)

# Visualization of Binomial Distribution
sbn.distplot(random.binomial(n=10, p=0.5, size = 1000), hist=True, kde=False)
plt.show()

# Demonstrating that both the Normal and Binomial Distribution are same when data points are large

sbn.distplot(random.normal(loc=50, scale=5, size =1000), hist= False, label = 'Normal')
sbn.distplot(random.binomial(n=100, p=0.5, size=1000), hist=False, label='Binomial')
plt.legend() # This is for showing the label in the plot
plt.show()


