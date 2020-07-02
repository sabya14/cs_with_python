"""
Problem Statement - https://leetcode.com/problems/partition-labels/
"""


def partition_labels(word):
    result = [-1]
    for index, curr_char in enumerate(word):
        split_at_index = 0
        for next_index, next_char in enumerate(word[index:]):
            if curr_char == next_char:
                print(next_index + index, next_index, index, next_index > split_at_index, curr_char, split_at_index)
                if next_index + index > split_at_index:
                    split_at_index = next_index + index
        if len(result) == 1:
            result.append(split_at_index)
        else:
            last_split_at = result[-1]
            if split_at_index > last_split_at and index < last_split_at:
                result[-1] = split_at_index
            elif split_at_index > last_split_at:
                result.append(split_at_index)
    final_result = []
    print(result)
    for index, value in enumerate(result[:-1]):
        final_result.append(result[index + 1] - result[index])
    return final_result
