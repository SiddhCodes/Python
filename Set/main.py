'''Set Powers'''
# Before starting we need to understand some of the terminology.
'''Mutable'''
# Sets are mutable you can change the values of set.
'''Duplicate'''
# You cannot have any duplicate values in sethat means every element will be unique
'''Unordered'''
# Sets are unordered and you cannot access them through index values
'''Heterogenous'''
# Set is semi-heterogenous it can store some data types like string, numbers, tuples but not everything

'''How Set stores value in python'''
# Each value in a set is hashed using a hash function (hash() in Python)
# The hash is used as an index to store the element in memory
# Since hashing does not maintain order, sets are unordered
# Only immutable (hashable) objects can be stored in a set (e.g., numbers, strings, tuples). Mutable objects like lists and dictionaries are not allowed
# See the video for more clear understanding.

'''Set Traversing'''
# A set cannot be traversed using the index values cause it is unordered and has no index
# So many times it will give random values. you can watch the video for complete understanding

'''Set methods'''
# Now set methods are very powerful cause you don’t have any indexing you cannot change the values but set is mutable so we use methods for this
# For adding and removing the elements you can use methods as follows
set = {1,2,3}
set.add(4) # add 4 to the set
set.remove(2) # remove 2 from the set
set.discard(5) # discard 5 from the set
popped_element = set.pop() # remove the element and return it
set.clear() # remove all elements from the set
# Now these are some of the basic methods but sets also have some special methods for performing some special operations between 2 sets.

a = {1,2,3}
b = {3,4,5}
union_set = a.union(b) # returns the union of 2 sets
intersection_set = a.intersection(b) # returns the intersection of 2 sets
deference_set = a.difference(b) # returns the difference of 2 sets
symmetric_diff = a.seymmetric_difference(b) # returns the symmetric difference of 2 sets

# So these are some other operationsof sets that can be performedbetween 2 sets. And we also have shortcuts for them
print(a|b) # returns the union of 2 sets
print(a&b) # returns the intersection of 2 sets
print(a-b) # returns the difference of 2 sets
print(a^b) # returns the symmetric difference of 2 sets

# Ok so we have seen these operations and while watching the video you have seen a ven diagram approach as well there are more methods you are open to try them and see the working
# But at the end set is not used that much in python lets continue.