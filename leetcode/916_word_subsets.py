# https://leetcode.com/problems/word-subsets/description/?envType=daily-question&envId=2025-01-10
from typing import List


def wordSubsets(self, words1: List[str], words2:  List[str]) -> List[str]:
    combined_freq = {}

    for word in words2:
        word_freq = {}
        for char in word:
            word_freq[char] = word_freq.get(char, 0) + 1
        for char, count in word_freq.items():
            combined_freq[char] = max(combined_freq.get(char, 0), count)

    result = []
    for word in words1:
        word_freq = {}
        for char in word:
            word_freq[char] = word_freq.get(char, 0) + 1

        is_universal = True
        for char, required_count in combined_freq.items():
            if word_freq.get(char, 0) < required_count:
                is_universal = False
                break
        if is_universal:
            result.append(word)

    return result
