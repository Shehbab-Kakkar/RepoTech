#!/usr/bin/python3.6
#how to initialized attributes of the class at the time of instanization
#using init method. init method is used to fully initialized an object
class Employee:
#       def enterEmployeeDetails(self):
       def __init__(self):    
              self.name = "Mohit"
       def displayEmployeeDetails(self):
              print(self.name)

employee = Employee()
#employee.enterEmployeeDetails()  
#AttributeError: 'Employee' object has no attribute 'name'
employee.displayEmployeeDetails()
