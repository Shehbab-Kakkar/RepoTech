#!/usr/bin/env python3.6
list = [("Name",34,"Number"),("Mohit",23,42347),("Ram",43,97684),("Chandan",12,14344),("Sita",67,67889)]
RollNumber = lambda list: list[1]
list.sort(key=RollNumber,reverse=True)
for list in list:
      print(list)
#for i in list[::]:
#    print(i)

#First sort on the basis of second position in the list.
#[("Chandan",12,14344),("Mohit",23,42347),("Name",34,"Number"),("Ram",43,97684),("Sita",67,67889)]
#reverse
#[("Sita",67,67889),("Ram",43,97684),("Name",34,"Number"),("Mohit",23,42347),("Chandan",12,14344)]
"""
('Sita', 67, 67889)
('Ram', 43, 97684)
('Name', 34, 'Number')
('Mohit', 23, 42347)
('Chandan', 12, 14344)

"""
