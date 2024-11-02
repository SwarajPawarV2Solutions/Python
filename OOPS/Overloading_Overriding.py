
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

# passing integer value
test_object1 = test(10)
test_object2 = test(5)

result = test_object1 + test_object2
print(result)

# passing string value
test_object1 = test('10')
test_object2 = test('5')

result = test_object1 + test_object2
print(result)



# Method Overloading

# Method Overloading can be thought as many methods with same name accepting different numbers of arguments with Same class.

# This should not be confused with polymorphism which requires different classes to have same method name and different functionalities.

# Python by default does not support method Overriding since two methods cannot have the same name in python.




#  Method Overriding

#  Method overriding is useful when we want to modify the behaviour of a methid in  subclass without changing the implementation in the superclass.

# It allows us to reuse code from the superclass while also customizing it to fit our specific needs in the subclass.

# we have already seen method overriding without explicitly mentioning it in inheritance.
