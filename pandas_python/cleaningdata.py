# Cleaning Data using Pandas

import pandas as pd

# loading csv file into the DataForm
df = pd.read_csv('rawdata.csv')
print(df.to_string())
df.columns = df.columns.str.strip()  # This will remove the whitespace

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
df['Calories'].fillna(130,inplace = True)

# Replacing using Mean, Median or Mode

df = pd.read_csv('rawdata.csv')
x = df['Calories'].mean()
df['Calories'].fillna(x, inplace = True)  # sum of all values divided by number of values

# Replacing using Median
df = pd.read_csv('rawdata.csv')
x = df["Calories"].median()
df["Calories"].fillna(x, inplace = True) # median = the value in the middle, after all values have been sorted ascending

# Replacing using mode
df = pd.read_csv('rawdata.csv')
x = df['Calories'].mode()[0]
df['Calories'].fillna(x, inplace = True)  # mode: the value that occurs most frequently

# Converting all the cells in the column: date
df = pd.read_csv('rawdata.csv')
df['Date'] = pd.to_datetime(df['Date'])
print(df.to_string())   # This will convert the cell having dates into string.

# Converting the cells containing Not a Time value
df.dropna(subset=['Date'], inplace = True)

# Replacing a value in cell using loc
df.loc[7, 'Duration'] = 45
# for big data sets:
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.loc[x, "Duration"]=120
print(df.to_string)

# Removing Rows
for x in df.index:
    if df.loc[x, "Duration"] > 120:
        df.drop(x, inplace = True)
print(df.to_string)

# Removing Duplicates
print(df.duplicated())

# Removing all duplicates
df.drop_duplicates(inplace= True)

