#-----------------------------------------------------------Building an iterator-----------------------------------------------------------
# An iterator is an object that can be iterated upon, meaning that you can traverse through all the values. Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().
# Write a class that generates the first n triangular numbers. A triangular number is a number obtained by the continued summation of natural numbers.
# e.g.
# 1, 3, 6, 10, 15, ...
# So, the nth term of the series is n*(n+1)/2
# For example, the first five triangular numbers are 1, 3, 6, 10, 15.
# Your task is to write an iterator, TriangularNums(n), which returns the first n triangular numbers.
# The class should have the following methods:
# __init__(self, n): A constructor that takes the number of terms n as input.
# __iter__(self): This method should return self.
# __next__(self): This method should return the next triangular number. If the number of terms exceeds n, it should raise a StopIteration exception.
# For example, for n = 5, the output should be:
# 1
# 3
# 6
# 10
# 15


class TriangularNums:
    # Calculate triangular numbers with x = t(t+1)/2
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        self.t = 1
        return self

    def __next__(self):
        if self.t > n:
            raise StopIteration

        x = self.t * (self.t + 1) / 2
        self.t += 1

        return int(x)
                               
n = int(input("Enter the nth term: "))
for x in TriangularNums(n):
    print(x)

#-----------------------------------------------------------List Comprehension-----------------------------------------------------------

# List comprehension is an elegant way to define and create lists based on existing lists.
# List comprehension is generally more compact and faster than normal functions and loops for creating list.
# However, we should avoid writing very long list comprehensions in one line to ensure that code is user-friendly.
# Remember, every list comprehension can be rewritten in for loop, but every for loop can’t be rewritten in the form of list comprehension.
# List comprehension is an example of functional programming.
# You can use list comprehension to create lists based on existing lists.
# The general syntax is:
# [expression for item in iterable if condition == True]
# For example, to create a list of squares of numbers from 0 to 9, you can use:
# squares = [x**2 for x in range(10)]
# This will create a list of squares of numbers from 0 to 9.
# You can also use list comprehension to filter elements from a list.
# For example, to create a list of even numbers from 0 to 9, you can use:
# evens = [x for x in range(10) if x % 2 == 0]
# This will create a list of even numbers from 0 to 9.
# You can also use list comprehension to create a list of tuples.
# For example, to create a list of tuples where each tuple is a pair of numbers and their squares, you can use:
# pairs = [(x, x**2) for x in range(10)]
# This will create a list of tuples where each tuple is a pair of numbers and their squares.
# You can also use list comprehension to create a list of dictionaries.
# For example, to create a list of dictionaries where each dictionary is a mapping of numbers to their squares, you can use:
# squares = {x: x**2 for x in range(10)}
# This will create a list of dictionaries where each dictionary is a mapping of numbers to their squares.
# You can also use list comprehension to create a list of sets.
# For example, to create a list of sets where each set is a set of numbers, you can use:
# sets = [{x, x**2} for x in range(10)]
# This will create a list of sets where each set is a set of numbers.
# You can also use list comprehension to create a list of strings.
# For example, to create a list of strings where each string is a string representation of a number, you can use:
# strings = [str(x) for x in range(10)]
# This will create a list of strings where each string is a string representation of a number.

numbers = [1, 2, 3, 4, 5, 6]
raisedNums = [x ** 3 for x in numbers] # List comprehension
print(raisedNums) # Prints [1, 8, 27, 64, 125, 216]

numbers = [1, 2, 3, 4, 5, 6]
raisedNums = [x ** 3 for x in numbers if x % 2 == 0]
print(raisedNums) # Prints [1, 8, 27, 64, 125, 216]