# compound interest calculator


"""principle=float(input("enter the principle :"))
rate=int(input("enter the rate :"))
time=int(input("enter the time :"))

while principle<=0:
    print(f"the principle cannot be negative or zero")
    principle=float(input("enter the principle :"))
while rate<=0:
    print(f"the rate cannot be negative or zero")
    rate=int(input("enter the rate :"))
while time<=0:
    print(f"the time cannot be negative or zero")
    time=int(input("enter the time :"))

print(principle)
print(rate)
print(time)
"""

""" the problem here is if we enter zero it directly jumps into print function skipping the while loops """
principle=0
rate=0
time=0

while True:
    principle=float(input("enter the principle :"))
    if principle<0:
        print("the principle cannot be negative")
    else :
        break

while True:
    rate=int(input("enter the rate :"))
    if rate<0:
        print("the rate cannot be negative")
    else :
        break

while True:
    time=int(input("enter the time :"))
    if time<0:
        print("the time cannot be negative")
    else :
        break


total=principle* pow((1+rate/100),time)
print(f"Balance after {time} years is :{total:.2f}")





