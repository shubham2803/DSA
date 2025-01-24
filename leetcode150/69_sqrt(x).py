# https://leetcode.com/problems/sqrtx/description/?envType=study-plan-v2&envId=top-interview-150

def mySqrt(x: int) -> int:
    if not x:
        return 0
    low, high = 1, x

    while low <= high:
        mid = (low + high) // 2
        if mid * mid == x:
            return mid
        elif mid * mid < x:
            low = mid + 1
        else:
            high = mid - 1

    return high
