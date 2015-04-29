#!/usr/bin/python
import pickle

fruit = dict(apple=1, berry=3, cherry=10, date=12, elderberry=22)

days = ("Montag", "Dienstag","Mittwoch","Donnerstag",
	"Freitag", "Samstag","Sonntag")

mix = [ fruit, days ]

with open("output.txt","w") as fhandle:
	pickle.dump(mix, fhandle)

with open("output.txt","rb") as fhandle:
	newmix = pickle.load(fhandle)

newfruits, newdays = newmix

print type(mix), type(newmix)
print type(days), type(newdays)
print type(fruit), type(newfruits)

print newdays
print newfruits
