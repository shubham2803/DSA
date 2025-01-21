# https://leetcode.com/problems/reverse-bits/description/?envType=study-plan-v2&envId=top-interview-150

def reverseBits(n: int) -> int:
    result = 0
    for _ in range(32):
        result = (result << 1) | (n & 1)
        n >>= 1
    return result
