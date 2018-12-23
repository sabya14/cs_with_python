# Named Tuples
from collections import namedtuple, deque

test_results = namedtuple('test_results', ['passed', 'failed'])
t = test_results(0, 4)
print(t)

# Unpacking sequences
p = 'Neel', 'is', 'a', 'coder'
name = p[0]
hobby = p[3]
print(name, hobby)
name, _, _, hobby = p
print(name, hobby)


# Updating multiple state variables
def fibonacci(n):
	x = 0
	y = 1
	for i in range(n):
		print(x)
		temp = y
		y = x + y
		x = temp


fibonacci(5)


# Updating multiple state variables
def fibonacci(n):
	x = 0
	y = 1
	for i in range(n):
		print(x)
		# Update states in one logical line
		x, y = y, x + y


fibonacci(5)

# Concatenating strings
names = ['a', 'b', 'c']
print(", ".join(names))

# Updating sequences
names = ['a', 'b', 'c']

del names[0]
names.pop()

names = deque(names)
del names[0]
names.pop()