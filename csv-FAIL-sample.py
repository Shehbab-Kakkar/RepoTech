#!/usr/bin/python3.6
path = "/home/skakkar/text.csv"
#file = open(path)
#for line in file:
#       print(line)
#lines = [line for line in open(path)]
#print(lines[0].strip().split(','))

dataset = [line.strip().split(',') for line in open(path)]
print(dataset)

#for line in open(path):
#      dataset =  line.strip().split(',')
#      print(dataset)
 
