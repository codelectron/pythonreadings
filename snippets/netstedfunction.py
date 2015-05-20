#!/usr/bin/python

print("Nested function")
def nest(n):
	def egg(n):
		return n*2
	return egg(n)

print nest(2)
print egg(2)
