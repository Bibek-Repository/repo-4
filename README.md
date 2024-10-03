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








