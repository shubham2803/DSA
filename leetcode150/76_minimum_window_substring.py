# https://leetcode.com/problems/minimum-window-substring/description/?envType=study-plan-v2&envId=top-interview-150
from collections import Counter, defaultdict


def minWindow(s: str, t: str) -> str:
    if not s or not t:
        return ""

    t_count = Counter(t)
    required = len(t_count)

    left, right = 0, 0
    window_count = defaultdict(int)
    formed = 0
    min_len = float("inf")
    min_window = (0, 0)

    while right < len(s):
        char = s[right]
        window_count[char] += 1

        if char in t_count and window_count[char] == t_count[char]:
            formed += 1

        while left <= right and formed == required:
            char = s[left]

            if right - left + 1 < min_len:
                min_len = right - left + 1
                min_window = (left, right)

            window_count[char] -= 1
            if char in t_count and window_count[char] < t_count[char]:
                formed -= 1

            left += 1

        right += 1

    start, end = min_window
    return s[start:end + 1] if min_len != float("inf") else ""
