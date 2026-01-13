
""" lists """
# Python lists are containers to store a set of values of any data type.
# lists are mutable , can be modified or changed after the creation unlike strings

list=["amol","prem", 1,True,"omya"]

print(list[4])
list[4]="bangya"

print(list[4])
# slicing similar as the string 

print(list[0:4])

""" list methods"""
# strings mai agar hum method chaley toh hume ek nayi strring milegi ,
#  pr list mai agar hum method chalay toh humara original list mai changes honge

l1=[1,33642,253,7,890,0]

#l1.sort()          # sorts the the list in increasing order
#l1.append("tommy") # adds a element in the end of the list 
#l1.reverse()       # will reverse a list 

l1.insert(3,10101) # will insert 10101 at index 3 in the list 
value=l1.pop(3)           # will pop the element at index 3 also returns its value
print(value) 
l1.remove(1)               # removes 1 from the list 
print(l1)