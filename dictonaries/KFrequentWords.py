from typing import List


class Solution:

    @staticmethod
    def top_k_frequent(words: List[str], k: int) -> List[str]:
        keyword_dict = {word: 0 for word in words}
        for word in words:
            if word in keyword_dict:
                keyword_dict[word] += 1
        dict_sorted_by_key = {key: keyword_dict[key] for key in sorted(keyword_dict.keys())}
        dict_sorted_value = {x[0]: x[1] for x in sorted(dict_sorted_by_key.items(), key=lambda x: x[1], reverse=True)}
        return list(dict_sorted_value.keys())[:k]
