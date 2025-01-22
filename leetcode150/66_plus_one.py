# https://leetcode.com/problems/plus-one/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def plusOne(digits: List[int]) -> List[int]:
    dig = ''.join(str(e) for e in digits)
    lst = []
    dig = int(dig)
    dig += 1
    for ele in str(dig):
        lst.append(int(ele))
    return lst
