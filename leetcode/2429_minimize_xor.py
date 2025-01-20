# https://leetcode.com/problems/minimize-xor/description/?envType=daily-question&envId=2025-01-15

def minimizeXor(num1: int, num2: int) -> int:
    ones = 0
    while num2:
        num2 &= (num2 - 1)
        ones += 1
    res = 0
    for i in range(31, -1, -1):
        if ones > 0 and (num1 >> i) & 1:
            res |= (1 << i)
            ones -= 1
    for i in range(32):
        if ones > 0 and ((res >> i) & 1) == 0:
            res |= (1 << i)
            ones -= 1
    return res
