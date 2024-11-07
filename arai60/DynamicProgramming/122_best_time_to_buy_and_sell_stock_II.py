from typing import List

"""
step1
"""
#time: O(N)
#space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock_day = 0
        max_sum_profit = 0
        for day in range(1, len(prices)):
            if prices[day] < prices[day-1]:
                max_sum_profit += prices[day-1] - prices[stock_day]
                stock_day = day
        max_sum_profit += prices[-1] - prices[stock_day] if (prices[stock_day] < prices[-1]) else 0
        return max_sum_profit
    
    
#推し進めれば、前日より上がっていれば売れば良い.個人的には買って売る回数が多くなって
#大変そうなので、私の回答を押したい笑

#time: O(N)
#space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        for day in range(1, len(prices)):
            if prices[day] > prices[day-1]:
                max_profit += prices[day] - prices[day-1]

        return max_profit


"""
step2
"""

# time: O(N)
# space: O(1)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_sum_profit = 0
        for i in range(1, len(prices)):
            if prices[i-1] < prices[i]:
                max_sum_profit += prices[i] - prices[i-1]

        return max_sum_profit

