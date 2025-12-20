'''Decorator'''
# A decorator is just a function that modifies another function without changing its actual code.
# Imagine you have a cake (your function). A decorator is like putting icing on the cake. It doesn’t change the cake itself, but makes it better, prettier, or adds some new flavor
# For creating a decorator you first have to create a decorator functions and then inside that we will create a wrapper.
# Its tough to understand with text see the video
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
# For making the decorator with Arguments it is tough for this we will move towards our next advance stuff *args , **kwargs.

'''Args and Kwargs'''
# They’re special keywords in Python used in function definitions to accept a flexible number of arguments
# Now you always don’t have to use Args and Kwargs the main thing is * , ** you can use any names in front of them.
# so *args are used for multiple positional arguments, and **kwargs are used for multiple key word arguments.
# And the *args becomes a tuple and **kwargs becomes a dictionary
# The use case is grea
# You don’t need to know how many inputs you'll getHelps in building flexible functions, decorators, APIs, and more.
def fun(*args,**kwargs):
   print("Args", args)
   print("Kwargs", kwargs)

fun(1,2,3,name="siddhant", age="20")

'''List, Dictionary and set comphrehension'''
# All of these Comprehensions are used to create List, Dictionary and set. But you don’t have to use multiple lines of code for loops and If-Else statements. 
labels = ["Even" if x % 2 == 0 else "Odd" for x in range(5)]
# ['Even', 'odd','Even', 'odd','Even']
Evens = {x: x*x for x in range (10) if x * 2 == 0}
# {0:0,2:4,4:16,6:36,8:64}
Unique_even_squares = {x*x for x in range (10) if x * 2 == 0}
# {0,4,16,36,64}

'''Lambda functions'''
# A lambda function is an anonymous, inline function defined using the lambda keyword
# It's often used for short, simple functions that are used only once or temporarily
# You can have multiple arguments but there will be only one expression.

# Lets see a basic example
square = lambda x: x ** 2
print(square(4)) # Output: 16
# The argument 4 is passed in x. you can also have multiple arguments and you can also include If - Else expressions 

check_even = lambda x : "Even" if x % 2 == 0 else "Odd"
print(check_even(7)) # Output: Odd

'''Map filter and zip'''

# Map is used for applying a function to multiple items.
# Takes a list (or any sequence
# Applies the same function to every item in that list
# Gives you back a new list (in Python 3, it gives a map object which you can convert to a list)
number = [1,2,3,4,5]
doubled = map(lambda x: x * 2, number)
print(list(doubled)) # Output: [2,4,6,8,10]
# Use map() when you want to transform every item in a list
# It doesn’t remove or skip items (that’s what filter() does)
# You can use it with lambda or normal functions


# Filter as the name suggest is used to filter out the stuff.
# Takes a list (or other sequence
# Checks each item using a function (a test
# Keeps only the items that pass the test (i.e., return True)
number = [1,2,3,4,5]
evens = filter(lambda x: x % 2 == 0, number)
print(list(evens)) # Output: [2,4]

'''Modules and packages'''
# Module is just a single file containing code and we can use this file code in other file
# A single Python file (.py
# Contains functions, variables, or classe
# Used to organize and reuse code
# Python comes with lots of ready-to-use modules like
# math (for math operations
# random (for generating random numbers
# datetime (for date and time)
import math 
print(math.sqrt(16)) # Output: 4.0
# A package is a folder that contains one or more modules (Python files). It may also contain sub-packages
# and you just have to use from and import keywords to use these things. You understood how these things work.
# There are third party packages as well like numpy, pandas, matplotlib etc. and we have to install all of these