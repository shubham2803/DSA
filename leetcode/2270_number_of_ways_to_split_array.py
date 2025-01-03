# https://leetcode.com/problems/number-of-ways-to-split-array/?envType=daily-question&envId=2025-01-03
from typing import List


def waysToSplitArray(nums: List[int]) -> int:
    prefix_sum_array = [0] * len(nums)

    for i in range(0, len(nums)):
        prefix_sum_array[i] = prefix_sum_array[i - 1] + nums[i]

    splits = 0
    for i in range(0, len(prefix_sum_array) - 1):
        if (prefix_sum_array[-1] - prefix_sum_array[i]) < prefix_sum_array[i]:
            splits += 1

    return splits


print(waysToSplitArray([10, 4, -8, 7]))
