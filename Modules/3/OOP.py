
class Truck:
    def __init__(self, value):
        self.mpg = value

x = Truck(17) ## We are setting the MPG of x equal to 17
print(x.mpg) ## This will print 17

#--------------------------------------------------------------

class Car:
    def setColor(self, newColor):
        self.color = newColor
    def honkHorn(self):
        print("Beep beep")

chevy = Car()
chevy.setColor('red') # Method that sets a new color for the chevy instance
chevy.honkHorn() # Method that prints 'Beep beep'
#--------------------------------------------------------------

class Car:
    def setColor(self, newColor):
        self.color = newColor
    def honkHorn(self):
        print("Beep beep")

chevy = Car()
ford = Car()
if chevy == ford:
    print("TRUE")
else:
    print("FALSE")

chevy.setColor('Red')
ford.setColor('Blue')
print(chevy.color)
print(ford.color)

#--------------------------------------------------------------

class Truck:
    numOfWheels = 4 # This is an example of a class attribute; all instances of Truck have 4 wheels
    def __init__(self, color, tinted=False):
        self.color = color # This is an example of an instance attribute; only some instances will have a color attribute (that is, if it was created like so `chevy = Truck('green')`
        self.tinted = tinted # This is an example of an instance attribute

chevy = Truck('Green', True)
chevy.color = 'Green' # This is another example of an instance attribute
print(chevy.numOfWheels) # This prints our class attribute numOfWheels

#--------------------------------------------------------------

class Vehicle:
    numOfWheels = 4
    def __init__(self):
        pass

class Truck(Vehicle):
    def __init__(self):
        pass

ford = Truck()
print(ford.numOfWheels)

#--------------------------------------------------------------Encapsulation

class Atom:
    def __init__(self, atno, x, y, z):
        self.atno = atno
        self.__position = (x, y, z) #__position is private
    def getPosition(self):
        return self.__position
    def setPosition(self, x, y, z):
        self.__position = (x, y, z)
    def translate(self, x, y, z):
        x0, y0, z0 = self.__position
        self.__position = (x0 + x, y0 + y, z0 + z)

atom = Atom(14, 1, 1, 2)
atom.translate(2, 3, 8)
print(atom.getPosition())

#--------------------------------------------------------------Inhertiance

class Molecule:
    def __init__(self, name = 'Generic'):
        self.name = name
        self.atomlist = []
    def addAtom(self, atom):
        self.atomlist.append(atom)
    def __repr__(self):
        str = 'This is a molecule named %s\n' %self.name
        str = str + 'It has %d atoms\n' %len(self.atomlist)
        for atom in self.atomlist:
            str = str + f'atom: {atom}\n'
        return str

class Better_Molecule(Molecule):
    def __init__(self, name = 'Generic', basis = '6-31G**'):
        self.basis = basis
        Molecule.__init__(self, name) # Calls the constructor for the parent function
    def addBasis(self):
        self.basis = []
        for atom in self.atomlist:
            self.basis.append(atom)

newMolecule = Better_Molecule('dihydrogen monoxide', '5-18Q**')
newMolecule.addAtom('H') # Object uses method defined in Molecule instead of Better_Molecule
newMolecule.addBasis() # Object can also use methods of Better_Molecule
print(newMolecule)

#--------------------------------------------------------------Polymorphism

import math

class Shape():
    def __init__(self, color):
        self.color = color
    
    def getArea(self): # We cannot calculate area if we do not know the shape
        pass

class Rectangle(Shape):
    
    def __init__(self, color, length=None, width=None):
        super().__init__(color)
        if length is not None:
            self.l = length
        if width is not None:
            self.w = width

    def setLength(self, length):
        self.l = length

    def setWidth(self, width):
        self.w = width
    
    def getArea(self):
        return self.l * self.w

class Circle(Shape):
    
    def __init__(self, color, radius=None):
        super().__init__(color)
        if radius is not None:
            self.r = radius

    def setRadius(self, radius):
        self.r = radius
    
    def getArea(self):
        return math.pi * self.r * self.r
        

shape1 = Shape("blue")

shape2 = Rectangle("red", 3, 4)
print(shape2.getArea()) # Prints 12

shape3 = Circle("orange")
shape3.setRadius(5)
print(shape3.getArea()) # Prints 78.5398163397

shape4 = Circle("orange", 2) # Calls second constructor of circle
print(shape4.getArea()) # Prints 12.5663706144
