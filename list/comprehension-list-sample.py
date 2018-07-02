#!/usr/bin/python3.6
l1 = ['e','f','g','s']
l2 = ['H','T','f','d']
#for a,b in list(zip(l1,l2)):
#     print(a,b)
#print([a+b for a,b in list(zip(l1,l2)])
#c = [i+j for i,j in zip(l1,l2)]
print([i+j for i,j in zip(l1,l2)])

a = [1,2,3,4,5]
b = [6,7,8,9,10]
c = [i+j for i,j in zip(a,b)] 
print(c)

numbers = [1, 2, 3]
letters = ["A", "B", "C"]
print([str(numbers)+letters for numbers,letters in zip(numbers,letters)])
'''
['eH', 'fT', 'gf', 'sd']
[7, 9, 11, 13, 15]
['1A', '2B', '3C']
'''
