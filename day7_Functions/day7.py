""" functions """

""" 
A function is a group of statements performing a specific task.

When a program gets bigger in size and its complexity grows, it gets difficult for a
program to keep track on which piece of code is doing what!

A function can be reused by the programmer in a given program any number of times 
"""

"""
function defination 

The part containing the exact set of instructions which are executed during the function
call.
"""

""" 
function call 
Whenever we want to call a function, we put the name of the function followed by
parentheses as follows:
"""

def avg():                                 # function defination 
    a=int(input("enter a number:"))
    b=int(input("enter a number:"))
    c=int(input("enter a number:"))

    average=(a+b+c)/3
    print(average)
    
avg()                                      # function call
print("thank u!")
avg()
avg()

"""
TYPES OF FUNCTIONS IN PYTHON
There are two types of functions in python:
• Built in functions (Already present in python)
• User defined functions (Defined by the user)
Examples of built in functions includes len(), print(), range() etc.
The avg() function we defined is an example of user defined function.

"""
# function can return multiple values 