'''Inheritance'''
# In general terms Inheritance means property or any possession that comes to an heir
# But our python neither have an old man or a child then inheritance works where ?
# It works between classes.
# Inheritance allows a class (child class) to inherit properties and behaviors (attributes and methods) from another class (parent class).
# Benefits of using inheritance is 
# 1) Code reusabilit
# 2) Organized structur
# 3) Easy to maintain and extend
'''Syntax of Inheritance'''
# Syntax is very simple just like you take parameters in functions here you will take parameters but those parameters will be classes
class Parent:
    def speak(self):
        print("I can speak!")
class Child(Parent):
    pass
# Now the inherited class has all the powers of parent class that means all the methods, attributes can be accessed by the instance of child class as well.
'''Constructor in Inheritance '''
# Lets say you have created a parent class with a constructor function inside it and then this class is inherited by another class then the constructor function of parent class will work for the child class as well. 
class Parent:
    def __init__(self,name):
        self.name = name

class Child(Parent):
    def Display(self):
        print(f"My name is {self.name}")

# Now lets say you need a new parameter in your child class you have to create a constructor function for your child class but the parameters that can be initialized in the parent class will be initialized using the super() function. Super function will target the parent class.
class Parent:
    def __init__(self,name):
        self.name = name

class Child(Parent):
    def __init__(self, name,age):
        super().__init__(name)
        self.age = age
    def Display(self):
        print(f"My name is {self.name} and I am {self.age} years old")

'''Types of Inheritance'''
# 1) Single Inheritance
# All the inheritance we saw above was single level.

# 2) Multiple Inheritance
# Multiple Inheritance means there will be 2 parent classes and only 1 child class and the child class will inherit all the attributes and methods of both parents.
# Note - The constructor function will be inherited of the first class that has been Inherited. This is MRO(Method Resolution Order) followed by python.
class Father:
    def Skills(self):
        print("Coding")

class Mother:
    def Skills(self):
        print("Cooking")

class Child(Father,Mother):
    def Show(self):
        print("I have a multiple skills")

# 3) Multilevel Inheritance
# This is a basic case where we will have
# grandparent class → parent class → child class
# The attributes and methods are passed on through all the classes.
class Grandparent:
    def Inherit(self):
        print("Inherit from Grandparent")

class Parent(Grandparent):
    pass

class child(Parent):
    pass
