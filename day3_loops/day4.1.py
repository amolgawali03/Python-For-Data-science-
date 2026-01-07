
""" pattern printing """

"""
n=int(input("enter a number :"))

for i in range (1,n+1):
    print(" "*(n-i),end=" ")
    print("*"*(2*i-1),end=" ")
    print("")
    
 """

"""
n=int(input("enter a number :"))

for i in range(1,n+1):
    if i==1 or i==n:
        print("*"*n,end="")
    else :
        print("*", end="")
        print(" "*(n-2), end="")
        print("*", end="")
    print("")

"""

""" count down timer program """

import time

my_time=int(input("Enter time in seconds: "))

for x in reversed(range(1,my_time+1)):
    secounds=x%60
    minutes=int(x/60)%60  #% operator used cause minutes should not exceed 60
    hours=int(x/3600)
    print(f"{hours:02}:{minutes:02}:{secounds:02}")

    time.sleep(1) 

print("time's uppp!")