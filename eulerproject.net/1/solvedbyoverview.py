#!/usr/bin/python

target=999999999

def SumDivisibleBy(number):
	p=target/number
	return number*(p*(p+1))/2

if __name__ == "__main__":
	print SumDivisibleBy(3)+SumDivisibleBy(5)-SumDivisibleBy(15)
