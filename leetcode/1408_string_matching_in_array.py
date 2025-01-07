# https://leetcode.com/problems/string-matching-in-an-array/description/?envType=daily-question&envId=2025-01-07
class Solution:
    def check_lps(self, arr):
        i = 1
        j = 0
        lps = [0] * len(arr)

        while i < len(arr):
            if arr[i] == arr[j]:
                j += 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def is_pattern_in_text(self, txt, pat):
        if not pat:
            return True
        if len(txt) < len(pat):
            return False

        lps = self.check_lps(pat)
        i = 0
        j = 0
        while i < len(txt):
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == len(pat):
                    return True
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1

        return False

    def stringMatching(self, words: List[str]) -> List[str]:
        out_map = {}
        for i in range(len(words)):
            for j in range(len(words)):
                if i != j and words[i] not in out_map:
                    if self.is_pattern_in_text(words[j], words[i]):
                        out_map[words[i]] = True
        return list(out_map.keys())
