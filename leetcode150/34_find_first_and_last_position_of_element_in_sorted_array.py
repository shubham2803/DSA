# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    def findFirst(nums, target):
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                first = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def findLast(nums, target):
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                last = mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    first = findFirst(nums, target)
    last = findLast(nums, target)
    return [first, last]


nums = [5,7,7,8,8,10]
target = 8
print(searchRange(nums, target))
