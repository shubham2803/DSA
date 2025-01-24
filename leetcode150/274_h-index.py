# https://leetcode.com/problems/h-index/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def hIndex(citations: List[int]) -> int:
    citations.sort()
    n = len(citations)

    for i in range(n):
        if citations[i] >= n - i:
            return n - i

    return 0
