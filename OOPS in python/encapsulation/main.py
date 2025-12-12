'''Encapsulation'''
# Encapsulation means putting data (variables) and code (functions) together in one place — inside a class
# It also means hiding the internal details of how things work, and only showing what is needed
# It keeps data safe from being changed by mistake
# It makes your code clean and easy to use
# It gives control over what others can access or change
'''Access modifiers in python'''
# Access modifiers means how we give access of our attributes and methods to the object or inherited classes. There are 3 types lets see them one by one.

# 1) Public Attributes and Methods.
# Till now every attribute and methods we have created are public means the inherited classes and objects can access them no matter what

# 2) protected Attributes and Methods
# python protected members are created using a single underscore but it still can be accessed from outside the class so you might wonder whats the point of using them
# Python doesn’t enforce protected access like other languages (e.g., Java or C++). But it uses a naming convention to tell developers

# 3) Private Attributes and Method
# A private variable or method means
# It cannot be accessed from outside the class — only from inside the class where it is defined
# In Python, we use two underscores (__) before the name to make it private.

class Demo:
    def __init__(self):
        self.name = "Public Member" # Public
        self._age = 20 # Protected 
        self.__salary = 0 # Private
    
    def show(self):
        print("Inside the class:")
        print("Public:", self.name)
        print("Protected:", self._age)
        print("Private:", self.__salary)
