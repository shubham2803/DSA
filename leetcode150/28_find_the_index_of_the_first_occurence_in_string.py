# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/?envType=study-plan-v2&envId=top-interview-150

def strStr(self, haystack: str, needle: str) -> int:
    def generate_lps(arr, lps):
        i = 1
        j = 0
        lps[0] = 0

        while i < len(arr):
            if arr[i] == arr[j]:
                j = j + 1
                lps[i] = j
                i += 1
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def is_substring(txt, pat):
        if not pat:
            return 0
        if len(pat) > len(txt):
            return -1

        lps = [0] * len(pat)
        lps = generate_lps(pat, lps)
        i = 0
        j = 0
        while i < len(txt):
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == len(pat):
                    return i - len(pat)
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        if i == len(txt) and j != len(pat):
            return -1

    return is_substring(haystack, needle)
