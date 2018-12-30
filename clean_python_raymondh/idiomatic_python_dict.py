"""Dictionary Skills"""
import argparse
import os
from collections import defaultdict, ChainMap

d = {
	'neel': 'blue',
	'gargy': 'red',
	'shybba': 'green'
}

# You cant mutate this dict, if using key in dict.
for k in d:
	print(k)

# you can mutate dict keys if using d.keys() as its saves a local copy of the dict keys
for k in d.keys():
	print(k)

# Looping of keys, values in dict
#  items in python 3 returns a view, which is pretty much the same as an iterator.
for k, v in d.items():
	print(k, v)

# Construct a dict from pairs
names = ['neel', 'gargy', 'shybba']
colors = ['red', 'blue', 'green']

d = dict(zip(names, colors))

# Counting with dict
colors = ['red', 'blue', 'green']
d = {}
counter = 0
for index, color in enumerate(colors):
	if color not in d:
		d[color] = 0
	d[color] = index + 1
print(d)

# Better way
d = {}
for index, color in enumerate(colors):
	d[color] = d.get(color, 0) + index + 1
print(d)

d = defaultdict(int)
for index, color in enumerate(colors):
	d[color] += index + 1
print(dict(d))

# Grouping with dict
names = ['neel', 'neel_1', 'gargy', 'ria', 'shybba']
d = {}
for name in names:
	key = len(name)
	if key not in d:
		d[key] = []
	d[key].append(name)
print(d)

# Grouping with set default
d = {}
for name in names:
	key = len(name)
	d.setdefault(key, []).append(name)
print(d)

d = defaultdict(list)
for name in names:
	key = len(name)
	d[key].append(name)
print(d)

# Linking dict together
defaults = {'color': 'red', 'user': 'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('-c', '--color')
namespace = parser.parse_args([])
command_line_args = {
	k: v for k, v in vars(namespace).items() if v
}
print(command_line_args)
d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)
print(d)

d = ChainMap(command_line_args, os.environ, defaults)
print(d)
