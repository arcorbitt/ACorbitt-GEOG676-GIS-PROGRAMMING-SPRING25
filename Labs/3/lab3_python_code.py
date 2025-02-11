#TAMU GIS Programming: Homework 3
#Topic: Fun with object oriented programming 100pts

#----------------------Outcomes----------------------------
#1. Learn how to open, read from, and write to a text file using python
#2. Learn how to create classes and objects in python
#3. Learn some of the built-in functions in python
#4. Go over the basics of Object Oriented Programming (OOP)

#----------------------Task --------------------------------

#1. Read data in from the provided text file found here (20pt)
#2. Create a class for each shape found in the text file (20pt)
#3. For each line, create a new object determined by the shape (e.g. Triangle object for line Triangle,8,1 base and height) (30pt)
#4. Iterate through your list and print out the area for each shape (30pt)

#----------------------Hand In-------------------------------

#1. Link to your GitHub Repository that contains the Python code
#2. Screenshot of the Executed Code Printout
#------------------------------------------------------------------------------------------------------------

#----------------------Creating Classes----------------------------

class Shape():
    def __init__(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.length = l
        self.width = w
    def getArea(self):
        return self.length * self.width
    
class Circle(Shape):
    def __init__(self, r):
        self.radius = r
    def getArea(self):
        return 3.14159 * self.radius**2   #could also use self.radius * self.radius
    
class Triangle(Shape):
    def __init__(self, b, h):
        self.base = b
        self.height = h
    def getArea(self):
        return 0.5 * self.base * self.height
    
#----------------------Read Text File----------------------------

with open('Shape.txt', 'r') as file: #open the file in read mode
    lines = file.readlines() #read all lines in the file

for line in lines:
    components = line.split(',') #split the line by comma
    shape = components[0] #get the shape name, first element in the list is always 0
    
    if shape == 'Rectangle':
        rect = Rectangle(int(components[1]), int(components[2])) #create a new Rectangle object
        print('Area of Rectangle is:', rect.getArea()) #print the area of the rectangle
    elif shape == 'Circle':
        cirl = Circle(int(components[1])) #create a new Circle object
        print('Area of Circle is:', cirl.getArea()) #print the area of the circle
    elif shape == 'Triangle':
        tri = Triangle(int(components[1]), int(components[2])) #create a new Triangle object
        print('Area of Triangle is:', tri.getArea())
    else:
        pass