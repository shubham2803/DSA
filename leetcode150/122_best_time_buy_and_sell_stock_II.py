# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/submissions/1496527947/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    if n < 2:
        return 0

    dp = [0] * n

    for i in range(1, n):
        dp[i] = dp[i - 1] + max(0, prices[i] - prices[i - 1])
    return dp[n - 1]
