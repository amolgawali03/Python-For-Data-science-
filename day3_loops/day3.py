"""format specifiers in python"""

# format specifiers = {value:flags} format a value based on the flags inserted 

price1=3333.034955
price2=-382394
price3=383344.099

print(f"price 1 is {price1:+,.2f}") 
print(f"price 2 is {price2:+,.2f}")
print(f"price 3 is {price3:+,.2f}")


"""
give us the price rounded of to 2 decimal places , will seperate 100os using ,
and + will get attached in the front if the value is positive 

"""

# .(number)f = round of to that many decimal places (fixed point)
# :(number)= allocates that many spaces 
# :< = left justify
# :> = right justify
# :^ = center align 
# :  = insert space before positive numbers 
# := = place sign to leftmost position 
# :, = comma seperator


"""while loops"""

""" 
In while loops, the condition is checked first. If it is true, the body of the loop
is executed otherwise not!
If the loop is entered, the process of [condition check & execution] is continued until
the condition becomes False.
note: If the condition never become false, the loop keeps getting executed

"""
num=int(input("enter the number :"))

while num<0 or num>10:
    print(f"{num} is not valid")
    num=int(input("enter the number :"))

print(f"your number is {num}")

food=input("enter a food u like(q to quit) :")

while not food=="q":
    print(f"you like {food}")
    food=input("enter another food u like(q to quit) :")

print("byeee")
