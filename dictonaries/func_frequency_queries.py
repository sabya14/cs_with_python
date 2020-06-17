"""
Problem Statement - https://www.hackerrank.com/challenges/frequency-queries/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
"""
from collections import defaultdict


def freq_query(queries):
    elem_count_state = defaultdict(int)
    freq_count_state = defaultdict(int)
    result = []
    for query in queries:
        operation_code, operation_value = query
        if operation_code == 1:
            if elem_count_state[elem_count_state[operation_value]]:
                freq_count_state[elem_count_state[operation_value]] -= 1
            elem_count_state[operation_value] += 1
            freq_count_state[elem_count_state[operation_value]] += 1

        if operation_code == 2:
            if operation_value in elem_count_state:
                freq_count_state[elem_count_state[operation_value]] -= 1
                elem_count_state[operation_value] -= 1
                freq_count_state[elem_count_state[operation_value]] += 1

        if operation_code == 3:
            if operation_value in freq_count_state and freq_count_state[operation_value] > 0:
                result.append(1)
            else:
                result.append(0)
    return result
