"""
5.1 From Cracking the coding interview
"""


def insertions(n, m, i, j):
    """
    Eg - > In 10001010, put 101 in 4-7 position, thus returning 11011010
    """
    m_shifted = m << i  # move m i places left to align with n
    right_mask = (1 << i) - 1  # produces 0...011
    left_mask = -1 << j + 1  # -1 is basically -1b1111111111111,<< j -> 11110000, if j is 4
    full_mask = left_mask | right_mask  # merging them
    n_cleared = n & full_mask  # Clearing using and
    result = n_cleared | m_shifted  # merge them
    return result


if __name__ == "__main__":
    insertions(0b00000111, 0b11, 6, 8)
