#!/usr/bin/python

sum  = 0
def fibonacci(a, b):
	global sum
	print a
	if a%2 == 0:
		sum += a
	if b < 4000000:
		return fibonacci(b, a+b)
	else:
		return 0


if __name__ == "__main__":
	print fibonacci(1,2)
	print "sum is ",sum
