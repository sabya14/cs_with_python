import inspect


def decorator_function(original_function):
	def wrapper_function():
		print("Check for cache here")
		# define your process
		return original_function()

	return wrapper_function


@decorator_function
def process_report():
	print("Processing Report")


def decorator_function_with_args(original_function):
	def wrapper_function(*args, **kwargs):
		print("Decorators with args, Check for cache here")
		return original_function(*args, **kwargs)

	return wrapper_function


@decorator_function_with_args
def process_report_with_args(report_id):
	print("Processing Report", report_id)


class LearnDecorator:

	def __init__(self, original_function, *args, **kwargs):
		self.original_function = original_function
		print(args, kwargs)

	def __call__(self, *args, **kwargs):
		print(*args)
		return self.original_function(*args, **kwargs)


@LearnDecorator
def class_decorator_test(report_id):
	print("Generate Report", report_id)


if __name__ == '__main__':
	process_report()
	process_report_with_args(123)
	class_decorator_test(1234)
