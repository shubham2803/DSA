# https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
def isHappy(n: int) -> bool:
    if n in [1, 7, 10]:
        return True
    elif n < 10:
        return False
    else:
        total = 0
        while n > 0:
            r = n % 10
            total += r * r
            n = n // 10
        return isHappy(total)
