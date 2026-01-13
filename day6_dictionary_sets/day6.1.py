
""" sets """
# Set is a collection of non-repetitive elements

# s=set()  # will return an empty set 
# s1={}  # will return an empty dictionary 
# print(type(s))
# print(type(s1))

s={1,2,4,346,"amol"}
print(s)
s.add("prem")
print(s)

""" 
PROPERTIES OF SETS
1. Sets are unordered => Element’s order doesn’t matter
2. Sets are unindexed => Cannot access elements by index
3. There is no way to change items in sets.
4. Sets cannot contain duplicate values.
"""
print(len(s))
s1={1,34,445,00,345,3,4}
s1.remove(00)
print(s1)
# s1.clear()  # empties the set s1

print(s1.union(s))  # union of sets 
print(s1.intersection(s))  # intersection of sets 

s2={18,'18'}
print(s2)

s3= set()
s3.add(20)
s3.add(20.0) # 20 == 20.0 are the same values 
s3.add('20')
print(len(s3))
 


