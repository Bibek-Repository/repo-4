# Correlation 

import pandas as pd

df = pd.read_csv('rawdata.csv')
print(df)
# df.corr()  # This won't work as there are non-numeric value in the table.

