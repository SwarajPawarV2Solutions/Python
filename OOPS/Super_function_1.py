# Super() function

# Super() function is used to access parent class methods directly inside a child class without mentioning parent class name explicitly.

# The super function is a built-in function in python. It is used to call a method of a parent class from a subclass and super function makes it easier to manage inheritance and avoid duplication of code.

# THe super function can be implemented in single inheritance and multiple inheritance as well. syntax for super function is as follows: 


# Super in single inheritance

class base_class():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        return  self.a + self.b
    
    
    
    
# child class

class child_class(base_class):
    def __init__(self,a,b,c,d):
        super().__init__(a,b) # here a and b are attributes defined in parent class init method.
        
        self.c = c
        self.d = d
        
    def sum_numbers(self):
        return  self.a + self.b + self.c + self.d
    
    
# object

c1 = child_class(1,2,3,4)
print(c1.sum_numbers())