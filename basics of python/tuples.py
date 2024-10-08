# tuples
# tuples are ordered, unchangeable (they cannot be modified after the creation) and allows duplication

tuple1=("apple", "orange", "pomegranate", "leechi", "apple")   # notice here that the items can be repeated.
print(tuple1)

# determing the length of tuples

a=len(tuple1)
print(a)
print()
print(len(tuple1))

# indexing to access the particular element of the tuple
print(tuple1[0])

# tuples with one item should be ended with comma

tuple2=("ram",)
print(tuple2)
print(tuple2[0])

#using type method to display the class of the variable. here we are using tuple class.
print(type(tuple2))

# access tuples

print(tuple1[0])
print(tuple1[1])
print(tuple1[-1]) # it prints the last item of the tuple
print(tuple1[-2]) # it prints the second last item and so on

# accessing particular range of tuple

print(tuple1[1:3])  # it prints tuple item corresponding to index 1 and index 2. notice that index 3 is not displayed

# if we start with colon : and end with an index, it will print all the values from starting to the index-1

print(tuple1[:3])

# if we start with an index and end with : then the items will be displayed from index to end

print(tuple1[2:])

# range of negative index

print(tuple1[-3:-1]) #-3 is included and -1 is not included

# using in keyword to check if the item is in a tuple?

if "apple" in tuple1:
    print("yes, 'apple' is in this tuple")

# update tuple
# tuples are unchangeable, but we can change tuples to list and then update and change the updated list back to the tuple

x=list(tuple1)
x[0]="banana"
tuple1=tuple(x)
print(tuple1)

# add tuple
# since tuple are unchangeable, convert it to list then use add property of list like append to add new items

x=list(tuple1)
x.append("cherry")
tuple1=tuple(x)

print(x)

# we can also add two tuples together

tuple3=("angur",)
tuple1+=tuple3   #tuple1=tuple1+tuple3
print(tuple1)

# removing Item from tuple
# convert it to list and remove the item

x=list(tuple1)
x.remove("angur")
tuple1=tuple(x)
print(tuple1)

# we can completety delete a tuple using del command

print(tuple3)
del tuple3

print("deleted")

# unpacking tuples

tuple4=("ram","hari","shyam")
(red, green, orange)=tuple4
print(red)
print(green)
print(orange)

# when unpacking if the number of items or values are greater than the variables, then * can be used

tuple5=("aa", "bb", "cc", "dd", "ee", "ff")
(black, white, *yellow)=tuple5
print(black)
print(white)
print(yellow) # yellow has a list of all the remaining values. hence yellow is converted to list

# a nd c takes the end values while b takes the remaining mid values
(a, *b, c)=tuple5
print(a)
print(b) 
print(c)

#looping the tuples

#using for loop

for x in tuple1:
    print(x)

#using index

for i in range(len(tuple1)):
    print(tuple1[i])
print()
i=0


#using while loop

while i< len(tuple1):
    print(tuple1[i])
    i+=1

#join tuples

tuple6=("ram", "bibek")
tuple7=("hari", "jenisha")
print(tuple6+tuple7)

# multiply tuples

tuple6*=3      # the tuple is repeated three times( repeatation is allowed in tuples)
print(tuple6)

#tuple methods

print(tuple6.count("ram"))  # counts the number of "ram" value in the tuple
print(tuple6.index("ram"))  # gives the index of the first "ram" value in the given tuple

