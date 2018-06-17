#!/usr/bin/python3.6
try:
    a=5/0
    print(a)
except Exception as f:#Any exeception
    print(f)

##############
try:
   n = int(input("Enter an Integer: "))
   print(n)
except ValueError: # Value special exception
    print("Not an Integer")

  
