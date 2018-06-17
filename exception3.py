#!/usr/bin/python3.6
a = 1
def RaiseException(a):
    if type(a) != type('a'):
         raise ValueError("This is not String")
try:
    RaiseException(a)
except ValueError as e:
    print(e)
       
