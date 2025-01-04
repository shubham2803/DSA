# https://leetcode.com/problems/roman-to-integer/description/?envType=study-plan-v2&envId=top-interview-150
def romanToInt(s: str) -> int:
    out = 0
    last = ' '
    for x in s[::-1]:
        if x == 'I':
            val = 1
            if last in 'VX':
                val = -1
        if x == 'V':
            val = 5
        if x == 'X':
            val = 10
            if last in 'LC':
                val = -10
        if x == 'L':
            val = 50
        if x == 'C':
            val = 100
            if last in 'DM':
                val = -100
        if x == 'D':
            val = 500
        if x == 'M':
            val = 1000
        last = x
        out += val

    return out
