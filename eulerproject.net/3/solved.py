#!/usr/bin/python
import sys

number = 600851475143

def myrange(max, min):
	a = min 
	while a < max:
		a += 1
		yield a

def generatePrime(max):
	list1 = myrange(max, 2)
	for i in list1:
		list2 = myrange(i - 1, 2)
		for k in list2:
			if i%k == 0:
				break
		else:
			yield  i

if __name__ == "__main__":
	pGen = generatePrime(number/2)
		
	for pnum in pGen:
		if number%pnum == 0:
			print "Prime factor is :", pnum	
	
