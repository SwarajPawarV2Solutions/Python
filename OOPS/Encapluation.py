# Encapluation

# The proceess of wrapping up variables and methods into a singleentityis known as Encapluation. It acts as a proactive shield that puts restrictions on accessing variables and method directly. and can prevent accidental or unauthorized modification of data.

# Access modifiers limit accessto the variables and functions of a class python uses three types of access modifiers; they are - private,public and protected.

#   1. public : accessible and modifiable outside class 
#   2. private : not easily accessibleand modifiable outside class
#   3. protected : objectscan be accesssible but can be made not modifiable outside class



# creating class
class Car():
    my_car = "Tesla" # class attribute
    
    def __init__(self):
        pass
    
    def info(self):
        return "This is my " + self.my_car
    
    
# creating Objects
my_car = Car()
print(my_car.info())
# print(my_car.my_car())


class person():
    
    phone_number = "111-222-333"    # public class attribute
    __country = "India"             # private class attribute
    
    def __init__(self,age,__name):
        self.age = age              # Public instance/ object attribute
        self.__name = __name        # private instance
        
    
    def general_info(self):
        return "My name is " + self.__name + " and my age is " + str(self.age)  # Public method
    
    
    def __residence(self):
        return "My name is " + self.__name + " and I am from " + self.__country # Private method
        

# creating objects

person1 = person(24, "Swaraj")
print(person1.general_info())
#print(person1.__residence())  # private method
print(person1.phone_number)


# Imp
# to access private methods in python we have a concept called name mangeling.

print(person1._person__country)
print(person1._person__residence())





# protected Attributes
# In protected class the variables and methods are mofifiable.

class Person ():
    
    _country  = "India"   # protected classs attribute
    
    def __init__(self,name_of):
        self.name = name_of
        
    #@property  
    def name(self):
        return self.name
    
    
p1 = Person("Mercedes Benz")
print(p1._country)
p1._country = "USA"
print(p1._country)

p2 = Person("Swaraj")
print(p2.name)