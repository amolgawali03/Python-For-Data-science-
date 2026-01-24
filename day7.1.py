"""
FUNCTIONS WITH ARGUMENTS / PARAMETERS
A function can accept some value it can work with. We can put these values in the
parentheses

Types:
1. Positional argments 
--> These are the most basic type - arguments passed in a specific order.

2. Default arguments
--> Arguments with default values that are used if no value is provided.

3. Keyword Arguments
--> Arguments passed by explicitly naming the parameter, allowing you to pass them in any order.

4. Variable-Length Positional Arguments (*args)
--> Allows a function to accept any number of positional arguments, collected as a tuple.

5. Variable-Length Keyword Arguments (**kwargs)
--> Allows a function to accept any number of keyword arguments, collected as a dictionary.



"""
def greet(name,ending):
    print("good day, "+ name)
    print(ending)

greet("amol","thank u")
greet("prem","thank u")
greet("neha","thanksss")

# return keywords takes a value from the function an gives it to a variable which is called 

def gre(name1):
    gr="hello "+ name1
    return gr
a= gre("amol") # now a will contain "hello amol"
print(a)


# DEFAULT PARAMETER VALUE
# We can have a value as default as default argument in a function.

def greet1(name2,ending1="thank u"):
    print(f"good day ,{name2}")
    print(ending1)

greet1("amol")
greet1("prem","thanks")

# keyword arguments

def details(name3, age, dept):
    print(f"Details are:\n{name3}\n{age}\n{dept}")
details(name3="amol",dept="cosa",age="21")    # order does not matter 
  
# variable length positional arguments *args

def sum_all(*numbers):
    return sum(numbers)

print(sum_all(1, 2, 3))        # 6
print(sum_all(1, 2, 3, 4, 5))  # 15

def display_name(*args):
    for arg in args:
        print(arg,end=" ")
display_name("mr","amol","gawali") 
print("\n")

# varaible length keyword arguments **kwargs

def info(**kwargs):

    """ for key in kwargs.keys():
        print(key) # will print all the keys 
    for value in kwargs.values():
        print(value) # will print all the values 
    """
    for key,value in kwargs.items():
        print(f"{key}:{value}")

info(street="MG road",city="Manali",zip="1244",state="HP")
print("\n")

def position(*ags,**kwars):  # order matters , pehle positional args fir keyword args 
    for arg in ags:
        print(arg,end=" ")
        
    print("\n")
    for key,value in kwars.items():
        print(f"{key}:{value}")
    
position("mr.","amol","somnath","gawali",
         street="MG road",city="Manali",zip="1244",state="HP")