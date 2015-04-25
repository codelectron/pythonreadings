#!/usr/bin/python

import random

print "This code show cases different data types in Python language"
print "Boolean type  can hold either True or False"
flag=True

# str function converts any given object to string which is required by print
print "The variable flag now holds " + str(flag)

flag = bool(random.randint(0, 1))

print "Now the fate of the flag is decided randomly "+ str(flag)
