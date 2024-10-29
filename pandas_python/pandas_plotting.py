import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data1.csv')
df.plot()
plt.show()

df.plot(kind = 'scatter', x = 'Duration', y = 'Calories', label = 'Bibekster')
plt.legend()
plt.show()  # Here, the graph shows high correlation.

# Scatterplot where there are no relationship between the columns:
df.plot(kind = 'scatter', x = 'Duration', y = 'Maxpulse')
plt.show()   # shows very low correlation.

# Histogram
df["Duration"].plot(kind = 'hist')
plt.show()
