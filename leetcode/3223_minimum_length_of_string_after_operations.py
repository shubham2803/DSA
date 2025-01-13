# https://leetcode.com/problems/minimum-length-of-string-after-operations/description/?envType=daily-question&envId=2025-01-13

def minimumLength(s: str) -> int:
    s_map = {}

    for i in s:
        s_map[i] = s_map.get(i, 0) + 1
    out = 0
    for k, v in s_map.items():
        if v % 2 == 0:
            out += 2
        else:
            out += 1
    return out
