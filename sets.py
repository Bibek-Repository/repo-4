#Sets in Python

set1={"apple", 25, "roses"}
print(set1)    # displaying the set1 can result in display of values that is unordered

# length of the set

print(len(set1))

set2={2.0007, True, "apple"}
print(set2)
print(type(set2))    # type of set2 is set

#the set constructor

set3=set(("apple", "orange", "grapes"))
print(set3)

# Accessing Set items

# using for loop

for x in set3:
    print(x)

# to check if an item is present in the set or not

print("orange" in set3)
print("apple" not in set3)

# add values to the set

set3.add("mango")
print(set3)

# add sets
set4={1.5000, "ram", True}
set3.update(set4)
print(set3)

# adding other iterable objects in a set

list1=["delta", "info"]
set3.update(list1)
print(set3)

# removing values from set

set3.remove("delta")  # discard can also be used
print(set3)

# to remove random values form set

x=set3.pop()
print(set3)
print(x)

set3.clear()   # clears the set
print(set3)

del set3  #deletes the set3
#print(set3)

# joining two sets together

set5={"yellow", "orange","pink"}
set6={"solar","lunar","space"}

# using union

set7=set5.union(set6)
print(set7)

#using |

set8=set5|set6   # it can also be used to join multiple sets
print(set8)

#joining multiple sets

set9={"abc", "rog"}

set10=set9.union(set5, set6)
print(set10)

#to join a set and tuple

setsample={"ram", "hari"}
tuplesample=("om", "kavita")
setsample=setsample.union(tuplesample)
print(setsample)

# using update method to join two sets

set5.update(set6)
print(set5)

# intersection of sets

set_a={"ram", "hari", 52}
set_b={52}

set_c=set_a & set_b
print(set_c)

set_c=set_a.intersection(set_b)   #the intersection method allows us to join set with other arrays too but & does not allow this
print(set_c)

set_d=set_a|set_b   #here the repeating values are only used once
print(set_d)

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)         # notice here that the intersection is added to the original set set1 instead of returning
print(set1)

print()
setI={1,2,3,4,0,True,False}
setII={1,2,10,False}

setIII=setI.intersection(setII)
print(setIII)

#difference method (-)
setI={1,2,3,4,0,True,False}
setII={1,2,10,False}
print(setI)

setIII=setI-setII
print(setIII)

setIII=setI.difference(setII)
print(setIII)

#instead of returning value we can update the given set using the difference_update() method

setI.difference_update(setII)
print(setI)

#symetric Difference (only keeps the value that are not common)

setI={1,2,3,4,0,True,False}
setII={1,2,10,False}
setIII=setI^setII
print(setIII)

# symmetric_difference_update() will update the set instead of returning

setI={1,2,3,4,0,True,False}
setII={1,2,10,False}
setII.symmetric_difference_update(setI)
print(setII)


# trying to update the intersection

set1={"apple", "orange", "banana", "mango"}
set2={"grapes","pomegramte", "apple", "banana"}

set1.intersection_update(set2)
print(set1)

set1={"apple", "orange", "banana", "mango"}
set2={"grapes","pomegramte", "apple", "banana"}
set3={"apple","orange"}

temp=set1.isdisjoint(set2)  # we can use < symbol here
print(temp)

temp=set3.issubset(set1)
print(temp)

temp=set1.issuperset(set3)
print(temp)







