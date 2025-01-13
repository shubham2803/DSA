# https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
    n_map = {}

    for i in range(len(nums)):
        if nums[i] not in n_map:
            n_map[nums[i]] = i
        else:
            if abs(i - n_map[nums[i]]) <= k:
                return True
            else:
                n_map[nums[i]] = i
    return False
