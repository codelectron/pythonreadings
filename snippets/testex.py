from  myerror import *

class Error(Exception):
   """Base class for other exceptions"""
   pass


def raiseExp():
	raise Error
	pass


if __name__ == "__main__":
	print "This is test"
	try:
		raiseExp()
	except MyError:
		print "Errorrrrrr"
		print e
	
