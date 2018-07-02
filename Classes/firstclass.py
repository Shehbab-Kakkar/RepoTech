#!/usr/bin/python3.6
#Check if an employee has achieved his weekly target or not
class Employee:            
         name = "Mohit"            #Attributes
         designation = "Sales Executive"
         salesMadeThisWeek = 6
         
         def hasAchievedTarget(self):   #self to access Attributes of class
                 if self.salesMadeThisWeek >=5:
                       print("Target has been achieved")
                 else:
                       print("Target not achieved")

employeeOne = Employee()     #object
print("Employee name is %s" % (employeeOne.name))
employeeOne.hasAchievedTarget()





