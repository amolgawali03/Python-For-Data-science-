# day 1 of python programming 
""" hello world program """

print ("hello world!!!!")
print ("hello from nashik")

""" Addition of two numbers """

n1=int(input("enter the first value :"))
n2=int(input("enter the second value :"))

print("sum :",n1+n2)


"""swapping two numbers"""

n1=int(input("enter the first value :"))
n2=int(input("enter the second value :"))

print(f"before swapping :\n n1={n1} \n n2={n2}")

n3=n1
n1=n2
n2=n3

print(f"after swapping :\n n1={n1} \n n2={n2}")

""" swapping without 3rd variable """

n1=int(input("enter the first value :"))
n2=int(input("enter the second value :"))

print(f"before swapping :\n n1={n1} \n n2={n2}")

n1=n1+n2
n2=n1-n2
n1=n1-n2

print(f"after swapping :\n n1={n1} \n n2={n2}")

""" type() function and typecasting """

age=23

age=float(age)
print(type(age)) 


a=13
b="amol"
c=True 
print(f"converted values: {str(a)},{float(a)},{bool(b)},{type(a)}")

""" bool is data type that returnes either true or false values,
these values are case-sensitive, and using lowercase variants like true or false will result in a NameError, 
by default bool returns true
 """

f=int(input("enter value:"))
g=input("enter value:")

print(f"type of values : {type(f)},{type(g)}")

# It is important to note that the output of input is always a string (even if a number is entered)

i=53
j=67

if i>j:
    print("i is greater")
else:
    print("j is greater")

print(f"average of i and j is: {i+j/2}") # avegare of two numbers 

print(f"square of f is:{f*f}") # square of a number 


# The f before the string means:

# 👉 This is an f-string (formatted string literal)


#It tells Python:

# “Hey, I want to insert variables or expressions directly inside this string.”

"""
 The {} are placeholders.

Anything inside {} is:

evaluated by Python

converted to a string

inserted into the final output """