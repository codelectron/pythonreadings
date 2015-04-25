#!/usr/bin/python
import sys

print("Python Integer")
print sys.maxsize

print type(sys.maxsize )
print type(sys.maxsize +1 )

a = 10
b = 20
c = -10

print type(a)
print isinstance(a, bool)
print max(a,b)
print max(a,c)
print cmp(a,b)
print abs(a)
print abs(c)

