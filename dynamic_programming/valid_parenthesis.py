"""
8.9 From cracking the coding interview, given a number n, find the total number of parenthesis that can
be derived from it.
"""


def find_parenthesis_index(_string):
    left = 0
    parenthesis_index = []
    left_index = []
    for (index, _char) in enumerate(_string):
        if _char == '(':
            left_index.append(index)
            left += 1
        else:
            left -= 1
            if left < 0:
                raise ValueError("Invalid parens")
            else:
                parenthesis_index.append((left_index.pop(), index))
    return parenthesis_index


def insert_at_left(paren_list):
    to_return = []
    for _string in paren_list:
        indexes = find_parenthesis_index(_string)
        print(_string)
        print(indexes)
        for _index in indexes:
            new_string = _string[:_index[0] + 1] + "()" + _string[_index[0] + 1:]
            print(new_string)
            to_return.append(new_string)
        print("---")
    return to_return


def insert_in_the_front(paren_list):
    to_return = []
    for x in paren_list:
        to_return.append(f"(){x}")
    return to_return


def parenthesis_builder(n):
    if n == 0:
        return []
    elif n == 1:
        return ["()"]
    elif n == 2:
        return ["(())", "()()"]
    else:
        _left = insert_at_left(parenthesis_builder(n - 1))
        _front = insert_in_the_front(parenthesis_builder(n - 1))
        to_return = _left + _front
        return set(to_return)


parenthesis_builder(4)

