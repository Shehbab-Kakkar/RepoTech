#!/usr/bin/python3.6
#https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists
#https://www.programiz.com/python-programming/methods/list/pop
#Yes, remove removes the first matching value, not a specific index:
a = [0, 2, 3, 2]
a.remove(2)
print("remove function",a)
#del removes the item at a specific index:
a = [3, 2, 2, 1]
del a[1]
print("del function",a)
#pop removes the item at a specific index and returns it.
a = [4, 3, 5]
a.pop(1)
print("pop function",a)


