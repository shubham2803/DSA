# https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


def candy(ratings: List[int]) -> int:
    n = len(ratings)
    i = 1
    out = n
    peak = 0
    valley = 0
    while i < n:
        if ratings[i] == ratings[i - 1]:
            i += 1

        peak = 0
        while i < n and ratings[i] > ratings[i - 1]:
            peak += 1
            out += peak
            i += 1
        valley = 0
        while i < n and ratings[i] < ratings[i - 1]:
            valley += 1
            out += valley
            i += 1

        out -= min(peak, valley)
    return out
