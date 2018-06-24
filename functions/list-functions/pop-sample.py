#!/usr/bin/python3.6
# programming language list
#https://www.programiz.com/python-programming/methods/list/pop
#pop  return value if no argument is pass then it take -1
language = ['Python', 'Java', 'C++', 'French', 'C']

# Return value from pop()
# When 3 is passed
return_value = language.pop(-3)
print('Return Value: ', return_value)

# Updated List
print('Updated List: ', language)
########################################
# programming language list
language = ['Python', 'Java', 'C++', 'Ruby', 'C']

# When index is not passed
print('When index is not passed:') 
print('Return Value: ', language.pop())
print('Updated List: ', language)

# When -1 is passed
# Pops Last Element
print('\nWhen -1 is passed:') 
print('Return Value: ', language.pop(-1))
print('Updated List: ', language)

# When -3 is passed
# Pops Third Last Element
print('\nWhen -3 is passed:') 
print('Return Value: ', language.pop(-3))
print('Updated List: ', language)
