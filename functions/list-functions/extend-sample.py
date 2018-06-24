#!/usr/bin/python3.6
a = [1, 2]
b = [3, 4]
c = ['hello','fully']
d = ('one','two')
f = {'fully', 10}
a += b
a = a + c
print(a)
a.extend(d)
a.extend(f)
# Output: a = [1, 2, 3, 4]
print('a = ', a)
