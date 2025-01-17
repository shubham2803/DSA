# https://leetcode.com/problems/number-of-1-bits/submissions/1511584770/?envType=study-plan-v2&envId=top-interview-150

def hammingWeight(n: int) -> int:
    q = n
    out = 0

    while q:
        r = q % 2
        q = q // 2
        if r == 1:
            out += 1

    return out
