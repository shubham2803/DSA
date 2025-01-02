# https://leetcode.com/problems/count-vowel-strings-in-ranges/description/?envType=daily-question&envId=2025-01-02
from typing import List


def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
    vowels = {
        'a': True,
        'e': True,
        'i': True,
        'o': True,
        'u': True,
    }
    prefix_sum = [0]
    for i in range(0, len(words)):
        if words[i][0] in vowels and words[i][-1] in vowels:
            prefix_sum.append(prefix_sum[-1] + 1)
        else:
            prefix_sum.append(prefix_sum[-1])
    out = []
    for l, r in queries:
        out.append(prefix_sum[r + 1] - prefix_sum[l])
    return out


print(vowelStrings(None, ["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]))
