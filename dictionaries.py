#dictionary

thisdict= {
    "brand": "tvs",
    "model": "apache",
    "year":2005
}

print(thisdict)             #output is in curly braces with the key pairs
print(type(thisdict))       #output gives class 'dict'
print(thisdict["brand"])

dict2= {
    "brand":"royal enfield",
    "model":"bullet",
    "model":"bullet",           #the second key model overides the first key model
    "year":"2024"
}
print(dict2)

print(len(thisdict))
print(len(dict2))

dict3={
    "brand":"dell",
    "model":"inspiron",
    "year":2010,
    "features":["nvdiagraphics", "8gb ram"]
}
print(dict3)
print(type(dict3["features"]))

#the dict() constructor

dict4=dict(book="DSA",author="Bibek Baiju",DateofPublish=1995,contents=["intro","objectives","conclusion"])
print(dict4)
print(dict4["book"])           #to access the value corresponding to the key book
print(dict4.get("author"))     #to access the value corresponding to the key author

print(dict4.keys())   # displays all the keys
print(dict4.values()) # displays all the values

dict4["DateofPublish"]=2000   #modification of the values in dictionary dict4
print(dict4.values())

#adding a new key and value pair in the dictionary

dict4["remarks"]="this is a technical book"
print(dict4.values())

print(dict4.items())
# lets make a change to the dict4 dictionary
dict4["author"]="John Mayer"
print(dict4.items())

#to check if a key is present in the dictionary

if "book" in dict4:
    print("yes, 'book' is in the dict4 dictionary")

#change the values of the dictionary

print(dict4["book"])
dict4["book"]="mathematics"
print(dict4["book"])

#to update a dictionary

dict4.update({"book":"linear maths"})
print(dict4["book"])

#to add pairs in the dictionary

dict4["publisher"]="ramesh publisher"
print(dict4["publisher"])

# dict4.pop("DateofPublish") # removes the DateofPublish key pair
# print(dict4)

# dict4.popitem()   # removes the last key value pair 
# print(dict4)

# del dict4["contents"] # it removes the key value pair corresponding to the key contents
# print(dict4)

# dict4.clear()    #it clears the dict4 dictionary
# print(dict4)

# del dict4   # it completely deletes the dict4 dictionary
# print(dict4)

#looping the dictionary
print()
for x in dict4:    # it displays all the keys in dictionary
    print(x)

print()                 # it prints all the values in dict4 dictionary
for x in dict4:
    print(dict4[x])

print()                 # it prints all the keys in dict4 dictionary
for x in dict4.keys():
    print(x)

print()                 # it prints all the values in dict4 dictionary
for x in dict4.values():
    print(x)

print()
for x,y in dict4.items():   #since items() method returns both keys and values of the dictionary
    print(x,y)

# to copy a dictionary

dict5=dict4.copy()
dict6=dict(dict4)
print()
print(dict5)
print()
print(dict6)

#Nested Dictionaries

dict7={
    "brand":"ferrari",
    "model":"m200",
    "year":2000
},{
    "color":"red",
    "price":"20B",
    "warranty":True
}

print()
print(dict7)

dict8={
    "child1":{
         "name":"bibek",
         "age":24
    },
    "child2":{
        "name":"dipsa",
        "age":26
    }
}
print(dict8)

#creating seperate dictionaries and adding them together

child1={
    "name":"hari",
    "age":10
}
child2={
    "name":"sita",
    "age":15
}
child3={
    "name":"ram",
    "age":20
}
myfamily={
    "child1":child1,
    "child2":child2,
    "child3":child3
}
print(myfamily)
print(myfamily["child3"]["age"])

#looping through the nested dictionaries

for x, obj in myfamily.items():    #here myfamily is a three key-value pair dictionary. items() returns the corresponding key and value to x and obj
    print(x)

    # for y,z in obj.items():
    #     print(y + ':', z)
    
    for y in obj:
        print(y + ':', obj[y])

print(myfamily.items())