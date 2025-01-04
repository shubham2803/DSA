# https://leetcode.com/problems/integer-to-roman/description/?envType=study-plan-v2&envId=top-interview-150
def intToRoman(self, num: int) -> str:
    thousand = num // 1000
    hundred = (num - (thousand * 1000)) // 100
    ten = (num - ((thousand * 1000) + (hundred * 100))) // 10
    single = (num - ((thousand * 1000) + (hundred * 100))) % 10

    out = ""

    map = {
        1000: 'M',
        900: 'CM',
        500: 'D',
        400: 'CD',
        100: 'C',
        90: 'XC',
        50: 'L',
        40: 'XL',
        10: 'X',
        9: 'IX',
        5: 'V',
        4: 'IV',
        1: 'I'
    }

    for k, v in map.items():
        while num >= k:
            out += v
            num -= k
    return out
