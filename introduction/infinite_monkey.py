from random import choice
from string import ascii_lowercase


def random_string_generator(size_of_string, index_list=None, previous_string = None):
    """

    :param size_of_string: the size of the random string to be generated
    :param index_list:  the index which are to be generated
    :return: A random string generated..
    choice(ascii_uppercase) - ascii uppercase is a seq, and choice returns a random
    element from it
    """
    if index_list is None:
        # return a whole generated string
        return str(''.join(choice(ascii_lowercase + ' ') for index in range(size_of_string)))
    elif previous_string is not None:
        previous_string = list(previous_string)
        for index in range(size_of_string):
            if index in index_list:
                continue
            previous_string[index] = choice(ascii_lowercase + ' ')
    return ''.join(previous_string)


def score(generated_string, desired_string, length):
    """

    :param generated_string: the string from generator function
    :param desired_string: the string desired
    :return: A score based on percentage which defines the percentage match
    """
    # number of correct matches
    match = 0
    for char_1, char_2 in zip(generated_string, desired_string):
        if char_1 is char_2:
            match = match+1
    percentage = (match/length) * 100
    return percentage


def index_list_matching(desired_string, generated_string):
    """

    :param desired_string: desired string
    :param generated_string: random generated string
    :return: the index position of list where the above two string match
    """
    index_list = []
    for index, (char_1, char_2) in enumerate(zip(generated_string, desired_string)):
        if char_1 == char_2:
            index_list.append(index)
    return index_list


def infinite_monkey():
    """
    :return: Solve the classic infinte monkey theorem.
    Used hill climbing for better result
    """
    desired_string = """methinks it is like a weasel and elongating the sentence"""
    length = len(desired_string)
    generated_string = random_string_generator(length)
    index_list = index_list_matching(desired_string, generated_string)
    tries = 0
    prev_score = 0
    pres_score = score(generated_string, desired_string, length)
    while pres_score != 100:
        # if pres, less than prev, use the same index list
        if pres_score < prev_score:
            generated_string = random_string_generator(length, index_list, generated_string)
        else:
            # else performance better, find latest index to be skipped
            index_list = index_list_matching(desired_string, generated_string)
            generated_string = random_string_generator(length, index_list, generated_string)
        tries = tries + 1
        # calculate score with the latest generated string
        pres_score = score(generated_string, desired_string, length)

    print(tries)
    print(generated_string)


infinite_monkey()