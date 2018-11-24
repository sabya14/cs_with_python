"""
Given two strings str1 and str2 and below operations that can performed on str1. Find minimum number of edits (operations) required to convert ‘str1’ into ‘str2’.

Insert
Remove
Replace
All of the above operations are of equal cost.
"""


def minimum_edit_distance(string_a, string_b):
	"""
	:param string_a: The actual input string
	:param string_b: The desired string
	:return: The minimum number of edits needed
	"""
	string_a_length = len(string_a)
	string_b_length = len(string_b)
	memo = [[0] * (string_a_length + 1) for i in range(string_b_length + 1)]
	for i in range(0, string_b_length + 1):
		for j in range(0, string_a_length + 1):
			if i == 0:
				memo[i][j] = j
			elif j == 0:
				memo[i][j] = i
			elif string_b[i - 1] == string_a[j - 1]:
				memo[i][j] = memo[i-1][j-1]
			else:
				memo[i][j] = 1 + min(memo[i][j-1], memo[i-1][j-1], memo[i-1][j])
	return memo


if __name__ == "__main__":
	print(minimum_edit_distance("A", "BAT"))