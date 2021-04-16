"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock
"""

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit_list = [0] * len(prices)
        
        max_price = prices[-1]
        price_index = len(prices) - 1
        for (index, price) in enumerate(reversed(prices)):
            if price > max_price:
                max_price = price
            price_index = len(prices) - index
            print(max_price,price_index )
            profit_list[price_index - 1] = max_price - price
        print(profit_list)
        return max(profit_list)
