#!/usr/bin/python3.6
#Create a fully initialized object by using init() metho in class
class Employee:  #Employee class
      #Method,  default parameter self
      def enterEmployeeDetails(self):  #Method  
          self.name = "Mark"  # Initialize instance attribute
      #display method
      def displayEmployeeDetails(self):
          print(self.name)

employee = Employee()  #employee is an object for class Employee
employee.displayEmployeeDetails() 
          

'''
Traceback (most recent call last):
  File "./init-sample.py", line 12, in <module>
    employee.displayEmployeeDetails()
  File "./init-sample.py", line 9, in displayEmployeeDetails
    print(self.name)
AttributeError: 'Employee' object has no attribute 'name'

''' 
###############Explaination###############
# Object is unable to find instance attribute in the second method
# As initialization happened in the first method which we don't call
# Solution in init() method for initization intance attributes
'''
   def  __init__(self):
         self.name = "Mark"
'''
#  Remove first method and use this method in place of it.
#  Program init-sample2.py
##########################################
