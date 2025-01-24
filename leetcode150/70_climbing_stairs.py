# https://leetcode.com/problems/climbing-stairs/?envType=study-plan-v2&envId=top-interview-150
def climbStairs(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 2

    dp1 = 1
    dp2 = 2

    for i in range(3, n + 1):
        current = dp1 + dp2
        dp1 = dp2
        dp2 = current

    return dp2
