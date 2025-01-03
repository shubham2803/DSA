# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

def strStr(haystack: str, needle: str) -> int:
    j = len(needle)

    for i in range(0, len(haystack)):
        if haystack[i:i + j] == needle:
            return i
    return -1
