# Multilevel inheritance

class Employee():
    def name(self):
        print("Employee Name: Swaraj")
        

class Salary(Employee):
    def sal(self):
        print("Salary of an Employee : 40000")
    
    
class Designation(Salary):
    def desig(self):
        print("The employee is working as a software Developer")
        
    
    
emp1 = Designation()
emp1.desig()
emp1.name()
emp1.sal()