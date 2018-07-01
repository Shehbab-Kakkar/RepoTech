#!/usr/bin/python3.6
#how to initialized attributes of the class at the time of instanization
#using init method. init method is used to fully initialized an object
class Employee:
#       def enterEmployeeDetails(self):
       def __init__(self,Paranthesisname):    
              self.InstanceAttributename = Paranthesisname
       def displayEmployeeDetails(self):
              print(self.InstanceAttributename)

employee01 = Employee('Shehbab')
employee02 = Employee('Lokesh')
#employee.enterEmployeeDetails()  
#AttributeError: 'Employee' object has no attribute 'name'
employee01.displayEmployeeDetails()
employee02.displayEmployeeDetails()
