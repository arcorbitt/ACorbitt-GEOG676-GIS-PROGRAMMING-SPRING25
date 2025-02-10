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