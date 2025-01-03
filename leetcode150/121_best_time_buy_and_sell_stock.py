# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/?envType=study-plan-v2&envId=top-interview-150
from typing import List


def maxProfit(prices: List[int]) -> int:
    min_price = prices[0]
    max_profit = 0

    for current_price in prices[1:]:
        if current_price < min_price:
            current_profit = 0
            min_price = current_price
        else:
            current_profit = current_price - min_price
            if current_profit > max_profit:
                max_profit = current_profit
    return max_profit
