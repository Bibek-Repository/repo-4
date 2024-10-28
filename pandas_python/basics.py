# loading a csv file into pandas dataframe:

import pandas as pd
df = pd.read_csv('data.csv')
print(df.to_string())

mydataset = {
    'motorcycle': ["Harleydavidson", "triump", "royalenfield"],
    'purchase':[3,7,2]
}
myvar = pd.DataFrame(mydataset)
print(myvar)

# Checking the version of pandas
print(pd.__version__)

# Creating simple Pandas Series from a list:
a = [1,6,3]
myvar = pd.Series(a)
print(myvar)

# Labels
print(myvar[0])  # It prints the value in index 0

# Creating Labels
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

# Accessing the item by the label
print(myvar["y"])

# Key/Value Objects as Series
motorcycle = {
    "day1": "100kms",
    "day2": "200kms",
    "day3": "300kms"
}
myvar = pd.Series(motorcycle, index = ["day1", "day2"])
print(myvar)

# Creating a DataFrame from two series:
data = {
    "person":["Bibek", "Ram", "shyam"],
    "age":[28,25,32]
    }
myvar = pd.DataFrame(data)
print(myvar)