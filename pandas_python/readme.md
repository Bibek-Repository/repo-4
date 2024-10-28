pandas
It is a python library. It is used to analyze data. .csv stands for comma separated values. It is a plain text file that stores tabular data in a simple format. Each line of the file represents a row, and each field within a row is separated by a comma. pandas references to panel data and python data analysis. It was created by Wes McKinney in 2008. Pandas analyze big data and make conclusions based on statistical theories. Pandas clean messy data sets, and make them readable and relevant. Relevant data is very important in data science. Data science is a branch of computer science where we study how to store, use and analyze data for deriving information from it. Pandas can do:
correlation between two or more columns
average value
max value
min value
Pandas are also used to delete rows that are not relevant, or contains wrong values, like emplty or NUll values. This is called cleaning the data. The source code for pandas: https://github.com/pandas-dev/pandas. Pip install pandas for installing pandas library. A pandas series is like a column in a table. It is 1D array holding data of any type. If nothing is specified, the values are labeled with the index number. We can also use a key/value object, like a dictionary, when creating a Series. The keys of the dictionary become the labels. To select only some of the items in the dictionary, index argument can be used which will specify only the items we want to include in the Series.

dataframes:
Data sets in pandas are usually multi-dimensional tables, called DataFrames. Series is like a column, a DataFrame is the whole table. DataFrames are 2D data structure, or a table with rows and columns. loc[] attribute can be used to return one or more rows. index argument will be used to print the specified index data. loc attribute can be used to retrun the specified row in the named index. To load data sets in dataframe from a csv file, we can use read_csv() method.

Pandas to read csv file
read_csv() method is used to read the csv file and load in to a dataframe. to_string() method will print the entire DataFrame. If the Dataframe is large, pandas will only return the first 5 rows and the last 5 rows. max_rows can be used to check the system's maximum rows. To change the maximum number of rows to display the entire DataFrame, max_rows can be used as shown in code file basics.py.

JSON
Big data sets are stored as JSON. JSON is a plain text, but has the format of an object. read_json() is used to load json into a dataframe. As in csv, to_string() is used to print the entire DataFrame. JSON objects have the same format as python dictionaries. Python dictionary can be loaded in a dataframe directly.

Analyzing the DataFrames:
head() method can be used to get a quick overview of the DataFrame. The head() method returns the headers and a specified number of rows, starting from the top. info() method will display all the information about the dataset. the info() method tells the non null values. based on this, we can know the null values. Null values can be bad when analyzing data. This is what is known as cleaning data.

Data Cleaning:
Data cleaning is the process of fixing bad data in our data set. Bad data can be:
empty cells (Null datasets)
data in wrong format
wrong data
duplicates

Remove Rows:
the rows containing empty cells can be removed using a function called dropna(). dropna() returns new dataframe and will not change the original. original dataframe can be changed by using inplace = True argument.

Replacing Using Mean, Median, Mode
To replace empty cels, mean mode or median value of the column can be used. Pandas uses mean(), median(), mode() methods to calculate the respective values for a specified column.