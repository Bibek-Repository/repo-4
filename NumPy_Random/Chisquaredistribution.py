# Chi Square Distribution

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sbn

x = random.chisquare(df=2, size = (2,3))
print(x)

# Visualization of Chi Square
sbn.distplot(random.chisquare(df = 1, size =1000), hist = False)
plt.show()

