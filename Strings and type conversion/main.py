'''How Strings work'''
# You know what strings are but you must also know string take more space than other data types like int, float etc
# This happens because String stores every character with their own Unicode
# Unicode is a universal character encoding standard that assigns a unique number (code point) to every character, regardless of language
# Like “A” unicode is 65 and “ ” this emoji unicode is 128522, you can check them by using ord() function in python and convert them back using chr() function
string = "A"
print(ord(string))
string = 65
print(chr(string))

'''String Indexing'''
# You must have thought there are so many characters in a string but can you access everyone
# Yes thats possible using indexing. Indexing starts from 0 and goes till the number of characters you have. eg - a = “Hello”  print(a[0]) ==> output - “H
# There is negative indexing as well and it starts from -1, but the starting position is from the back of the string eg - a = “Hello”  print(a[-1]) ==> output - “o”

'''String Slicing'''
# You know how to access characters in string. But there are slicing option as well.
# Slicing means cutting out a slice from string and this is also done using index values eg - a = “hello”  a[1:4:1]  ==> output “ello”
# So here we have start , stop and steps position and keep a note if we use stop at 4 it will slice till 3 only. 

'''Type conversion'''
# For understanding type conversion you have to look at these 4 things
#  int() float() str() bool()
#  There are more functions like this but these are 4 main 
# function, looking at these functions you can guess these are used to convert one data type to another 
# eg a = 12 a = str(a) 
# print(a)  ==> “12” 
# (a will be converted to string)

'''Type conversion types'''
# There are 2 types of conversion Implicit and ExImplicit

# Implicit
#  In this python automatically converts data from one data type to another.
#  You have already seen the example before
# eg - a = 12 
# print(a/2) 
# output - 6.
# Clearly we had the data type as int but after dividing python automatically converted the data type to float. 

# ExImplicit
# In this we as a user use in build functions to convert one data type to another
# You have seen the example at previous page

#  int() - Integer
# float() - Float                
# complex() - Complex        
# str() - String                  
# list() - List                 
# tuple() - Tuple             
# set() - Set                
# dict() - Dictionary                
# bool() - Boolean
 
# There are some explicit conversions that you might not understand but further we will understand.

'''Type conversion concepts'''
# Some important concepts of type conversions are you cannot convert a character to a int() that basic watch the video for more set of information
# bool() converter turns everything to True and False but which thing will be converted to true and which false. Lets see
#  There are truthy values and Falsy values, and there are only 7 falsy values that means only 7 things will be converted to false rest True. 

# 0
# 0.0 
#False 
#“”
# []
# {}
# ()

# All these values are falsy remaining will be converted to True.
