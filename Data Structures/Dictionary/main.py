'''Dictionary Powers'''
# Before starting we need to understand some of the terminology.
'''Mutable'''
#  Dictionaries are mutable, meaning you can change, add, or remove key-value pairs after creation
'''Duplicate'''
# Keys must be unique, but you can have duplicates in values
'''Ordered'''
# Dictionary follows insertion order
'''Heterogenous'''
# A dictionary can store different types of keys and values, like integers, strings, lists, or even another dictionary.

'''Dictionary syntax and working'''
# Now we know we have to use key and value pairs to store values in dictionary
# And the keys in dictionary acts like index values that we use in List
student = {"name":"siddhant", "age":20}
print(student["name"]) # accessing the value of key "name" Output: siddhant
student["age"] = 21 # changing the value of key "age"
# Again telling we can perform CRUD(create, read, update, delete) operations on values but not all on keys cause the keys cannot be changed after creation

'''Dictionary traversing'''
# We can traverse both keys and values in dictionary, but default loop is set on keys and you can access the values because of keys.
# So technically you can traverse on both keys and values at the same time
number = {1:10,2:20,3:30,4:40,5:50}
for i in number:
    print(i, ":", number[i])
# Do see the video explanation for better understanding

'''Dictionary methods'''
# There are not many dictionary methods lets see the working of some
# as you all know we can use help(dict) for getting the information of all the methods available.

