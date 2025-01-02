# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def removeDuplicates(self, nums: List[int]) -> int:
    j = 2
    flag = True
    for i in range(2, len(nums)):

        if nums[j] != nums[i] and flag:
            nums[j] = nums[i]
        if nums[i] == nums[j - 2]:
            flag = True
            continue
        else:
            j += 1
    return j

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
print(removeDuplicates(None, nums))
