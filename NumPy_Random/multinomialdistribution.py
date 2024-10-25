# Multinomial Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

# rolling dice multinomial distributions
x = random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6])
print(x)

# Generating the plot
sbn.distplot(random.multinomial(n=6, pvals=[1/6,1/6,1/6,1/6,1/6,1/6]), hist=False, label='multinomial')
plt.legend()
plt.show()

# Difference between multinomial and normal distribution
sbn.distplot(random.normal(loc=50, scale=5, size=1000), hist = False, label='Normal Distribution')
sbn.distplot(random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6]), hist = False, label='Multinomial Distribution')
plt.legend()
plt.show()


