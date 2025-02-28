# https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
def isIsomorphic(s: str, t: str) -> bool:
    s_map = {}
    t_map = {}

    for i in range(len(s)):
        if s[i] not in s_map:
            s_map[s[i]] = i

        if t[i] not in t_map:
            t_map[t[i]] = i

        if t_map[t[i]] != s_map[s[i]]:
            print(t[i], s[i])
            print(t_map, s_map)
            return False

    return True


print(isIsomorphic('barc', 'baba'))


