import os
import sys
import threading
import urllib.request
from contextlib import contextmanager, redirect_stdout
from functools import wraps

def web_lookup(url, saved={}):
	if url in saved:
		return saved[url]
	page = urllib.request.urlopen(url).read()
	saved[urllib] = page
	return page


def web_cache(func):
	saved = {}

	def cache_check(*args, **kwargs):
		if args in saved:
			return cache_check(*args, **kwargs)
		result = func(*args, **kwargs)
		saved[args] = result
		return result

	return cache_check


@web_cache
def web_lookup_cached(url, saved={}):
	if url in saved:
		return saved[url]
	page = urllib.request.urlopen(url).read()
	saved[urllib] = page
	return page


web_lookup("https://www.google.com/")
web_lookup_cached("https://www.google.com/")

# Context managers

# Open file
with open('text.txt') as f:
	data = f.read()
	print(data)

# How to use locks
lock = threading.Lock()
lock.acquire()

try:
	print("CS")
finally:
	lock.release()

# New way:

lock = threading.Lock()
with lock:
	print("CS")

try:
	os.remove('tasd.txt')
except OSError:
	pass


@contextmanager
def ignored(*exceptions):
	try:
		yield
	except exceptions:
		pass


with ignored(OSError):
	os.remove('asd.txt')


with open('help.txt', 'w+') as f:
	oldstdout = sys.stdout
	sys.stdout = f
	try:
		print(help(pow))
	finally:
		sys.stdout = oldstdout
with open('help_1.txt', 'w+') as f:
	with redirect_stdout(f):
		help(pow)
