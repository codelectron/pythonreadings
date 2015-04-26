#!/usr/bin/python
import sys


i = 100
print i, type(i)
i = long(i)
print i, type(i)
num = sys.maxsize + 1
print num, type(num)

num = int(sys.maxsize + 1)
print num, type(num)
