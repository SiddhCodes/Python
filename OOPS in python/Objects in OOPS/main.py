'''Objects'''
# For understanding objects first look at this example you have a bag factory and that factory requires material of the bag, number of zips you need in that bag and number of pockets you need in your bag.
# So this is a kind of a blueprint and using this blueprint Reebok, campus and some other companies provided their requirements and created their bags
# Thus these companies became objects who created their bags using the blueprint. 
'''Object syntax'''
# It is very easy to create an object you just have to call the class inside a variable and that variable becomes an object.
# The object has all the powers of a class therefore a class object can access attributes and methods of a class.
class Fruit:
    name = "Apple"

# Creating an object 
f = Fruit()

# Accessing the attribute 
print(f.name)