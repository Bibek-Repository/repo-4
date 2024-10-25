# Logistic Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

x = random.logistic(loc=1, scale=2, size=(2,3))
print(x)

# Visualization
sbn.distplot(random.logistic(size=1000), hist = False)
plt.show()

# Difference between normal and logistic Distribution
sbn.distplot(random.logistic( size = 1000), hist = False, label = 'Bibek logistic')
sbn.distplot(random.normal(scale=2, size = 1000), hist = False, label='Bibek normal')
plt.legend()
plt.show()

