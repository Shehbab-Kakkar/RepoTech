#!/usr/bin/python3.6
a = [1, 2]
b = [3, 4]
c = ['hello','fully']   #List
d = ('one','two')   #tuples
f = {'fully', 10}  #set
a += b   #Adding List and List
a = a + c
print(a)
a.extend(d)  # extending tuples to the list
a.extend(f)  # extending set to the list
# Output: a = [1, 2, 3, 4]
print('a = ', a)
