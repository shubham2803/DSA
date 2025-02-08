# https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/description/?envType=daily-question&envId=2025-02-03
from typing import List


def longestMonotonicSubarray(self, nums: List[int]) -> int:
    if len(nums) < 2:
        return 1
    slope = 1
    prev = nums[0]
    max_slope = 1
    up = nums[1] > nums[0]
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            slope += 1
            if not up:
                slope = 2
            up = True
        elif nums[i] < nums[i - 1]:
            slope += 1
            if up:
                slope = 2
            up = False
        else:
            slope = 1
        max_slope = max(max_slope, slope)

    return max_slope
