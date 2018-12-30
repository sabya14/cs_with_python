import random
import threading
import time

counter = 0

##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True


def fuzz():
	if FUZZ:
		time.sleep(random.random())


###########################################################################################

def worker():
	global counter
	counter += 1
	print('The count is %d' % counter)
	print('---------------')


print("Normal Version")
print('Starting up')
for i in range(10):
	worker()
print('Finishing up')
print('---------------')


counter_thread = 0

##########################################################################################
# Fuzzing is a technique for amplifying race condition errors to make them more visible

FUZZ = True


def fuzz():
	if FUZZ:
		time.sleep(random.random())


###########################################################################################

def worker():
	fuzz()
	global counter_thread
	fuzz()
	counter_thread += 1
	fuzz()
	print('The count is %d' % counter_thread)
	fuzz()
	print('---------------')
	fuzz()


fuzz()
print('Threaded Version')
fuzz()
print('Starting up')
fuzz()
for i in range(10):
	fuzz()
	threading.Thread(target=worker).start()
	fuzz()
print('Finishing up')
fuzz()
print('---------------')
