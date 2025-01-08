# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/?envType=daily-question&envId=2025-01-08
from typing import List


def countPrefixSuffixPairs(self, words: List[str]) -> int:
    def isPrefixAndSuffix(str1, str2):
        if str2.startswith(str1) and str2.endswith(str1):
            return True
        return False

    w = len(words)
    out = 0
    for i in range(w):
        for j in range(i + 1, w):
            if isPrefixAndSuffix(words[i], words[j]):
                out += 1
    return out
