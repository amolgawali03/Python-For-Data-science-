# weight convertor program 

"""weight=float(input("Enter your weight :"))
unit=input("enter the unit(K or L) :")

if unit=="K":
    weight=weight*2.205
    unit="lbs."
    print(f"your weight is {round(weight,2)} {unit}")
elif unit=="L":
    weight=weight/2.205
    unit="kgs."
    print(f"your weight is {round(weight,2)} {unit}")
else:
    print(f"{unit} entered is invalid")"""


"""logical operators"""

# used to evaluate multiple conditions (and , or, not)
# and = both conditions must be true
# or = atleast one condition must be true 
# not = inverts the condition ( not true , not false )

temp =float(input("enter the temperature :"))
is_sunny=True
is_raining=False

if temp>=30 and is_sunny:
    print("It is Hot outside !!!")
    print("It is Sunnyy, Stay home")
elif 30>temp>=20 and is_sunny:
    print("The weather is good !!!")
    print("U can go outdoors")
elif 20>temp>10 and  is_sunny:
    print("it is a bit cold outside")
    print("it is cloudy !")
elif 10>temp>0 and is_raining:
    print("It is pouring ouside!")
    print("stay indoors")
elif temp<=0:
    print("it is cold outside!!!")
    if is_raining:
        print("it is also raining!")
    if is_sunny:
        print("it is also sunny !!")
     
else:
    print("the input entered is invalid!")

"""conditional expressions"""

# a onne line shortcut for if else statements (ternary operator)
#prints or asigns one of two values based on the condition
# x if condition else y

num=23
age=10
a=7
b=24
print("positive" if num>0 else "negative")
print("adult" if age>=18 else "child")
print("a" if a>b else "b")




