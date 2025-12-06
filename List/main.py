'''List Powers'''
# Before starting we need to understand some of the terminology.
'''Mulable'''
# Mutability refers to whether an object's value can be changed after creation. And List allows this
'''Duplicates'''
# we know data structures are used to store multiple values so duplicates means same value occuring multiple time. List allows this
'''Ordered'''
# List maintains ordered data structure maintains the sequence of elements as they were inserted. This means you can access elements using their position (index)
'''Heterogenous'''
# List have heterogenous nature that means we can have multiple data types inside the list.
'''List Basics'''
# First we have to know what is the syntax of list and how, to create a list we have to use square brackets ([])

name = ["siddhant","aman","ajit","himanshu","yash","aditya"]
number = [1,2,3,4,5,6,7,8,9]
# Now list has Indexing and slicing and it is same as string if you forgot how string indexing and slicing works watch the video or revise the notes.
# The changes we saw in string and list is about mutability, we can’t change the values of string. but we can of list.

# Define a list 
number = [1,2,3,4,5]
# modify the value at index 1 (2nd element)
number[1] = 99
# print the updated list
print(number) # output: [1,99,3,4,5]

'''List Traversing and methods'''
# Now list traversing is also similar to string traversing it can be looped using the index values and directly
# Now list has some methods that are used to do many, and don’t worry if you are not sure what are methods, for now just think they are like function, further we will see it clearly.
# Now see some of the examples of the methods you will get it what they are used for.

number = [1,2,3,4,5,6,7,8,9] # initial list
number.append(10) # add 10 to the end
number.insert(2,15) # inserts 15 at index 2 
number.remove(5) # removes the first occurrence of 5
popped_item = number.pop(2) # removes the element at index 2 and returns it
index = number.index(15) # returns the index of the first occurrence of 15
count_5 = number.count(5) # returns the count occurrence of 5 in the list
number.sort() # sorts the list in ascending order
number.reverse() # sorts the list in descending order
new_number = number.copy() # creates a copy of the list
number.clear() # Removes all elements from the list

# So these are some methods that are used in list . 
