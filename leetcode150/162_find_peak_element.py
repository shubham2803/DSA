# https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def findPeakElement(nums: List[int]) -> int:
    s = 0
    e = len(nums) - 1

    while s < e:
        mid = (s + e) // 2
        if nums[mid] > nums[mid + 1]:
            e = mid
        else:
            s = mid + 1
    return s
