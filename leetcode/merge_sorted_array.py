# https://leetcode.com/problems/merge-sorted-array/submissions/1493481211/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    """
    Do not return anything, modify nums1 in-place instead.
    """
    end_idx = len(nums1) - 1
    while m > 0 and n > 0:
        if nums1[m - 1] >= nums2[n - 1]:
            nums1[end_idx] = nums1[m - 1]
            m -= 1
        else:
            nums1[end_idx] = nums2[n - 1]
            n -= 1
        end_idx -= 1
    while n > 0:
        nums1[end_idx] = nums2[n - 1]
        n -= 1
        end_idx -= 1
    print(nums1)


merge(None, [1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
merge(None, [0], 0, [1], 1)
