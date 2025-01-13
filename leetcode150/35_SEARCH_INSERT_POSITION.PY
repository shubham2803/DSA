# https://leetcode.com/problems/search-insert-position/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def searchInsert(self, nums: List[int], target: int) -> int:
    s = 0
    e = len(nums) - 1

    while s <= e:
        mid = (s + e) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            s = mid + 1
        else:
            e = mid - 1
    return s
