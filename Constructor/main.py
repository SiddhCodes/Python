'''What is constructor'''
# You saw last example where we wanted material, zips and pockets from the user to create an object.
# If we talk about a function we can ask the user using parameters, but in class we can’t have parameters for that we use constructor
# A constructor is a method that runs automatically when we call a class and this constructor function will target the objects location
class Student:
    def __init__(self, name):
        self.name = name # instance Attribute

# Creating an object with a value 
s = Student("Siddhant")

# Accesing the Attribute
print(s.name)
# To target the objects location we use self keyword.
# For clear understanding watch the video carefully. we will create the bag factory and will create multiple objects where self will target the specific locations of the objects.
