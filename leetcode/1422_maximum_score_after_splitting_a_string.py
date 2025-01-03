# https://leetcode.com/problems/maximum-score-after-splitting-a-string/description/?envType=daily-question&envId=2025-01-01
def maxScore(s: str) -> int:
    pre_sum = [0] * len(s)

    for i in range(1, len(s)):
        pre_sum[i] = pre_sum[i - 1] + int(s[i])

    zero_count = 0
    max_split = 0
    for i in range(0, len(pre_sum) - 1):
        if s[i] == '0':
            zero_count += 1

        max_split = max(max_split, (pre_sum[-1] - pre_sum[i]) + zero_count)

    return max_split
