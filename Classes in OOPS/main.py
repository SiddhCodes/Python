'''Classes'''
# A class is like a blueprint or template for creating objects
# Think of a class like the blueprint of a house. It defines what the house should have (rooms, windows, etc.) but doesn’t build the house. An object is the actual house built using that blueprint
'''Syntax of class'''
# A class is also created with a basic keyword class and a name in front of it
class Car :
    brand = "toyota"
# Creating a class is super simple now lets see what is inside class. There are 2 types of things inside class Attributes and Methods
# Attributes - Variables defined inside the class are Attribute
# Methods - Functions defined inside a class are Methods.
class Animal:
    species = "Dog" # Attribute
    def make_sound(self): # Method
        print("Bark") 
'''Accessing attributes and methods'''
# A class is initialised only one time when we first run the program. and for accessing the attributes and methods we have to first access the class and then attributes and methods.
class Animal:
    type = "car" # Attribute
    def sound (self): # Method
        print("Meow!")
# Directly accesing attribute and method using the class 
print(Animal().type) # Access attribute
Animal().sound() # call Method
