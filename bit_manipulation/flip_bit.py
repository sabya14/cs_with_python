"""
Flip a single bit to achieve longest sequence of 1 in a bit string
Problem 5.3 - Cracking the coding interview.
"""


def flip_bit(number):
    binary_string = str(bin(number))
    print(binary_string)
    _max = 0
    left = 0
    right = 0
    single_zero_found = False
    previous_char = -1
    for index, c in enumerate(binary_string[2:]):
        c = int(c)
        if c:
            if single_zero_found:
                right += 1
            else:
                left += 1
        else:
            if previous_char == c:
                left = 1
                right = 0
                single_zero_found = False
            else:
                _max = _max if _max > (left + right) else left + right
                if not single_zero_found:
                    left = left + 1
                else:
                    left = right + 1
                right = 0
                single_zero_found = True
        previous_char = c
    _max = _max if _max > (left + right) else left + right


if __name__ == "__main__":
    flip_bit(1775)
    flip_bit(21)
    flip_bit(39)
    flip_bit(11)
    flip_bit(1)
