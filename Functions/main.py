'''What are functions'''
#  Functions in Python group reusable code into a block that can be executed by calling the function name. This helps avoid repetition and makes programs modular and readable
# There are many in-build functions in python like print(), input() len() etc
#  But you can create your own function and they are called as user defined functions. To make your own function you have to use def keyword and then name the function. After this you have to call the function using name() and paranthesis.
def greet ():
    print("hello, welcome to python!")

greet() # calling the function

'''Functions parameters and arguments'''
# First thing I want to talk about is parameters, parameters are variables listed inside the function definition. For making the function we have to accept inside the parenthesis of the function
def greet(name): # name is a parameter
    print(f"hello {name}")

greet()

# Arguments are the Values passed to a function when it is called
#  For example you can say you have created the parameters that are working like variables then we can pass the values to our variables using arguments
def greet(name): # name is a parameter
    print(f"hello {name}")

greet("alice") # alice is the argument 

# As you can see name is the parameter and Alice is the argument that we passed to name. And you can pass N number of parameters and arguments but they must be same like if you have taken 3 parameters you have to provide 3 arguments otherwise there will be error.
# And another thing is first parameter, will always capture first argument and so on. These arguments are called argument.

'''Types of Arguments'''
# Now there are 3 types of argument that we can pass to parameters. positional argument, default argument, keyword argument, For understanding these we will first see examples
def add(a, b): 
    return a + b
print(add(5,5))

def introduce (name,age):
    print(f"Hello, my name is {name} and I am {age} years old.")
introduce(age=25, name="siddhant")

def greet (name="siddhant"):
    print(f"hello {name}")

greet()
greet("siddhant")

# First example shows how positional arguments work
# Second example shows hoe default argument works here if you don’t pass any value still the function will run
# Last example shows how keyword argument works using this you can pass values in any order