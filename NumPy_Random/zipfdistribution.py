# Zipf Distribution

import matplotlib.pyplot as plt
import seaborn as sbn
from numpy import random

x = random.zipf(a =2, size=(2,3))
print(x)

# Visualization of Zipf Distribution
x = random.zipf(a=2, size= 1000)
sbn.distplot(x[x<10], kde = False, label= 'Zipf Distribution')
plt.legend()
plt.show()