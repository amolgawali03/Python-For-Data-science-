# if else statements 

# if= do some code only if the condition is true else doo something else 

"""even odd checker """

n=int(input("enter the number:"))

if n%2==0:
    print(f"{n} is an even number !")
else:
    print(f"{n} is a odd number !")


""" calculator using python """

operator=input("enter a operator(+ - * /) :")
 
num1=float(input("enter the first number :"))
num2=float(input("enter the second number :")) # if we do not type caste the input, string concatination will occur , and our output :1011

if operator=="+":
    result=num1+num2
    print(f"The addition is : {round(result,3)}")
elif operator=="-":
    result=num1-num2
    print(f"The substraction is : {round(result,3)}")
elif operator=="*":
    result=num1*num2
    print(f"The multiplication is : {round(result,3)}")
elif operator=="/":
    result=num1/num2
    print(f"The division is : {round(result,3)}")
else :
    print(f"{operator}entered is invalid operator")

""" spam detector """

p1="Make a lot of money"
p2="buy now"
p3="subscribe this"
p4="click this"


message=input("enter a comment :")

if p1 in message or p2 in message or p3 in message or p4 in message:
    print("This comment is a spam!")
else:
    print ("This comment is not a spam")

# in keyword is used to check if the substring is present in the sring or not 
# case sensetive , the string must exactly match with the spam comments 