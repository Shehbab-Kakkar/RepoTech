#!/usr/bin/python3.6
class Employee:
      def  employeeDetails(self):
           self.name = "Ben"
           print("Name = ",self.name)
      
      @staticmethod  #declarator
      def welcomeMessage():
           print("Welcome to our organization!")
employee = Employee()
employee.employeeDetails()   # object.Method
Employee.employeeDetails(employee)   # class.Method(object)
employee.welcomeMessage()


#declarator called statemethod
#declarator are function which extend another function funcationlity
'''staticmethod  ignore the binding of object'''
#statemethod ignore self parameter 

#####################################
'''static method  |   instance method '''

#@staticmethod        #def employeeDetails(self)

#####################################
