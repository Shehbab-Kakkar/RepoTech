#!/usr/bin/python3.6
class Employee:
      def  employeeDetails(self):
           self.name = "Ben"
           print("Name = ",self.name)

employee = Employee()
employee.employeeDetails()   # object.Method
Employee.employeeDetails(employee)   # class.Method(object)

