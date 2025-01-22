# https://leetcode.com/problems/powx-n/submissions/1517013440/?envType=study-plan-v2&envId=top-interview-150
def myPow(x: float, n: int) -> float:
    out = 1
    p = n
    if n < 0:
        p = -1 * p
    while p:
        if p % 2:
            out = out * x
            p = p - 1
        else:
            x = x * x
            p = p // 2
    if n < 0:
        out = 1 / out

    return out
