#Sets are like lists, but can NOT contain duplicate values; sets also use curly brackets instead of square brackets.
#Sets are funny in that when we create an empty set we need to use set() instead of using two curly brackets like one may think.
#Yet we can create an non-empty set using curly brackets.
#Sets are unordered, changeable, and indexed.
#Sets can contain any type of data, including other sets.
#Sets can be nested and can have any length.
#Like lists, we can add to sets using add() to add a new value to the set.
#If we want to add many values to our set, we use the update() method in order to add them.
#All duplicates will be removed from the set. Without warning.

# mySet = {} Cannot create empty set like this
# mySet = {'a', 'b'} But you can create non-empty set like this
mySet = set()
mySet.add(1)
mySet.add(2)
print(mySet) # Prints {1, 2}
mySet.add(1)
print(mySet) # Still prints {1, 2}
otherSet = {5, 6, 7}
mySet.update(otherSet) # Adds {5, 6, 7} to the contents of mySet
print(mySet) # Prints {1, 2, 5, 6, 7}

#To remove elements from our set, we use the remove() method. This method removes the element we specify.
#If the element is not found, we get a KeyError.
#We can also use the discard() method to remove an element from a specific index.
#If the element is not found, nothing happens.
#We can also use the pop() method to remove an element from the set.
#This will remove the last element of the set.
#If the set is empty, a KeyError is thrown.

mySet = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
mySet.discard('a')
mySet.remove('b')
mySet.pop()
print(mySet) # Prints {'c', 'd', 'e', 'f'}

#We can use the union() method to create a new set composed of the values of two sets.
#The union() method returns a new set with all the values from both sets.
#The union() method will remove any duplicates.
#The update() method will also combine two sets, but will not remove duplicates.
#The update() method will add the values of one set to another set.
#The intersection() method will return a new set with only the values that are in both sets.
#The intersection() method will return a new set with only the values that are in both sets.
#The difference() method will return a new set with only the values that are in the first set, but not the second.

mySet = {'a', 'b', 'c', 'd', 'e', 'f', 'g'}
otherSet = {'z', 'y', 'x', 'w', 'v', 'u', 'b', 'a'}

union = mySet.union(otherSet)
intersection = mySet.intersection(otherSet)
difference = mySet.difference(otherSet)

print(union) # Prints {'c', 'v', 'd', 'w', 'z', 'u', 'y', 'x', 'a', 'b', 'f', 'g', 'e'}
print(intersection) # Prints {'a', 'b'}
print(difference) # Prints {'c', 'd', 'f', 'g', 'e'}
