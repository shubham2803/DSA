# https://leetcode.com/problems/minimum-operations-to-exceed-threshold-value-ii/description/?envType=daily-question&envId=2025-02-13

import heapq
from typing import List


def minOperations(nums: List[int], k: int) -> int:
    heapq.heapify(nums)
    out = 0

    while len(nums) > 1 and nums[0] < k:
        first = heapq.heappop(nums)
        second = heapq.heappop(nums)
        new_val = (min(first, second) * 2) + max(first, second)
        heapq.heappush(nums, new_val)
        out += 1

    return out
