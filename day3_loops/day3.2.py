""" sum of first n natural numbers """

num=int(input("enter the number :"))
sum=0
i=1

while (i<=num):
    sum+=i
    i+=1

print(f"The addition of first {num} natural numbers is :{sum}")

""" table using while loop """

n=int(input("enter a number :"))

print(f"Table of {n} is :\n")
i=1
while i<=10:
    print(f"{n} X {i} = {n*i}")
    i+=1





