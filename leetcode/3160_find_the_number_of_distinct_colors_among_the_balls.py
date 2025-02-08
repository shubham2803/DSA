# https://leetcode.com/problems/find-the-number-of-distinct-colors-among-the-balls/description/?envType=daily-question&envId=2025-02-07
from collections import defaultdict
from typing import List


def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
    n = len(queries)
    ans = [0] * n
    mp = {}
    color = defaultdict(int)
    i = 0
    for x, c in queries:
        if x in mp:
            c0 = mp[x]
            color[c0] -= 1
            if color[c0] == 0:
                color.pop(c0)
        mp[x] = c
        color[c] += 1
        ans[i] = len(color)
        i += 1
    return ans
