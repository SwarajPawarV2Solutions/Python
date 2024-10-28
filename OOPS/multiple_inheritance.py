# parent class

class Geometry():
    
    def __init__(self):
        pass
    
    def area(self,radious):
        self.radious = radious
        return  3.14 * self.radious ** 2

# creating Object
my_circle = Geometry()
print(my_circle.area(5))


# Child class of Geometry

class square (Geometry):
    def __init__(self):
        pass
    
    def area(self,side_value):
        self.side = side_value
        return self.side ** 2
    
    def info(self):
        return "This is a square class"
    

# Creating object of my_square
my_square = square()
print(my_square.area(5))


# Parent class
class ArithmaticOperations():
    def __init__(self):
        print("This is a parent class")
        
    def square(self,number):
        self.number = number
        return self.number ** 2
    
    
# creating object 

square_of_num = ArithmaticOperations()
print(square_of_num.square(10))

# Child class of ArithmaticOperation

class cube(ArithmaticOperations):
    def __init__(self,num_value):
        self.num = num_value
        
    def cube_of_number(self):
        return self.num ** 3
    

# Creating Object of cube

cube_of_num = cube(2)
print(cube_of_num.cube_of_number())



# Multiple inheritance 

# derrived class

class test(Geometry,ArithmaticOperations):
    def __init__(self):
        print("Trying to inherit multiple classes at once.")
        
    def info(self):
        print("This is just to test if multiple inheritence works")
        
    def area(self,number_value):
        self.number = number_value
        return number_value ** 2
    
my_test = test()
my_test.info()
print(my_test.area(2))
print(my_test.square(5))