# https://leetcode.com/problems/neighboring-bitwise-xor/description/?envType=daily-question&envId=2025-01-17
from typing import List


def doesValidArrayExist(derived: List[int]) -> bool:
    out = 0
    for i in derived:
        out ^= i

    return out == 0
