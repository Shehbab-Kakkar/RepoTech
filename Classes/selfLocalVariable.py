#!/usr/bin/python3.6
class state:
    def district(self):
        self.name = "Punjab"
        print("Name of the state: {}".format(self.name))
        self.Nos = 22
#We are using variable 'Nos' of first function in second.
'''using self we can access it in other function'''    
    def rivers(self):
        self.number = "Five"
        print("Number of rivers are",self.number)
        print("Number of district: ",self.Nos)

punjab = state()
punjab.district()
punjab.rivers()
