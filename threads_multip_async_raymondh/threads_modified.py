import random
import threading
import time

"""
In this we will modify the threaded code that we wrote in file threads.py
"""
import threading, time, random, queue

##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True


def fuzz():
	if FUZZ:
		time.sleep(random.random())


###########################################################################################

counter = 0
counter_queue = queue.Queue()


def counter_manager():
	"""
	This will be implemented as a daemon thread, i.e it will keep waiting for tasks from a queue.
	Once that queue is finished, the main thread will exit, automatically killing this.
	I have EXCLUSIVE rights to update the counter variable
	"""
	# Infinite loop will keep waiting for tasks, and notify when done
	global counter

	while True:
		increment = counter_queue.get()
		fuzz()
		oldcnt = counter
		fuzz()
		counter = oldcnt + increment
		fuzz()
		print_queue.put([
			'The count is %d' % counter,
			'---------------'])
		fuzz()
		counter_queue.task_done()


t = threading.Thread(target=counter_manager)
t.daemon = True
t.start()
del t

###########################################################################################

print_queue = queue.Queue()


def print_manager():
	"""
	This will be implemented as a daemon thread, i.e it will keep waiting for tasks from a queue.
	Once that queue is finished, the main thread will exit, automatically killing this.
	I have EXCLUSIVE rights to call the "print" keyword
	"""
	# Infinite loop will keep waiting for tasks, and notify when done
	while True:
		job = print_queue.get()
		fuzz()
		for line in job:
			print(line, end='')
			fuzz()
			print()
			fuzz()
		print_queue.task_done()
		fuzz()


t = threading.Thread(target=print_manager)
t.daemon = True
t.start()
del t


###########################################################################################

def worker():
	"""My job is to increment the counter and print the current count"""
	# Now as we add an task to counter queue, our infinite Daemon of counter manager listens to it and processes it.
	counter_queue.put(1)
	fuzz()


# Now as we add an task to counter queue, our infinite Daemon of print manager listens to it and processes it.
print_queue.put(['Starting up'])
fuzz()

worker_threads = []
for i in range(10):
	# Now we start non daemon workers
	t = threading.Thread(target=worker)
	worker_threads.append(t)
	t.start()
	fuzz()
for t in worker_threads:
	# We wait for all the threads to finish
	fuzz()
	t.join()

# We wait for queue to finish up, join in queue waits for the task to complete and then exits.
# The daemon threads for count and print manager  will be killed automatically.
counter_queue.join()
fuzz()
print_queue.put(['Finishing up'])
fuzz()
print_queue.join()
fuzz()
