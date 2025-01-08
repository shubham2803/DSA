# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/?envType=daily-question&envId=2025-01-08

def countPrefixSuffixPairs(self, words: List[str]) -> int:
    def isPrefixAndSuffix(str1, str2):
        concat = str1 + ':' + str2
        print(concat)
        n = len(concat)
        j = 0
        lps = [0] * n
        for i in range(1, n):
            while j > 0 and concat[i] != concat[j]:
                j = lps[j - 1]
            if concat[i] == concat[j]:
                j += 1
            lps[i] = j
        m = len(str1)
        return (lps[-1] == m) and (lps[m: (2 * m) + 1][-1] == m)

    w = len(words)
    out = 0
    for i in range(w):
        for j in range(i + 1, w):
            if isPrefixAndSuffix(words[i], words[j]):
                out += 1
    return out
