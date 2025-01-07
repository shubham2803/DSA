from typing import List


def check_lps(arr):
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


def is_pattern_in_text(txt, pat):
    if not pat:
        return True
    if len(txt) < len(pat):
        return False

    lps = check_lps(pat)
    print(pat, lps)
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

print(is_pattern_in_text('yoxwp', 'oyo'))
print(is_pattern_in_text('abdabd', 'dab'))

