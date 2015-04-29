#!/usr/bin/python
import csv
csvlist = []
for i in range(0, 3):
	name = raw_input("Enter name of the Animal:")
	place = raw_input("Enter place of origin:")
	csvlist.append([name, place])

print csvlist

print "Creating Zoo CSV file"
try:
	with open("Zoo.csv","wt") as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(["Animal", "Place"])
		for row in csvlist:	
			csvwriter.writerow(row)
except:
	print "Some Exception, unable to write, quitting..."
	exit(1)

	

try:
	with open("Zoo.csv","r") as csvfile:
		csvreader = csv.reader(csvfile)
		for name, animal in csvreader:
			print name, animal
except:
	print "Some Exception unable to read, quitting..."
