# https://leetcode.com/problems/median-of-two-sorted-arrays/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    l = len(nums1) - 1
    m = len(nums2) - 1
    out = []
    i, j = 0, 0
    while i <= l and j <= m:
        if nums1[i] < nums2[j]:
            out.append(nums1[i])
            i += 1
        else:
            out.append(nums2[j])
            j += 1
    while i <= l:
        out.append(nums1[i])
        i += 1
    while j <= m:
        out.append(nums2[j])
        j += 1
    s = 0
    e = len(out) - 1
    if len(out) % 2 == 1:
        return out[(s + e) // 2]
    else:
        return (out[(s+e)//2] + out[(s+e+1)//2]) / 2


nums1 = [1, 2]
nums2 = [3, 4]
print(findMedianSortedArrays(nums1, nums2))
