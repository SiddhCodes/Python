'''What is OOPS'''
# For understanding oops first lets see what we were doing in python for creating a program of addition we first use imperative approach.
a = 12
b = 12
print(a+b)
# This approach is simple just use 2 variables and add them one problem with this is you have to make 2 other variables for adding 2 other numbers
# Next approach is using functions to add 2 numbers this is functional approach
def add (a,b):
    print(a+b)
add(3,2)
add(10,10)
# Here the good thing is we can add multiple numbers without using multiple variables
'''What is OOPS'''
# And our next approach is object oriented programming approach.
class Add:
    def __init__(self, a, b):
        print(a + b)
obj = Add(12,12)
# OOPS (Object-Oriented Programming System) is a programming paradigm based on the concept of "objects", which can contain data (attributes) and code (methods)
# I know it is tough to understand right now but it will be easy after learning there are many concepts that we have to learn like classes, objects , Encapsulation, inheritance, Polymorphism,  etc. So lets start.
