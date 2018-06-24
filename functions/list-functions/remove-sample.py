#!/usr/bin/python3.6
# If a list contains duplicate elements
# the remove() method removes only the first instance

# animal list
animal = ['cat', 'dog', 'dog', 'guinea pig', 'dog']

# 'dog' element is removed
animal.remove('dog')  #While remove only one element
animal.remove('got')  #Element not in the list

#Updated Animal List
print('Updated animal list: ', animal)


