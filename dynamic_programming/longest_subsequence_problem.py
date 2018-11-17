def longest_subsequence_problem(string_a, string_b):
	# Get the length of the strings
	len_a = len(string_a)
	len_b = len(string_b)

	# Create a memo, and extra row for creating a row and column with indices zero.
	# Helps in reducing complexity of code
	memo = [[0] * (len_b + 1) for i in range(0, (len_b + 1))]
	# For skipping index 0, we add 1 to range
	for _index_b in range(len_b + 1):
		for _index_a in range(len_a + 1):
			if _index_b == 0 or _index_a == 0:
				memo[_index_b][_index_a] = 0

			# As we have added 1 to index, we need subtract 1 to find the exact from the string
			elif string_b[_index_b - 1] == string_a[_index_a - 1]:
				memo[_index_b][_index_a] = 1 + memo[_index_b - 1][_index_a - 1]
			else:
				memo[_index_b][_index_a] = max(memo[_index_b - 1][_index_a], memo[_index_b][_index_a - 1])
	for row in memo:
		print(*row)
	return memo[len_b][len_a]


if __name__ == "__main__":
	print(longest_subsequence_problem("AGGTAB", "GXTXAYB"))\



