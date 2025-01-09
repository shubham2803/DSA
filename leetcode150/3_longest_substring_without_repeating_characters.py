# https://leetcode.com/problems/longest-substring-without-repeating-characters/?envType=study-plan-v2&envId=top-interview-150

def lengthOfLongestSubstring(s: str) -> int:
    if not s:
        return 0
    if len(s) < 2:
        return 1
    sub_l = ''
    max_w = 0

    for i in range(0, len(s) - 1):
        start = i
        next = i + 1

        sub = s[start]
        s_map = {}
        while (next < len(s)) and (s[start] != s[next]):
            if s[next] not in s_map:
                sub += s[next]
                s_map[s[next]] = True
            else:
                break
            next += 1

        if len(sub) > len(sub_l):
            sub_l = sub
            max_w = len(sub_l)
    return max_w


print(lengthOfLongestSubstring('au'))
