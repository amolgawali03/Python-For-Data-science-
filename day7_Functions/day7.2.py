

""" Recursion """
# Recursion = a function that calls itself

"""
Recursion has ONLY 2 parts 🧠
1. Base Case (STOP condition)

This tells Python:

“Dont call the function again. Stop now.”

Without this → infinite loop → program crash 💥

2. Recursive Case (CALL again)

This is where the function:

calls itself with a smaller or simpler problem
"""
# example 
def count(x):
    if x == 0:      # Base case
        return
    print(x)
    count(x - 1)    # Recursive call
"""
count(5) → prints 5 → calls count(4)
count(4) → prints 4 → calls count(3)
count(3) → prints 3 → calls count(2)
count(2) → prints 2 → calls count(1)
count(1) → prints 1 → calls count(0)
count(0) → STOP
"""
def factorial(n):
    if(n==0) or (n==1):
        return 1
    return n * factorial(n-1)

n=int(input("enter a number:"))
print((f"The Factorial of {n} is :{factorial(n)}"))

""" lambda function """

"""
A lambda function is a small, anonymous function (a function without a name).
 -It is used when you need a simple function for a short time.

syntax:
 lambda arguments : expression

- only one expression 
- no return keyword needed 

"""
square = lambda a: a*a
print(square(5))

check_even = lambda y: "Even" if y % 2 == 0 else "Odd"
print(check_even(7))
