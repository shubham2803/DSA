# https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/description/?envType=daily-question&envId=2025-02-05
def areAlmostEqual(self, s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    first_change = []
    second_change = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if not first_change:
                first_change = [s1[i], s2[i]]
            elif not second_change:
                second_change = [s2[i], s1[i]]
            else:
                return False
    if not second_change:
        return False
    return first_change == second_change
