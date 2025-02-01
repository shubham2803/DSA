# https://leetcode.com/problems/special-array-i/description/?envType=daily-question&envId=2025-02-01
from typing import List


def isArraySpecial(nums: List[int]) -> bool:
    if len(nums) < 2:
        return True
    if (nums[0] % 2) == 0:
        prev = 0
    else:
        prev = 1
    for i in range(1, len(nums)):
        if (nums[i] == nums[i - 1]) or ((nums[i] % 2) == prev):
            return False
        prev = nums[i] % 2
    return True
