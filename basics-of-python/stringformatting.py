# Creating an f-string
txt = f"The price is Rs. 100"
print(txt)

# Placeholders and Modifiers
price = 800
txt = f"The price is Rs.{price}"
print(txt)

# Displaying the price with 2 decimals
price = 25
txt = f"The price is Rs.{price:.2f}"
print(txt)

# The value can be directly kept in the placeholder
print(f"The price is Rs.{65:.2f}")

# Performing the math operations in F-strings
print(f"The total working hour is {6*8}")
a=5
b=10
print(f"{a*b-10}")

# if else statements inside the placeholder:
price = 100
print(f"It is very {'Expensive' if price>50 else 'Cheap'}")

# Executing functions in F-Strings
name = "Bibek"
txt = f"I love {name.upper()}"
print(txt)

# Using the self made functions in the placeholder
def myconverter(x):
    return x*10
txt = f"the value of x is {myconverter(20)}"
print(txt) 

# Using a comma as a thousand separator:
price = 125000
print(f"The price is {price:,}")

# String format()
price = 500
txt = "The price is Rs.{}"
print(txt.format(price))

# Formatting the price to have two decimals
price = 800
txt = "The price is Rs.{:.2f}"
print(txt.format(price))

# Multiple values
price = 1000
itemno = 23
count = 12
txt = "The price is {}, item number is {}, count is {}"
print(txt.format(price, itemno, count))

quantity = 20
item = "Book"
price = 5000
txt = "I need {} number of {}s for Rs.{:.2f}"
print(txt.format(quantity, item, price))

# Index Numbers
quantity = 4
item = "Bikes"
price = 1000000
txt = "I need {0} number of {1} for Rs.{2:,.2f}"
print(txt.format(quantity, item, price))

age = 28
name = "Bibek"
txt = "His name is {1}. {1} is {0} years old"
print(txt.format(age, name))

# Named Indexes
bike = "I have a {model} which was designed by {company}"
print(bike.format(model="pulsar", company="bajaj"))

