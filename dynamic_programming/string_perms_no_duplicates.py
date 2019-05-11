"""
Given a string with possible duplicates, return strings with no duplicates
"""


def permutations_former(_string, hash_table, _permutations):
    for _char in hash_table:
        hash_table_copy = hash_table.copy()
        if hash_table[_char] <= 1:
            hash_table_copy.pop(_char)
        else:
            hash_table_copy[_char] -= 1
        if not hash_table_copy:
            _permutations.append(_char + _string)
            return _permutations
        permutations_former(_string + _char, hash_table_copy, _permutations)
    return _permutations


def permutations(_string):
    _permutations = []
    hash_table = {}
    for char in _string:
        if char in hash_table:
            hash_table[char] += 1
        else:
            hash_table.update({char: 1})

    return permutations_former("", hash_table, _permutations)


print(permutations("aabb"))
