# Pareto Distributions

import matplotlib.pyplot as plt
import seaborn as sbn
from numpy import random

x = random.pareto(a = 2, size =(2,3))
print(x)

# Visualization of Pareto Distribution
sbn.distplot(random.pareto(a=2, size=1000), hist= False, label='Pareto distribution', kde = False) # kde won't show the actual graph
plt.legend()
plt.show()
