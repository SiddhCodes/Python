'''Polymorphism'''
# Polymorphism is a core concept in Object-Oriented Programming =(OOP). The word means "many forms" — and in programming, it allows the same interface or method name to behave differently depending on the object or context
# Polymorphism can be achieved in python in two ways well if we talk about compile time languages there are 3 ways but python does not support Method overloading
# Method overloading means having same name methods inside a class but parameters will be different but in python the latest definition will overwrite the previous one
# Method Overriding
# This is where a child class overrides a method of the parent class, and Python decides at runtime which method to call, based on the object type.
class Animal:
    def Sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def Sound(self):
        print("Dog barks")

# Duck Typing
# Python follows the philosophy:If it walks like a duck and quacks like a duck, it must be a duck.
class Duck:
    def talk(self):
        print("Quack!")

class Human:
    def talk(self):
        print("hello!")

# In the speak() function, we don’t care if it's a Duck or a Human — we only care that the object has a talk() method.
