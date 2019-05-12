"""
8.11 Problem from cracking the coding interview
https://practice.geeksforgeeks.org/problems/coin-change/0
"""
from math import floor


def n_cents(n, cent_list, index):
    if index >= len(cent_list) - 1:
        return 1
    cent = cent_list[index]
    print("Cent", cent)
    possible_way_to_use = 0
    result = 0
    while possible_way_to_use * cent <= n:
        print(
            f"Adding {possible_way_to_use} cents of value {cent},"
            f" left value {n - (possible_way_to_use * cent)}")
        result += n_cents(n - (possible_way_to_use * cent), cent_list, index + 1)
        possible_way_to_use += 1
    print("Returning of")
    return result


print(n_cents(10, [25,10,5,1], 0))
