#!/usr/bin/python3.6
class Employee:
          def __init__(self,name):
              self.name = name
          def displayEmployeeDetails(self):
              print(self.name)

employee = Employee("Shehbab")      #Object one
employeeTwo = Employee("Kakkar")    #Object second
employee.displayEmployeeDetails()
employeeTwo.displayEmployeeDetails()

#self.name = name
#Here self.name is referring to instance attribute name
#'name'  refers to value passing the Parentheses

'''
[root@node01 Classes]# ./init-sample3.py
Shehbab
Kakkar

'''
