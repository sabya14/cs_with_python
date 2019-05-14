"""
8.11 Problem from cracking the coding interview
https://practice.geeksforgeeks.org/problems/coin-change/0
"""


def n_cents(n, cent_list, index, _dict):
    if n == 0:
        return 1
    if index > len(cent_list) - 1:
        return 0
    cent = cent_list[index]
    possible_way_to_use = n // cent
    result = 0
    while possible_way_to_use > -1:
        print(
            f"Adding {possible_way_to_use} cents of value {cent},"
            f" left value {n - (possible_way_to_use * cent)}")
        if not ((n - (possible_way_to_use * cent), index + 1) in _dict):
            _dict[(n - (possible_way_to_use * cent), index + 1)] = n_cents(n - (possible_way_to_use * cent),
                                                                                      cent_list, index + 1, _dict)
        result += _dict[(n - (possible_way_to_use * cent), index + 1)]
        possible_way_to_use -= 1
    return result


print(n_cents(4, [3, 2, 1], 0, {}))
print('--------')
print(n_cents(10, [6, 5, 3, 2], 0, {}))
print(n_cents(11, [5, 2, 1], 0, {}))
