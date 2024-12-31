# https://leetcode.com/problems/remove-element/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def removeElement(self, nums: List[int], val: int) -> int:
    idx = 0
    for x in nums:
        if x != val:
            nums[idx] = x
            idx += 1
    return idx
