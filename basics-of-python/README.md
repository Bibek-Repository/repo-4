# repo-4

10/1/2024

Tuples in python. 

Tuples are ordered, unchangeable arrays in python. Tuples allow duplication of values. The values are inserted inside round brackets (parenthesis). length of the tuple can be accessed using len() method. Tuples are indexed so the values or items in tuples can be accessed using the index value starting from 0: sampletuple[index]. Tuples can have one value. It is defined simmilar to multi value tuples but comma is needed at the end of the value. The type of the tuple can be displayed using type() method. Negative index are allowed in tuples as illustrated in the code file tuples.py. : is used to display range of items. The first index is included while the last one is excluded. An empty value before : denotes the first value of the tuple while the empty value after : refers to the ending value of the tuple. To check the presence of particular value in tuple, we can use if and in keywords. To update the tuple, we have to change the tuple to list and update it and later convert it to tuple again. We can add two tuples together using + operator. Deleting can be done by using del keyword. Unpacking a tuple can be done using variables in parenthesis and * can be used for multi value assignment. looping in tuple is similar to lists. For and while loops can be used. In for loop indexing can be done to access the values of tuples as shown in code. Muliplying a tuple with a number will append the tuple to itself for the times being multiplied. Two methods count() and index() can be used to count the number of the particular value and the index of the particular value(first one). 

Sets in Python

A set is a collection which is unordered, unchangeable*, and unindexed
written with Curly braces
do not allow duplication of values
The values False and 0, True and 1 are considered same in set. Thus they cannot be used simultaneously in the same set.
len method is used to find the length of the set
A set can be used to store different values of different data types: string, int and boolean for example can all be in the same set
sets are defined as objects with the data type 'set'
set constructor can be used to construct a set. Two round brackets are used and set keyword is used
We cannot change the set items, but items/values can be added
Two sets can be added together using update() method
Value can be added to a set using add() method
remove operation can be done using remove() or discard() method
pop() method randomly removes a value from the set and returns the removed value
clear() method clears the set
The union() and update() methods joins all items from both sets.
The intersection() method keeps ONLY the duplicates.
The difference() method keeps the items from the first set that are not in the other set(s).
The symmetric_difference() method keeps all items EXCEPT the duplicates.
del keyword is used for completely deleting the set
update() method doesn't return a value but rather joins two sets
Both union() and update() will exclude any duplicate items.

The intersection_update() method will also keep ONLY the duplicates, but it will change the original set instead of returning a new set.
the difference_update() method will not return the value but update the set to the difference of two sets
symmetric_difference_update() method will remove the intersection values, updates the set with the other values from both sets.

&= is intersection_update
isdisjoint() method checks if the two sets have intersection or not
issubset() method checks if one set contains other set
issuperset() returns whether this set contains another set or not

Dictionary

Dictionary are used to store data values in key(pairs)
They are ordered, changeable and do not allow duplicates
If the key values are repeated then the following key value will override the previous key value
len() method is used to display the total number of key pair
The values in dictionary can have any data types including lists, tuples as shown in the code file: dictionaries.py
The data type of dictionary in python is class "dict"
The dict() constructor can be used to create dictionary
Accessing items can be done via key names or get method
keys() method displays all the keys in the dictionary
values() method will display all the values in the dictionary
items() method will display all the key value pair in the dictionary
if statement can be used to check if a key is present in the dictionary
update({"key":"value"}) can be used to update a dictionary
pop() and popitems() method are used to remove the key value pair
adding a new pair can be done as shown in the code
del key word can be used to delete a key value pair or the dictionary itself
clear() method is used to completely clear the dictionary
copy() method and dict() method can be called to copy a dictionary to another new

python IF else statement

if else statement can be used to check the condition of a statement as shown in code
if else statement involves indentation
if...elif...else statement can be used for multiple conditions
if elif and else falls in the same line while the methods and functions comes with indentation


Python while loop

Else can be used right after while condition is completed or not met
break statement will move the execution out of loop
continue statement will skip the code and continue to the loop

Python For loop

for loops are generally used with python arrays: lists, tuples, sets, dictionaries
for loop can also be used to loop through a string
break statement is used to break out of the loop statement, else statement is not executed
continue statement immediately skips the code after it but then continue back to the loop
range() method has single parameter, double parameter or triple parameter:
        single parameter: it defines 0 to the end(excluded)
        double parameter: it defines start and the end(excluded)
        triple parameter: it defines start, end and the gap
pass keyword can be used to perform no activity in a loop


Functions in python

Functions are called
Upon the calling, they return some value
They take parameters as the input which they later work on
Arguments are the parameters. Any number of Arguments can be passed to the Function
While defining the function, we take parameters inside the parenthesis while we pass arguments from the calling function
if we don't know the number of arguments to pass to a function, then we can use tuples or dictionaries, that can take any number of values. In dictionaries **kwargs are used while *parameter is used for tuple.
In dictionary we use both key and value as arguments while in tuples we only use values as shown in code
Default parameter values can be added in the parameter of the function defining. This parameter value is used when no argument are passed as demonstrated in code
We can also pass a list or dictionary as an argument and access the values or keys respectively
Value can be returned in python using return keyword
Upon calling the function, it returns the value
If there is no content for the function, then pass keyword can be used to prevent error.
In python there are two parameters broadly: one is the positional argument and the other is keyword argument
when defining a parameter, if we use ,/ then keyword arguments are not allowed. keyword arguments are can be placed without order but positional arguments are to be placed in order.
Any argument before the / , are positional-only, and any argument after the *, are keyword-only.
In the code section, we have used the tri_recursion function. The function calls itself with the parameter reduced by 1, and returns the value. At first the else statement is executed which returns 0 to the result and the result value is used to return the value of the last recursion which also displays the result by print method.



lambda functions in python

lambda functions are small anonymous functions in python
lambda arguments : expression #syntax of lambda function
arguments are passed via a variable as shown in code section

classes or objects in python

Python is an object oriented Programming language
object of the class can be created and the property of the class can be accessed using the object
the __init__() function is the built in function that takes the parameter self and other user defined parameters
this function is always executed when the class is initiated. like in code section, the p1 object is defined which initiates the class 
the __str__() function is used to provide return values
The self parameter can have any name but should be always at the start and it refers to the properties of the element
modifying any value of the property in class can be done as shown in code
delete any property can be done via del keyword
we can also delete whole object of the class using del keyword
pass keyword can be used in empty classes to prevent any error

Python Inheritance

Inheritance allows us to define a class that inherits all the methods and properties of another class
parent class is the class where the child class inherits from
parent class is also known as base class
child class is also known as derived class
In the code, class Student is the derived class and class Person is the base class
I accessed the Person class method called func_1() using the object of the Student class
the student class has the parameter of the class Person to denote parent child relationship between the two
During the inheritance,the child class can also have __init__() method to initialize the child class just like in class child in the code section. This will override the __init__() class in the Parent class. To prevent this from happening, the __init__() method from the parent class is called in the __init__() function of the child class with the same parameters.
the super() method will allow the child class to call __init__() function from the parent class automatically
we can add properties and method to the child class as shown in the code section

iterators in python

Iterators are the objects in python that will iterate over values of the iterables in python. Iterables could be any list, dictionary, tuple and sets
As shown in code, iterables can be used to iterate the values in class using loop. __iter__() and __next__() methods can be used. In the code section, first we define a object of a class. The object is used to call the __iter__() method and the __next__() method is used to increment the value which is printed using print() method.

polymorphism in python

It refers to the methods/functions/operators that can operate on many objects or classes.
Function polymorphism: the function can be used for many objects. Such as len() function can be used for strings, tuples, dictionary, tuples etc
class polymorphism: different class with same method name can be called. For example in the code section, move() method is called by the objects of each class
Class Polymorphism: In class polymorphism, the methods of same name are in parent class as well as child class. In the code section, the method move() is available in both parent class: vehicle and child class: motorcycle and car. When we call the move() method from the object of the motorcycle class, the move() method is called from the class motorcycle. But when the move() method is called using the object of the car class which has pass statement, move() method from the parent class Vehicle is invoked.

scope in python

There are two scope of variable in python. The global scope of a variable denotes that the variable retains its value inside and outside of any method. The local scope of a variable denotes that the variable retains its value only inside the method. If a variable is declared global inside a method as illustrated in code file: Scope.py, the variable retains the value outside the scope of the local method
The keyword: nonlocal can be used to make the variable retain its value outside the method within another method as shown in code file: scope.py

Modules in Python:

It refers to the library of code in python. It contains functions which can be used.
In the file, python_modules.py, movie() method is defined. movie() is called in another file: import.py
In import.py, import python_modules.py has been used to import the module.
as keyword can be used to rename a module which can be easier to code
some of the build in modules are cmath, math, etc. 
A complex number can be represented in two forms: polar form and rectangular form. They can be interchanged using polar() method and rect() method in the cmath module.
to convert the value from radian to degree, degree() method can be used. This method is in math module of the python
The variable as a type of complex if the value stored is complex
The polar Variable are stored as tuple containing the magnitude and phase
Power and Logarithmic Functions: cmath.exp(), for returning the the exponential raised to certain power
cmath.log(x,base): returns the log of x to the base
cmath.log(x): returns the log of x to the natural base e
cmath.log10(x): returns the base 10 log of the variable x
cmath.sqrt(x): It returns the square root of the variable x 
cmath module will return a complex number
Trigonometric Functions: cmath.asin(x): returns the arc of sin that is inverse of sine of a variable x
cmath.sin(x): returns the sine of a variable x
similarly, cosine and tangent function as similar syntax
Classification Function: isfinite() returns a true or false if the value in infinite in both real and imaginary part
isinf() returns true or false if the value in real and imaginary part is infinite
isclose() method returns the closeness of two variables within some tolerance which can be defined as shown in code
isnan() returns true if the value is not a number else false
cmath.pi It returns the value of Pi                       
cmath.e  It returns the value of exponential
cmath.tau It returns the value of tau contant                 
math.inf  It returns the infinite value which is float('inf')                
cmath.infj It return the infinite imaginary value in complex form        
cmath.nan It returns the not a number value                     
cmath.nanj  It returns the not a number value in complex imaginary form.

Dates and Time in Python

datetime module can be imported.
now() method calls the date and time of the system right now
.year .month .hour etc can be used to extract specific date time formats
datetime() constructor can be called to construct a new date time. arguments are sperated by the comma
strftime() method can be called for the format of the date and time as shown in code file: dates.py

Maths in Python

There are some built in functions in python that helps us perform the mathematical operations:
These include: 
max(): returns the maximum value in the tuple
min(): returns the minimum value
abs(): returns the absolute value(the value with no sign)
pow(): returns the value raised to certain power
Also, there is a module called math module in python. The module can be imported to call different functions in python related to maths.
import math
sqrt(): This function returns the square root of a value
ceil(): This function returns the upper integer value
floor(): This function returns the lower integer value
pi(): This function returns the value of pi 

Python JSON

JSON is a syntax for storing and exchanging data
JSON is a text written with Javascript Object Notation

Python RegEx

A RegEx, or Regular Expression, is a sequence of characters that forms a search pattern. RegEx can be used to check if a string contains the specified search pattern.

RegEx Module
Python has a built-in package called re, which can be used to work with Regular Expressions.

RegEx in Python
When you have imported the re module, you can start using regular expressions:

RegEx Functions
The re module offers a set of functions that allows us to search a string for a match:

findall: Returns a list containing all matches
search: Returns a Match object if there is a match anywhere in the string
split: Returns a list where the string has been split at each match
sub: Replaces one or may matches with a string

Metacharacters 
They are characters with special meaning:
[] A set of characters. Example: "[a-m]"
\ signals a special sequence (can also be used to escape special characters). Example: "\d"
. Any character (except newline character) "he..o"
^ Starts with Example: "^hello"
$ Ends with Example: "planet$"
* Zero or more occurences Example:"he.*o"
+ One or more occurences Example:"he.+o"
? Zero or one occurences Example: "he.?o"
{} Exactly the specified number of occurences Example:"he.{2}o"
| Either or Example: "falls|stays"
() Capture and group

Special Sequences
A special sequence is a \ followed by one of the characters in the list below, and has a special meaning:

\A : Returns a match if the specified characters are at the beginning of the string Example: "\AThe"
\b : Returns a match where the specified characters are at the beginning or at the end of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string") Example: r"\bain" r"ain\b"
\B : Returns a match where the specified characters are present, but NOT at the beginning (or at the end ) of a word (the "r" in the beginning is making sure that the string is being treated as a "raw string") r"\Bain" r"ain\B"
\d : Returns a match where the string contains digits (numbers from 0-9) "\d"
\D : Returns a match where the string DOES NOT contain digits Example : "\D"
\s : Returns a match where the string contains a white space character Example: "\s"
\S : Returns a match where the string DOES NOT contain a white space Example : "\S"
\w " Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9), and the underscore_character) Example: "\w"
\W : Returns a match where the string DOES NOT contain any word characters Example: "\W"
\Z : Returns a  match if the specified characters are at the end of the string Example : "Spain\Z"

Sets

A set is a set of characters inside a pair of square brackets [] with a special meaning:

[arn] Returns a match where one of the specified characters (a,r, or n) is present
[a-n] Returns a match for any lower case character, alphabetically between a and n
[^arn] Returns a match for any character EXCEPT a,r, and n
[0123] Returns a match where any of the specified digits(0,1,2, or 3) are present
[0-9] Returns a match for any digit between 0 and 9
[0-5][0-9] Returns a match for any two-digit numbers from 00 and 59
[a-zA-Z] returns a match for any character alphabetically bewteen a and z, lower case OR upper case
[+] In sets, +, *, ., |, (), $, {} has no special meaning, so [+] means: return a match for any + character in the string

The findall() Function
The findall() function returns a list containing all matches.

The list contains the matches in the order they are found.
If no matches are found, an empty list is returned.

The search() Function
The search() function searches the string for a match, and returns a Match object if there is a match.
If there is more than one match, only the first occurrence of the match will be returned.

The split() Function
The split() function returns a list where the string has been split at each match.

We can control the number of occurrences by specifying the maxsplit parameter.

The sub() Function
The sub() function replaces the matches with the text of our choice.

We can control the number of replacements by specifying the count parameter.

Match Object
A Match Object is an object containing information about the search and the result.
If there is no match, the value None will be returned, instead of the Match Object.

The Match object has properties and methods used to retrieve information about the search, and the result:
.span() returns a tuple containing the start-, and end positions of the match.
.string returns the string passed into the function
.group() returns the part of the string where there was a match.

If there is no match, the value None will be returned, instead of the Match Object.

Python PIP

PIP
It is a package manager for Python packages, or modules.
A package contains all the files needed for a module.
Modules are python code libraries that can be included in a project.
To check if PIP is installed: pip --version
 https://pypi.org/project/pip/ link to download the PIP
To download a package : pip install <package_name>. In the code section, we have used camelcase package
more packages : https://pypi.org/
To remove a package : pip uninstall <package_name>
To list all the packages that are installed : pip list

Try and Except in Python

The try block will test a block of code for errors. If there is error except block is executed. But if there are no errors and try block is executed then else block is executed as shown in code section. The finally block will be executed regardless of the try except block.
Exception Handling
if the try block raises an error, the except block will be executed. There can be multiple exceptions as shown in code file. If the try block is executed, then, the exception is not raised and hence, else block will be executed. The finally block will be executed regardless of error or no error. To raise an exception raise keyword can be used. In the code section, if statement is filled with exception that is being raised. TypeError can be raised using the raise keyword.

Python User Input
input() method can be used to take input from the user. The string inside the input parameter is prompted in the display as shown in code file.

Python String Formatting

F-Strings
It allows to format the string to be printed. f is placed at the beginning of the string literal to format it. {}: are the placeholders. They contain: variables, operations, functions, and modifiers to format the value. A placeholder can have a modifier to format the value. colon ':' is added to include the modifier. In the code file. .2f and , are used. .2f will add two decimal places while , will add comma in every 3 digits. Value can be directly added in the placeholder without the variable. Mathematical operations: values or variables, can be done within the placeholder as shown in code file. if...else statements can be included inside the placeholders. Functions can also be executed inside the placeholder. In the code file upper() function is used. User defined functions can be used in the placeholder.
string format() are not used in python 3. But for practise, I have included it in the code file.

