# Using a package in Python

import camelcase

x = camelcase.CamelCase()   
txt = "bibekster ultra"
print(x.hump(txt))   # Each string before the white space is camelcased and returned
print(type(x.hump(txt))) 

x = camelcase.CamelCase()
txt = "the dextron"
print(x.hump(txt))
