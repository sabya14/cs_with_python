__author__ = "Sabyaschi Nandy sabya.nandy14@gmail.com"
"""
See the usefulness of dynamic programming through a basic solution for fibonacci series

KEY POINTS-1. Understand whether the problem is of DP or not.
				For that try to look for things - Does it overlapping subproblems property.
												- Or optimal subtructure property.
			2. After figuring that your, try to formulated a recurrence relation.
			3. Find out what to do in every state.
			4. Using memoization to store result of each state
			5. Code it. 											
"""


def recursive_fibonacci(number, counter):
	"""
	Get the fibonacci series up to "number" and also count the total number of steps involved.
	:param number: The number up to which we have to find the series
	:counter: A variable which keeps a track if the no of steps
	:return: A list, containing the series
	"""
	if number == 0:
		counter += 1
		return [0], counter
	elif number == 1:
		counter += 1
		return [0, 1], counter
	else:
		counter += 1
		larger_series, counter = recursive_fibonacci(number - 1, counter)
		smaller_series, counter = recursive_fibonacci(number - 2, counter)
		# get the last two number of each series, add them and add to the larger_series.
		n = smaller_series[-1] + larger_series[-1]
		return larger_series + [n], counter


def dynamic_programming_fibonacci(number, counter):
	"""
	Get the fibonacci series up to "number" and also count the total number of steps involved.
	:param number: The number up to which we have to find the series
	:counter: A variable which keeps a track if the no of steps
	:return: A list, containing the series
	"""
	# Create a blank memo list to store the values for the series
	memos = [0] * (number + 1)
	if number == 0:  # base
		return [0], 1
	if number == 1:
		return [0, 1], 1
	else:
		memos[0] = 0
		memos[1] = 1
		for i in range(2, (number + 1)):
			counter = counter + 1
			memos[i] = memos[i - 1] + memos[i - 2]
		return memos, counter


if __name__ == "__main__":
	for i in range(0, 10):
		print(recursive_fibonacci(i, 0))
		print(dynamic_programming_fibonacci(i, 0))
