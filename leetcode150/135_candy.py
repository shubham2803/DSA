# https://leetcode.com/problems/candy/description/?envType=study-plan-v2&envId=top-interview-150

from typing import List


def candy(ratings: List[int]) -> int:
    i = 0
    j = 1
    out_list = [1] * len(ratings)
    while j < len(ratings):
        if ratings[j] > ratings[i]:
            out_list[j] = max(out_list[i], out_list[i] + 1)
        i += 1
        j += 1
    i = len(ratings) - 1
    j = i - 1

    while i > 0:
        if ratings[j] > ratings[i]:
            out_list[j] = max(out_list[j], out_list[i] + 1)
        i -= 1
        j -= 1
    return sum(out_list)
