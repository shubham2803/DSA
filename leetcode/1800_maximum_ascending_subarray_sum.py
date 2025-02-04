# https://leetcode.com/problems/maximum-ascending-subarray-sum/description/?envType=daily-question&envId=2025-02-04
from typing import List


def maxAscendingSum(self, nums: List[int]) -> int:
    max_asc = 0

    start = nums[0]
    current_total = start
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            current_total += nums[i]
        else:
            max_asc = max(current_total, max_asc)
            current_total = nums[i]

    return max(current_total, max_asc)