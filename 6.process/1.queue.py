#!/usr/bin/python
from multiprocessing import Process, Queue
import time
import sys

def Worker(queue):
	
	while(True):
		if not queue.empty():
			msg = queue.get()
			print msg	
		else:
			time.sleep(1)
			sys.stdout.write('#')
			sys.stdout.flush()



if __name__ == "__main__":
	queue = Queue()
	worker = Process(target=Worker, args=((queue),))
	worker.daemon = True
	worker.start()
		
	while(True):
		mesg = raw_input("Enter to print:")
		queue.put(mesg)
