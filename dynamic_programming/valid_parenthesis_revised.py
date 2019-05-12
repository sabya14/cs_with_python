"""
8.9 From cracking the coding interview, given a number n, find the total number of parenthesis that can
be derived from it.
"""


def parenthesis_build(_string, left, right, result):
    if left < 0 or right < left:
        return
    if left == 0 and right == 0:
        result.append(_string)
        return result
    else:
        if left:
            result = parenthesis_build(_string + "(", left - 1, right, result)
        if right > left:
            result = parenthesis_build(_string + ")", left, right - 1, result)
    return result

print(parenthesis_build('', 3, 3, []))
