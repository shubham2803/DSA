# https://leetcode.com/problems/word-break/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def wordBreak(self, s: str, wordDict: List[str]) -> bool:
    wordSet = set(wordDict)
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in wordSet:
                dp[i] = True
                break

    return dp[len(s)]
