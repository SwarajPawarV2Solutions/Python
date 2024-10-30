
# Super in Multiple inheritance

class base_class1():
    def __init__(self):
        pass
    def add(self,a,b):
        self.a = a
        self.b = b
        return  self.a + self.b
    
    
    
    
# child class

class base_class2():
    def __init__(self):
        pass
    def multiply(self,x,y):
        self.x = x
        self.y = y
        
    def sum_numbers(self):
        print(self.x * self.y)
    

class child_class(base_class1,base_class2):
    def __init__(self,c,d):
        self.c = c
        self.d = d
        
    def sum_numbers(self,a,b,x,y):
        super().add(a,b) # no need to specify which base class
        super().multiply(x,y)
        return self.c + self.d


# creating child class object

c = child_class(5,6)
print(c.sum_numbers(1,2,3,4))