# https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/?envType=daily-question&envId=2025-02-19


def getHappyString(n: int, k: int) -> str:
    def dfs(prefix, n, k):
        if n == 0:
            return prefix
        for c in 'abc':
            if prefix and c == prefix[-1]:
                continue
            cnt = 2 ** (n2 - len(prefix) - 1)
            if cnt >= k:
                return dfs(prefix + c, n - 1, k)
            else:
                k -= cnt
        return ""

    n2 = n
    return dfs("", n, k)
