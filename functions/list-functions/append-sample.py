#!/usr/bin/python3.6
#The append() method takes a single item and adds it to the end of the list.
#The item can be numbers, strings, another list, dictionary etc.
# animal list
animal = ['cat', 'dog', 'rabbit']  
wild_animal = ['tiger', 'fox']
dict = {'Name':'Motu','number':432425}
# an element is added
animal.append('guinea pig') #String
animal.append(wild_animal) # append list
animal.append(dict) # append dictionary
#Updated Animal List
print('Updated animal list: ', animal)
