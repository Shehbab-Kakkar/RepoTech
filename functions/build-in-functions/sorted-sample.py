#!/usr/bin/env python3.6
#https://www.programiz.com/python-programming/methods/built-in/sorted
metal = ("Iron","Calicum","Alkaline","Sodium","Floride","gold") #tuples
sorted_metal = sorted(metal)
print('Sorted List: ',sorted_metal)  #Print sorted list
print('Original List: ',metal)         # Original list
print("\n\n")
#############################

metal = ["Iron","Calicum","Alkaline","Sodium","Floride","gold"]
metal.sort(reverse=False)
print("Sort List: ",metal)   #Original  list got changed in sort()
