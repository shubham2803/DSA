# https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def majorityElement(self, nums: List[int]) -> int:
    max_count = out = 0

    for ele in nums:
        if max_count == 0:
            out = ele

        if out == ele:
            max_count += 1
        else:
            max_count -= 1
    return out


print(majorityElement(None, [3, 2, 3, 2, 2, 1, 1, 1, 2, 2, 2]))
