"""
Problem Statement - https://www.hackerrank.com/challenges/abbr/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
"""


def find_first_matching_char(word, match_against):
    for index, char in enumerate(word):
        for index_match, char_match in enumerate(match_against):
            if char == char_match or char.upper() == char_match:
                return index, index_match
    return -1, -1


def find_first_matching_upper_case_char(word, match_against):
    for index, char in enumerate(word):
        for index_match, char_match in enumerate(match_against):
            if char == char_match and char.isupper():
                return index, index_match
    return -1, -1


def remove_char_at_specific_index(word, index):
    if len(word) > index:
        word = word[0: index:] + word[index + 1::]
    return word


def remove_lower_case_letter(word):
    return "".join(list(map(lambda x: x if x.isupper() else "", word)))


def abbreviation(input_data, convert_to):
    if conversion(input_data, convert_to):
        return "YES"
    else:
        return "NO"


results = {}


def conversion(input_data, convert_to):
    print(results)
    if input_data+convert_to in results:
        return results[f"{input_data}{convert_to}"]
    without_small_case = remove_lower_case_letter(input_data)
    if without_small_case == "" and convert_to == "" or without_small_case == convert_to:
        results[f"{input_data}{convert_to}"] = True
        return True

    else:
        input_pos, match_pos = find_first_matching_upper_case_char(input_data, convert_to)
        if input_pos != -1:
            reduced_input = remove_char_at_specific_index(input_data, input_pos)
            reduced_convert_to = remove_char_at_specific_index(convert_to, match_pos)
            return conversion(reduced_input, reduced_convert_to)
        else:
            input_pos, match_pos = find_first_matching_char(input_data, convert_to)
            if input_pos != -1:
                reduced_input = remove_char_at_specific_index(input_data, input_pos)
                reduced_convert_to = remove_char_at_specific_index(convert_to, match_pos)
                return conversion(reduced_input, reduced_convert_to)
            results["asd"] = 123
            results[f"{input_data}{convert_to}" = False
            return False
