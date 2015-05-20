#!/usr/bin/python
from multiprocessing import Process, Queue
import time
import sys

def Worker(queue1, queue2):
	
	while(True):
		if not queue1.empty():
			msg = queue1.get()
			queue2.put( msg[::-1])
		else:
			pass
			#time.sleep(1)
			#sys.stdout.write('#')
			#sys.stdout.flush()



if __name__ == "__main__":
	queue_in = Queue()
	queue_out = Queue()
	worker = Process(target=Worker, args=((queue_in) , (queue_out)))
	worker.daemon = True
	worker.start()
		
	while(True):
		mesg = raw_input("Enter to print:")
		if mesg == "quit":
			sys.exit(0)
		queue_in.put(mesg)
		print queue_out.get()

