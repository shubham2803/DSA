# https://leetcode.com/problems/valid-anagram/?envType=study-plan-v2&envId=top-interview-150

def isAnagram(self, s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    s_count = [0] * 26

    for i in range(len(s)):
        s_count[ord(s[i]) - ord('a')] += 1
        s_count[ord(t[i]) - ord('a')] -= 1

    return all(count == 0 for count in s_count)