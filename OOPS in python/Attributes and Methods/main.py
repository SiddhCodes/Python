'''Types of Attribute'''
# Types of Attribute
# Class attribute - 22 A normal variable created inside a class is is a class attribute and thats it.
# Instance attribute - A attribute created using an instance like self.name, self.age etc. It is known as instance attribute.
class Car:
    wheels = 4 # Class attribute
    def __init__(self, color):
        self.color = color # Instance attribute

'''Types of Methods'''
# Instance Method -An instance method Works with instance =(object) of the class. This method can access and modify instance attributes.
class MyClass:
    def instance_method(self):
        print("this is an instance method")

# Class Method - Static Method - This method works with the class itself it will not target the instance (object). we have to use @classmethod decorator for creating the class method and it takes cls as their first parameter.
class MyClass: 
    @classmethod
    def class_method(cls):
        print("This is a class method")
# Static Method - This method doesn’t access class or instance directly it also uses a decorator @staticmethod it just acts like a regular function placed inside a class. 
class MyClass:
    @staticmethod
    def static_method():
        print("This is a static method")

