#!/usr/bin/env python3.6
##list.reverse()
os = ['Windows', 'macOS', 'Linux']
os.reverse()
print(os)
#Reversing of list using slicing operator
os = ['Win', 'mac','dos','job','ful', 'Linux','Hell','Mot']
print(os[::-1])
#Accessing Individual Elements in Reversed Order
#If you need to access individual elements of a list in reverse order, it's better to use reversed() method.
for i in reversed(os):
      print(i)

