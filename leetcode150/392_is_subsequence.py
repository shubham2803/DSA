# https://leetcode.com/problems/is-subsequence/description/?envType=study-plan-v2&envId=top-interview-150
def isSubsequence(self, s: str, t: str) -> bool:
    if not s:
        return True
    i = 0
    j = 0

    while j < len(t) and i < len(s):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            j += 1
    return i == len(s)
