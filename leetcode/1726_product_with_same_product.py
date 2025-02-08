# https://leetcode.com/problems/tuple-with-same-product/description/?envType=daily-question&envId=2025-02-06
from collections import defaultdict
from typing import List


def tupleSameProduct(self, nums: List[int]) -> int:
    n = len(nums)
    freq = defaultdict(int)
    for i in range(n - 1):
        x = nums[i]
        for j in range(i + 1, n):
            freq[x * nums[j]] += 1
    return sum(f * (f - 1) * 4 for f in freq.values())
