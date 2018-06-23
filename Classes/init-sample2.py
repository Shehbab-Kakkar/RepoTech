#!/usr/bin/python3.6
#As soon as the object is invoked __init__(self) method is first being call
# Declare all your attribute in init method then your object
# is fully initialized object.
class Employee:
          def __init__(self):
              self.name = "Mark"
          def displayEmployeeDetails(self):
              print(self.name)

employee = Employee()
employee.displayEmployeeDetails()

'''
[root@node01 Classes]# ./init-sample2.py
Mark
'''
