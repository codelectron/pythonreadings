#!/usr/bin/python
import json 

fruit = dict(apple=1, berry=3, cherry=10, date=12, elderberry=22)

days = ("Montag", "Dienstag","Mittwoch","Donnerstag",
	"Freitag", "Samstag","Sonntag")

mix = [ fruit, days ]

with open("output.json","w") as fhandle:
	json.dump(mix, fhandle)

with open("output.json","rb") as fhandle:
	newmix = json.load(fhandle)

newfruits, newdays = newmix

print type(mix), type(newmix)
print type(days), type(newdays)
print type(fruit), type(newfruits)

print newdays
print newfruits
