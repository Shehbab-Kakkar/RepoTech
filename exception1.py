#!/usr/bin/python3.6
#Multiple execeptions

try:
  sum = 0
  file = open('number.txt','r')
  for number in file:
      sum = sum + 1.0/int(number)
  print(sum)

except FileNotFoundError:
    print("number.txt file not exists")
except ValueError:
    print("Number should in integers")
except ZeroDivisionError:
    print("Number is in file equal to Zero!")
except IOError:
    print("File not exists")
finally :
    print("Sum = %f " % sum)
    #file.close()
