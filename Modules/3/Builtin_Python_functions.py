#------------------------------------------------------------abs()------------------------------------------------------------

# abs() function returns the absolute value of a number. The argument may be an integer or a floating point number. If the argument is a complex number, its magnitude is returned.
value = -8271.18
absolute_value = abs(value)
# Prints 8271.18
print(absolute_value)

#------------------------------------------------------------bool()------------------------------------------------------------

# bool() function returns a boolean value. It returns False if the argument is False, None, 0, or an empty sequence or collection. Otherwise, it returns True.
# The following values are considered False in Python:
# False, None, 0, 0.0, 0j, '', [], (), {}, set(), range(0)
# All other values are considered True.
value = 0
boolean_value = bool(value)
# Prints False
print(boolean_value)

# Define SomeClass with an attribute hasData
class SomeClass:
    def __init__(self, hasData):
        self.hasData = hasData

# Instead of this....
x = SomeClass(True)  # Define x as an instance of SomeClass with hasData attribute
if x.hasData:
    result = True
else:
    result = False

# You can do...
result = bool(x.hasData)

#------------------------------------------------------------enumerate()------------------------------------------------------------

# enumerate() function adds a counter to an iterable and returns it as an enumerate object. This enumerate object can then be used directly in for loops or be converted into a list of tuples using list() method.
# The enumerate() function takes two parameters:
# iterable - a sequence, an iterator, or objects that supports iteration
# start (optional) - a number that specifies the start value of the counter. Default is 0
# The enumerate() function returns an enumerate object that produces a sequence of tuples, and each of the tuples is an index-value pair.
# The enumerate object can be converted into a list of tuples using list() method.
# The enumerate object can be directly used in for loops.
# The enumerate object can be used to create a dictionary containing the index-value pairs.

# Example 1: Using enumerate() in for loops
# Define a list
numbers = ['apple', 'banana', 'cherry', 'dates']
# Iterate over the list using enumerate
for index, value in enumerate(numbers):
    # Prints index and value
    print(index, value)
    
# Example 2: Using enumerate() in list comprehension
# Define a list
numbers = ['apple', 'banana', 'cherry', 'dates']
# Create a list of tuples containing index and value
result = [(index, value) for index, value in enumerate(numbers)]
# Prints [(0, 'apple'), (1, 'banana'), (2, 'cherry'), (3, 'dates')]
print(result)

# Example 3: Using enumerate() to create a dictionary
# Define a list
numbers = ['apple', 'banana', 'cherry', 'dates']
# Create a dictionary containing index-value pairs
result = dict(enumerate(numbers))
# Prints {0: 'apple', 1: 'banana', 2: 'cherry', 3: 'dates'}
print(result)

summerMonths = ["June", "July", "August", "September"]
for (index, value) in enumerate(summerMonths):
    print("Month ", value, " @ index: ", index)
# Prints
# Month  June  @ index:  0
# Month  July  @ index:  1
# Month  August  @ index:  2
# Month  September  @ index:  3

#------------------------------------------------------------eval()------------------------------------------------------------

# eval() function parses the expression argument and evaluates it as a Python expression. In simple terms, the eval() function runs the python code (which is passed as an argument) within the program.
# The eval() function takes three parameters:
# expression - the string parsed and evaluated as a Python expression
# globals (optional) - a dictionary
# locals (optional) - a mapping object. Dictionary is the standard and commonly used mapping type in Python.
# The eval() function returns the result of the evaluated expression.
# The eval() function raises an exception if the parsed expression is not a valid Python expression.
# The eval() function can also be used to execute arbitrary code objects (such as those created by compile()).
# The eval() function can also be used to execute a dynamically created Python expression.
# The eval() function can also be used to execute a dynamically created Python code object.

# Example 1: Using eval() to evaluate an expression
# Define an expression
expression = "2 + 3"
# Evaluate
result = eval(expression)
# Prints 5
print(result)

# Example 2: Using eval() to evaluate an expression with variables
# Define variables
a = 2
b = 3
# Define an expression
expression = "a + b"
# Evaluate
result = eval(expression)
# Prints 5
print(result)

# Example 3: Using eval() to evaluate an expression with dictionary
# Define a dictionary
variables = {'a': 2, 'b': 3}
# Define an expression
expression = "a + b"
# Evaluate
result = eval
(expression, None, variables)
# Prints 5
print(result)

# Example 4: Using eval() to evaluate an expression with dictionary and locals
# Define a dictionary
variables = {'a': 2, 'b': 3}
# Define a mapping object
mapping = {}
# Define an expression
expression = "a + b"
# Evaluate
result = eval(expression, mapping, variables)
# Prints 5
print(result)

# Example 5: Using eval() to execute a dynamically created Python expression
# Define a dictionary
variables = {'a': 2, 'b': 3}
# Define an expression
expression = "a + b"
# Evaluate
result = eval
(expression, None, variables)
# Prints 5
print(result)

# Example 6: Using eval() to execute a dynamically created Python code object
# Define a dictionary
variables = {'a': 2, 'b': 3}
# Define an expression
expression = "a + b"
# Compile the expression
code = compile(expression, '<string>', 'eval')
# Evaluate
result = eval
(code, None, variables)
# Prints 5
print(result)

i = 4
result = eval('i + 1')
print(result)
# Prints 5
print(eval('i + 1'))
# Prints 5

#------------------------------------------------------------float()------------------------------------------------------------

# float() function returns a floating point number constructed from a number or a string. If no argument is passed, it returns 0.0.
# The float() function can convert integers, strings, or bytes to floating-point numbers.
# The float() function returns 0.0 if no argument is passed.
# The float() function can also convert a string or bytes to a floating-point number.
# The float() function can also convert a string with scientific notation to a floating-point number.
# The float() function can also convert a string with a percentage to a floating-point number.
# The float() function can also convert a string with a currency symbol to a floating-point number.
# The float() function can also convert a string with a comma to a floating-point number.

# Example 1: Using float() to convert an integer to a floating-point number
# Define an integer
number = 10
# Convert to float
result = float(number)
# Prints 10.0
print(result)

# Example 2: Using float() to convert a string to a floating-point number
# Define a string
number = "10"
# Convert to float
result = float(number)
# Prints 10.0
print(result)

# Example 3: Using float() to convert a string with scientific notation to a floating-point number
# Define a string with scientific notation
number = "1.5e2"
# Convert to float
result = float(number)
# Prints 150.0
print(result)

# Example 4: Using float() to convert a string with a percentage to a floating-point number
# Define a string with a percentage
number = "50%"
# Convert to float
result = float(number.strip('%')) / 100
# Prints 0.5
print(result)

# Example 5: Using float() to convert a string with a currency symbol to a floating-point number
# Define a string with a currency symbol
number = "$100"
# Convert to float
result = float(number.strip('$'))
# Prints 100.0
print(result)

# Example 6: Using float() to convert a string with a comma to a floating-point number
# Define a string with a comma
number = "1,000"
# Convert to float
result = float(number.replace(',', ''))
# Prints 1000.0
print(result)

# Example 7: Using float() to convert a string with a comma and a currency symbol to a floating-point number
four = '4.6' # You cannot do math to this value
float_val = float(four) 
print(float_val + 5)
# Prints 9.6

#------------------------------------------------------------hasattr()------------------------------------------------------------

# hasattr() function returns True if the object has the given named attribute and False if it does not.
# The hasattr() function takes two parameters:
# object - object whose named attribute is to be checked
# name - name of the attribute to be searched
# The hasattr() function returns True if the object has the given named attribute and False if it does not.
# The hasattr() function can be used to check if an object has a specific attribute or not.
# The hasattr() function can be used to check if an object has a specific method or not.
# The hasattr() function can be used to check if an object has a specific property or not.

# Example 1: Using hasattr() to check if an object has a specific attribute
# Define a class
class Person:
    name = "John"
    age = 23
    country = "USA"
# Create an object of the class
person = Person()
# Check if the object has the attribute name
result = hasattr(person, 'name')
# Prints True
print(result)

# Example 2: Using hasattr() to check if an object has a specific method
# Define a class
class Person:
    def greet(self):
        return "Hello"
# Create an object of the class
person = Person()
# Check if the object has the method greet
result = hasattr(person, 'greet')
# Prints True
print(result)

# Example 3: Using hasattr() to check if an object has a specific property
# Define a
class Person:
    @property
    def age(self):
        return 23
# Create an object of the class
person = Person()
# Check if the object has the property age
result = hasattr(person, 'age')
# Prints True
print(result)

# Example 4: Using hasattr() to check if an object has a specific attribute
# Define a class
class Person:
    name = "John"
    age = 23
    country = "USA"
# Create an object of the class
person = Person()
# Check if the object has the attribute name
result = hasattr(person, 'name')
# Prints True
print(result)

# Example 5: Using hasattr() to check if an object has a specific method
# Define a class
class Person:
    def greet(self):
        return "Hello"
# Create an object of the class
person = Person()
# Check if the object has the method greet
result = hasattr(person, 'greet')
# Prints True
print(result)

# Example 6: Using hasattr() to check if an object has a specific property
# Define a class
class Person:
    @property
    def age(self):
        return 23
# Create an object of the class
person = Person()
# Check if the object has the property age
result = hasattr(person, 'age')
# Prints True
print(result)

# Example 7: Using hasattr() to check if an object has a specific attribute
# Define a class
class Person:
    name = "John"
    age = 23
    country = "USA"
# Create an object of the class
person = Person()
# Check if the object has the attribute name
result = hasattr(person, 'name')
# Prints True
print(result)

# Example 8: Using hasattr() to check if an object has a specific method
# Define a
class Person:
    def greet(self):
        return "Hello"
# Create an object of the class
person = Person()
# Check if the object has the method greet
result = hasattr(person, 'greet')
# Prints True
print(result)

class Vehicle():
    def __init__(self):
        self.color = 'Red'
myCar = Vehicle()
hasColor = hasattr(myCar, 'color')
hasMpg = hasattr(myCar, 'mpg')
print(hasColor) # Prints True
print(hasMpg) # Prints False

#------------------------------------------------------------getattr()------------------------------------------------------------

# getattr() function returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.
# The getattr() function takes three parameters:
# object - object whose named attribute is to be accessed
# name - name of the attribute to be accessed
# default (optional) - value that is returned when the named attribute is not found
# The getattr() function returns the value of the named attribute of an object. If not found, it returns the default value provided to the function.
# The getattr() function can be used to access the value of a specific attribute of an object.
# The getattr() function can be used to access the value of a specific method of an object.
# The getattr() function can be used to access the value of a specific property of an object.

# Example 1: Using getattr() to access the value of a specific attribute
# Define a
class Person:
    name = "John"
    age = 23
    country = "USA"
# Create an object of the class
person = Person()
# Access the value of the attribute name
result = getattr(person, 'name')
# Prints John
print(result)

# Example 2: Using getattr() to access the value of a specific method
# Define a class
class Person:
    def greet(self):
        return "Hello"
# Create an object of the class
person = Person()
# Access the value of the method greet
result = getattr(person, 'greet')
# Prints <bound method Person.greet of <__main__.Person object at 0x0000020E2A2C3F70>>
print(result)

# Example 3: Using getattr() to access the value of a specific property
# Define a class
class Person:
    @property
    def age(self):
        return 23
# Create an object of the class
person = Person()
# Access the value of the property age
result = getattr(person, 'age')
# Prints 23
print(result)

# Example 4: Using getattr() to access the value of a specific attribute
# Define a class
class Person:
    name = "John"
    age = 23
    country = "USA"
# Create an object of the class
person = Person()
# Access the value of the attribute name
result = getattr(person, 'name')
# Prints John
print(result)

# Example 5: Using getattr() to access the value of a specific method
# Define a class
class Person:
    def greet(self):
        return "Hello"
# Create an object of the class
person = Person()
# Access the value of the method greet
result = getattr(person, 'greet')
# Prints <bound method Person.greet of <__main__.Person object at 0x0000020E2A2C3F70>>
print(result)

# Example 6: Using getattr() to access the value of a specific property
# Define a class
class Person:
    @property
    def age(self):
        return 23
# Create an object of the class
person = Person()
# Access the value of the property age
result = getattr(person, 'age')
# Prints 23
print(result)

class Vehicle():
    def __init__(self):
        self.color = 'Red'
myCar = Vehicle()
# These two lines are equal
color1 = getattr(myCar, 'color')
print(color1) # Prints Red
color2 = myCar.color
print(color2) # Prints Red

#------------------------------------------------------------input()------------------------------------------------------------

# input() function reads a line from input, converts it into a string and returns it.
# The input() function takes a single parameter:
# prompt (optional) - a string that is written to standard output (usually screen) without a trailing newline
# The input() function reads a line from input, converts it into a string and returns it.
# The input() function can be used to take input from the user.
# The input() function reads the input as a string.
# The input() function can be used to read input from the user and convert it into an integer.
# The input() function can be used to read input from the user and convert it into a floating-point number.

# Example 1: Using input() to take input from the user
# Take input from the user
name = input("Enter your name: ")
# Prints the input
print(name)

# Example 2: Using input() to take input from the user and convert it into an integer
# Take input from the user
age = int(input("Enter your age: "))
# Prints the input
print(age)

# Example 3: Using input() to take input from the user and convert it into a floating-point number
# Take input from the user
salary = float(input("Enter your salary: "))
# Prints the input
print(salary)

# Example 4: Using input() to take input from the user
# Take input from the user
name = input("Enter your name: ")
# Prints the input
print(name)

# Example 5: Using input() to take input from the user and convert it into an integer
# Take input from the user
age = int(input("Enter your age: "))
# Prints the input
print(age)

# Example 6: Using input() to take input from the user and convert it into a floating-point number
# Take input from the user
salary = float(input("Enter your salary: "))
# Prints the input
print(salary)

userInput = input("What is your name? ")
print("The user's name is ", userInput)
# Prints whatever you input

#------------------------------------------------------------int()------------------------------------------------------------

# int() function converts a number or a string to an integer. If no arguments are given, it returns 0.
# The int() function can convert a floating-point number or a string to an integer.
# The int() function returns 0 if no arguments are given.
# The int() function can convert a string with a specific base to an integer.

# Example 1: Using int() to convert a floating-point number to an integer
# Define a floating-point number
number = 10.5
# Convert to int
result = int(number)
# Prints 10
print(result)

# Example 2: Using int() to convert a string to an integer
# Define a string
number = "10"
# Convert to int
result = int(number)

# Example 3: Using int() to convert a string with a specific base to an integer
# Define a string with a specific base
number = "10"
# Convert to int
result = int(number, 2)
# Prints 2
print(result)

# Example 4: Using int() to convert a floating-point number to an integer
# Define a floating-point number
number = 10.5
# Convert to int
result = int(number)
# Prints 10
print(result)

x = .18467
y = 3.141592
print("x - ", int(x)) # Prints x - 0
print("y - ", int(y)) # Prints y - 3
