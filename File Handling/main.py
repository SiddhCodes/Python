'''What are files'''
# You all know what are files any name with an extension is file
# Now that extension can be .py , .txt , .mp3 etc. and when we want to handle these files we will use file handling. 
'''File handling'''
# File handling means Creating, Reading, Updating, Deleting(CRUD) operations that we can perform in files
# Now lets see how to perform these operations in python.
# We have to use open() function to open a file in python.
# Now there are multiple modes to open the file
'''Mode'''
# ‘r’ - Read (default) – file must exist.
# ‘w’ - Write – creates file or overwrites.
# ‘a’ - Append – adds to end of file.
# ‘x’ - Create – creates a new file, fails if it exists
'''Syntax'''
file = open("myFile.txt", "r")
print(file.read()) # read entire file
# print(file.readline()) # read oneline
# print(file.readlines()) # real all line into the list
file.close()
# This is the basic syntax through which we can open a text file and the ‘r’ there represents read mode and there are multiple modes like this as mentioned before. see the video for other modes as well.
# Now after working you have to close the file manually but for this we have with keyword
with open("data.txt","r") as f:
    content = f.read()
    print(content)
# Now Lets create a basic file handling project.