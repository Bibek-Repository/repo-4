# Cleaning Data using Pandas

import pandas as pd

# loading csv file into the DataForm
df = pd.read_csv('rawdata.csv')
print(df.to_string())

# The data set contains wrong format("date") in row 26
# The data set contains wrong data ("Duration in row 7")
# The data set contains duplicates in row 11 and row 12

# Remove rows
df = pd.read_csv('rawdata.csv')
new_df = df.dropna()
print(new_df.to_string())

# Removing rows in the original dataframe
df = pd.read_csv('rawdata.csv')
df.dropna(inplace = True)
print(df.to_string())

# Replacing Empty Values
df = pd.read_csv('rawdata.csv')
df.fillna(130, inplace = True)

# Replacing only for specified columns
df = pd.read_csv('rawdata.csv')
df["Calories"].fillna(130,inplace = True)

# Replacing using Mean, Median or Mode

df = pd.read_csv('rawdata.csv')
x = df['Calories'].mean()
df["Calories"].fillna(x, inplace = True)  # sum of all values divided by number of values

# Replacing using Median
df = pd.read_csv('rawdata.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True) # median = the value in the middle, after all values have been sorted ascending

# Replacing using mode
df = pd.read_csv('rawdata.csv')
x = df["Calories"].mode()[0]
df["Calories"].fillna(x, inplace = True)  # mode: the value that occurs most frequently

