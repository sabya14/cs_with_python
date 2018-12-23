def outer_function():
	message = 'Hi'

	def inner_function():
		print(message)
	return inner_function()


# outer_function()


def outer_function_1(msg):

	def inner_function():
		print("Hey" + msg)
	return inner_function


# My func is a closure, that is it remembers the variable message even after outer function has finished
# executing.
if __name__ == "__main__":
	hi_func = outer_function_1("Everyone")
	hi_func()
# hello_function = outer_function_1("hello")
# hello_function()
