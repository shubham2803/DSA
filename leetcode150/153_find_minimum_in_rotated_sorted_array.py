# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def findMin(nums: List[int]) -> int:
    s = 0
    e = len(nums) - 1

    while s < e:
        mid = (s + e) // 2
        if nums[mid] < nums[e]:
            e = mid
        else:
            s = mid + 1
    return nums[s]
