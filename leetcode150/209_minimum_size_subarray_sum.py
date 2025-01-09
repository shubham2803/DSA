# https://leetcode.com/problems/minimum-size-subarray-sum/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def minSubArrayLen(target: int, nums: List[int]) -> int:
    left = 0
    n = len(nums)
    min_count = n + 1
    total = 0

    for right in range(0, n):
        total += nums[right]

        while total >= target:
            min_count = min(min_count, right - left + 1)
            total -= nums[left]
            left += 1

    return min_count if min_count <= n else 0


nums = [1,4,4]
target = 4
print(minSubArrayLen(target, nums))
