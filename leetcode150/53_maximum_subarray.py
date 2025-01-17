# https://leetcode.com/problems/maximum-subarray/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def maxSubArray(nums: List[int]) -> int:
    current_sum = 0
    max_sum = sum(nums)
    for i in nums:
        current_sum += i
        if current_sum > max_sum:
            max_sum = current_sum
        if current_sum < 0:
            current_sum = 0
    return max_sum
