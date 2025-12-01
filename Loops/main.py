'''Loops in python'''
# Loops in Python allow us to execute a block of code multiple times without rewriting it.
# Ok lets do one thing go to your VS code and print “hello world” 100 times
# Manually printing will take 100 code lines to print it. but using loops we need only 2 lines to print 100 times, thats the power of loops

'''Types of loops'''
# There are 2 types of loops in python. For and While loop.
# For understanding both types of loop we well see a great 

# example- you have a bucket filled with water and an empty bucket with a mug. 
# In scenario 1 you have to transfer 4 mugs of water from 1 bucket to another
# In scenario 2 you have to transfer all the water from 1st bucket to another via mug.

'''Intuition of loops'''
# In first scenario you know the number of mugs to transfer from one bucket to another.
#  Here you know how many numbers of iteration you have to go through, like you have to transfer only 4 mugs.
# So when you know the number of iterations you will use a for loop.

#  In the second scenario, you don't know how many mugs you need to transfer, but you do know the condition that determines when to stop.
# So when you don’t know how many iteration you have to use but you know a condition that determines when to stop you will use  loop

'''For loop'''
'''Range function'''
# Before understanding for loops you should know how range function works
# The range() function is used to generate a sequence of numbers, which is commonly used in loops
# Syntax of range function is simple range(start, stop, steps)
# you have 3 points from where you want to start, till where you want to stop and how many steps you want
# If you don’t mention start point the default value will be 0 .
# if you don’t mention the steps the default steps will be 1.
# you have to mention the stop point otherwise the range 
# function will not work.

'''Loops for numbers'''
# For using loops with numbers you need the range function.
# Best way to understand is going with an example
# You have to print numbers from 1 - 5. we will solve this question using for loop and range function

for i in range(1,6):
    print(i)

# So this is how you use a for loop. watch the full video for clear understanding of syntax.

'''Loops for strings'''
# Loops for strings work slightly differently. You can iterate through a string in two ways
# A. Using index values
# B.  Iterating directly over the string.

#  Iterating using the index values, Now we know that index values are numbers and for numbers we again have to use range function.
a = "Siddhant" 
for i in range(len(a)):
    print(a[i])

#  Here you iterated over the string using the index values for better understanding watch the video
# Second way is simpler we can directly iterate but using this method will give you the direct access to the characters instead of index values.
a = "Siddhant" 
for char in a:
    print(char)

'''Break continue else'''
# Things written above are very important for loops
#  Lets say you have this race track and you have to complete 20 laps but when you were completing the 16th laps and it started raining now you cannot complete the rounds
# The above example simulate the example of your break statement.
# The break statement in Python is used to exit a loop prematurely when a certain condition is met. Once break is encountered, the loop stops immediately, and control moves to the next statement after the loop
# The Continue statement skips one of the iteration and rest of the iterations will run for understanding lets say you will not run the 16th lap but all other lap will be there.
# You have seen the else statement used with if, but it can also be used with loops. When else is used with a loop, it only executes if the loop completes without encountering a break statement. If break is executed, the else block will not run.

'''While loop'''
# You have previously taken the information of loops and you also know conditional statements it is going to be easy for you to understand this now
# The while loop repeats a block of code as long as a condition is True. It is useful when the number of iterations is unknown before execution

# while condition:
    # code to be executed if condition is true

# So there is not much that you have to understand about while loop it also have break, continue and else.
# Now you just have to find out which loop will be used on what questions. 