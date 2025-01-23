# https://leetcode.com/problems/house-robber/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def rob(nums: List[int]) -> int:
    if not nums:
        return 0

    if len(nums) == 1:
        return nums[0]

    dp1 = nums[0]
    dp2 = max(nums[0], nums[1])

    for i in range(2, len(nums)):
        current = max(dp2, nums[i] + dp1)
        dp1 = dp2
        dp2 = current

    return dp2
