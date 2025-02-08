# https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/?envType=daily-question&envId=2025-02-02
from typing import List


def check(self, nums: List[int]) -> bool:
    if len(nums) < 2:
        return True
    rotations = 0
    for i in range(1, len(nums)):
        if rotations == 1 and nums[i] > nums[0]:
            return False
        if nums[i] < nums[i - 1]:
            rotations += 1
            if nums[i] > nums[0]:
                return False
        if rotations > 1:
            return False
    return True
