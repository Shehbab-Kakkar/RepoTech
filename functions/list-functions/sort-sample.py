#!/usr/bin/env python3.6
#list.sort(key=..., reverse=...)
# take second element for sort
def takeSecond(elem):
    return elem[2]
# random list
random = [(2, 2, 5), (3, 4, 1), (4, 1, 6), (1, 3, 0)]
# sort list with key
random.sort(key=takeSecond,reverse=True)
# print list
print('Sorted list:', random)


#First based on the function takeSecond sorting will happen as per position second of each item of the list
#[(1, 3, 0),(3, 4, 1),(2, 2, 5),(4, 1, 6)]
#Second reverse
#[(4, 1, 6),(2, 2, 5),(3, 4, 1),(1, 3, 0)]

