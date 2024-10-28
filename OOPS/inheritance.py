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
