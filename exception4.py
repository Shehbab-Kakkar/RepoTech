#!/usr/bin/python3.6
#assert exception
def TestCase(a , b):
    assert a > b, "a is greater than b"
try:
     TestCase(2,4)
except AssertionError as e:
      print(e)
