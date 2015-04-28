#!/usr/bin/python
import os

print "With - Compound statement"
fileName = os.getcwd()+"/"+__file__
print fileName

with open(fileName, "r") as f:
	print f.readlines()
	print "\n"
	f.seek(0)
	print "\n"
	print f.readlines()
