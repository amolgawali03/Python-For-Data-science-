# practice 
n1=int(input("enter a number :"))
n2=int(input("enter a number :"))
n3=int(input("enter a number :"))


def greatest(n1,n2,n3):
    if n1>n2 and n1>n3:
        return n1
    elif n2>n1 and n2>n3:
        return n2
    elif n3>n1 and n3>n2:
        return n3
    else:
        print("numbers are equal")



print(f"The greatest number among these numbers is :{greatest(n1,n2,n3)}")

def f_to_c(f):
    return 5*(f-32)/9

f=float(input("Enter temperature in F: "))
print(f"The temprature in °C is :{round(f_to_c(f),2)}")

"""
How do you prevent a python print() function to print a new line at the end.
--> print(n, end="")
"""
def sum(n):
    if n==1:
        return 1
    return sum(n-1) + n
n=int(input("enter a number: "))
print(f"The sum of first {n} natural nums is: {sum(n)}")

def pattern(p):
    if(p==0):
        return
    print("*"*(p))
    pattern(p-1)

p=int(input("enter a number: "))
pattern(p)
