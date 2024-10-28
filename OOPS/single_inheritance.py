# parent class

class car():
    def __init__(self):
        print("This is a car class and its been created")
    
    def close_doors(self):
        return "doors closed"
    
    def display(self,brand):
        self.brand = brand
        return " This is " + self.brand + " car"


# Creating Objects

my_car = car()
print(my_car.close_doors())
print(my_car.display("mercedes"))


# child / derrived class
class tesla(car):
    def __init__(self):
        pass
    
    def open_doors(self):
        return " Doors are opened vertically"
    
    def close_doors(self):
        return "Doors are Closed vertically"
    
    

my_tesla = tesla()
print(my_tesla.open_doors())
print(my_tesla.close_doors())
print(my_tesla.display("tesla"))