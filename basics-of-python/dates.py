# Dates in Python

import datetime

x=datetime.datetime.now()
print(x)

# To return indivisual date and time values

x=datetime.datetime.now()
print(x.year)
print(x.month)
print(x.day)
print(x.hour)
print(x.minute)
print(x.second)
print(x.microsecond)
 
# datetime class constructor

x=datetime.datetime(2023,3,10)
print(x)

# strftime() method

x=datetime.datetime(2024,8,6)
print(x.strftime("%B"))

x=datetime.datetime.now()
print(x.strftime("%B"))            # Output: October
print(x.strftime("%a"))            # Output: Tue
print(x.strftime("%A"))            # Output: Tuesday
print(x.strftime("%w"))            # Output: 2   weekday as number 0-6
print(x.strftime("%b"))            # Output: Oct
print(x.strftime("%d"))            # Output: 08
print(x.strftime("%m"))             # Output: 10   month as a number
print(x.strftime("%y"))              # Output: 24 short form of year
print(x.strftime("%Y"))              # Output: 2024
print(x.strftime("%H"))              # Output:11 
print(x.strftime("%I"))     # Output:11
print(x.strftime("%p"))     # Output:AM
print(x.strftime("%M"))     # Output:52
print(x.strftime("%S"))     # Output:28
print(x.strftime("%f"))     # Output:798763
print(x.strftime("%z"))     # Output: prints offset
print(x.strftime("%j"))     # Output:282
print(x.strftime("%U"))     # Output:40
print(x.strftime("%W"))     # Output:41
print(x.strftime("%c"))     # Output:Tue Oct  8 11:52:28 2024
print(x.strftime("%C"))     # Output:20
print(x.strftime("%x"))     # Output: 10/08/24
print(x.strftime("%X"))     # Output:11:52:28
print(x.strftime("%%"))     # Output: %
print(x.strftime("%G"))     # Output: 2024
print(x.strftime("%u"))     # Output: 2
print(x.strftime("%V"))      # Output: 41

  

