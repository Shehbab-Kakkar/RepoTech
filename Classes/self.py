#!/usr/bin/python3.6
class Company:
      def employee(self):  '''self is reference to object itself'''
           pass
     
company01 = Company()
company01.employee()  #Actually mentioned below

#Class.function(object)
'''
Class = Company
function = employee
object = company

Company.employee(company01)
'''

Company.employee(company01)
