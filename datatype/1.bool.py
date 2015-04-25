#!/usr/bin/python

import random

print "This code show cases different data types in Python language"
print "Boolean type  can hold either True or False"
flag=True

# str function converts any given object to string which is required by print
print "The variable flag now holds " + str(flag)

flag = bool(random.randint(0, 1))

print "Now the fate of the flag is decided randomly "+ str(flag)

print "Some Boolean operations"
print "using not operater"
print flag, not flag
print "And the output of \" flag is not (not flag) \""
print flag is not (not flag)
print "And the output of \" not flag is flag \""
print not flag is flag
print "Also let me try to see what happens if I apply arithmetics on boolean"
print "multiply flag with flag"
print flag*flag

print "divide flag with flag"
print flag*flag

print "Add flag with flag"
print flag+flag

print "Subtract flag with flag"
print flag-flag

print bool(0+0j)
