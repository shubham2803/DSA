# https://leetcode.com/problems/group-anagrams/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def groupAnagrams(strs: List[str]) -> List[List[str]]:
    s_map = {}

    for s in strs:
        e_sorted = sorted(s)
        e_sorted = ''.join(e_sorted)
        if e_sorted not in s_map:
            s_map[e_sorted] = [s]
        else:
            s_map[e_sorted].append(s)

    return list(s_map.values())
