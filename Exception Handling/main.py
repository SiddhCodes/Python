'''Errors'''
# Errors occur due to mistakes in the code that prevent it from running. These can be syntax errors or logical errors
'''Syntax Error'''
# print("hello world" # missing closing parenthesis
# Now this above code will give the error of syntax
'''Indentation Errors'''
# def func():
# print("hello") # no indentation
# You already know what is indentation and if you don’t follow it you will get the error
# There is one more tab error when you mix tabs and spaces
# These errors cannot be handled. but what can be handled are exceptions. 
'''Exceptions'''
# Exceptions are unexpected events or errors that occurs during the execution of a program, which disrupts the normal flow of the program.
print("start")
print(10/0) # raises ZeroDivisionError
print("end") # this line will never run
# Now this is a ZeroDIvisionError and can be counted as Exception and because of this exception the next line cannot be executed
# Like this there are many other exceptions just leave the three errors we saw at start otherwise others are exceptions.
# And the good part is we can handel them lets see how.
'''Exception Handling'''
'''Keyword'''
# try - Wrap the block of code that might cause an exception
# except - Handle the exception if it occurs
# else - Run code only if no exception occurs
# Finally - Run code no matter what, whether there’s an exception or not
# raise - Manually throw an exception
# So these are the keywords that we use and all these keywords has their separate purpose as mentioned.
# To see the code part see the video.