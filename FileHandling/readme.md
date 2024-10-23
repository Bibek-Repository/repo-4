Python File Handling

Several operations like creating, reading, updating, and deleting files can be done in python. These operations are known as File handling. File Handling is essential for web application.
To open a file in python, open() function is used. The open() function has two parameters: filename, and mode.
Different modes for opening a file in python are as follows:

"r" - Read: It opens the file for reading. If there is no such file error is created.
"a" - Append: It opens the file for appending(continuing). If there is no such file, new file is created.
"w" - Write: It opens the file for writing, creates the file if it does not exist
"x" - Create: It creates the file, If the file already exists, error is returned.

"t" - Text mode
"b" - Binary mode

Reading a file in python

First of all the file is opened using open() function
Then, read() method is called to read the content of the file. If the file is located in different location, path to file is to be included. An integer parameter can be added to print the total number of characters to be printed.
readline() method is used to read a line of the file
It can be called again to read another line of the file and so on.
for loop can be used to print all the lines in the file.
close() method is used to close the file.
closing the file is important because sometimes due to buffering, changes made to a file may not show until we close the file.

Write a file in Python
"a" is append mode. It will append to the end of the file
"w" is write mode. It will overwrite the content of the file. If the file does not exist, the file will be newly created.

Creating a new file in Python
"x": It will create a file. If the file exists, then it will return an error
"a": It will create a file. If the file exists, then it will append at the end.
"w": It will create a file. If the file exits, then it will overwrite the content.


