# json in python

import json

# conversion of JSON to python

x='{"name":"Bibek", "age":28, "address":"Sinamangal"}'    # a JSON
print(type(x))

y=json.loads(x)        # It returns a dictionary out of the JSON value:x  # parse the JSON value
print(type(y))
print(y["name"])

# Conversion from Python to JSON

x=json.dumps(y)
print(x)
print(type(x))

# conversion of different python objects to JSON

print(json.dumps({'name':'Bibek','address':'sinamangal','phone':9849266866}))   # A dictionary to JSON
print(json.dumps(["apple", "orange", True, 23048, 1]))      # A list
print(json.dumps(list({"apple","orange","harley davidson"})))    # a set
print(json.dumps(("Jyoti","ramesh","dipsa","bibek","krishala")))   # a tuple
print(json.dumps(31.76)) 
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))

x= {
    "name":"Bibek",
    "age":"28",
    "married":False,
    "divorced":False,
    "pets":None,
    "musics":[
        {"name":"qer34", "mpg":27.5},
        {"name":"qer34", "mpg":27.5}
    ]
}
print(json.dumps(x))







