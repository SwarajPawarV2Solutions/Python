
# Operator Overloading:

# Overloading is achived using method and operator having different functionalities with same name

# Operator overloading is achived by allowing same operator to have different meanings.

# These operators work for built-in classes. but the same operator behaves differently with different types. 


# operator overloading for + operator 

class test():
    def __init__(self,a):
        self.a = a
        
    def __add__(self,other):
        return self.a + other.a
    

#  creating objects for test

# passing integer values
test_object1 = test(10)
test_object2 = test(5)

result = test_object1 + test_object2
print(result)

# passing string values
test_object1 = test('10')
test_object2 = test('5')

result = test_object1 + test_object2
print(result)



# Method Overloading

# Method Overloading can be thought as many methods with same name accepting different numbers of arguments with Same class.

# This should not be confused with polymorphism which requires different classes to have same method name and different functionalities.

# Python by default does not support method Overriding since two methods cannot have the same name in python.


class test_a():
    
    def add(self,a,b):  # add() with 2 attributes
        self.a = a
        self.b = b
        print (self.a + self.b)
        
    def add(self,a,b,c=0):  # add() with 3 attributes and if we want to give only 2 inputs then we also added c = 0 as default value so it will not give error of test_a.add() missing 1 required positional argument: 'c'.
        self.a = a
        self.b = b
        self.c = c
        print (self.a + self.b + self.c)
        
test_object = test_a()

# calling add method
test_object.add(1,2)
test_object.add(1,2,3)

#  Method Overriding

#  Method overriding is useful when we want to modify the behaviour of a methid in  subclass without changing the implementation in the superclass.

# It allows us to reuse code from the superclass while also customizing it to fit our specific needs in the subclass.

# we have already seen method overriding without explicitly mentioning it in inheritance.
