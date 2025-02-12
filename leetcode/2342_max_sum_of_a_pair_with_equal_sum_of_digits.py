# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/?envType=daily-question&envId=2025-02-12
from typing import List


def maximumSum(self, nums: List[int]) -> int:
    data_dict = {}
    for x in nums:
        digit_sum = 0
        val = x
        while x:
            remain = x % 10
            digit_sum += remain
            x = x // 10
        if digit_sum not in data_dict:
            data_dict[digit_sum] = [val]
        else:
            data_dict[digit_sum].append(val)

    max_sum = -1
    for k, v in data_dict.items():
        v = sorted(v)[::-1]
        if len(v) >= 2:
            max_sum = max(sum(v[:2]), max_sum)
    return max_sum

