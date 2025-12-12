'''What are Dunder methods'''
# Dunder methods are special methods in Python that start and end with double underscores, like __init__, __str__, __add__, etc
# They automatically get called when you perform certain actions on an object
# They help you Customize behavior of your class
# Make your class objects behave like built-in data types (like strings, lists, etc)
class Parent:
    def __init__(self,name):
        self.name = name

p = Parent("Ravi")
print(p.name)
