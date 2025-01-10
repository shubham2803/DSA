# https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def longestConsecutive(nums: List[int]) -> int:
    if not nums:
        return 0

    nums_set = set(nums)
    out = 0

    for num in nums_set:
        if num - 1 not in nums_set:
            curr_num = num
            count = 1
            while curr_num + 1 in nums_set:
                count += 1
                curr_num += 1

            out = max(count, out)

    return out
