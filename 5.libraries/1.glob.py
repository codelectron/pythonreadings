#!/usr/bin/python
import glob
import os

listofpyfiles = glob.glob('*.py')
print listofpyfiles
os.chdir("..")

listofpyfiles = glob.glob('*.py')
print listofpyfiles
