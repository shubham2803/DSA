# https://leetcode.com/problems/counting-words-with-a-given-prefix/description/?envType=daily-question&envId=2025-01-09
from typing import List


def prefixCount(self, words: List[str], pref: str) -> int:
    def get_pi(joint):
        n = len(joint)
        pi = [0] * n

        i = 1
        j = 0

        while i < n:
            if joint[i] == joint[j]:
                j += 1
                pi[i] = j
                i += 1
            else:
                if j != 0:
                    j = pi[j - 1]
                else:
                    j = 0
                    i += 1
        return pi

    def isPrefix(pref, word):
        joint = pref + ':' + word
        m = len(pref)
        pi = get_pi(joint)

        return pi[(2 * m)] == m

    out = 0
    for word in words:
        if len(word) < len(pref):
            continue
        if isPrefix(pref, word):
            out += 1
    return out
