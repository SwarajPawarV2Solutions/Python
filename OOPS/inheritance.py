# Inheritance is a process of obtaining properties and characterstics (variables and methods) of another class. In the hierarchical order,the class which inherits another class is called subclass or child class, and the other classis the parent class   

# Purpose of Inheritance 
#  OverWriting the method of parent class in a derived class

# In python there are 3 types of inheritance
#   1. Singlr Inheritance
#   2. Multiple Inheritance
#   3. Multilevel Inheritance


# Parent class
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "Some sound"

# Child class inheriting from Animal
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Woof!"

# Another child class inheriting from Animal
class Cat(Animal):
    def speak(self):
        return f"{self.name} says Meow!"

# Creating objects of Dog and Cat
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Accessing inherited method and overridden methods
print(dog.speak())  # Output: Buddy says Woof!
print(cat.speak())  # Output: Whiskers says Meow!

