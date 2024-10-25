import matplotlib.pyplot as plt
import seaborn as sns   # Here, seaborn is a library

# Plotting a Distplot

sns.displot([0,1,2,3,4,5])
plt.show()

sns.distplot([0,1,2,3,4,5])  # distplot() is depreciated in this version of python.
plt.show()

# Plotting a Distplot without Histogram
sns.distplot([0,1,2,3,4,5], hist = False)  # Histogram is the one in the blue rectangle 
plt.show()