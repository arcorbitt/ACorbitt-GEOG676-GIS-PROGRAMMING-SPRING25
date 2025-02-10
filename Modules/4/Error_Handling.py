#--------------------------------------------Types of Errors--------------------------------------------#
# 1. Syntax Error
# 2. Exception Error

#--------------------------------------------Syntax Error--------------------------------------------#
# Syntax errors are errors that occur when the code is not written correctly.
# These errors are caught by the Python interpreter when the code is run.
# The interpreter will display an error message and will not run the code.
# Syntax errors are usually caused by:
# - Missing colons
# - Missing parentheses
# - Missing quotation marks
# - Missing brackets
# - Incorrect indentation
# - Incorrect spacing

# Example of a Syntax Error
# print("Hello, World") # This will run correctly
# print("Hello, World') # This will throw a SyntaxError

#--------------------------------------------Exception Error--------------------------------------------#
# Exception errors are errors that occur when the code is run.
# These errors are caught by the Python interpreter when the code is run.
# The interpreter will display an error message and will not run the code.
# Exception errors are usually caused by:
# - Trying to divide by zero
# - Trying to access an index that does not exist
# - Trying to access a key that does not exist
# - Trying to access a value that does not exist
# - Trying to access a file that does not exist
# - Trying to access a variable that does not exist

# Example of an Exception Error
# print(5/0) # This will throw a ZeroDivisionError
# print(myList[10]) # This will throw an IndexError
# print(myDict['key']) # This will throw a KeyError
# print(myTuple[0]) # This will throw an IndexError
# print(myVar) # This will throw a NameError

#-----f = open(r"/path/to/file/file.txt", "r")
#-----print(f.read())
#-----f.close()

#Imagine in the code snippet above that we try to run the code as is with this odd looking file path.
#We will get a FileNotFoundError as the file does not exist.
#We can catch this error by using a try-except block.
#The try block will try to run the code, and if it fails, the except block will run.
#The except block will catch the error and display a message to the user.
#The finally block will run regardless of whether the code in the try block fails or not.

# Example of a try-except block
# try:
#     f = open(r"/path/to/file/file.txt", "r")
#     print(f.read())
#     f.close()
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("Code has run")

#--------------------------------------------Try / Except Statement--------------------------------------------#
# The try-except statement is used to catch exceptions that occur during the execution of a program.
# The try block contains the code that may throw an exception.
# The except block contains the code that will be executed
# if an exception occurs in the try block.
# The finally block contains the code that will be executed
# regardless of whether an exception occurs in the try block or not.
# The else block contains the code that will be executed if
# no exceptions occur in the try block.

try:
    file = open(r"/path/to/file/file.txt", "r")
except FileNotFoundError:
    print("file not found")

try:
    otherFile = open(r"/path/to/other/file/otherfile.txt", "r")
except:
    print("file not found")

#catching EOFError

try:
    file = open(r"/path/to/file/file.txt", "r")
except FileNotFoundError:
    print("file not found")

#linking multiple exceptions together

try:
    file = open(r"/path/to/file/file.txt", "r")
except EOFError:
    print("input / output error")
except FileNotFoundError:
    print("file not found error")
except:
    print("some other kind of error")

#--------------------------------------------Finally Block--------------------------------------------#

# The finally block is used to execute code that should always run,
# regardless of whether an exception occurs in the try block or not.
# The finally block is executed after the try block and any except block(s).
# The finally block is useful for cleaning up resources, such as closing files or database connections.

file = None
try:
    file = open(r"C:/Users/ms_ra/GitHub/GEOG676-GIS-PROGRAMMING-SPRING25/Modules/4/sample.txt", "r")
except FileNotFoundError:
    print("file not found error")
except EOFError:
    print("input / output error")
except:
    print("some other kind of error")
finally:
    if file is not None:
        file.close()
        print("Closing file")
    