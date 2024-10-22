import re

# To check if there is a match or not

txt = "The rain in Kathmandu"
x = re.search("^The.*Kathmandu$", txt)   # To check if txt starts with The and Ends with Kathmandu

if x:
    print("Yes! We have a match!")
else:
    print("No match")

txt = "123 is a number"
x = re.search("^1.*number$", txt)

if x:
    print("There is a match")
else:
    print("There is no match")

# The findall() function

txt = "Dashain in Nepal"
x = re.findall("ai", txt)    # It finds the string in txt and returns it. The x is list 
print(x)

txt = "The blackhole in the Universe"
x = re.findall("e", txt)
print(x)

txt = "The ultra man"
x = re.findall("z", txt)  # Empty set is returned as there is no z in the string
print(x)

# The search() Function
txt = "Ther sunny day in Kathmandu"
x = re.search("\s", txt)    # If no match is found, None is returned
print(type(x))
print(x)
print("The first white-space character is located in position:", x.start())

txt = "The Rock is awesome"
x = re.search("Kathmandu", txt)
print(x)

# The split() Function
txt = "Bibekster in python"   # It will split at each white-space character
x = re.split("\s", txt)
print(x)

txt = "Bibekster in Python"
x = re.split("\s", txt, 1)   # splits the stirng at the first occurence
print(x)

txt = "Bibekster in Python and AI"
x = re.split("\s", txt, 2)   # splits the first two string separated by white-space and rest is printed as it is
print(x)

# The sub() Function
txt = "The rain in Kathmandu valley"
x = re.sub("\s", "ad", txt)   # First parameter: White Space. The second parameter will replace first parameter
print(x)

txt = "The rain in Nepal"
x = re.sub("rain", "apple", txt)
print(x)

# Controlling the number of replacements
txt = "The rain in USA"
x = re.sub("\s", "-", txt, 2)   # It will replace the white space at first two locations
print(x)

txt = "The Bibekster is the stormis"
x = re.search("is", txt)   # This will return an object
print(type(x))
print(x)

txt = "The Bibekster is storm"
x = re.search(r"\bB\w+", txt) # The re will look for string that starts with B and ends at white space
print(x.span())   # The span() function will print the range of the word

txt = "The Champ is Crazy and Cool"
x = re.search(r"\bC\w+", txt) # Notice here that only the first Champ is returned
print(x.span())

# To print the string associated with search() function
print(x)
print(x.string)   # It will return all the string

txt = "The Champ is Crazy and Cool"
x = re.search(r"\bC\w+", txt)
print(x.group())  # It will return the match string

