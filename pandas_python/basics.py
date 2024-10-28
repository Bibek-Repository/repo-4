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

# Creating Pandas dataframe:
data = {
    "country": ["Nepal", "USA", "Canada","India"],
    "code":[977, 1, 2, 3]
}

# loading data into DataFrame object:
df = pd.DataFrame(data)
print(df)

# Locating Row
print(df.loc[0])  # This is return a pandas Series
print(df.loc[1])

# a list of Indexes:
print(df.loc[[0,1]])

# Named Indexes
data = {
    "college": ["ismt", "goldengate", "kathford"],
    "date": [2023,2012,2014]
}
df = pd.DataFrame(data, index = ["study1", "study2", "study3"])
print(df)

# Locating Named Index
print(df.loc["study1"])

# To load files into a DataFrame
df = pd.read_csv('data.csv')
print(df)

# loading CSV into a dataframe
df = pd.read_csv("data.csv")
print(df.to_string())  # It will print the entire DataFrame

# To check the maximum rows using pandas
print(pd.options.display.max_rows)   # It shows 60 which is the maximum number of rows

# Setting maximum number of rows to display the Dataframe:
pd.options.display.max_rows = 1000
print(pd.options.display.max_rows)
df = pd.read_csv('data.csv')
print(df)

# To load JSON file into a DataFrame:
df = pd.read_json('sample3.json')  # sample3.json is a sample json file from the internet 
print(df.to_string)

# Dictionary as JSON
dict = {
    "Motorcycle":{
        "0":"harley",
        "1":"royal",
        "2":"triumph"
    },
    "engine":{
        "0":"l23",
        "1":"m23",
        "2":"a13"
    }
}
df = pd.DataFrame(dict)
print(df)

# Analyzing DataFrames
df = pd.read_json('sample3.json')
print(df.head(10))   # We can do this in the csv file too

# printing the first 5 rows
print(df.head())

# print the last rows
print(df.tail(10))   # This will print the last 10 rows
print(df.tail())     # This will print the last 5 rows by defaault

# Info about the Data
print(df.info())   # the information such as 35 entries, are given

