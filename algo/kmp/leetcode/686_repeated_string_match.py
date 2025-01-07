# https://leetcode.com/problems/repeated-string-match/?envType=problem-list-v2&envId=string-matching

def repeatedStringMatch(a: str, b: str) -> int:
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
            return True
        if len(pat) > len(txt):
            return False

        lps = [0] * len(pat)
        lps = generate_lps(pat, lps)
        i = 0
        j = 0

        while i < len(txt):
            if txt[i] == pat[j]:
                i += 1
                j += 1
                if j == len(pat):
                    print(i-len(pat))
                    return True
            else:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return False

    repeat = len(b) // len(a)
    min = 1

    while min <= repeat + 2:
        if is_substring(a * min, b):
            return min
        else:
            min += 1

    return -1

a = 'abcd'
b = 'cdabcdab'

print(repeatedStringMatch(a, b))