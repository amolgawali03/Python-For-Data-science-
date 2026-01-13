
"""examples """
"""
d={
    "kand":"event",
    "karma":"actions",
    "soch":"belive"
}

word=input("enter the meaning of the word u want: ")
print(d.get(word))
"""

""" this program will return the hindi vaule of the word u entered , if the word not in dictionary it will return none 

n1=int(input("enter the number:"))
n2=int(input("enter the number:"))
n3=int(input("enter the number:"))
n4=int(input("enter the number:"))
n5=int(input("enter the number:"))
n6=int(input("enter the number:"))
n7=int(input("enter the number:"))
n8=int(input("enter the number:"))

s=set()
s.add(n1)
s.add(n2)
s.add(n3)
s.add(n4)
s.add(n5)
s.add(n6)
s.add(n7)
s.add(n8)
print(s)
s1={18,'18'}
print(s1)
"""
D1={}
name=input("enter your name: ")
v=input("enter your favroite language :")
D1.update({name:v})

name=input("enter your name: ")
v=input("enter your favroite language :")
D1.update({name:v})

name=input("enter your name: ")
v=input("enter your favroite language :")
D1.update({name:v})

name=input("enter your name: ")
v4=input("enter your favroite language :")
D1.update({name:v4})

print(D1,type(D1))

# If the names of 2 friends are same; what will happen to the program
# the value will get updated . only the updated key value will be shown in the dictionary 

"""
Can you change the values inside a list which is contained in set S?
s = {8, 7, 12, "Harry", [1,2]}
--> no ,
The list [1,2] cannot even be stored inside the set.

A set can only contain hashable (immutable) elements

Lists are mutable, so they are unhashable

Python does not allow mutable objects inside a set
"""
