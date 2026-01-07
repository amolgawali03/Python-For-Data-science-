"""for loops """

# used to execute a block of code a fixed number of times 
# A for loop is used to iterate through a sequence like list, tuple, or string [iterables] 

for x in range(1,11):
    print(x)

print("")

# reversed function 

for x in reversed(range(1,11)):
        print(x)
        
print("")

# step size
for x in range(1,11,2):
    print(x)
print("")
# break statement 

""" break is used to come out of the loop when encountered. It instructs the program to –
exit the loop now."""

for x in range(1,11):
     if x==7:
          break
     else:
          print(x)
print("")


# continue statement 
""" ‘continue’ is used to stop the current iteration of the loop and continue with the next
one. It instructs the Program to “skip this iteration” """

for x in range(0,11):
     if x==3:
          continue
     else:
          print(x)

# pass statement
"""pass is a null statement in python.
It instructs to “do nothing”"""

"""table using for loops"""

num=int(input("Enter a number:"))
print(f"Table of {num} is :")

for i in range(1,11):
     print(f"{num} X {i} = {num*i}")

"""prime number check """

n=int(input("enter a number :"))


for i in range(2,n):
     if (n%i)==0:
          print("number is not prime")
          break
else:
     print("number is prime ")


"""factorial of a number"""

f=int(input("enter a number :"))
product=1

for i in range(1,f+1):
     product*=i
    
print(F"factorial of {f} is :{product}")    

""" fibonacci series """

j=int(input("enter a number :"))


print(f"fibonacci series upto {n} is :")
a,b=0,1
while a<=j:
    print(a,end=" ")
    c=a+b
    a=b
    b=c

    
     
     
