#!/usr/bin/python3.6
#https://stackoverflow.com/questions/7961363/removing-duplicates-in-lists
myList = [1, 2, 3, 1, 2, 5, 6, 7, 8]
cleanlist = []
[cleanlist.append(x) for x in myList if x not in cleanlist]
print(cleanlist)
