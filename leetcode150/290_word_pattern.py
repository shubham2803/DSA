# https://leetcode.com/problems/word-pattern/?envType=study-plan-v2&envId=top-interview-150
def wordPattern(self, pattern: str, s: str) -> bool:
    words = s.split()
    m = len(words)
    n = len(pattern)

    if m != n:
        return False

    s_map, w_map = {}, {}

    for i in range(n):
        if pattern[i] not in s_map:
            s_map[pattern[i]] = words[i]
        elif s_map[pattern[i]] != words[i]:
            return False

        if words[i] not in w_map:
            w_map[words[i]] = pattern[i]
        elif w_map[words[i]] != pattern[i]:
            return False

    return True
