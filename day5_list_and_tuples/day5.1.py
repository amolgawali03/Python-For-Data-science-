""" tuples """

# A tuple is an immutable data type in python.
# huma ek asise data type ki jarurat thi joh diffrent data types ke values bhi store kare aur immutable bhi ho , hence comes tuple 

a=(1,2,3,"amol","prem",2639)
# a=(1,) # a tuple with only one element
print(type(a))

# slicing similar as list 
print(a[1:4])
print(a[0:])

""" tuple methods """

b=('i','k',12323,"amol",'i')
# value=b.count('i')  # will return the number of times the value is repeated in a tuple 
# value=b.index('i')   # will return the index of first occurrence of i in b
concatinate=a+b
print(concatinate) 

print(len(b)) 
