# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    if not nums:
        return [-1, -1]
    if len(nums) < 2:
        if nums[0] == target:
            return [0, 0]
    s = 0
    e = len(nums) - 1

    while s <= e:
        mid = (s + e) // 2
        if nums[mid] == target:
            s = mid
            e = mid
            while (s > 0) and nums[s - 1] == target:
                if nums[s - 1] == target:
                    print(s)
                    s = s - 1
            while (e < len(nums) - 1) and nums[e + 1] == target:
                if nums[e] == target:
                    e = e + 1
            return [s, e]
        elif target > nums[mid]:
            s = mid + 1
        else:
            e = e - 1
    return [-1, -1]


nums = [8, 8, 8, 8]
target = 8
print(searchRange(nums, target))
