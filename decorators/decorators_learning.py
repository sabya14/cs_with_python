def outer_function():
	message = 'Hi'

	def inner_function():
		print(message)
	return inner_function()


outer_function()


def outer_function_1():
	message = 'Hi'

	def inner_function():
		print(message)
	return inner_function


# My func is a closure, that is it remembers the variable message even after outer function has finished
# executing.
my_func = outer_function_1()
my_func()
my_func()
my_func()
