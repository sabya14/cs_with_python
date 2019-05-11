"""
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the
knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1] which represent values and weights
associated with n items respectively. Also given an integer W which represents knapsack capacity, find out the maximum
value subset of val[] such that sum of the weights of this subset is smaller than or equal to W.
You cannot break an item, either pick the complete item, or don’t pick it (0-1 property).
"""


def knapsack_0_1(weights_list, values_list, weight):
    length = len(weights_list)
    memo = [[0] * (length + 1) for i in range(length + 1)]
    bag = [[0] * (length + 1) for i in range(length + 1)]
    for i in range(length + 1):
        available_wt = weight
        for j in range(0, length + 1):
            # Skip this scenarios
            if j > i:
                memo[i][j] = 0
            # For aiding memoization
            elif i == 0 or j == 0:
                memo[i][j] = 0
            # If addition is possible to current bag, i.e total wt available is greater that current item weight
            elif available_wt >= weights_list[j - 1]:
                # Check if better to add this weight, or continue with the last weight
                memo[i][j] = max(memo[i][j - 1], memo[i - 1][j - 1] + values_list[i - 1])
                available_wt = available_wt - weights_list[j - 1]

                # Additional logic to maintain which elements are added to the bag, at the current moment
                if memo[i][j - 1] < memo[i - 1][j - 1] + values_list[i - 1]:
                    bag[i][j] = bag[i - 1][j - 1], weights_list[i - 1]
                else:
                    bag[i][j] = bag[i - 1][j - 1]
            # If not possible keep the last state.
            else:
                memo[i][j] = memo[i][j - 1]
                bag[i][j] = bag[i][j - 1]

    print(*bag, sep="\n")
    print("******")
    return memo


if __name__ == "__main__":
    print(*(knapsack_0_1([10, 20, 30], [60, 100, 120], 50)), sep="\n")
