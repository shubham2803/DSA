# https://leetcode.com/problems/count-number-of-bad-pairs/description/?envType=daily-question&envId=2025-02-09
from typing import List


def countBadPairs(self, nums: List[int]) -> int:
    data_dict = {}
    n = len(nums)
    good = 0
    for i in range(n):
        k = nums[i] - i
        good += data_dict.get(k, 0)
        data_dict[k] = data_dict.get(k, 0) + 1

    total_pairs = (n * (n - 1)) // 2

    return total_pairs - good
