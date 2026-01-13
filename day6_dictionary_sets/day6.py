
""" Dictionary """

# Dictionary is a collection of keys-value pairs.
# used because lookup is faster. 

marks={
        "amol":100,
        "prem":90,
        0:"om",
        "list":[1,34,4345,44]
}

# print(type(marks))
#print(marks["amol"])
#print(marks["list"])

""" properties of dict
1. It is unordered.
2. It is mutable.
3. It is indexed.
4. Cannot contain duplicate keys

"""
""" methods """
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"amol":99,"neha":99})
print(marks)

print(marks.get("amol"))
print(marks.get("jordi"))  # it will returnn none 
# print(marks["jordi"])  # returns an error 

value =marks.pop(0) # Removes a key and returns its value.
print(value )

marks.popitem()
print(marks)    # Removes the last inserted key-value pair.


