# lambda functions in python

x = lambda a:a+10
print(x(10))

# Any number of arguments can be passed to the lambda function

y = lambda a,b: a*b         #lambda here returns the value to y, and we pass arguments to y
print(y(5,4))

summation = lambda a,b,c: a+b+c
print(summation(1,2,3))

# lets use this lambda function

def func_1(n):
    return lambda a:a*n

temp=func_1(4)                          # Here, func_1 returns the lambda function which is assigned to temp. Thus argument
print(temp(3))                          # can be passed via temp.

def func_2(n):
    return lambda a,b:a*b+n

z=func_2(3)
print(z(4,5))

