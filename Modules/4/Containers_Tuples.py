#Tuples are those variables that look like they are lists, but use parenthesis instead of square brackets.
#Unlike lists, tuples are immutable and once they've been set you cannot add or remove values. 
#Tuples are faster than lists and are used when you want to protect data from being changed.
#Tuples are defined by the use of parenthesis.
#Tuples can contain any type of data, including other tuples.
#Tuples are rather simple in that you can pretty much only do two things: count and index.
#There are NO append()-esque methods for tuples.

myTuple = ('a', 'b', 'c', 'a') 
tuples = myTuple.count('a') # Returns a value of 2
indexOfB = myTuple.index('b') # Returns a value of 1
print(tuples) # Prints 2

#The above code will print 2 as there are two 'a's in the tuple. The index of 'b' is 1 as it is the second element in the tuple.
#The following code will throw an error as tuples are immutable and we cannot change the value of the tuple:

# myTuple[0] = 'd' # Throws an error

#The above code will throw an error as tuples are immutable and we cannot change the value of the tuple.
#The following code will throw an error as tuples are immutable and we cannot remove values from the tuple:

# myTuple.remove('a') # Throws an error

#The above code will throw an error as tuples are immutable and we cannot remove values from the tuple.
#The following code will throw an error as tuples are immutable and we cannot add values to the tuple:

# myTuple.append('d') # Throws an error

#The above code will throw an error as tuples are immutable and we cannot add values to the tuple.
#The following code will throw an error as tuples are immutable and we cannot sort the tuple:

# myTuple.sort() # Throws an error

#The above code will throw an error as tuples are immutable and we cannot sort the tuple.
#The following code will throw an error as tuples are immutable and we cannot reverse the tuple:

# myTuple.reverse() # Throws an error

#The above code will throw an error as tuples are immutable and we cannot reverse the tuple.
#The following code will throw an error as tuples are immutable and we cannot pop the tuple:

# myTuple.pop() # Throws an error

#The above code will throw an error as tuples are immutable and we cannot pop the tuple.
#The following code will throw an error as tuples are immutable and we cannot clear the tuple:

# myTuple.clear() # Throws an error

#The above code will throw an error as tuples are immutable and we cannot clear the tuple.
