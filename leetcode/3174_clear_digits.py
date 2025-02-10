# https://leetcode.com/problems/clear-digits/description/?envType=daily-question&envId=2025-02-10

def clearDigits(s: str) -> str:
    s_list = list(s)

    n = len(s)
    i = 0
    while i < n:
        if s_list[i].isdigit():
            s_list.pop(i - 1)
            i = i - 1
            s_list.pop(i)
            i = i - 1
        n = len(s_list)
        i = i + 1
    return ''.join(s_list)
