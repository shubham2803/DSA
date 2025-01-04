# https://leetcode.com/problems/unique-length-3-palindromic-subsequences/description/?envType=daily-question&envId=2025-01-04
def countPalindromicSubsequence(s: str) -> int:
    out = 0
    map = {}
    for i in range(0, len(s)):
        if s[i] not in map:
            map[s[i]] = [i]
        else:
            map[s[i]].append(i)

    for values in map.values():
        left = values[0]
        right = values[-1]

        if right >= left + 1:
            print(s[left+1: right])
            out += len(set(s[left+1: right]))
    return out


print(countPalindromicSubsequence('bbcbaba'))
