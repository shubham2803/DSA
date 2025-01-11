# https://leetcode.com/problems/construct-k-palindrome-strings/description/?envType=daily-question&envId=2025-01-11

def canConstruct(s: str, k: int) -> bool:
    if len(s) < k:
        return False

    s_map = {}

    for i in s:
        s_map[i] = s_map.get(i, 0) + 1
    odd_count = 0
    for v in s_map.values():
        if (v % 2) == 1:
            odd_count += 1

    if odd_count > k:
        return False
    return True
