# https://leetcode.com/problems/palindrome-number/submissions/1515959808/?envType=study-plan-v2&envId=top-interview-150

def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    res = 0
    num = x

    while num:
        r = num % 10
        num = num // 10
        res = (res * 10) + r
    return res == x
