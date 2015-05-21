#!/usr/bin/python


target=4000000
a=0
b=1
sum = 0
while b < target :
        x = a
        a = b
        b = x + b
        if b%2 == 0:
                sum += b

print sum
