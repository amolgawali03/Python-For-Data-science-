
username=input("Enter a username :")

result= len(username)

if result<=12 and username.isalpha() :
    print(f"{username} entered is valid!!!")
else:
    print(f"{username} entered is invalid!")

""" replace """

letter = "Dear <|name|>\n you are selected\n<|date|>"

print(letter.replace("<|name|>","amol").replace("<|date|>","24 march 2026"))

""" check double space """
name=input("Enter a string :")
result1=name.find("  ")# this will give us the index of the substring (double space)

print(result1)


""" strings are imutable 
What does “immutable” mean?

Immutable = cannot be changed after creation.
"""