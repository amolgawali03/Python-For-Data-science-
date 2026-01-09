# mablis game 
# it a word game where we create a story by filling in the blanks with random words 

"""
adjective1=input("enter a adjective(description):")
noun=input("enter a noun(place,person,thing):")
adjective2=input("enter a adjective(description):")
verb=input("enter a verb ending with 'ing':")
adjective3=input("enter a adjective(description):") """

"""
print(f"today i went to a {adjective1} playgroud ")
print(f"i saw {noun} playing ")
print(f"{noun} was {adjective2} and {verb}")
print(f"i was {adjective3}!!!") """

""" Arithematic operators """

a=13
b=4

print(a+b) # +(addition) operator
print(a-b) #-(substraction) operator
print(a*b) # *(multiplication) operator
print(a**b) # to the power
print(a/b) # /(division) operator
print(a%b) # % (modulus) operator

a+=1
print(a)


"""math functions"""

"""
x=22.45
y=-2
z=2

result1=round(x) # round off the value to the nearest integer 
result2=abs(y)  # absolute value return 
result3=max(x,y,z)
result4=min(x,y,z)
result5=pow(x,z)

print(f"\n{result1}")
print(f"\n{result2}")
print(f"\n{result3}")
print(f"\n{result4}")
print(f"\n{result5}") """

# to use certain math functions we import math 

import math
j=9.9

print(math.pi) # return value of pi
print(math.e) # return value of e
"""
result6=math.sqrt(j) 
result6=math.ceil(j) #round of j up j=10
result6=math.floor(j) #round of j down j=9

"""
"""area of circle"""

r=float(input("enter the radius :"))

area=math.pi * pow(r,2)

print(f"area of circle is : {round(area,2)} cm^2")


"""calculating hypotenous"""

f=float(input("enter the value of side f :"))
g=float(input("enter the value of side g :"))

h=math.sqrt(pow(f,2)+pow(g,2))

print(f"the value of side h is :{round(h,2)}")