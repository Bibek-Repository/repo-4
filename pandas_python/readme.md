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

Cleaning the Data of Wrong Format
In the rawdata.csv file two datas in the Date column, should be of string type. But they are not. To fix it, either we can remove the row or we can convert all cells in the columns into the same format. to_datetime() will convert the data into date in string format.

Removing Rows:
NaT value can be fixed by deleting entire row. dropna() method will be used to do this as shown in code file.

Wrong Data:
It is difficult to identify wrong values. It can be replaced by using loc. for big data sets, we can set some boundaries and replace the values that are outside of the boundaries.

Duplicates:
The duplicated() method returns a boolean value for each row. The duplicated() method will help to discover duplicates. To remove the duplicates, the drop_duplicates() method is used. inplace = true parameter will make sure that method does NOT return a new DataFrame, but it will remove all duplicates from the original DataFrame.

Data Correlations:
corr() method calculates the relationship between each column in data set. correlations ranges from -1 to 1. -1 and 1 are good correlation while if it is close to 0 it means that it has bad correlation. -1 correlation means that the increment in one will give decrement in other while 1 correlation means that the increment in one will give increment in other too.

Pandas-Plotting
plot() method is used to create diagrams. pyplot submodule of the matplotlib library can be used to visualize the diagramm on the screen.

Scatter Plot
kind argument is used to make a scatter plot. kind = 'scatter'. A scatter plot needs and x-axis and y-axis.

Histogram:
We use kind argument to specify a histogram. A histogram needs only one column. A histograms shows the frequency of each interval, eg. how may workouts lasted between 50 and 60 minutes.

Spatial Data:
spatial data refers to data that is represented in a geometric space. Example points on a coordinate system. We deal with spatial data problems on many tasks. Eg finding if a point is inside a boundary or not. Scipy provides us with the module scipy.spatial, which has functions for working with spatial data. 

Triangulation:
A triangulation of a polygon is to divide the polygon into multiple triangles with which we can compute an area of the polygon. A Triangulation with points means creating surface composed triangles in which all of the given points are on at least one vertex of any triangle in the surface. One method to generate these triangulations through points is the Delaunay() Triangulation.

Convex hull:
A convex hull is the smallest polygon that covers all the given points. convexhull() method is used to create a convex hull.

KDTrees
KDTrees are a datastructure optimized for nearest neighbor queries. Example, in a set of points using KDTrees we can efficiently ask which points are nearest to a certain given point. The KDTree() method returns a KDTree object. The query() method returns the distance to the nearest neighbor and the location of the neighbors.

Distance Matrix
There are many Distance Metrics used to find various types of distances between two points in data science, Euclidean distance, cosine distance etc. The distance between two vectors may not only be the length of straight line between them, it can also be the angle between them from origin, or number of unit steps required. machine learning algorithm like K Nearest Neighbors or K means etc depend on the Distance Matrix. Cityblock Distance (Manhattan Distance) is the distance computed using 4 degrees of movement. We can move up, down, right, left not diagonally. Cosine Distance is the cosine angle between the two points.
