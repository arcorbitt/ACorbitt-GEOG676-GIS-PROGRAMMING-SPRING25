#Container types are the main workers of Python programming. They hold and manage other objects.
#The Python standard library provides several container types. These data types get their name because they contain several values.
#The main container types are:
#- Lists
#- Tuples
#- Sets
#- Dictionaries
#- Strings
#- Collections

#---------------------------------------------------------Lists---------------------------------------------------------

#Lists are the most versatile and widely used data structure in Python. A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
#List elements are indexed, the first element has index [0], the second element has index [1], and so on.
#When we say that lists are ordered, it means that the items have a defined order, and that order will not change.
#Lists are changeable, meaning that we can change, add, and remove items in a list after it has been created.
#List can contain any type of data, including other lists.
#Lists can be nested and can have any length.
#Lists are very much Python's array data type.
#To add elements to our list, we simply use the append() method. This method adds an element to the end of the list.

myList = [] # Creation of a blank list

myList.append(5)
myList.append(6)
myList.append(5478919) # Adding of integers
myList.append(.057) # Adding float
myList.append("HELLO") # Adding string

print(myList) # Prints [5, 6, 5478919, 0.057, 'HELLO']
print(myList[3]) # Prints .057

myList = []
myList.append('a')
myList.append('b')
myList.append('c')
myList.append('d')
myList.append('a')
myList.append('1')
myList.append('2')
myList.append('3')
myList.append('4')

numOfa = myList.count('a') # Returns a value of 2
isEinList = 'e' in myList # Returns False as e is not in the list
isBinList = 'b' in myList # Returns True as b is in the list
indexOfA = myList.index('a') # Returns 0 as 0 is the first index with a
indexOfOne = myList.index('1') # Returns 5 as 1 is in index 5
myList.reverse() # Reverses the list
print(myList) # Prints ['4', '3', '2', '1', 'a', 'd', 'c', 'b', 'a']
myList.sort() # Sorts the list
print(myList) # Prints ['1', '2', '3', '4', 'a', 'a', 'b', 'c', 'd']

#In the example above if we wish to grab the 3rd element (i.e. 5478919), we would have to write:

myList[2] # Equal to 5478919

# myList[0] is equal to 5
# myList[1] is equal to 6



#To remove elements from our list, we use the remove() method. This method removes the first occurrence of the element we specify.
#If the element is not found, we get a ValueError.
#We can also use the pop() method to remove an element from a specific index.
#If we don't specify an index, the pop() method removes the last element.
#We can also use the del keyword to remove an element from a specific index.

myList.remove(6) # Removes the first occurrence of 6
print(myList) # Prints [5, 5478919, 0.057, 'HELLO']

myList.pop(1) # Removes the element at index 1
print(myList) # Prints [5, 0.057, 'HELLO']

del myList[0] # Removes the element at index 0
print(myList) # Prints [0.057, 'HELLO']

#We can also use the clear() method to remove all elements from a list.
#We can also use the del keyword to delete the list completely.

myList.clear() # Removes all elements from the list
print(myList) # Prints []

del myList # Deletes the list completely


