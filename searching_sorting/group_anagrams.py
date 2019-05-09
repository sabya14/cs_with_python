"""
Problem 10.2 Cracking the coding interview.
Sort a group of arrays such that anagrams are together
"""


def sort_anagrams(_list):
    _hash = {}
    for word in _list:
        sorted_word = "".join(sorted(word))
        if sorted_word in _hash:
            _hash[sorted_word].append(word)
        else:
            _hash.update({sorted_word: [word]})
    result = []
    for _item in _hash.values():
        result = result + _item
    return result


if __name__ == "__main__":
    print(sort_anagrams(['abc', 'deb', 'ebc', 'dbe', 'cab']))
