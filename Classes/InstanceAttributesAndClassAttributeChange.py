#!/usr/bin/python3.6
class School:
    numberOfstudents = 2000
    
school01 = School()
school02 = School()

print(school01.numberOfstudents)
print(school02.numberOfstudents)

School.numberOfstudents = 1000
print(school01.numberOfstudents)
print(school02.numberOfstudents)

#Object is an instance of a class
#now we are going to create instance AttributeError

school01.name = "DC Model Sr. Sce. schoool"
school02.name = "Convent School"
print(school01.name)
print(school02.name)
