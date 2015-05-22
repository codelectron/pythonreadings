#!/usr/bin/python
import sys

max = 999
min = 100
maxnum = 0
def checkPalindrom(number):
        strNum = str(number)
        length = len(strNum)/2
        if len(strNum)%2 == 0:
                str1, str2 = strNum[:length], strNum[length:]
        else:
                str1, str2 = strNum[:length] , strNum[length+1:]
        return str1 == str2[::-1]

for i in range(max,min,-1):
        for k in range(i,min,-1):
                res = checkPalindrom(i*k)
                if res :
                        if maxnum < i*k:
                                maxnum = i*k

print maxnum
