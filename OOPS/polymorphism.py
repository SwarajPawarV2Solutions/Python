# Polymorphism

# Types of Polymorphism
#   1. Operator Polymorphism
#   2. Function Polymorphism
#   3. class and method polymorphism


class Book():
    def __init__(self,name,pages):
        self.name = name
        self.pages = pages
        
    def length(self):
        return "The book " + self.name + ' is of '+ str(self.pages) + ' pages.'
    
    
    
class movie():
    def __init__(self,name,duration):
        self.name = name
        self.duration = duration
        
    def length(self):
        return "The movie " + self.name + ' is of '+ str(self.duration) + ' hours.'
    
    
# book Object 
book1 = Book('python',800)
print(book1.length())

# Movie Object
movie1 = movie("Abcd",3)
print(movie1.length())
    