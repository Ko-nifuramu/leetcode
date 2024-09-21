from typing import List

"""
step1:
approach1 -> brute-force: pricesを2回traverseして全てのstockとsell dayで求める
approach2 -> prices[i] - i-1までの中で最小の価格
"""

#所要時間: 7:41
#time: O(N)
#space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        stock_day = 0
        max_profit = 0
        for sell_day, price in enumerate(prices):
            if price < prices[stock_day]:
                stock_day = sell_day
                continue
            max_profit = max(prices[sell_day] - prices[stock_day], max_profit)
        return max_profit

#time: O(N)
#space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int: 
        if len(prices) <= 1:
            return 0
        
        min_stock_price = prices[0]
        max_profit = 0
        for price in prices:
            if price < min_stock_price:
                min_stock_price = price
            else:
                max_profit = max(price - min_stock_price, max_profit)
            
        return max_profit
        