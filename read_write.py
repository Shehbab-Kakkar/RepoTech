#!/usr/bin/python3.6
f=open("/root/Python/funny.txt")
for line in f:
    token=line.split(' ')
    print(token)
f.close()
