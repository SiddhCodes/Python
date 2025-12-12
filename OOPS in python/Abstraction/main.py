'''Abstraction'''
# Abstraction does not exist in python but we can achieve it using a library we will see what is a library later.
# Abstraction is used to simplifying complex systems by focusing on essential features and hiding unnecessary details
# It is used to define a common interface for different subclasses
'''Abstract classes and methods '''
# Abstract classes are classes that contains one or more abstract methods
# A method that is defined but not implemented in the abstract class. subclasses must provide the implementation
from abc import ABC, abstractmethod

class Animal(ABC): # Abstract class
    @abstractmethod
    def make_sound(self): # Abstract method
        pass

class Dog(Animal):
    def make_sound(self):
       print("Dog says Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Cat says Meow!")