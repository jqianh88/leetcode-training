"""
You are given an array `prices` where `prices[i]` is the price of a given stock on the `ith` day. 
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. 
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return `0`. 

Inputs: 
- prices: array

Outputs: 
- maximum profit: int
"""

# First pass
# def maximum_profit(prices: list) -> int: 

#     prices_hashmap = {day: price for day, price in enumerate(prices)}
#     profit = 0
#     for i, price in enumerate(prices):
#         for j in prices[i:]: 
#             print(prices[i:])
#             new_profit = price - j
#             if new_profit < 0 and new_profit < profit:
#                 profit = new_profit

#     return abs(profit)

import collections


collections.Counter().items()
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        left, right = 0, 1
        while right < len(prices):
            if prices[left] < prices[right]:
                profit = prices[right] - prices[left]
                max_profit = max(profit, max_profit)

            else: 
                left = right
            right += 1
        return max_profit


if __name__=='__main__':
    prices =  [7, 1, 5, 3, 6, 4] # [7, 6, 4, 3, 1] 
    print(Solution().maxProfit(prices=prices))
