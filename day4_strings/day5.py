
str="amol"
str1='amol'
str2="""amol is a great at\nsports """
str3="""amol is a great at\tsports """
str4="amol is a \"Athelatic\""

""" \n ,\t , \, \\ are some escape sequence characters"""
print(str)
print(str1)
print(str2)
print(str3)
print(str4)


"""string slicing """

"""
A string in python can be sliced for getting a part of the strings.
Consider the following string:
   
name=" A m o o l" --> lenght =5
       | | | | |
       0 1 2 3 4 
       -5 -4 -3 -2 -1

The index in a sting starts from 0 to (length -1) in Python

 """
name="amool"

sl=name[0:3] # start from index zero all the way till 3 (excluding 3)
char=name[1:3] # start from index 1 all the way till 3 (excluding 3)

print(sl)
print(char)

print(name[-4:-1]) # negative indexing --> convert into corresponding positive indexes 
print(name[1:4])

word="amazing"

print(word[:5]) # same as [0:5]
print(word[1:]) # same as [1:7]

""" We can provide a skip value as a part of our slice like this:"""
print(word[1:6:2])

""" reverse a string """

print(word[::-1])