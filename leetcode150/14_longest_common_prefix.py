# https://leetcode.com/problems/longest-common-prefix/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def longestCommonPrefix(strs: List[str]) -> str:
    out = ""
    if not strs:
        return out

    for i in range(0, len(strs[0])):
        for j in strs:
            if i >= len(j) or strs[0][i] != j[i]:
                return strs[0][:i]

    return strs[0]


print(longestCommonPrefix(["a"]))
