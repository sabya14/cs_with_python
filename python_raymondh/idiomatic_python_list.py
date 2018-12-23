"""
Transforming code into beautiful, idiomatic python
"""
from functools import partial

"""
LOOPS
"""
# BASIC LOOPS
for i in [1, 2, 3, 4, 5]:
	print(i ** 2)

# Range produces an iter, only one item is produced at a time, so is faster.
for i in range(6):
	print(i ** 2)

# Looping over a collection
colors = ['red', 'blue', 'green']
for i in range(len(colors)):
	print(colors[i])

# Better
for color in colors:
	print(color)

# Looping backwards
for i in range(len(colors) - 1, -1, -1):
	print(colors[i])

for color in reversed(colors):
	print(color)

# Looping over collection and indices:
for i, color in enumerate(colors):
	print(i, '-->', color)

# Looping over two collections
colors = ['red', 'blue', 'green']

names = ['neel', 'gargy', 'shybba']

n = min(len(colors), len(names))
for i in range(n):
	print(names[i], '-->', colors[i])

# zip creates an extra dict tow loop over both list, so not scalable in 2.7.
# now in python 3 it has replaced traditional zip
for name, color in zip(names, colors):
	print(name, '-->', color)

# Looping in sorted orders
for color in sorted(colors):
	print(color)

for color in sorted(colors, reverse=True):
	print(color)


# Custom sorting
def compare_len(c1, c2):
	if len(c1) > len(c2): return -1
	if len(c1) < len(c2): return 1
	return 0


print(sorted(colors, key=len))

# Call a function with sentinel value
read = [1, 2, '', 3]
i = 0
blocks = []
while True:
	block = read[i]
	if block == '':
		break
	blocks.append(block)
	i += 1

print("Blocks", blocks)

# Simple solution, we iter over a iterable until we hit a sentinel value.
# To make list a iterable, we iter over it, and pass it two a partial function
blocks = []
for block in iter(partial(next, iter(read)), ''):
	blocks.append(block)

print("Blocks", blocks)


# Distinguish multiple exit points in loop
def find(seq, target):
	found = False
	for i, value in enumerate(seq):
		if value == target:
			found = True
			break
	if not found:
		return -1
	return 1


print(find([1, 2, 3, 4], 3))
print(find([1, 2, 3, 4], 7))


def find_better(seq, target):
	for i, value in enumerate(seq):
		if value == target:
			return 1
	else:
		return -1


print(find_better([1, 2, 3, 4], 3))
print(find_better([1, 2, 3, 4], 7))
