# Defining a class
class Dog:
    # Constructor method to initialize attributes
    def __init__(self, name, breed):
        self.name = name  # attribute for the dog's name
        self.breed = breed  # attribute for the dog's breed

    # Method to display dog info
    def bark(self):
        return f"{self.name} says Woof!"

# Creating objects (instances) of the Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog2 = Dog("Max", "Bulldog")

# Accessing attributes
print(f"{dog1.name} is a {dog1.breed}.")  # Output: Buddy is a Golden Retriever.
print(f"{dog2.name} is a {dog2.breed}.")  # Output: Max is a Bulldog.

# Calling methods
print(dog1.bark())  # Output: Buddy says Woof!
print(dog2.bark())  # Output: Max says Woof!



